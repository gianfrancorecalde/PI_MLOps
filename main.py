import pandas as pd
import numpy as np
import datetime as dt

from fastapi import FastAPI

app = FastAPI() #

games = pd.read_parquet('steam_Games')
items = pd.read_parquet('user_Items')
reviews = pd.read_parquet('user_Reviews')

@app.get("/PlayTimeGenre/{genero}")
async def PlayTimeGenre(genero :str):
    df_merged = pd.merge(items, games, left_on='item_id', right_on='id')
    df_genres_filtrados = df_merged[df_merged['genres']==genero.lower]
    df_filtrado_final = pd.merge(reviews,df_genres_filtrados, on=['user_id','item_id'])
    agrupado = df_filtrado_final.groupby('posted')['playtime_forever'].sum()
    agrupado_ordenado = agrupado.sort_values(ascending=False)
    anio=agrupado_ordenado.idxmax()
    return {"Año de lanzamiento con más horas jugadas para Género "+genero : anio.year}

@app.get("/UserForGenre/{genero}")
async def UserForGenre(genero :str):
    return {"message": "Hello World"}

@app.get("/UsersRecommend/{genero}")
async def UsersRecommend(genero :str):
    return {"message": "Hello World"}

@app.get("/UsersNotRecommend/{genero}")
async def UsersNotRecommend(genero :str):
    return {"message": "Hello World"}

@app.get("/sentiment_analysis/{genero}")
async def sentiment_analysis(genero :str):
    return {"message": "Hello World"}