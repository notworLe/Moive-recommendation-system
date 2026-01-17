import asyncio
import httpx

class TheMovieDataBase:
    def __init__(self, api_key):
        self.api_key = api_key

    async def search_movie(self, name: str):
        endpoint = "https://api.themoviedb.org/3/search/movie"
        params = {
            "api_key": self.api_key,
            "query": name
        }

        # Handle long request
        async with httpx.AsyncClient() as client:
            response = await client.get(endpoint, params=params)

        return response.json()

