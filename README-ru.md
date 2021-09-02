Genshin daily reward collector
===
Ежедневно собирает награды с сайта Genshin Impact с помощью запросов или браузера.

Установка
---
1. Убедитесь что python3 установлен.
 1. Используйте `pip install -r requirements.txt` для установки
    необходимых библиотек для python.
1. Настройте **genshin_daily_reward_collector.py** через файл
    конфигураций **genshin_collector_config.txt**
    ### Настройки файла genshin_collector_config.txt
 +  Ипользовние программы через реквесты
	 1. Используте `auth_type: request`
	 2. Чтобы заполнить поле `url: ` используйте [адрес сайта](https://webstatic-sea.mihoyo.com/ys/event/signin-sea/index.html?act_id=e202102251931481&lang=en-us) на котором появляются ежедневные награды.
	 3. Чтобы заполнить поле `cookie: `
		 1. Перейдите за сайт из поля  `url: `
		 2. Откройте консоль (`F12`)
		 3. Используйте команду `document.cookie` или `copy(document.cookie)` чтобы сразу скопировать данные в буфер обмена
		 4. Поля `browser_profile_path: `, `webdriver_exec_path: `, `firefox_binary_path: `, `web_browser: ` в этом случае не обязательны к заполнению
 
 + Использование программы через автоматизированный браузер
	 1. Используте `auth_type: browser`
	 2.  Чтобы заполнить поле `url: ` используйте [адрес сайта](https://webstatic-sea.mihoyo.com/ys/event/signin-sea/index.html?act_id=e202102251931481&lang=en-us) на котором появляются ежедневные награды.
	 3. Поле `cookie: ` не обязательно к заполнению.
	 4. Поле `browser_profile_path: ` это путь к профилю браузера (если вы используйте firefox то его можно найти по адресу [about:profiles](about:profiles) в разделе **Root Directory**). Используйте любой профиль  браузера в котором в котором зарегистриррован ваш аккаунт miHoYo.
	 5. Поле `webdriver_exec_path: `это путь к вэбдрайверу, для firefox его можно скачать [тут](https://github.com/mozilla/geckodriver/releases/tag/v0.29.1).
	 6. Поле `firefox_binary_path: ` это путь к исполняемому файлу исполуемого браузера (например **C:\\Program Files\\Mozilla Firefox\\firefox.exe**)
	 7. Поле `web_browser: `  позволяет выбрать между браузером `chrome` или `firefox`по умолчанию будет выбран `firefox`.
	  


Как использовать
---
### Использование в ручном режиме

Запустить файл genshin_daily_reward_collector.py командой `python genshin_daily_reward_collector.py `
- Если награда собрана успешно вы получите ответ `OK`
- Если награда уже собрана вы получите ответ `Traveler, you've already checked in today~`

### Запуск по расписанию

- Использование **sсheduler.pyw**
	1.  Настройте файл конфигурации **sheduler_config.txt**.
		Пример:

			[Sheduler_config]
			period: daily, 20:00
			skript_name_py: genshin_daily_reward_collector.py 
	

	- Воможные опции для поля `period: ` hourly, daily, weekly, monthly
		
	2. Добавьте файл **sсheduler.pyw** в автозагрузку.
	- Время до выполнения скрипта можно узнать при помощи команды `python sсheduler.pyw time` скрипт при этом не будет исполнен.


- Запуск при помощи планировщика заданий Windows [ссылка](https://remontka.pro/windows-task-scheduler/)
- Запуск при помощи cron (Linux) [ссылка](https://www.nic.ru/help/planirovshik-cron-zapusk-programm-po-raspisaniyu_6791.html)


Лицензия
---
Genshin daily reward collector бесплатное программное обеспечение с открытым исходным кодом под лицензией [Apache 2.0 License](https://github.com/create-go-app/cli/blob/master/LICENSE).
