from typing import Optional, List

from pydantic import BaseModel
from sqlmodel import Field, SQLModel, Relationship


class GuestBase(SQLModel):
    name: str = Field(unique=True)
    has_plus_one: bool


class RSVPBase(SQLModel):
    guest_name: str = Field(unique=True)
    plus_one_name: Optional[str]
    attending: bool
    shuttle_or_driving: Optional[str]
    shuttle_lodging_location: Optional[str]
    driving_num_seats: Optional[int]
    dietary_restrictions: Optional[str]
    mobility_restrictions: Optional[str]
    num_children: Optional[int]


class Guest(GuestBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    rsvps: Optional["RSVP"] = Relationship(back_populates="guests")


class RSVP(RSVPBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    guest_id: Optional[int] = Field(default=None, foreign_key="guest.id")
    guests: List[Guest] = Relationship(back_populates="rsvps")


class RSVPCreate(RSVPBase):
    pass


class RSVPPost(RSVPBase):
    id = Optional[int]
    guest_id = int


class RSVPUpdate(RSVPBase):
    guest_name: str = Field(unique=True)
    plus_one_name: Optional[str]
    attending: Optional[bool]
    shuttle_or_driving: Optional[str]
    shuttle_lodging_location: Optional[str]
    driving_num_seats: Optional[int]
    dietary_restrictions: Optional[str]
    mobility_restrictions: Optional[str]
    num_children: Optional[int]


class RSVPRead(RSVPBase):
    id: int


class RSVPName(BaseModel):
    name: str


class GuestRead(GuestBase):
    id: int
