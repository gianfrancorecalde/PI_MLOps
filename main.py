import pandas as pd
import numpy as np
import FastAPI
import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/")
def PlayTimeGenre(genero: str):
    return 