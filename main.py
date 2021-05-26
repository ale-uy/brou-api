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

@app.get("/sex_education", response_class=HTMLResponse)
def api_flix():
    try:
        return """
            <html>
                <head>
                    <title>Flix App</title>
                </head>
                <body>
                    <center>
                        <h1>Sex Education (español)</h1>
                        <h2>Temporada 1</h2>
                        <h3><a href="https://www.fembed.com/v/05ol3j-mno6">Capitulo 1</a></h3>
                        <h3><a href="https://www.fembed.com/v/2w9m6j8elo6">Capitulo 2</a></h3>
                        <h3><a href="https://femax20.com/v/mzokwj8m1oq">Capitulo 3</a></h3>
                        <h3><a href="https://femax20.com/v/7qv7lp2zw9g">Capitulo 4</a></h3>
                        <h3><a href="https://femax20.com/v/5jo41dmzxo0">Capitulo 5</a></h3>
                        <h3><a href="https://femax20.com/v/8xop148mqo7">Capitulo 6</a></h3>
                        <h3><a href="https://femax20.com/v/dw9rq78ppog">Capitulo 7</a></h3>
                        <h3><a href="https://www.fembed.com/v/54oy6zxnxvl">Capitulo 8</a></h3>
                    </center>
                </body>
            </html>
        """
    except Exception as e:
        return 'No funciona, error: {}'.format(e)

@app.get("/", response_class=HTMLResponse)
def root():
    try:
        return """
            <html>
                <head>
                    <title>Flix App</title>
                </head>
                <body>
                    <center><h1>"BIENVENID@ :)"</h1></center>
                </body>
            </html>
        """
    except Exception as e:
        return 'No funciona, error: {}'.format(e)
