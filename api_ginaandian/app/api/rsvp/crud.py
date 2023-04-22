from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select
from sqlalchemy.dialects.postgresql import insert

from api.orm.models import RSVP, RSVPRead, RSVPCreate, RSVPUpdate, RSVPPost
from api.db import get_session

router = APIRouter(prefix="/rsvp")


@router.get("", response_model=List[RSVPRead])
async def retrieve_rsvps(
    *,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
    name: None | str = None
):
    stmt = select(RSVP).offset(offset).limit(limit)
    if name:
        stmt = stmt.where(RSVP.guest_name == name)
    rsvps = session.exec(stmt).all()
    return rsvps


@router.get("/{id}", response_model=RSVPRead)
async def retrieve_rsvp_by_id(*, session: Session = Depends(get_session), id: int):
    rsvp = session.get(RSVP, id)
    if not rsvp:
        raise HTTPException(status_code=404, detail="rsvp not found")
    return rsvp


@router.get("/guest/{guest_id}", response_model=RSVPRead)
async def retrieve_rsvp_by_guest_id(
    *, session: Session = Depends(get_session), guest_id: int
):
    rsvp = session.get(RSVP, guest_id)
    if not rsvp:
        raise HTTPException(status_code=404, detail="rsvp not found")
    return rsvp


@router.post("", response_model=RSVPRead)
async def create_rsvp(rsvp: RSVPCreate, session: Session = Depends(get_session)):
    rsvp_exists = session.execute(
        select(RSVP).where(RSVP.guest_name == rsvp.guest_name)
    ).scalar_one_or_none()
    if rsvp_exists:
        raise HTTPException(status_code=409, detail="RSVP for this name already exists")
    db_rsvp = RSVP.from_orm(rsvp)
    session.add(db_rsvp)
    session.commit()
    session.refresh(db_rsvp)
    return db_rsvp


@router.patch("/{id}", response_model=RSVPRead)
async def update_rsvp(
    id: int, rsvp: RSVPUpdate, session: Session = Depends(get_session)
):
    db_rsvp = session.get(RSVP, id)
    if not db_rsvp:
        raise HTTPException(status_code=404, detail="RSVP not found")
    rsvp_data = rsvp.dict(exclude_unset=True)
    for key, value in rsvp_data.items():
        setattr(db_rsvp, key, value)
    session.add(db_rsvp)
    session.commit()
    session.refresh(db_rsvp)
    return db_rsvp

# @router.post("", response_model=RSVPRead)
# async def upsert_rsvp(body: RSVPPost, session: Session = Depends(get_session)):
#     rsvp = session.execute(
#         select(RSVP).where(RSVP.guest_name == body.guest_name)
#     ).scalar_one_or_none()

#     if rsvp:



@router.delete("/{id}")
async def delete_rsvp(*, session: Session = Depends(get_session), id: int):

    rsvp = session.get(RSVP, id)
    if not rsvp:
        raise HTTPException(status_code=404, detail="RSVP not found")
    session.delete(rsvp)
    session.commit()
    return {"ok": True}
