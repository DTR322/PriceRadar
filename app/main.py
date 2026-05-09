from fastapi import FastAPI
from app.finance.router import router as router_products

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(router_products)