from typing import List

from fastapi import APIRouter, Depends, Query
from sqlmodel import Session, select

from api.orm.models import Guest, GuestRead
from api.db import get_session

router = APIRouter(prefix="/guests")


@router.get("", response_model=List[GuestRead])
async def retrieve_guests(
    *,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
    name: None | str = None,
    has_plus_one: None | bool = None
):
    stmt = select(Guest).offset(offset).limit(limit)
    if name:
        stmt = stmt.where(Guest.name == name)
    if has_plus_one:
        stmt = stmt.where(Guest.has_plus_one == has_plus_one)
    rsvps = session.exec(stmt).all()
    return rsvps
