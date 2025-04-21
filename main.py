
from fastapi import FastAPI, HTTPException
import pandas as pd
import requests

app = FastAPI()

data = pd.read_csv("worldbank_countries.csv")

@app.get("/country/{name}")
def get_country(name : str):
    result = data[data["Country"].str.lower() == name.lower()]
    if result.empty:
        raise HTTPException(status_code = 404, detail = "Country not found")
    return {
        "Country": result.iloc[0]["Country"],
        "URL": result.iloc[0]["URL"]
        }


@app.get("/meta/{code}")
def get_country_metadata(code: str):
    url = f"https://api.worldbank.org/v2/country/{code.upper()}?format=json"
    print("fethching:", url)
    response = requests.get(url)

    try:
        data = response.json()
        info = data[1][0]

        return {
            "Country": info['name'],
            "Capital": info['capitalCity'],
            "Region": info['region']['value'],
            "Income level": info['incomeLevel']['value'],
            "Lending Type": info['lendingType']['value']
        }
    except Exception as e:
        print("Error while parsing", e)
        raise HTTPException(status_code = 500, detail = "Unexpected error")