'''Collect reward with requests or browser'''
from request_collector import *
from browser_collector import *
import config_parser
import genshin_daily_reward_collector

if __name__ == '__main__':
    c = config_parser.ConfigParser(
        filename = "genshin_collector_config.txt",
        config_header="Config_section",
        configs_list = ['auth_type', 'cookie', 'browser_profile_path', 'webdriver_exec_path', 'firefox_binary_path', 'web_browser', 'url']
    )
    config = c.get_configs()

    if config['auth_type'] == 'browser':
        t = genshin_daily_reward_collector.WebDriverClass(
                browser_profile_path=config['browser_profile_path'],
                webdriver_exec_path=config['webdriver_exec_path'],
                firefox_binary_path=config['firefox_binary_path'],
                web_browser=config['web_browser'],
                url = config['url']
            )
        t.driver_init()
        t.main()
    
    if config['auth_type'] == 'request':
        print(config['cookie'])
        c = RequestCollector( 
            act_id=config['url'].split('=')[-1], 
            cookie=config['cookie']
        )
        c.main()    
            