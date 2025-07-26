import time
from controller import fetch_podcast_episodes_data, add_episodes_to_db

def main():
    offset = 0

    while offset < 10:
        podcast_episode_data = fetch_podcast_episodes_data(offset=offset*10)
        if podcast_episode_data:
            add_episodes_to_db(episodes_schema=podcast_episode_data)
            offset += 1
        time.sleep(5)

if __name__ == "__main__":
    main()
    