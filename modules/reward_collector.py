'''Collect reward with requests or browser'''
from os import stat
from request_collector import RequestCollector
from browser_collector import WebDriverClass
import config_parser

class RewardCollector():
    @staticmethod
    def get_configs():  # sourcery skip: inline-immediately-returned-variable
        c = config_parser.ConfigParser(
            filename = "genshin_collector_config.txt",
            config_header="Config_section",
            configs_list = ['auth_type', 'cookie', 'browser_profile_path', 'webdriver_exec_path', 'firefox_binary_path', 'web_browser', 'url']
        )
        config = c.get_configs()
        return config
    
    @staticmethod
    def collect_browser(config):
        t = WebDriverClass(
        browser_profile_path=config['browser_profile_path'],
        webdriver_exec_path=config['webdriver_exec_path'],
        firefox_binary_path=config['firefox_binary_path'],
        web_browser=config['web_browser'],
        url = config['url']
            )
        t.driver_init()
        t.main()
    
    @staticmethod
    def collect_requests(config):
        c = RequestCollector( 
            act_id=config['url'].split('=')[-1], 
            cookie=config['cookie']
        )
        c.main()



if __name__ == '__main__':
    config = RewardCollector.get_configs()

    if config['auth_type'] == 'browser':
        RewardCollector.collect_browser(config)
    
    if config['auth_type'] == 'request':  
        RewardCollector.collect_requests(config)
         
            