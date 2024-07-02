import pandas as pd
import numpy as np
from scipy.spatial.distance import cosine

# Sample data
data = {
    'user_id': [1, 1, 1, 2, 2, 2, 3, 3, 3],
    'match_id': [1, 2, 4, 1, 2, 4, 1, 3, 4],
    'team1': ['Liverpool', 'Real Madrid', 'Inter Miami',
              'Liverpool', 'Real Madrid', 'Inter Miami',
              'Liverpool', 'Real Madrid', 'Inter Miami'],
    'team2': ['Barcelona', 'Manchester City', 'Al Nassr',
              'Barcelona', 'Manchester City', 'Al Nassr',
              'Athletico Madrid', 'Al Nassr', 'Manchester City'],
    'rating': [5, 3, 2, 4, 2, 5, 2, 5, 4]
}
df = pd.DataFrame(data)
user_match_matrix = df.pivot_table(index='user_id', columns='match_id', values='rating')
user_match_matrix = user_match_matrix.fillna(0)


# Similarity
def calculate_user_similarity(matrix):
    similarity_matrix = np.zeros((matrix.shape[0], matrix.shape[0]))
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[0]):
            if i != j:
                similarity_matrix[i, j] = 1 - cosine(matrix[i], matrix[j])
    return similarity_matrix

user_similarity_matrix = calculate_user_similarity(user_match_matrix.values)


# Recommend football matches
def recommend_matches_for_user(user_id, user_match_matrix, user_similarity_matrix, matches_data, n_recommendations=3):
    user_index = user_id - 1
    similar_users_indices = np.argsort(user_similarity_matrix[user_index])[::-1]
    recommendations = {}

    for similar_user_index in similar_users_indices:
        if similar_user_index != user_index:
            similar_user_ratings = user_match_matrix.iloc[similar_user_index]
            for match_id, rating in similar_user_ratings.items():
                if user_match_matrix.iloc[user_index][match_id] == 0:
                    team1 = matches_data.loc[matches_data['match_id'] == match_id, 'team1'].values[0]
                    team2 = matches_data.loc[matches_data['match_id'] == match_id, 'team2'].values[0]
                    match_name = f"{team1} vs {team2}"
                    if match_id not in recommendations:
                        recommendations[match_id] = {
                            'match_name': match_name,
                            'rating_sum': rating
                        }
                    else:
                        recommendations[match_id]['rating_sum'] += rating

    # Sort recommendations by rating
    sorted_recommendations = sorted(recommendations.items(), key=lambda x: x[1]['rating_sum'], reverse=True)

    # Get recommendations
    top_recommendations = sorted_recommendations[:n_recommendations]

    return top_recommendations


# Example usage for all users
matches_data = df[['match_id', 'team1', 'team2']].drop_duplicates().reset_index(drop=True)

for user_id in range(1, 4):
    recommended_matches = recommend_matches_for_user(user_id, user_match_matrix, user_similarity_matrix, matches_data, n_recommendations=3)
    print(f"Recommended football matches for user {user_id}:")
    for match_id, info in recommended_matches:
        print(f"Match Name: {info['match_name']}, Predicted Rating Sum: {info['rating_sum']}")
    print()  
