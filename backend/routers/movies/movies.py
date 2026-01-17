from fastapi import APIRouter, HTTPException
from backend.routers.model import model
from .moviesDB import TheMovieDataBase
from ... import schemas

MOVIES_DB = TheMovieDataBase("a224d1984c5771d15fc531a47dae66fb")

IMAGE_PATH = "https://image.tmdb.org/t/p/w500"

router = APIRouter(
    prefix='/movies',
    tags=['movies']
)

# Try
#   "Tom and Huck (1995)",
#   "Sudden Death (1995)",
#   "Sudden Death (1995)",
@router.get('/{name_movie}', response_model=schemas.Movie)
async def get_image_path(name_movie: str):
    if name_movie not in model.data.index:
        raise HTTPException(status_code=404, detail=f'Can\'t found the movie name: {name_movie}')

    # Fix error can't found movie in TMDB
    name_length = len(name_movie)
    name_request = name_movie
    if name_length >= 10:
        name_request =  name_movie[:name_length // 2]

    # Request to TMDB
    response = await MOVIES_DB.search_movie(name_request)
    print('Loading.... to TMDB')

    if response['total_results'] == 0:
        raise HTTPException(status_code=404, detail='The Movie DataBase return 0 result')

    # Get the first movie after search
    first_movie = response['results'][0]


    return {
        'name': name_movie,
        'genres':  model.data.loc[name_movie, 'genres'],
        'image_url': f'{IMAGE_PATH}{first_movie['poster_path']}'
    }



