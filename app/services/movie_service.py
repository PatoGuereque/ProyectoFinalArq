import os
import pandas as pd
from ..models import User

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, '../data/movie_results.csv')

movies_df = pd.read_csv(filename)

class MovieService:
    def query_movies(request, user: User):
        preferences = list(map(int, user.preferences.split(',')))
        result = 1
        for preference in preferences:
            result *= preference
        result %= 5
        result += 1
        ascending = request.args.get('rating', 'true') == "false"
        movies = movies_df[movies_df['preference_key'] == result].sort_values(by='rating', ascending=ascending).head(n = 10)[["movie_title", "rating", "year"]]
        return movies.to_string()