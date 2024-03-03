import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from keras.layers import Input, Dense, Dropout
from keras.models import Model
from keras import regularizers

# Load data
def load_data():
    books_data = pd.read_excel('Best_Books.xlsx')
    users_data = pd.read_csv('goodreads_interactions.csv')
    return books_data, users_data

# Preprocess data
def preprocess_data(books_data, users_data):
    merged_data = pd.merge(users_data, books_data, on='book_id', how='inner', validate='one_to_many')
    genres = pd.get_dummies(merged_data['genre 1'])
    merged_data = pd.concat([merged_data, genres], axis=1)
    user_item_matrix = pd.pivot_table(merged_data, values='Rating', index='user_id', columns='book_id').fillna(0)
    return user_item_matrix

# Build and train autoencoder model
def build_autoencoder_model(input_shape):
    input_layer = Input(shape=input_shape)
    encoded = Dense(256, activation='relu', activity_regularizer=regularizers.l1(10e-5))(input_layer)
    encoded = Dropout(0.5)(encoded)
    encoded = Dense(128, activation='relu', activity_regularizer=regularizers.l1(10e-5))(encoded)
    encoded = Dropout(0.5)(encoded)
    encoded = Dense(64, activation='relu', activity_regularizer=regularizers.l1(10e-5))(encoded)
    decoded = Dense(128, activation='relu')(encoded)
    decoded = Dropout(0.5)(decoded)
    decoded = Dense(256, activation='relu')(decoded)
    decoded = Dropout(0.5)(decoded)
    decoded = Dense(input_shape, activation='sigmoid')(decoded)
    autoencoder = Model(input_layer, decoded)
    autoencoder.compile(optimizer='adam', loss='mse')
    return autoencoder

# Generate book recommendations
def recommend_books(user_item_matrix, books_data, num_recommendations=50):
    # Code for recommendation function
    pass

if __name__ == '__main__':
    # Load data
    books_data, users_data = load_data()

    # Preprocess data
    user_item_matrix = preprocess_data(books_data, users_data)

    # Build and train autoencoder model
    autoencoder = build_autoencoder_model(user_item_matrix.shape[1])
    autoencoder.fit(user_item_matrix, user_item_matrix, epochs=50, batch_size=64, validation_split=0.2)

    # Generate book recommendations for user with id=1
    recommended_books = recommend_books(user_item_matrix, books_data, user_id=1)
    print(recommended_books)
