from pydantic import BaseModel


class PodcastEpisodeSchema(BaseModel):
    name: str
    spotify_id: str
    release_date: str
    description: str
    duration: int

    class Config:
        orm_mode = True