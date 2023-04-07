import uvicorn
from fastapi import FastAPI

from api.rsvp import crud

app = FastAPI()
app.include_router(crud.router, tags=["RSVP"])


@app.get("/ding")
async def ding():
    """Mic Check hahaha // I be anti-myth rhythm rock shocker"""
    return "Dong!"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
