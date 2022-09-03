#!/usr/bin/env python3
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import scraper_brou
import scraper_bs


app = FastAPI()

@app.get("/api_brou/v1")
def api_brou():
    try:
        datos = scraper_brou.query()
        return datos
    except Exception as e:
        return 'No funciona el scraper, error: {}'.format(e)

@app.get("/api_brou/v2")
def api_brou_2():
    try:
        datos = scraper_bs.query()
        return datos
    except Exception as e:
        return 'No funciona el scraper, error: {}'.format(e)
