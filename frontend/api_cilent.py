import requests

API_URL = "http://127.0.0.1:8000/"

def get_movie_image(name: str):
    endpoint = f'{API_URL}/poster'
    params = {
        "query": name
    }
    response = requests.get(endpoint, params=params).json()
    return response

recommended_movies = ['Rugrats Movie, The (1998)', 'Aladdin and the King of Thieves (1996)']
a = [get_movie_image(movie) for movie in recommended_movies]
print(a)
def recommend(name_moive: str, limit: int = 10):
    endpoint = f'{API_URL}/recommend'
    params = {
        "name_moive": name_moive,
        'limit': limit
    }
    response = requests.get(endpoint, params=params).json()
    return response

def get_name_movies():
    endpoint = f'{API_URL}/movies/name'
    response = requests.get(endpoint).json()
    return response
