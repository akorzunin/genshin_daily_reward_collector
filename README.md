Genshin daily reward collector
===
Collects daily rewards from the Genshin Impact site using queries or your browser.

Setup
---
1. Make sure python3 is installed.
1. Use `pip install -r requirements.txt` to install
    required libraries for python. 
1. Configure **genshin_daily_reward_collector.py** through the
    config file **genshin_collector_config.txt**
    ### Configuration file genshin_collector_config.txt
 + Using the program via Requests
	 1. Use `auth_type: request`.
	 2. To fill field `url: ` use [website address](https://webstatic-sea.mihoyo.com/ys/event/signin-sea/index.html?act_id=e202102251931481&lang=en-us) where the daily rewards appear.
	 1. To fill field `cookie: `.
		 1. Go to the site from the field `url: `
		 2. Open the console (`F12`)
		 3. Use command `document.cookie` or `copy(document.cookie)` to copy data to clipboard immediately
		 4. The fields `browser_profile_path: `, `webdriver_exec_path: `, `firefox_binary_path: `, `web_browser: ` are optional in this case
 
 + Using the program via an automated browser
	 1. Use `auth_type: browser`.
	 2.  To fill in the `url: ` field, use [website address](https://webstatic-sea.mihoyo.com/ys/event/signin-sea/index.html?act_id=e202102251931481&lang=en-us) where the daily rewards appear.
	 3. The field `cookie: ` is optional.
	 4. The field `browser_profile_path: ` is the path to your browser profile (if you use firefox it can be found at [about:profiles](about:profiles) under **Root Directory**). Use any browser profile in which your miHoYo account is registered.
	 5. Field `webdriver_exec_path: ` this is path to webdriver, for firefox it can be downloaded [here](https://github.com/mozilla/geckodriver/releases/tag/v0.29.1).
	 6. The field `firefox_binary_path: ` is the path to the executable file of the browser to be used (for example **C:\\Program Files\\Mozilla Firefox\\\firefox.exe**)
	 7. The field `web_browser: ` allows you to choose between `chrome` or `firefox` browser.
	  


How to use
---
### Use in manual mode

Run the file genshin_daily_reward_collector.py with the command `python genshin_daily_reward_collector.py `
- If the reward is collected successfully you will get an answer `OK`
- If the reward is already collected you'll get the answer  `Traveler, you've already checked in today~`

### Run on schedule

- Using **schedule.pyw**
	1.  Set up the configuration file **sheduler_config.txt**.
		Example:

			[Sheduler_config]
			period: daily, 20:00
			skript_name_py: genshin_daily_reward_collector.py 
	

	- Possible options for `period: ` hourly, daily, weekly, monthly
		
	2. Add the file **scheduler.pyw** to the autorun.
	- You can find out the time before the script runs with the command `python ссheduler.pyw time` the script will not run.


- Run with Windows Task Scheduler [link](https://www.windowscentral.com/how-create-automated-task-using-task-scheduler-windows-10)
- Run with cron (Linux) [link](https://www.jessicayung.com/automate-running-a-script-using-crontab/)


License
---
Genshin daily reward collector is free and open-source software licensed under the [Apache 2.0 License](https://github.com/create-go-app/cli/blob/master/LICENSE).

