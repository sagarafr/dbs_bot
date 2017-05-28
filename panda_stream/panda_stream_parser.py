from html.parser import HTMLParser
from requests import get
from utils.get_last_episode import get_last_episode


class DragonBallSuperParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self._important_information = []
        self._blacklist_information = ["Signaler un problème avec une vidéo",
                                       "N'hésitez pas à laisser un commentaire pour partager vos impressions sur cet épisode ou nous aider à tenir le site à jour en cas de problème avec les vidéos.",
                                       "Patience !"]
        self._current_tag = ""

    @property
    def important_information(self):
        return self._important_information

    def reset_important_information(self):
        self._important_information = []

    def handle_comment(self, data):
        pass

    def handle_decl(self, decl):
        pass

    def handle_pi(self, data):
        pass

    def handle_charref(self, name):
        pass

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_entityref(self, name):
        pass

    def handle_starttag(self, tag, attrs):
        attrs = [(str(pair[0]).replace(' ', ''), str(pair[1]).replace(' ', '')) for pair in attrs]
        if tag == "span":
            for pair in attrs:
                if pair == ('style', 'color:red;'):
                    self._current_tag = "span"

    def handle_endtag(self, tag):
        if tag == "span" and self._current_tag == "span":
            self._current_tag = ""

    def handle_data(self, data):
        if self._current_tag == "span":
            if data not in self._blacklist_information:
                self._important_information.append(data)


class PandaStreamParser:
    def __init__(self):
        self._dbs_parser = DragonBallSuperParser()
        self._last_dbs_episode = 92

    @property
    def dbs_parser(self):
        return self._dbs_parser

    @property
    def last_dbs_episode(self):
        return self._last_dbs_episode

    @last_dbs_episode.setter
    def last_dbs_episode(self, value):
        self._last_dbs_episode = value

    @property
    def dbs_important_information(self):
        return self._dbs_parser.important_information

    def dbs_feed(self, text: str):
        self.dbs_parser.feed(text)

    def clear_dbs(self):
        self.dbs_parser.reset_important_information()

    def get_dbs_last_information(self):
        old_information = self.dbs_important_information
        self.last_dbs_episode = get_last_episode("http://panda-streaming.net/dragon-ball-super-{}-vostfr/", self.last_dbs_episode)
        response = get("http://panda-streaming.net/dragon-ball-super-{}-vostfr/".format(self.last_dbs_episode))
        if response.status_code == 200:
            self.clear_dbs()
            self.dbs_feed(response.text)
            if old_information != self.dbs_important_information:
                return self.dbs_important_information
        return None
