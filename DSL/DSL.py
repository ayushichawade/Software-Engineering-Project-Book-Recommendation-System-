import pandas as pd

def recommend_by_genre(genre, books_df):
    genre_books = books_df[books_df['genres'] == genre]
    top_books = genre_books.nlargest(5, 'rating')
    return top_books[['title', 'author', 'rating']]

def recommend_by_popularity(books_df):
    top_books = books_df.nlargest(5, 'rating')
    return top_books[['title', 'author', 'rating']]

def recommend_by_user_rating(user_id, interaction_df, books_df):
    user_interactions = interaction_df[interaction_df['user_id'] == user_id]
    user_interactions = user_interactions.merge(books_df, on='book_id')
    top_books = user_interactions.nlargest(5, 'Rating')
    return top_books[['title', 'author', 'Rating']]

# Load data
books_df = pd.read_excel('Best_Books.xlsx')
interaction_df = pd.read_csv('goodreads_interactions.csv')

# Example usage:
genre_recommendations = recommend_by_genre('Mystery', books_df)
popularity_recommendations = recommend_by_popularity(books_df)
user_recommendations = recommend_by_user_rating(1234, interaction_df, books_df)

print("Genre Recommendations:")
print(genre_recommendations)
print("\nPopularity Recommendations:")
print(popularity_recommendations)
print("\nUser Recommendations:")
print(user_recommendations)
