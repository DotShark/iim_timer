from sqlmodel import Session, create_engine
from models import Map, Player, Time

engine = create_engine("postgresql://postgres:password@localhost:5000/timer")

with Session(engine) as session:
    session.add(Map(name="bhop_japan", image_url="https://pouf.dotshark.ovh/discord/bhop_japan.jpg", start_zone="", end_zone=""))
    session.add(Map(name="bhop_muchfast", image_url="https://pouf.dotshark.ovh/discord/bhop_muchfast.jpg", start_zone="", end_zone=""))
    session.add(Map(name="bhop_oldschool", image_url="https://pouf.dotshark.ovh/discord/bhop_oldschool.jpg", start_zone="", end_zone=""))
    session.add(Map(name="bhop_glxy", image_url="https://pouf.dotshark.ovh/discord/bhop_glxy.jpg", start_zone="", end_zone=""))
    session.add(Map(name="bhop_exiled", image_url="https://pouf.dotshark.ovh/discord/bhop_exiled.jpg", start_zone="", end_zone=""))
    session.add(Map(name="bhop_whiteglow", image_url="https://pouf.dotshark.ovh/discord/bhop_whiteglow.jpg", start_zone="", end_zone=""))
    session.add(Map(name="bhop_christmas", image_url="https://pouf.dotshark.ovh/discord/bhop_christmas.jpg", start_zone="", end_zone=""))
    session.add(Map(name="bhop_badges_mini", image_url="https://pouf.dotshark.ovh/discord/bhop_badges_mini.jpg", start_zone="", end_zone=""))
    session.commit()

    session.add(Player(name="DotShark", unique_id="76561198107326409"))
    session.commit()

    session.add(Time(time=157, max_speed=1200, average_speed=800, map_id=1, player_id=1))
    session.add(Time(time=184, max_speed=1200, average_speed=800, map_id=2, player_id=1))
    session.add(Time(time=176, max_speed=1200, average_speed=800, map_id=3, player_id=1))
    session.add(Time(time=33, max_speed=1200, average_speed=800, map_id=4, player_id=1))
    session.add(Time(time=78, max_speed=1200, average_speed=800, map_id=5, player_id=1))
    session.add(Time(time=42, max_speed=1200, average_speed=800, map_id=6, player_id=1))
    session.add(Time(time=59, max_speed=1200, average_speed=800, map_id=7, player_id=1))
    session.add(Time(time=481, max_speed=1200, average_speed=800, map_id=8, player_id=1))
    session.commit()