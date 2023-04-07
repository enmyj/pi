from typing import Optional

from sqlmodel import Field, SQLModel


class RSVPBase(SQLModel):
    name: str = Field(unique=True)
    plus_one_name: Optional[str]
    RSVP: bool
    shuttle: bool
    hotel_location: Optional[str]
    driving: Optional[bool]
    available_seats_in_car: Optional[int]
    food_restrictions: Optional[str]
    mobility_restrictions: Optional[str]
    children_count: Optional[int]


class RSVP(RSVPBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class RSVPCreate(RSVPBase):
    pass


class RSVPRead(RSVPBase):
    id: int
