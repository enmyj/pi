from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select

from api.orm.models import User, UserRead, UserUpdate
from api.db import get_session

router = APIRouter(prefix="/users")


@router.get("", response_model=List[UserRead])
async def retrieve_users(
    *,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
):
    users = session.exec(select(User).offset(offset).limit(limit)).all()
    return users


@router.get("/{id}", response_model=UserRead)
async def retrieve_user(*, session: Session = Depends(get_session), id: int):
    user = session.get(User, id)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    return user


@router.post("", response_model=UserRead)
async def create_user(body: dict, session: Session = Depends(get_session)):
    flattened_body = flatten(body, target_fields=TARGET_USER_FIELDS)
    if not flattened_body:
        raise HTTPException(
            status_code=400,
            detail=(
                "None of the expected target keys were "
                f"found in POST body: {TARGET_USER_FIELDS}"
            ),
        )

    user = User(**flattened_body)
    session.add(user)
    session.commit()
    return user


@router.patch("/{id}", response_model=UserRead)
async def update_user(
    *, session: Session = Depends(get_session), id: int, user: UserUpdate
):
    db_user = session.get(User, id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    user_data = user.dict(exclude_unset=True)
    for key, value in user_data.items():
        setattr(db_user, key, value)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


@router.delete("/{id}")
async def delete_user(*, session: Session = Depends(get_session), id: int):

    user = session.get(User, id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    session.delete(user)
    session.commit()
    return {"ok": True}
