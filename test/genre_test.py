import unittest
import pandas as pd

def recommend_books():
    # Read books data from Excel
    books_df = pd.read_excel('Best_Books.xlsx')

    # Get user's favorite genres
    user_fav_genres = input('Enter your favorite genres (separated by commas): ').split(',')

    # Filter books based on user's favorite genres
    matched_books_df = books_df[books_df[['genre 1', 'genre 2', 'genre 3', 'genre 4', 'genre 5']].apply(lambda x: x.isin(user_fav_genres)).any(axis=1)]

    # Count how many favorite genres match for each book
    genre_counts = matched_books_df[['genre 1', 'genre 2', 'genre 3', 'genre 4', 'genre 5']].apply(lambda x: sum(x.isin(user_fav_genres)), axis=1)

    # Filter books that match at least two favorite genres
    matched_books_df = matched_books_df[genre_counts >= 2].reset_index(drop=True)

    # Read user interactions data
    user_df = pd.read_csv('goodreads_interactions.csv')

    # Filter user ratings with at least 4 stars
    user_ratings_df = user_df[user_df['Rating'] >= 4]

    # Get unique book IDs rated by the user
    user_rated_book_ids = user_ratings_df['book_id'].unique()

    # Exclude books already rated by the user
    collab_filtered_books_df = matched_books_df[~matched_books_df['book_id'].isin(user_rated_book_ids)]

    # Calculate weighted score for recommendation
    C = books_df['rating'].mean()
    m = books_df['numRatings'].quantile(0.9)
    collab_filtered_books_df['weighted_score'] = (collab_filtered_books_df['numRatings'] / (collab_filtered_books_df['numRatings'] + m) * collab_filtered_books_df['rating']) + (m / (collab_filtered_books_df['numRatings'] + m) * C)

    # Sort books by weighted score
    collab_filtered_books_df = collab_filtered_books_df.sort_values('weighted_score', ascending=False).reset_index(drop=True)

    # Return recommended books
    return collab_filtered_books_df.head(10)

class TestRecommendBooks(unittest.TestCase):
    def test_recommend_books(self):
        # Run the recommendation function
        recommended_books = recommend_books()
        # Assert that recommended books are not empty
        self.assertGreater(recommended_books.shape[0], 0, "No books found for the given genres")

# Run the tests
unittest.main(argv=[''], exit=False)
