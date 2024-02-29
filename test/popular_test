import pandas as pd

class TestBookRecommendation(unittest.TestCase):
    def setUp(self):
        self.book_features_df = pd.read_excel('Best_Books.xlsx')
        self.book_interactions_df = pd.read_csv('goodreads_interactions.csv')
        # Load sample data for testing
        self.book_features_df = pd.DataFrame({
            'book_id': [1, 2, 3],
            'title': ['The Hunger Games', 'Harry Potter and the Order of the Phoenix', 'To Kill a Mockingbird']
        })
        self.book_interactions_df = pd.DataFrame({
            'book_id': [1, 2, 2, 3],
            'is_read': [True, True, False, True],
            'rating': [4, 5, None, 3],
            'likedPercent': [80, 90, None, 70],
            'numRatings': [100, 50, None, 120]
        })

    def test_data_loading(self):
        self.assertIsNotNone(self.book_features_df)
        self.assertIsNotNone(self.book_interactions_df)

    def test_merge_data(self):
        df = pd.merge(self.book_features_df, self.book_interactions_df, on='book_id', how='left', validate='one_to_many')
        self.assertFalse(df.empty)

    def test_data_cleanup(self):
        df = pd.merge(self.book_features_df, self.book_interactions_df, on='book_id', how='left', validate='one_to_many')
        df = df.drop_duplicates()
        df = df.dropna()
        self.assertEqual(len(df), 3)  # Check if duplicates and missing values are removed

    def test_popularity_calculation(self):
        df = pd.merge(self.book_features_df, self.book_interactions_df, on='book_id', how='left', validate='one_to_many')
        df = df.drop_duplicates()
        df = df.dropna()

        popularity_score = df.groupby('book_id').agg({'is_read': 'sum', 'rating': 'mean', 'likedPercent': 'mean', 'numRatings': 'mean'})
        popularity_score['popularity'] = popularity_score['is_read'] / popularity_score['is_read'].sum() + popularity_score['rating'] + popularity_score['likedPercent'] + popularity_score['numRatings']
        popularity_score = popularity_score.sort_values(by='popularity', ascending=False).head(50)

        self.assertFalse(popularity_score.empty)

    def test_popular_books_display(self):
        df = pd.merge(self.book_features_df, self.book_interactions_df, on='book_id', how='left', validate='one_to_many')
        df = df.drop_duplicates()
        df = df.dropna()

        popularity_score = df.groupby('book_id').agg({'is_read': 'sum', 'rating': 'mean', 'likedPercent': 'mean', 'numRatings': 'mean'})
        popularity_score['popularity'] = popularity_score['is_read'] / popularity_score['is_read'].sum() + popularity_score['rating'] + popularity_score['likedPercent'] + popularity_score['numRatings']
        popularity_score = popularity_score.sort_values(by='popularity', ascending=False).head(50)

        popular_books = pd.merge(self.book_features_df, popularity_score, on='book_id', how='left', validate='one_to_one')
        self.assertFalse(popular_books.empty)

if __name__ == '__main__':
    unittest.main()
