import pandas as pd

book_features_df = pd.read_excel('Best_Books.xlsx')
book_interactions_df = pd.read_csv('goodreads_interactions.csv')

df = pd.merge(book_features_df, book_interactions_df, on='book_id', how='left', validate='one_to_many')

df = df.dropna()
df = df.drop_duplicates()

popularity_score = df.groupby('book_id').agg({'is_read': 'sum', 'rating': 'mean', 'likedPercent': 'mean', 'numRatings': 'mean'})
popularity_score['popularity'] = popularity_score['is_read'] / popularity_score['is_read'].sum() + popularity_score['rating'] + popularity_score['likedPercent'] + popularity_score['numRatings']
popularity_score = popularity_score.sort_values(by='popularity', ascending=False).head(50)

popular_books = book_features_df.loc[book_features_df['book_id'].isin(popularity_score.index)]
popular_books = pd.merge(popular_books, popularity_score, on='book_id', how='left').sort_values(by='popularity', ascending=False)
print(popular_books[['book_id', 'title', 'popularity']])
