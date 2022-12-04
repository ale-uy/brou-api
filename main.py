#!/usr/bin/env python3

from fastapi import FastAPI
import scraper_brou
import scraper_bs
import uvicorn


#app = flask.Flask(__name__)

app = FastAPI()

@app.get("/v1")
def api_brou():
    try:
        datos = scraper_brou.query()
        return datos
    except Exception as e:
        return 'No funciona el scraper, error: {}'.format(e)

@app.get("/v2")
def api_brou_2():
    try:
        datos = scraper_bs.query()
        return datos
    except Exception as e:
        return 'No funciona el scraper, error: {}'.format(e)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
