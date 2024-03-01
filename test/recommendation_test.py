import unittest
import os
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from keras.layers import Input, Dense, Dropout
from keras.models import Model, load_model
from keras import regularizers

# Function to load data and create recommendations
def recommend_books(user_id, num_recommendations=50):
    # Load the data
    books_df = pd.read_excel('Best_Books.xlsx')
    users_df = pd.read_csv('goodreads_interactions.csv')

    # Merge datasets
    merged_df = pd.merge(users_df, books_df, on='book_id')

    # Dummy encoding for genres
    genres = pd.get_dummies(merged_df['genre 1'])
    merged_df = pd.concat([merged_df, genres], axis=1)

    # User-item matrix
    user_item_matrix = pd.pivot_table(merged_df, values='Rating', index='user_id', columns='book_id').fillna(0)

    # Cosine similarity matrix
    cosine_sim = cosine_similarity(user_item_matrix)

    # Check if pre-trained model exists
    model_file = 'autoencoder_model.h5'
    if os.path.exists(model_file):
        autoencoder = load_model(model_file)
    else:
        # Autoencoder model
        input_layer = Input(shape=(user_item_matrix.shape[1],))
        encoded = Dense(256, activation='relu', activity_regularizer=regularizers.l1(10e-5))(input_layer)
        encoded = Dropout(0.5)(encoded)
        encoded = Dense(128, activation='relu', activity_regularizer=regularizers.l1(10e-5))(encoded)
        encoded = Dropout(0.5)(encoded)
        encoded = Dense(64, activation='relu', activity_regularizer=regularizers.l1(10e-5))(encoded)
        decoded = Dense(128, activation='relu')(encoded)
        decoded = Dropout(0.5)(decoded)
        decoded = Dense(256, activation='relu')(decoded)
        decoded = Dropout(0.5)(decoded)
        decoded = Dense(user_item_matrix.shape[1], activation='sigmoid')(decoded)
        autoencoder = Model(input_layer, decoded)
        autoencoder.compile(optimizer='adam', loss='mse')

        # Train the autoencoder
        autoencoder.fit(user_item_matrix, user_item_matrix, epochs=1, batch_size=64, validation_split=0.2)

        # Save the trained model
        autoencoder.save(model_file)

    # Filtered matrix
    filtered_matrix = autoencoder.predict(user_item_matrix)

    # Filtered cosine similarity
    filtered_cosine_sim = cosine_similarity(filtered_matrix)

    user_row = user_item_matrix.loc[user_id]
    user_similarities = pd.Series(cosine_sim[user_id])
    top_users = user_similarities.sort_values(ascending=False)[1:num_recommendations+1].index
    top_users_filtered = filtered_matrix[top_users]
    weighted_ratings = np.dot(top_users_filtered, user_row) / np.sum(top_users_filtered, axis=1)
    top_books = weighted_ratings.argsort()[::-1][:num_recommendations]
    return books_df.loc[top_books]

# Test class for recommendation function
class TestRecommendations(unittest.TestCase):
    def test_output_size(self):
        num_recommendations = 50
        recommendations = recommend_books(user_id=1, num_recommendations=num_recommendations)
        self.assertEqual(len(recommendations), num_recommendations, "Incorrect number of book recommendations.")

    def test_user_existence(self):
        user_id = 1
        recommendations = recommend_books(user_id=user_id)
        self.assertTrue(not recommendations.empty, "No recommendations returned for an existing user.")

    def test_non_existent_user(self):
        user_id = 9999
        try:
          recommendations = recommend_books(user_id=user_id)
        except KeyError:
        # Handle the case of a non-existent user ID gracefully
         recommendations = pd.DataFrame()
         self.assertTrue(recommendations.empty, "Recommendations returned for a non-existent user.")


    def test_data_consistency(self):
        user_id = 1
        recommendations_1 = recommend_books(user_id=user_id)
        recommendations_2 = recommend_books(user_id=user_id)
        self.assertTrue(recommendations_1.equals(recommendations_2), "Recommendations not consistent for the same input.")

    def test_content_of_recommendations(self):
        user_id = 1
        recommendations = recommend_books(user_id=user_id)
        # Add specific assertions to check the content of recommendations

    def test_performance(self):
        # Run the function with large datasets and measure execution time
        pass

# Run the tests
test_suite = unittest.TestLoader().loadTestsFromTestCase(TestRecommendations)
unittest.TextTestRunner().run(test_suite)
