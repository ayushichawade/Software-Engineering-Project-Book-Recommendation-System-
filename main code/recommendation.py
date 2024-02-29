import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from keras.layers import Input, Dense, Dropout
from keras.models import Model
from keras import regularizers


books_df = pd.read_excel('Best_Books.xlsx')
users_df = pd.read_csv('goodreads_interactions.csv')


merged_df = pd.merge(users_df, books_df, on='book_id', how='inner', validate='one_to_many')



genres = pd.get_dummies(merged_df['genre 1'])


merged_df = pd.concat([merged_df, genres], axis=1)

#  user-item matrix
user_item_matrix = pd.pivot_table(merged_df, values='Rating', index='user_id', columns='book_id')


user_item_matrix = user_item_matrix.fillna(0)

# cosine similarity matrix
cosine_sim = cosine_similarity(user_item_matrix)

# autoencoder model
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


autoencoder.fit(user_item_matrix, user_item_matrix, epochs=50, batch_size=64, validation_split=0.2)


filtered_matrix = autoencoder.predict(user_item_matrix)


filtered_cosine_sim = cosine_similarity(filtered_matrix)

def recommend_books(user_id, num_recommendations=50):

    user_row = user_item_matrix.loc[user_id]


    user_similarities = pd.Series(cosine_sim[user_id])


    top_users = user_similarities.sort_values(ascending=False)[1:num_recommendations+1].index


    top_users_filtered = filtered_matrix[top_users]


    weighted_ratings = np.dot(top_users_filtered, user_row) / np.sum(top_users_filtered, axis=1)


    top_books = weighted_ratings.argsort()[::-1][:num_recommendations]


    return books_df.loc[top_books]

recommend_books(user_id=1)
