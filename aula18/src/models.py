from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from db import Base

class PodcastEpisode(Base):
    __tablename__ = 'episodes'
    id = Column(Integer, primary_key=True, index=True)
    spotify_id = Column(String)
    name = Column(String)
    release_date = Column(DateTime)
    description = Column(String)
    duration = Column(Integer)
    created_at = Column(DateTime, default=func.now())