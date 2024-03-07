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
    # Create a new DataFrame with no duplicate entries or books with missing values
    cleaned_df = df.dropna().drop_duplicates()
    return cleaned_df

def calculate_popularity_score(df, score_function):
    # Calculate the popularity score using a custom score function
    popularity_score = score_function(df)
    return popularity_score.head(50)

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

    # Define a higher-order function for calculating the popularity score
    def custom_popularity_score(df):
        # Define the score calculation
        score = df.groupby('book_id').agg({'is_read': 'sum', 'rating': 'mean', 'likedPercent': 'mean', 'numRatings': 'mean'})
        score['popularity'] = score['is_read'] / score['is_read'].sum() + score['rating'] + score['likedPercent'] + score['numRatings']
        return score.sort_values(by='popularity', ascending=False)

    # Calculate popularity score using the custom function
    popularity_score = calculate_popularity_score(cleaned_df, custom_popularity_score)

    # Display popular books
    display_popular_books(book_features_df, popularity_score)
