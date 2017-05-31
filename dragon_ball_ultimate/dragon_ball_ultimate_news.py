import requests
from copy import deepcopy
from dragon_ball_ultimate.dragon_ball_ultimate_parser import DragonBallUltimate


class DragonBallUltimateNews:
    def __init__(self):
        self._parser = DragonBallUltimate()
        self._article_updated = []
        # TODO change this and put in the config file
        self._max_article = 10
        self.update()

    def update(self):
        cpt_try = 0
        updated = False
        while cpt_try < 3 and not updated:
            try:
                responce = requests.get("http://www.dragonball-ultimate.com/page/news", timeout=5)
            except TimeoutError:
                cpt_try += 1
                continue

            if responce.status_code == 200:
                updated = True
                self._parser.reset_data()
                self._parser.feed(responce.text)
                self._parser.merge_article_and_link()
                for article in self._parser.article:
                    print(article)
                if len(self._article_updated) == 0:
                    self._article_updated = deepcopy(self._parser.article)
                else:
                    front_news_title = self._article_updated[0].title
                    for article in self._parser.article:
                        if article.title != front_news_title:
                            self._article_updated.insert(0, article)
                        else:
                            break
                del self._article_updated[self._max_article:]

    @property
    def article_update(self):
        return self._article_updated
