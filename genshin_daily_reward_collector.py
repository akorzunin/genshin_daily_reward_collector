import datetime
from contextlib import redirect_stdout
from reward_collector import RewardCollector


def main():
    LOG_FILENAME = 'log.txt'
    config = RewardCollector.get_configs()

    with open(LOG_FILENAME, "a+") as f:
        with redirect_stdout(f):
            f.write(f'{str(datetime.datetime.today())[:-7]} log: ')
            # run collector
            if config['auth_type'] == 'browser':
                RewardCollector.collect_browser(config)
            if config['auth_type'] == 'request':  
                RewardCollector.collect_requests(config)

if __name__ == '__main__':
    main()