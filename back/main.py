from fastapi import FastAPI


app = FastAPI()


@app.get("/maps")
def get_maps():
    return {"data": "get maps"}


@app.get("/maps/{_id}")
def get_map_by_id(_id: int):
    return {"data": "get map by id"}


@app.get("/maps/{_id}/times")
def get_times_by_map_id(_id: int):
    return {"data": "get times by map id"}


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
    return {"data": "get players"}


@app.get("/players/{_id}")
def get_player_by_id(_id: int):
    return {"data": "get player by id"}


@app.get("/players/{_id}/times")
def get_times_by_player_id(_id: int):
    return {"data": "get times by player id"}


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
    return {"data": "get time by id"}


@app.post("/times")
def post_time():
    return {"data": "post time"}


@app.put("/times/{_id}")
def put_time_by_id(_id: int):
    return {"data": "put time by id"}


@app.delete("/times/{_id}")
def delete_time_by_id(_id: int):
    return {"data": "delete time by id"}
