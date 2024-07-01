# from fastapi import FastAPI, Body, Response, status
# from src.model_training import load_model, prediction
import joblib
from pydantic import BaseModel
import pandas as pd
from flask import Flask, request, jsonify

class Data(BaseModel):
    year: int = None
    month: int
    stateDescription: int
    sectorName: int

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

@app.route("/predict", methods=['POST'])
def predict():
    data = request.get_json()
    df = pd.DataFrame([data])
    model = joblib.load("data/model/main.joblib")
    preds = model.predict(df)
    return "The predicted income is: " + str(preds[0])
    
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80)