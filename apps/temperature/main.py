import uvicorn
from fastapi import FastAPI
from handlers.temperature import temperature_router

app = FastAPI()
app.include_router(temperature_router, prefix="/temperature", tags=["temperature"])


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8081)
