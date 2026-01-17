from fastapi import APIRouter, HTTPException
from models.recommendation import Recommendation

model = Recommendation()

router = APIRouter(
    prefix='/models',
    tags=['models']
)

@router.get('/recommend')
def recommend(movie_name: str, limit: int = 10):
    if movie_name not in model.data.index:
        raise HTTPException(status_code=404, detail=f'Can\'t found the movie name: {movie_name}')
    return model.recommend(name_movie=movie_name, limit=limit)



@router.get('/get_all_name')
def name_movies():
    try:
        return list(model.get_name_movie())
    except Exception as e:
        return str(e)
