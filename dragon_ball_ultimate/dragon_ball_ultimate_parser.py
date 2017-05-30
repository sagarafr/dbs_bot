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

    def __str__(self):
        return "Title: " + self._title + "\nDate: " + self._date + "\nResume: " + self._resume + "\nLink: " + self._link


class DragonBallUltimate(HTMLParser):
    def __init__(self):
        super().__init__()
        self._current_tag = ""
        self._article = []
        self._link = []
        self._article_state = 0

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
        if self._current_tag == "article" and [str(a[0]) for a in attrs] == ["href"] and attrs[0][1] not in self._link:
            self._link.append(attrs[0][1])
        if tag == "article":
            self._current_tag = tag

    def handle_endtag(self, tag):
        if tag == "article":
            self._current_tag = ""
            self._article_state = 0

    def handle_data(self, data):
        if self._current_tag == "article":
            if not self.is_online_space(data):
                if self._article_state == 0:
                    self._article.append(Article(title=data))
                elif self._article_state == 1:
                    self._article[len(self._article) - 1].date = data
                elif self._article_state == 3:
                    self._article[len(self._article) - 1].resume = data
                self._article_state += 1

    def merge_article_and_link(self):
        for cpt_article in range(0, len(self._article)):
            if cpt_article < len(self._link):
                self._article[cpt_article].link = self._link[cpt_article]

    @property
    def link(self):
        return self._link

    @property
    def article(self):
        return self._article

    @staticmethod
    def is_online_space(data: str):
        for cara in data:
            if not cara.isspace():
                return False
        return True
