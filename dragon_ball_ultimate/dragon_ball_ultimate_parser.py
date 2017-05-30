from html.parser import HTMLParser


class Article:
    def __init__(self, title: str = "", date: str = "", resume: str = "", link: str = ""):
        self._title = title
        self._date = date
        self._resume = resume
        self._link = link

    @property
    def title(self):
        return self._title

    @property
    def date(self):
        return self._date

    @property
    def resume(self):
        return self._resume

    @property
    def link(self):
        return self._link

    @title.setter
    def title(self, value):
        self._title = value

    @date.setter
    def date(self, value):
        self._date = value

    @resume.setter
    def resume(self, value):
        self._resume = value

    @link.setter
    def link(self, value):
        self._link = value


class DragonBallUltimate(HTMLParser):
    def __init__(self):
        super().__init__()
        self._current_tag = ""
        self._data = []
        self._article = []
        self._link = []

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
        if tag == "a" and [str(a[0]) for a in attrs] == ["href", "title"]:
            self._link.append(attrs)
        if tag == "article":
            self._current_tag = tag
            self._data.append(attrs)

    def handle_endtag(self, tag):
        if tag == "article":
            self._current_tag = ""

    def handle_data(self, data):
        if self._current_tag == "article":
            if not self.is_online_space(data):
                self._data.append(data)

    @property
    def data(self):
        return self._data

    @property
    def link(self):
        return self._link

    @staticmethod
    def is_online_space(data: str):
        for cara in data:
            if not cara.isspace():
                return False
        return True
