from fastapi import APIRouter, FastAPI

from api.guests import crud

app = FastAPI()

api_v1_router = APIRouter()
api_v1_router.include_router(crud.router, tags=["Guests"])




appv1 = FastAPI()
appv1.include_router(crud.router, tags=["Users"])


import uvicorn
from fastapi import FastAPI
from mangum import Mangum

from app.api import appv1
from app.orm.models import SQLModel
from app.utils.db import get_postgres_engine


# For API Gateway with HTTP setup, using a $default stage + other named/versioned stages
# as necessary). All versioning here handled on FastAPI-side using the sub-application.
# There are lots of other ways to do this, though...
app = FastAPI()
app.mount("/v1", appv1)
lambda_handler = Mangum(app)


# NOTE: AWS HTTP Gateway automatically reserves /ping for heatlh check lol!
@app.get("/ding")
async def ding():
    """Mic Check hahaha // I be anti-myth rhythm rock shocker"""
    return "Dong!"


# temporary table create, useful for testing (do this with Alembic for real)
@app.on_event("startup")
def on_startup():
    engine = get_postgres_engine()
    SQLModel.metadata.create_all(engine, checkfirst=True)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)