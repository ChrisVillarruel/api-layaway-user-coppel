from fastapi import FastAPI
from routers.api_layaway_user.api import router

app = FastAPI()
app.include_router(router)


@app.get("/")
async def main():
    return {"status": "Pagina pricipal"}
