from fastapi import FastAPI
import scraper_brou

app = FastAPI()

#domain where this api is hosted for example : localhost:5000/docs to see swagger documentation automagically generated.


@app.get("/")
def home():
    data = scraper_brou.query()
    return data
