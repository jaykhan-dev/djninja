from datetime import datetime
from ninja import Schema

class TrackSchema(Schema):
    title: str
    artist: str
    duration: float
    last_play: datetime
    song_file: str

class NotFoundSchema(Schema):
    message: str