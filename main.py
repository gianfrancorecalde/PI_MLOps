import pandas as pd
import numpy as np

from fastapi import FastAPI

app = FastAPI() #

games = pd.read_parquet('steam_Games')
items = pd.read_parquet('user_items')
reviews = pd.read_parquet('user_Reviews')

@app.get("/PlayTimeGenre/{genero}")
async def PlayTimeGenre(genero :str):
    
    games
    return {"message": "Hello World"}