"""Collector for daily reward with requests .
"""
import requests



class RequestCollector(object):
    """Collector for the request collector .

    kwargs:
        cookie: cookies srt from document.cookie console command
        act_id: end of url basically
    """
    def __init__(self, **kwargs):
        super(RequestCollector, self).__init__()
        self.cookie = kwargs.get('cookie', None)
        self.act_id = kwargs.get('act_id', None)

    def loadCookies(self, cookies):
        """Parse the cookies string into a dict .
        """        
        loadedCookies = {}
        for cookiedata in cookies.split("; "):
            d1, d2 = cookiedata.split("=", 1)
            loadedCookies[d1] = d2
        return loadedCookies

    def getReward(self, loadedCookies):
        """Get reward data .
        """        
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Origin': 'https://webstatic-sea.mihoyo.com',
            'Connection': 'keep-alive',
        }

        params = (
            ('lang', 'en-us'),
            ('act_id', self.act_id),
        )

        try:
            response = requests.get('https://hk4e-api-os.mihoyo.com/event/sol/home', headers=headers, params=params, cookies=loadedCookies)
            return response.json()
        except requests.exceptions.ConnectionError as e:
            print(f"Connection error! {e}")
            raise 'Cannot get Reward data\n' + repr(e)
        except Exception as e:
            print(f"Unknown error! {e}")
            raise 'Cannot get Reward data\n' + repr(e)
            
    def claimReward(self, loadedCookies):
        """Claim the reward - in - place
        """        
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/json;charset=utf-8',
            'Origin': 'https://webstatic-sea.mihoyo.com',
            'Connection': 'keep-alive',
            'Referer': f'https://webstatic-sea.mihoyo.com/ys/event/signin- sea/index.html?act_id={self.act_id}&lang=en-us',
        }

        params = (
            ('lang', 'en-us'),
        )

        data = {
            'act_id': self.act_id
        }

        try:
            response = requests.post('https://hk4e-api-os.mihoyo.com/event/sol/sign', headers=headers, params=params, json=data, cookies=loadedCookies)
            return response.json()
        except requests.exceptions.ConnectionError as e:
            print(f"Connection error! {e}")
            raise 'Cannot claim daily check-in reward\n' + repr(e)
        except Exception as e:
            print(f"Unknown error! {e}")
            raise 'Cannot claim daily check-in reward\n' + repr(e)
        
    def main(self, ):
        """Read and print the reward .
        """        

        c = self.loadCookies(self.cookie)
        self.getReward(c)
        p = self.claimReward(c)
        print(p['message'])

if __name__ == '__main__':
    c = RequestCollector( cookie='test', 
        act_id='test')
    c.main()

                            


