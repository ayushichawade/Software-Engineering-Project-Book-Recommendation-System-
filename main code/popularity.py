import pandas as pd

def load_data():
    # Load the CSV files
    book_features_df = pd.read_excel('Best_Books.xlsx')
    book_interactions_df = pd.read_csv('goodreads_interactions.csv')
    return book_features_df, book_interactions_df

def merge_datasets(book_features_df, book_interactions_df):
    # Merge the two datasets on book_id
    merged_df = pd.merge(book_features_df, book_interactions_df, on='book_id', how='left', validate='one_to_many')
    return merged_df

def clean_data(df):
    # Remove any duplicate entries or books with missing values
    df = df.dropna()
    df = df.drop_duplicates()
    return df

def calculate_popularity_score(df):
    # Calculate the popularity score
    popularity_score = df.groupby('book_id').agg({'is_read': 'sum', 'rating': 'mean', 'likedPercent': 'mean', 'numRatings': 'mean'})
    popularity_score['popularity'] = popularity_score['is_read'] / popularity_score['is_read'].sum() + popularity_score['rating'] + popularity_score['likedPercent'] + popularity_score['numRatings']
    popularity_score = popularity_score.sort_values(by='popularity', ascending=False).head(50)
    return popularity_score

def display_popular_books(book_features_df, popularity_score):
    # Display the top 50 popular books
    popular_books = book_features_df.loc[book_features_df['book_id'].isin(popularity_score.index)]
    popular_books = pd.merge(popular_books, popularity_score, on='book_id', how='left', validate='one_to_one').sort_values(by='popularity', ascending=False)
    print(popular_books[['book_id', 'title', 'popularity']])

if __name__ == '__main__':
    # Load data
    book_features_df, book_interactions_df = load_data()

    # Merge datasets
    merged_df = merge_datasets(book_features_df, book_interactions_df)

    # Clean data
    cleaned_df = clean_data(merged_df)

    # Calculate popularity score
    popularity_score = calculate_popularity_score(cleaned_df)

    # Display popular books
    display_popular_books(book_features_df, popularity_score)
