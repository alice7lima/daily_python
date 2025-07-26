import base64
import json
import os

import requests
from db import Base, SessionLocal, engine
from dotenv import load_dotenv
from models import PodcastEpisode
from schema import PodcastEpisodeSchema

load_dotenv()
CLIENT_ID = os.getenv("SPOTIFY_API_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_API_CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")

Base.metadata.create_all(bind=engine)


def authenticate():
    login_url = "https://accounts.spotify.com/api/token"
    data = {"grant_type": "client_credentials"}

    base64_auth = base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode()
    headers = {
        "Authorization": "Basic " + base64_auth,
        "Content-Type": "application/x-www-form-urlencoded",
    }

    response = requests.post(url=login_url, headers=headers, data=data)

    if response.status_code != 200:
        raise Exception(
            "Erro ao tentar autenticar na API do Spotify! Confira as credenciais."
        )

    response_dict = json.loads(response.text)
    return response_dict["access_token"]


def fetch_podcast_episodes_data(offset=0):
    search_endpoint = "https://api.spotify.com/v1/search"
    data = {
        "q": "diário de bordo",
        "type": "episode",
        "market": "BR",
        "limit": 10,
        "offset": offset,
    }
    access_token = authenticate()
    response = requests.get(
        url=search_endpoint,
        params=data,
        headers={"Authorization": f"Bearer {access_token}"},
    )

    episodes = []
    if response.status_code == 200:
        data = response.json()
        for episode in data["episodes"]["items"]:
            episodes.append(
                PodcastEpisodeSchema(
                    name=episode["name"],
                    spotify_id=episode["id"],
                    release_date=episode["release_date"],
                    description=episode["html_description"],
                    duration=episode["duration_ms"],
                )
            )

        return episodes
    else:
        return None


def add_episodes_to_db(episodes_schema: list[PodcastEpisodeSchema]):
    with SessionLocal() as db:
        for episode in episodes_schema:
            db_episode = PodcastEpisode(
                name=episode.name,
                spotify_id=episode.spotify_id,
                release_date=episode.release_date,
                description=episode.description,
                duration=episode.duration,
            )
            db.add(db_episode)
            db.commit()
            db.refresh(db_episode)
