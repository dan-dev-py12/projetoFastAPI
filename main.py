from fastapi import FastAPI

app = FastAPI()

from auth_routes import auth_routes
from order_routes import order_routes


@app.get("/ordens")
def get
# para rodar o nosso codigo executar no terminal: uvicorn main:app --reload