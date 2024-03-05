import yaml

dsl_data = {
    'recommendations': {
        'by_genre': {
            'Mystery': recommend_by_genre.__doc__,
            # Add more genres here
        },
        'by_popularity': recommend_by_popularity.__doc__,
        'by_user_rating': recommend_by_user_rating.__doc__,
    }
}

with open('recommendations.dsl.yaml', 'w') as f:
    yaml.dump(dsl_data, f, default_flow_style=False)
