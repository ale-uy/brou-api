from fastapi import FastAPI
import scraper_brou

app = FastAPI()


@app.get("/api_brou/v1")
def api_brou():
    try:
        datos = scraper_brou.query()
        return datos
    except Exception as e:
        return 'No funciona el scraper, error: {}'.format(e)

