import datetime
import logging
from modules.request_collector import RequestCollector
import os
from dotenv import load_dotenv

def main():
    load_dotenv()
    STREAM_HANDLER = os.getenv('STREAM_HANDLER', False)
    COOKIE = os.getenv('COOKIE')
    LOG_FILENAME = 'log.txt'

    logging.basicConfig(
        filename=LOG_FILENAME, 
        format='%(asctime)s [%(levelname)s]: %(message)s', 
        level=logging.INFO,
        )
    if STREAM_HANDLER:
        logging.getLogger().addHandler(logging.StreamHandler())

    config = {
        'url': 'https://webstatic-sea.mihoyo.com/ys/event/signin-sea/index.html?act_id=e202102251931481',
        'cookie': COOKIE,
    }

    c = RequestCollector( 
        act_id=config['url'].split('=')[-1], 
        cookie=config['cookie']
        )
    c.main()

if __name__ == '__main__':
    main()