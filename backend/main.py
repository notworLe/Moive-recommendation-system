from fastapi import FastAPI
from .routers import poster
from models.recommendation import Recommendation

model = Recommendation()

app = FastAPI()
app.include_router(poster.router)

@app.get('/')
async def home():
    return 'this is home'

@app.get('/recommend')
async def recommend(name_moive: str, limit: int = 10):
    try:
        return model.recommend(name_movie=name_moive, limit=limit)
    except Exception as e:
        return str(e)

@app.get('/movies/name')
def name():
    try:
        return list(model.get_name_movie())
    except Exception as e:
        return str(e)


