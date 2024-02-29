import pandas as pd


def read_books_from_excel(file_path):
    return pd.read_excel(file_path)


def read_user_preferences():
    return input('Enter your favorite genres (separated by commas): ').split(',')


def filter_books_by_genre(books_df, user_fav_genres):
    genre_cols = ['genre 1', 'genre 2', 'genre 3', 'genre 4', 'genre 5']
    matched_books_df = books_df[books_df[genre_cols].isin(user_fav_genres).any(axis=1)]
    genre_counts = matched_books_df[genre_cols].apply(lambda x: sum(x.isin(user_fav_genres)), axis=1)
    return matched_books_df[genre_counts >= 2].reset_index(drop=True)


def read_user_ratings(file_path):
    user_df = pd.read_csv(file_path)
    return user_df[user_df['Rating'] >= 4]['book_id'].unique()


def filter_books_by_user_ratings(matched_books_df, user_rated_book_ids):
    return matched_books_df[~matched_books_df['book_id'].isin(user_rated_book_ids)]


def calculate_weighted_score(collab_filtered_books_df, books_df):
    C = books_df['rating'].mean()
    m = books_df['numRatings'].quantile(0.9)
    collab_filtered_books_df['weighted_score'] = (
        (collab_filtered_books_df['numRatings'] / (collab_filtered_books_df['numRatings'] + m) * collab_filtered_books_df['rating']) +
        (m / (collab_filtered_books_df['numRatings'] + m) * C)
    )
    return collab_filtered_books_df


def print_recommendations(collab_filtered_books_df, user_fav_genres):
    print(f"Recommended books for {', '.join(user_fav_genres)}:\n")
    for i, book in collab_filtered_books_df.head(10).iterrows():
        print(f"{i+1}. {book['book_id']} ({book['title']}) - {book['weighted_score']:.2f} weighted score, {book['likedPercent']}% liked")


def main():
    books_df = read_books_from_excel('Best_Books.xlsx')
    user_fav_genres = read_user_preferences()
    matched_books_df = filter_books_by_genre(books_df, user_fav_genres)
    user_rated_book_ids = read_user_ratings('goodreads_interactions (1).csv')
    collab_filtered_books_df = filter_books_by_user_ratings(matched_books_df, user_rated_book_ids)
    collab_filtered_books_df = calculate_weighted_score(collab_filtered_books_df, books_df)
    collab_filtered_books_df = collab_filtered_books_df.sort_values('weighted_score', ascending=False).reset_index(drop=True)
    print_recommendations(collab_filtered_books_df, user_fav_genres)


if __name__ == "__main__":
    main()
