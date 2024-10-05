from fastapi import FastAPI
from sqlmodel import Session, select, create_engine
from models import Map, Player, Time

app = FastAPI()
engine = create_engine("postgresql://postgres:password@localhost:5000/timer")


# region maps
@app.get("/maps")
def get_maps():
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


@app.get("/maps/{_id}")
def get_map_by_id(_id: int):
    with Session(engine) as session:
        results = session.exec(statement=select(Map).where(Map.id == _id))
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


@app.get("/maps/{_id}/times")
def get_times_by_map_id(_id: int):
    with Session(engine) as session:
        results = session.exec(statement=select(Time).where(Map.id == _id))
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


@app.post("/maps")
def post_map():
    return {"data": "post map"}


@app.put("/maps/{_id}")
def put_map_by_id(_id: int):
    return {"data": "put map by id"}


@app.delete("/maps/{_id}")
def delete_map_by_id(_id: int):
    return {"data": "delete map by id"}


# endregion
# region players
@app.get("/players")
def get_players():
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


@app.get("/players/{_id}")
def get_player_by_id(_id: int):
    with Session(engine) as session:
        results = session.exec(statement=select(Player).where(Player.id == _id))
        datas = results.all()
        return [
            Player(
                id=data.id,
                name=data.name,
                unique_id=data.unique_id
            ) for data in datas
        ]


@app.get("/players/{_id}/times")
def get_times_by_player_id(_id: int):
    with Session(engine) as session:
        results = session.exec(statement=select(Time).where(Player.id == _id))
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


@app.post("/players")
def post_player():
    return {"data": "post player"}


@app.put("/players{_id}")
def put_player_by_id():
    return {"data": "put player by id"}


@app.delete("/players")
def delete_player_by_id():
    return {"data": "delete player by id"}


# endregion
# region times
@app.get("/times/{_id}")
def get_time_by_id(_id: int):
    with Session(engine) as session:
        results = session.exec(statement=select(Time).where(Time.id == _id))
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


@app.post("/times")
def post_time():
    return {"data": "post time"}


@app.put("/times/{_id}")
def put_time_by_id(_id: int):
    return {"data": "put time by id"}


@app.delete("/times/{_id}")
def delete_time_by_id(_id: int):
    return {"data": "delete time by id"}
# endregion
