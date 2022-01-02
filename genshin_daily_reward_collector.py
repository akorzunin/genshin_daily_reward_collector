import datetime
import logging
# from contextlib import redirect_stdout
from reward_collector import RewardCollector
import os
from dotenv import load_dotenv

def main():
    load_dotenv()
    LOG_FILENAME = 'log.txt'
    # get settings from config file
    config = RewardCollector.get_configs()
    # redefine cookies if .env file have COOKIE field
    COOKIE = os.getenv('COOKIE')
    if COOKIE is not None:
        config['COOKIE'] = COOKIE
    logging.basicConfig(
        filename=LOG_FILENAME, 
        filemode='a+', 
        format='%(asctime)s [%(levelname)s]: %(message)s', 
        level=logging.INFO,
        )
    # logging.info(COOKIE)
    if config['auth_type'] == 'browser':
        RewardCollector.collect_browser(config)
    if config['auth_type'] == 'request':  
        RewardCollector.collect_requests(config)


    # with open(LOG_FILENAME, "a+") as f:
    #     with redirect_stdout(f):
    #         f.write(f'{str(datetime.datetime.today())[:-7]} log: ')
    #         # run collector
    #         if config['auth_type'] == 'browser':
    #             RewardCollector.collect_browser(config)
    #         if config['auth_type'] == 'request':  
    #             RewardCollector.collect_requests(config)

if __name__ == '__main__':
    main()