import pandas as pd

def find_popular_books():
  
    book_features_df = pd.read_excel('Best_Books.xlsx')
    book_interactions_df = pd.read_csv('goodreads_interactions.csv')

    # Merge the two datasets on book_id
    df = pd.merge(book_features_df, book_interactions_df, on='book_id', how='left', validate='one_to_many')

    # Remove any duplicate entries or books with missing values
    df = df.dropna()
    df = df.drop_duplicates()

    # Calculate the popularity score
    popularity_score = df.groupby('book_id').agg({'is_read': 'sum', 'rating': 'mean', 'likedPercent': 'mean', 'numRatings': 'mean'})
    popularity_score['popularity'] = popularity_score['is_read'] / popularity_score['is_read'].sum() + popularity_score['rating'] + popularity_score['likedPercent'] + popularity_score['numRatings']
    popularity_score = popularity_score.sort_values(by='popularity', ascending=False).head(50)

    # Display the top 50 popular books
    popular_books = book_features_df.loc[book_features_df['book_id'].isin(popularity_score.index)]
    popular_books = pd.merge(popular_books, popularity_score, on='book_id', how='left', validate='one_to_one').sort_values(by='popularity', ascending=False)
    return popular_books[['book_id', 'title', 'popularity']]




import unittest

class TestOutput(unittest.TestCase):
    def test_output_length(self):
        actual_output = find_popular_books()
        self.assertEqual(len(actual_output), 50, "Incorrect number of popular books.")
        
    def test_output_uniqueness(self):
        actual_output = find_popular_books()
        self.assertTrue(actual_output['book_id'].is_unique, "Duplicate book IDs found.")
        
    def test_output_title_not_empty(self):
        actual_output = find_popular_books()
        self.assertFalse(actual_output['title'].str.strip().str.len().eq(0).any(), "Empty titles found.")
        
    def test_output_popularity_non_negative(self):
        actual_output = find_popular_books()
        self.assertTrue((actual_output['popularity'] >= 0).all(), "Negative popularity score found.")

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
