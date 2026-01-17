import requests

API_URL = "http://127.0.0.1:8000/"

def get_movie_image(name: str):
    endpoint = f'{API_URL}/movies/{name}'
    response = requests.get(endpoint)
    return response.json()

# recommended_movies = ['Rugrats Movie, The (1998)', 'Aladdin and the King of Thieves (1996)']

def recommend(name_moive: str, limit: int = 10):
    endpoint = f'{API_URL}/models/recommend'
    params = {
        "movie_name": name_moive,
        'limit': limit
    }
    response = requests.get(endpoint, params=params).json()
    return response


def get_all_name():
    endpoint = f'{API_URL}/models/get_all_name'
    response = requests.get(endpoint).json()
    return response

def get_info(name_movie: str):
    endpoint = f'{API_URL}/movies/{name_movie}'
    response = requests.get(endpoint)
    return response.json()
