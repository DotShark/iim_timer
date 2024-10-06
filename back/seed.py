from os import getenv
from time import perf_counter
from dotenv import load_dotenv
from sqlmodel import Session, create_engine, select
from models import Map, Player, Seeding, Time

if not getenv("IS_DOCKER"):
    load_dotenv("../.env")

postgres_url = getenv("POSTGRES_URL")
if not postgres_url:
    raise Exception("Missing POSTGRES_URL env variable")
engine = create_engine(postgres_url)

with Session(engine) as session:
    seeding = session.exec(statement=select(Seeding)).first()
    if seeding and seeding.done:
        print("The required data is already in the database")
        exit()

    print("Going to (re)create all required data")
    start_time = perf_counter()

    times = session.exec(statement=select(Time)).all()
    for time in times:
        session.delete(time)
    session.commit()
    print("- Deleted all times")

    players = session.exec(statement=select(Player)).all()
    for player in players:
        session.delete(player)
    session.commit()
    print("- Deleted all players")

    maps = session.exec(statement=select(Map)).all()
    for map in maps:
        session.delete(map)
    session.commit()
    print("- Deleted all maps")

    # Creating Maps
    session.add(Map(id=1, name="bhop_japan", image_url="https://pouf.dotshark.ovh/discord/bhop_japan.jpg", start_zone="", end_zone=""))
    session.add(Map(id=2, name="bhop_muchfast", image_url="https://pouf.dotshark.ovh/discord/bhop_muchfast.jpg", start_zone="", end_zone=""))
    session.add(Map(id=3,name="bhop_oldschool", image_url="https://pouf.dotshark.ovh/discord/bhop_oldschool.jpg", start_zone="", end_zone=""))
    session.add(Map(id=4,name="bhop_glxy", image_url="https://pouf.dotshark.ovh/discord/bhop_glxy.jpg", start_zone="", end_zone=""))
    session.add(Map(id=5, name="bhop_exiled", image_url="https://pouf.dotshark.ovh/discord/bhop_exiled.jpg", start_zone="", end_zone=""))
    session.add(Map(id=6, name="bhop_whiteglow", image_url="https://pouf.dotshark.ovh/discord/bhop_whiteglow.jpg", start_zone="", end_zone=""))
    session.add(Map(id=7, name="bhop_christmas", image_url="https://pouf.dotshark.ovh/discord/bhop_christmas.jpg", start_zone="", end_zone=""))
    session.add(Map(id=8, name="bhop_badges_mini", image_url="https://pouf.dotshark.ovh/discord/bhop_badges_mini.jpg", start_zone="", end_zone=""))
    session.commit()
    print("- Created maps")

    # Creating Players
    session.add(Player(id=1, name="obvixus", unique_id="6561198135765316"))
    session.add(Player(id=2, name="human", unique_id="76561198102400829"))
    session.add(Player(id=3, name="DotShark", unique_id="76561198107326409"))
    session.add(Player(id=4, name="Lev", unique_id="76561198295193272"))
    session.add(Player(id=5, name="Rai", unique_id="76561198445924825"))
    session.commit()
    print("- Created players")

    # Creating Times
    session.add(Time(time=157, max_speed=1200, average_speed=800, map_id=1, player_id=1))  # obvixus
    session.add(Time(time=184, max_speed=1200, average_speed=800, map_id=2, player_id=1))
    session.add(Time(time=176, max_speed=1200, average_speed=800, map_id=3, player_id=1))
    session.add(Time(time=33, max_speed=1200, average_speed=800, map_id=4, player_id=1))
    session.add(Time(time=78, max_speed=1200, average_speed=800, map_id=5, player_id=1))
    session.add(Time(time=42, max_speed=1200, average_speed=800, map_id=6, player_id=1))
    session.add(Time(time=59, max_speed=1200, average_speed=800, map_id=7, player_id=1))
    session.add(Time(time=481, max_speed=1200, average_speed=800, map_id=8, player_id=1))

    session.add(Time(time=160, max_speed=1150, average_speed=790, map_id=1, player_id=2))  # human
    session.add(Time(time=190, max_speed=1150, average_speed=790, map_id=2, player_id=2))
    session.add(Time(time=180, max_speed=1150, average_speed=790, map_id=3, player_id=2))
    session.add(Time(time=34, max_speed=1150, average_speed=790, map_id=4, player_id=2))
    session.add(Time(time=80, max_speed=1150, average_speed=790, map_id=5, player_id=2))
    session.add(Time(time=44, max_speed=1150, average_speed=790, map_id=6, player_id=2))
    session.add(Time(time=60, max_speed=1150, average_speed=790, map_id=7, player_id=2))
    session.add(Time(time=490, max_speed=1150, average_speed=790, map_id=8, player_id=2))

    session.add(Time(time=170, max_speed=1100, average_speed=780, map_id=1, player_id=3))  # DotShark
    session.add(Time(time=185, max_speed=1100, average_speed=780, map_id=2, player_id=3))
    session.add(Time(time=175, max_speed=1100, average_speed=780, map_id=3, player_id=3))
    session.add(Time(time=32, max_speed=1100, average_speed=780, map_id=4, player_id=3))
    session.add(Time(time=79, max_speed=1100, average_speed=780, map_id=5, player_id=3))
    session.add(Time(time=41, max_speed=1100, average_speed=780, map_id=6, player_id=3))
    session.add(Time(time=58, max_speed=1100, average_speed=780, map_id=7, player_id=3))
    session.add(Time(time=475, max_speed=1100, average_speed=780, map_id=8, player_id=3))

    session.add(Time(time=165, max_speed=1050, average_speed=770, map_id=1, player_id=4))  # Lev
    session.add(Time(time=182, max_speed=1050, average_speed=770, map_id=2, player_id=4))
    session.add(Time(time=172, max_speed=1050, average_speed=770, map_id=3, player_id=4))
    session.add(Time(time=31, max_speed=1050, average_speed=770, map_id=4, player_id=4))
    session.add(Time(time=76, max_speed=1050, average_speed=770, map_id=5, player_id=4))
    session.add(Time(time=40, max_speed=1050, average_speed=770, map_id=6, player_id=4))
    session.add(Time(time=56, max_speed=1050, average_speed=770, map_id=7, player_id=4))
    session.add(Time(time=470, max_speed=1050, average_speed=770, map_id=8, player_id=4))

    session.add(Time(time=168, max_speed=1000, average_speed=760, map_id=1, player_id=5))  # Rai
    session.add(Time(time=186, max_speed=1000, average_speed=760, map_id=2, player_id=5))
    session.add(Time(time=178, max_speed=1000, average_speed=760, map_id=3, player_id=5))
    session.add(Time(time=35, max_speed=1000, average_speed=760, map_id=4, player_id=5))
    session.add(Time(time=77, max_speed=1000, average_speed=760, map_id=5, player_id=5))
    session.add(Time(time=43, max_speed=1000, average_speed=760, map_id=6, player_id=5))
    session.add(Time(time=55, max_speed=1000, average_speed=760, map_id=7, player_id=5))
    session.add(Time(time=490, max_speed=1000, average_speed=760, map_id=8, player_id=5))

    session.commit()
    print("- Created times")

    session.add(Seeding(done=True))
    session.commit()

    # Calculate and print elapsed time
    elapsed_time = perf_counter() - start_time
    print(f"Complete! Took {round(elapsed_time * 1000)}ms")