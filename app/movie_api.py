import requests
from flask import current_app

def search_movie_by_title(title):
    api_key = current_app.config["OMDB_API_KEY"]

    url = "https://www.omdbapi.com/"
    params = {
        "apikey": api_key,
        "t": title
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

    if data.get("Response") == "False":
        return {"error": data.get("Error", "Movie not found")}

    return data