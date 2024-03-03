import pandas as pd

def load_books_data(file_path):
    return pd.read_excel(file_path)

def get_user_favorite_genres():
    return input('Enter your favorite genres (separated by commas): ').split(',')

def filter_books_by_genre(all_books_df, user_fav_genres):
    genre_cols = ['genre 1', 'genre 2', 'genre 3', 'genre 4', 'genre 5']
    matched_books_df = all_books_df[all_books_df[genre_cols].isin(user_fav_genres).any(axis=1)]
    genre_counts = matched_books_df[genre_cols].apply(lambda x: sum(x.isin(user_fav_genres)), axis=1)
    return matched_books_df[genre_counts >= 2].reset_index(drop=True)

def load_user_ratings(file_path):
    user_df = pd.read_csv(file_path)
    return user_df[user_df['Rating'] >= 4]

def filter_books_by_user_ratings(matched_books_df, user_ratings_df):
    user_rated_book_ids = user_ratings_df['book_id'].unique()
    return matched_books_df[~matched_books_df['book_id'].isin(user_rated_book_ids)]

def calculate_weighted_scores(books_df):
    C = books_df['rating'].mean()
    m = books_df['numRatings'].quantile(0.9)
    books_df['weighted_score'] = (books_df['numRatings'] / (books_df['numRatings'] + m) * books_df['rating']) + (m / (books_df['numRatings'] + m) * C)
    return books_df.sort_values('weighted_score', ascending=False).reset_index(drop=True)

def display_recommendations(recommended_books_df, num_recommendations=10):
    print(f"Recommended books for {', '.join(user_fav_genres)}:\n")
    for i, book in recommended_books_df.head(num_recommendations).iterrows():
        print(f"{i+1}. {book['book_id']} ({book['title']}) - {book['weighted_score']:.2f} weighted score, {book['likedPercent']}% liked")

if __name__ == '__main__':
    # Load data
    all_books_df = load_books_data('Best_Books.xlsx')
    user_fav_genres = get_user_favorite_genres()
    
    # Filter books by user's favorite genres
    matched_books_df = filter_books_by_genre(all_books_df, user_fav_genres)
    
    # Load user ratings
    user_ratings_df = load_user_ratings('goodreads_interactions (1).csv')
    
    # Filter books by user ratings
    collab_filtered_books_df = filter_books_by_user_ratings(matched_books_df, user_ratings_df)
    
    # Calculate weighted scores
    collab_filtered_books_df = calculate_weighted_scores(collab_filtered_books_df)
    
    # Display recommendations
    display_recommendations(collab_filtered_books_df)
