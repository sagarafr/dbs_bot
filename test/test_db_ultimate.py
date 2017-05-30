import requests
from dragon_ball_ultimate.dragon_ball_ultimate_parser import DragonBallUltimate


def main():
    parser = DragonBallUltimate()
    parser.feed(requests.get("http://www.dragonball-ultimate.com/page/news").text)
    parser.merge_article_and_link()
    for article in parser.article:
        print(article)


if __name__ == '__main__':
    main()
