import unittest
import pandas as pd

# Import the functions to be tested
from your_module import (
    read_books_from_excel,
    read_user_preferences,
    filter_books_by_genre,
    read_user_ratings,
    filter_books_by_user_ratings,
    calculate_weighted_score
)

# Mock data paths for testing
BOOKS_FILE_PATH = 'test_books.xlsx'
USER_RATINGS_FILE_PATH = 'test_user_ratings.csv'


class TestYourModule(unittest.TestCase):

    def setUp(self):
        books_df = pd.read_excel('Best_Books.xlsx')
        self.books_data = {
            'book_id': [1, 2, 3, 4],
            'title': ['Book 1', 'Book 2', 'Book 3', 'Book 4'],
            'genre 1': ['Fiction', 'Non-fiction', 'Fiction', 'Non-fiction'],
            'genre 2': ['Fantasy', 'Science Fiction', 'Mystery', 'Drama'],
            'genre 3': ['Romance', 'Fantasy', 'Thriller', 'Adventure'],
            'numRatings': [100, 200, 150, 300],
            'rating': [4.5, 3.8, 4.0, 4.2]
        }
        self.user_ratings_data = {
            'book_id': [2, 3, 4, 5],
            'Rating': [4, 5, 3, 4]
        }

    def test_read_books_from_excel(self):
        # Create a sample Excel file with the test data
        books_df = pd.DataFrame(self.books_data)
        books_df.to_excel(BOOKS_FILE_PATH, index=False)

        # Test reading books from the Excel file
        df = read_books_from_excel(BOOKS_FILE_PATH)
        self.assertTrue(df.equals(books_df))

    def test_read_user_preferences(self):
        # Test user input for favorite genres
        user_input = 'Fiction, Fantasy, Romance'
        with unittest.mock.patch('builtins.input', return_value=user_input):
            genres = read_user_preferences()
            self.assertEqual(genres, ['Fiction', ' Fantasy', ' Romance'])

    def test_filter_books_by_genre(self):
        # Test filtering books by genre
        books_df = pd.DataFrame(self.books_data)
        user_fav_genres = ['Fiction', 'Fantasy']
        filtered_books_df = filter_books_by_genre(books_df, user_fav_genres)
        expected_books_df = books_df.iloc[[0, 2]].reset_index(drop=True)
        self.assertTrue(filtered_books_df.equals(expected_books_df))

    def test_read_user_ratings(self):
        # Create a sample CSV file with the test data
        user_ratings_df = pd.DataFrame(self.user_ratings_data)
        user_ratings_df.to_csv(USER_RATINGS_FILE_PATH, index=False)

        # Test reading user ratings from the CSV file
        user_rated_book_ids = read_user_ratings(USER_RATINGS_FILE_PATH)
        self.assertEqual(user_rated_book_ids, [2, 3, 4, 5])

    def test_filter_books_by_user_ratings(self):
        # Test filtering books by user ratings
        books_df = pd.DataFrame(self.books_data)
        user_rated_book_ids = [2, 3]
        filtered_books_df = filter_books_by_user_ratings(books_df, user_rated_book_ids)
        expected_books_df = books_df.iloc[[0, 3]].reset_index(drop=True)
        self.assertTrue(filtered_books_df.equals(expected_books_df))

    def test_calculate_weighted_score(self):
        # Test calculating weighted score
        books_df = pd.DataFrame(self.books_data)
        collab_filtered_books_df = pd.DataFrame({
            'book_id': [1, 2],
            'numRatings': [100, 200],
            'rating': [4.5, 3.8]
        })
        expected_weighted_scores = [4.47, 3.75]
        collab_filtered_books_df = calculate_weighted_score(collab_filtered_books_df, books_df)
        for idx, row in collab_filtered_books_df.iterrows():
            self.assertAlmostEqual(row['weighted_score'], expected_weighted_scores[idx], places=2)

    # Add more test cases for other functions if needed

    def tearDown(self):
        # Clean up any test files generated during testing
        import os
        if os.path.exists(BOOKS_FILE_PATH):
            os.remove(BOOKS_FILE_PATH)
        if os.path.exists(USER_RATINGS_FILE_PATH):
            os.remove(USER_RATINGS_FILE_PATH)


if __name__ == '__main__':
    unittest.main()
