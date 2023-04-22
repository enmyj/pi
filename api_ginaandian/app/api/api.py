import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.rsvp import crud, guests

app = FastAPI()
app.include_router(crud.router, tags=["RSVP"])
app.include_router(guests.router, tags=["Guests"])

origins = [
    "https://ginaandian.com",
    "http://localhost:8000"

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/miccheck")
async def miccheck():
    """Mic Check hahaha // I be anti-myth rhythm rock shocker"""
    return "hahaha"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
