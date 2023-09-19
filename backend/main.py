from fastapi import FastAPI

from app.api.routes import router
from app.loader import init_pool

app = FastAPI()
app.include_router(router)


@app.on_event("startup")
async def startup_event():
    await init_pool()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
