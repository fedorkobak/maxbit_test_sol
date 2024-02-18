import pickle
from fastapi import FastAPI

import pandas as pd

with open("model.pck", "rb") as f:
    model = pickle.load(f)
games = (
    pd.read_parquet("ml_test_rec_sys.parquet")
    ["GameTitle"].unique().tolist()
)
app = FastAPI()

@app.get("/")
def get_recommendations(user_id : str)->list:
    '''
    Получить рекомендации для некоторого 
    пользователя.
    
    Arguments
    ----------
    user_id : str
        id пользователя для котого 
        требуется получить рекомендации.

    Returns
    ----------
    out : list
        список названий игр отсортированный так,
        чтобы на более ранних позициях появлялись
        те игры, которые пользователь оценит высоко.
    '''
    res = {
        game : model.predict(user_id, game).est
        for game in games
    }
    res = sorted(
        res.keys(), key=lambda k: res[k], reverse=True
    )

    return res