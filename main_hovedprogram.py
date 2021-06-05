from fastapi import FastAPI

from core import settings


app = FastAPI(Title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)

@app.get("/")
def hello_api():
    return {"detail":"Hello World"}
