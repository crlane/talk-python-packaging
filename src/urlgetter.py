import requests
import sys


def get_url(url):
    session = requests.Session()
    return session.get(url)


def command_line():
    if not len(sys.argv) > 1:
        print("Please supply a url to fetch!")
        sys.exit(1)
    url = sys.argv[1]
    response = get_url(url)
    print('Got response: {} from url: {}'.format(response.status_code, url))
    print('Content: {}'.format(response.content[:1000]))
