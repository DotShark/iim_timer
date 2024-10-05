from fastapi import FastAPI
from sqlmodel import Field, Session, select, create_engine
from models import Map, Player, Time


app = FastAPI()
engine = create_engine("postgresql://postgres:password@localhost:5000/timer")


def query(model, where=None):
    with Session(engine) as session:
        if where is None:
            results = session.exec(statement=select(model))
        else:
            results = session.exec(statement=select(model).where(where))
        datas = results.all()
        return [model(id=data.id, name=data.name, image_url=data.image_url, start_zone=data.start_zone, end_zone=data.end_zone) for data in datas]


@app.get("/maps")
def get_maps():
    return query(Map, None)


@app.get("/maps/{_id}")
def get_map_by_id(_id: int):
    return query(Map, Map.id == _id)


@app.get("/maps/{_id}/times")
def get_times_by_map_id(_id: int):
    return query(Time, Time.map_id == _id)


@app.post("/maps")
def post_map():
    return {"data": "post map"}


@app.put("/maps/{_id}")
def put_map_by_id(_id: int):
    return {"data": "put map by id"}


@app.delete("/maps/{_id}")
def delete_map_by_id(_id: int):
    return {"data": "delete map by id"}


@app.get("/players")
def get_players():
    return query(Player, None)


@app.get("/players/{_id}")
def get_player_by_id(_id: int):
    return query(Player, Player.id == _id)


@app.get("/players/{_id}/times")
def get_times_by_player_id(_id: int):
    return query(Time, Time.player_id == _id)


@app.post("/players")
def post_player():
    return {"data": "post player"}


@app.put("/players{_id}")
def put_player_by_id():
    return {"data": "put player by id"}


@app.delete("/players")
def delete_player_by_id():
    return {"data": "delete player by id"}


@app.get("/times/{_id}")
def get_time_by_id(_id: int):
    return query(Time, Time.id == _id)


@app.post("/times")
def post_time():
    return {"data": "post time"}


@app.put("/times/{_id}")
def put_time_by_id(_id: int):
    return {"data": "put time by id"}


@app.delete("/times/{_id}")
def delete_time_by_id(_id: int):
    return {"data": "delete time by id"}
