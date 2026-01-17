from fastapi import FastAPI
from .routers import model
from .routers.movies import movies

app = FastAPI()
app.include_router(movies.router)
app.include_router(model.router)

@app.get('/')
def home():
    return 'this is home'
