from sqlmodel import Field, SQLModel, Relationship
from typing import List
from datetime import datetime

class Map(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    image_url: str
    start_zone: str
    end_zone: str
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    # Relationships
    times: List["Time"] = Relationship(back_populates="map")


class Player(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    unique_id: str
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    # Relationships
    times: List["Time"] = Relationship(back_populates="player")


class Time(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    time: float
    max_speed: float
    average_speed: float
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    map_id: int = Field(foreign_key="map.id")
    player_id: int = Field(foreign_key="player.id")

    # Relationships
    map: Map = Relationship(back_populates="times")
    player: Player = Relationship(back_populates="times")