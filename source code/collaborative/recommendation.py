import pandas as pd


books_df = pd.read_excel('Best_Books.xlsx')


user_fav_genres = input('Enter your favorite genres (separated by commas): ').split(',')


genre_cols = ['genre 1', 'genre 2', 'genre 3', 'genre 4','genre 5']
matched_books_df = books_df[books_df[genre_cols].isin(user_fav_genres).any(axis=1)]
genre_counts = matched_books_df[genre_cols].apply(lambda x: sum(x.isin(user_fav_genres)), axis=1)
matched_books_df = matched_books_df[genre_counts >= 2].reset_index(drop=True)


user_df = pd.read_csv('goodreads_interactions (1).csv')
user_ratings_df = user_df[user_df['Rating'] >= 4]
user_rated_book_ids = user_ratings_df['book_id'].unique()
collab_filtered_books_df = matched_books_df[~matched_books_df['book_id'].isin(user_rated_book_ids)]


C = books_df['rating'].mean()
m = books_df['numRatings'].quantile(0.9)
collab_filtered_books_df['weighted_score'] = (collab_filtered_books_df['numRatings'] / (collab_filtered_books_df['numRatings'] + m) * collab_filtered_books_df['rating']) + (m / (collab_filtered_books_df['numRatings'] + m) * C)


collab_filtered_books_df = collab_filtered_books_df.sort_values('weighted_score', ascending=False).reset_index(drop=True)
print(f"Recommended books for {', '.join(user_fav_genres)}:\n")
for i, book in collab_filtered_books_df.head(10).iterrows():
    print(f"{i+1}. {book['book_id']} ({book['title']}) - {book['weighted_score']:.2f} weighted score, {book['likedPercent']}% liked")
