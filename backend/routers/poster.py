import requests
from fastapi import APIRouter

API_KEY = "a224d1984c5771d15fc531a47dae66fb"
URL = "https://api.themoviedb.org/3/search/movie"
IMAGE_PATH = "https://image.tmdb.org/t/p/w500"

router = APIRouter(

)

@router.get('/poster')
def get_image_path(query: str, size: str=''):
    sizes = ['w200', 'w342', 'w500']
    if size != '':
        if size not in sizes:
            raise ValueError('Lỗi')
        size += f'/{size}'
    if len(query) >= 10:
        query =  query[:len(query)//2]
    params = {
        "api_key": API_KEY,
        "query": query
    }
    response = requests.get(URL, params=params).json()
    print(response)
    if response['total_results'] == 0:
        return None
    # Get the first movie after search
    first_movie = response['results'][0]
    return f'{IMAGE_PATH}{first_movie['poster_path']}{size}'


