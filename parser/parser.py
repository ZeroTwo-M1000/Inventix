import threading

import requests

from decorators.parser_dec import ParserDecorators
from www.www import arguments


@ParserDecorators.infinite
@ParserDecorators.count_time
def fn(f):
    data = f.get_data()
    for review in data['reviews']:
        requests.post('http://127.0.0.1:8000/api/review', json=review)


def main():
    for arg in arguments:
        threading.Thread(target=fn, args=(arg,)).start()


if __name__ == "__main__":
    main()
