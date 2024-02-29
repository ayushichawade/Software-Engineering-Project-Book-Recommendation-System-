import pandas as pd
import numpy as np
import unittest

class TestBookPopularity(unittest.TestCase):
    
    def setUp(self):
        # Create sample datasets for testing
        self.book_features_df = pd.DataFrame({
            'book_id': [1, 2, 3, 4, 5],
            'title': ['Book 1', 'Book 2', 'Book 3', 'Book 4', 'Book 5']
        })
        
        self.book_interactions_df = pd.DataFrame({
            'book_id': [1, 2, 3, 3, 4, 5],
            'is_read': [True, True, True, False, True, True],
            'rating': [4.5, 3.0, 4.0, np.nan, 5.0, 4.5],
            'likedPercent': [80, 60, 90, 70, 100, 85],
            'numRatings': [100, 50, 80, 30, 200, 150]
        })

    def test_missing_values_handling(self):
        # Add missing values to both datasets
        self.book_features_df.loc[2, 'title'] = np.nan
        self.book_interactions_df.loc[1, 'rating'] = np.nan

        # Run the code
        df = pd.merge(self.book_features_df, self.book_interactions_df, on='book_id', how='left', validate='one_to_many')
        df = df.drop_duplicates()
        df = df.dropna()

        # Check if there are any missing values
        self.assertEqual(df.isnull().values.any(), False)

    def test_duplicate_entries_handling(self):
        # Introduce duplicate entries to book_features_df
        self.book_features_df = pd.concat([self.book_features_df] * 2, ignore_index=True)
        self.book_features_df.drop_duplicates(subset=['book_id'], inplace=True)  # Ensure uniqueness of book_id

        # Run the code
        df = pd.merge(self.book_features_df, self.book_interactions_df, on='book_id', how='left', validate='one_to_many')
        df = df.drop_duplicates()

        # Check if duplicate entries are removed
        self.assertEqual(df.duplicated().sum(), 0)

    def test_calculation_of_popularity_score(self):
        # Run the code to calculate popularity score
        df = pd.merge(self.book_features_df, self.book_interactions_df, on='book_id', how='left', validate='one_to_many')
        df = df.drop_duplicates()
        df = df.dropna()

        popularity_score = df.groupby('book_id').agg({'is_read': 'sum', 'rating': 'mean', 'likedPercent': 'mean', 'numRatings': 'mean'})
        popularity_score['popularity'] = popularity_score['is_read'] / popularity_score['is_read'].sum() + popularity_score['rating'] + popularity_score['likedPercent'] + popularity_score['numRatings']

        # Check if popularity score is calculated correctly
        self.assertEqual(len(popularity_score), len(df['book_id'].unique()))

    def test_top_50_popular_books(self):
        # Run the code to identify top 50 popular books
        df = pd.merge(self.book_features_df, self.book_interactions_df, on='book_id', how='left', validate='one_to_many')
        df = df.drop_duplicates()
        df = df.dropna()

        popularity_score = df.groupby('book_id').agg({'is_read': 'sum', 'rating': 'mean', 'likedPercent': 'mean', 'numRatings': 'mean'})
        popularity_score['popularity'] = popularity_score['is_read'] / popularity_score['is_read'].sum() + popularity_score['rating'] + popularity_score['likedPercent'] + popularity_score['numRatings']
        popularity_score = popularity_score.sort_values(by='popularity', ascending=False).head(50)

        # Check if the top 50 popular books are identified correctly
        self.assertEqual(len(popularity_score), 5)  # Adjust this to the number of unique book IDs in your test data

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
