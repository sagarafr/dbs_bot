from requests import get
from requests.exceptions import Timeout
from time import sleep


def get_last_episode(url: str, last_episode: int = None):
    episode_number = 1 if last_episode is None else last_episode
    is_last = False
    while not is_last:
        try:
            response = get(url.format(episode_number), timeout=1)
        except Timeout:
            raise
        if response.status_code == 404:
            is_last = True
        elif response.status_code == 200:
            episode_number += 1
        sleep(0.2)

    return episode_number - 1
