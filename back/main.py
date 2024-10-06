from fastapi import FastAPI, HTTPException
from sqlmodel import Session, select, create_engine, desc
from models import Map, Player, Time

app = FastAPI()
engine = create_engine("postgresql://postgres:password@localhost:5000/timer")


# region maps
@app.get("/maps", tags=["maps"])
def get_maps() -> list[Map]:
    with Session(engine) as session:
        results = session.exec(statement=select(Map))
        datas = results.all()
        return [
            Map(
                id=data.id,
                name=data.name,
                image_url=data.image_url,
                start_zone=data.start_zone,
                end_zone=data.end_zone
            ) for data in datas
        ]


@app.get("/maps/{_id}", tags=["maps"])
def get_map_by_id(_id: int) -> Map:
    with Session(engine) as session:
        results = session.exec(statement=select(Map).where(Map.id == _id))
        map = results.first()
        if not map:
            raise HTTPException(status_code=404, detail="Map not found")
        return map 


@app.get("/maps/{_id}/times", tags=["maps"])
def get_times_by_map_id(_id: int) -> list[Time]:
    with Session(engine) as session:
        statement = select(Time).where(Time.map_id == _id).order_by("time")
        results = session.exec(statement)
        datas = results.all()
        return [
            Time(
                id=data.id,
                time=data.time,
                max_speed=data.max_speed,
                average_speed=data.average_speed,
                created_at=data.created_at,
                updated_at=data.updated_at,
                map_id=data.map_id,
                player_id=data.player_id
            ) for data in datas
        ]


@app.post("/maps", tags=["maps"])
def post_map():
    return {"data": "post map"}


@app.put("/maps/{_id}", tags=["maps"])
def put_map_by_id(_id: int):
    return {"data": "put map by id"}


@app.delete("/maps/{_id}", tags=["maps"])
def delete_map_by_id(_id: int):
    return {"data": "delete map by id"}


# endregion
# region players
@app.get("/players", tags=["players"])
def get_players() -> list[Player]:
    with Session(engine) as session:
        results = session.exec(statement=select(Player))
        datas = results.all()
        return [
            Player(
                id=data.id,
                name=data.name,
                unique_id=data.unique_id
            ) for data in datas
        ]


@app.get("/players/{_id}", tags=["players"])
def get_player_by_id(_id: int) -> Player:
    with Session(engine) as session:
        results = session.exec(statement=select(Player).where(Player.id == _id))
        player = results.first()
        if not player:
            raise HTTPException(status_code=404, detail="Map not found")
        return player


@app.get("/players/{_id}/times", tags=["players"])
def get_times_by_player_id(_id: int) -> list[Time]:
    with Session(engine) as session:
        statement = select(Time).where(Time.player_id == _id).order_by("time")
        results = session.exec(statement)
        datas = results.all()
        return [
            Time(
                id=data.id,
                time=data.time,
                max_speed=data.max_speed,
                average_speed=data.average_speed,
                created_at=data.created_at,
                updated_at=data.updated_at,
                map_id=data.map_id,
                player_id=data.player_id
            ) for data in datas
        ]


@app.post("/players", tags=["players"])
def post_player():
    return {"data": "post player"}


@app.put("/players{_id}", tags=["players"])
def put_player_by_id():
    return {"data": "put player by id"}


@app.delete("/players", tags=["players"])
def delete_player_by_id():
    return {"data": "delete player by id"}


# endregion
# region times
@app.get("/times/{_id}", tags=["times"])
def get_time_by_id(_id: int) -> Time:
    with Session(engine) as session:
        results = session.exec(statement=select(Time).where(Time.id == _id))
        time = results.first()
        if not time:
            raise HTTPException(404, detail="Time not found")
        return time


@app.post("/times", tags=["times"])
def post_time():
    return {"data": "post time"}


@app.put("/times/{_id}", tags=["times"])
def put_time_by_id(_id: int):
    return {"data": "put time by id"}


@app.delete("/times/{_id}", tags=["times"])
def delete_time_by_id(_id: int):
    return {"data": "delete time by id"}
# endregion
