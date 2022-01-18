"""collects daily reward from web site"""
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException


class WebDriverClass(object):
    """Get token from web site
    kwargs:
        url: 'https://developer.spotify.com/console/get-album-tracks/'
        web_browser: 'firefox' or 'chrome'
        browser_profile_path:'C:\\Users\\Akorz\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\ukml7b3k.automation'
        firefox_binary_path: "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
        webdriver_exec_path: "C:\\Users\\akorz\\Downloads\\geckodriver-v0.29.1-win64\\geckodriver.exe"
    """

    def __init__(self, *args, **kwargs):
        super(WebDriverClass, self).__init__()
        self.url = kwargs.get('url', 'https://developer.spotify.com/console/get-album-tracks/')
        self.web_browser = kwargs.get('web_browser', 'firefox')
        self.browser_profile_path = kwargs.get('browser_profile_path', 'C:\\Users\\Akorz\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\ukml7b3k.automation')
        self.firefox_binary_path = kwargs.get('firefox_binary_path', "C:\\Program Files\\Mozilla Firefox\\firefox.exe")
        self.webdriver_exec_path =kwargs.get('webdriver_exec_path', "C:\\Users\\akorz\\Downloads\\geckodriver-v0.29.1-win64\\geckodriver.exe")
        
    def driver_init(self, ):
        """Initialize the driver
        """        
        if(self.web_browser == 'chrome'):
            options = webdriver.ChromeOptions()
            options.add_argument(f"user-data-dir={self.browser_profile_path}")
            self.driver = webdriver.Chrome(executable_path=self.webdriver_exec_path, chrome_options=options)
            self.driver.get(self.url)

        if(self.web_browser == 'firefox'):
            binary = FirefoxBinary(self.firefox_binary_path)
            profile = FirefoxProfile(self.browser_profile_path)
            self.driver = webdriver.Firefox(firefox_profile=profile, firefox_binary=binary, executable_path=self.webdriver_exec_path)
            self.driver.get(self.url)
        else: 
            print("not a suitable browser")
            return None

    def main(self, ):
        """Main method for the button click .
        """        
        try:
            WebDriverWait(self.driver, 300).until(EC.presence_of_element_located((By.CLASS_NAME, 'components-home-assets-__sign-content_---list---3L0nzm')))
            # wait till data refresh
            sleep(1)
            btn = self.driver.find_elements_by_class_name('components-home-assets-__sign-content_---item---1VLDOZ')
            # click every element until cath an error only one elem can be clicked
            try:
                for i in btn:
                    i.click()
                    sleep(0.1)
            except ElementClickInterceptedException:
                sleep(1)
        finally:
            self.driver.close()

if __name__ == '__main__':
    t = WebDriverClass(
            browser_profile_path= 'C:\\Users\\Akorz\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\ukml7b3k.automation',
            webdriver_exec_path= 'C:\\Users\\akorz\\Downloads\\geckodriver-v0.29.1-win64\\geckodriver.exe',
            firefox_binary_path= 'C:\\Program Files\\Mozilla Firefox\\firefox.exe',
            web_browser='firefox',
            url = 'https://webstatic-sea.mihoyo.com/ys/event/signin-sea/index.html?act_id=e202102251931481'
        )
    t.driver_init()
    t.main()