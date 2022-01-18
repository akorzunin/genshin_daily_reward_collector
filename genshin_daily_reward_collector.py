import datetime
import logging
from modules.reward_collector import RewardCollector
import os
from dotenv import load_dotenv

def main():
    load_dotenv()
    STREAM_HANDLER = os.getenv('STREAM_HANDLER', False)
    LOG_FILENAME = 'log.txt'
    # get settings from config file
    config = RewardCollector.get_configs()
    # redefine cookies if .env file have COOKIE field
    COOKIE = os.getenv('COOKIE')
    if COOKIE is not None:
        config['cookie'] = COOKIE
    if STREAM_HANDLER:
        logging.getLogger().addHandler(logging.StreamHandler())
    logging.basicConfig(
        filename=LOG_FILENAME, 
        format='%(asctime)s [%(levelname)s]: %(message)s', 
        level=logging.INFO,
        )
    # logging.info(COOKIE)
    if config['auth_type'] == 'browser':
        RewardCollector.collect_browser(config)
    if config['auth_type'] == 'request':  
        RewardCollector.collect_requests(config)

if __name__ == '__main__':
    main()