import requests
import fake_useragent
from bs4 import BeautifulSoup

user = fake_useragent.UserAgent().random

header = {'user-agent': user}

link = "https://data.binance.vision/?prefix=data/spot/daily/aggTrades/"
responce = requests.get(link, headers=header)
# soup = BeautifulSoup(responce.text, 'lxml') # используем парсер lxml который также нужно установить
# block = soup.find('div', id = "tool_padding")

# # Check js
# check_js = block.find('div', id = "javascript_check")
# status_js = check_js.find_all('span')[1].text
# result_js = f'javascript: {status_js}'

# # Check flash
# check_flash = block.find('div', id = "flash_version")
# status_flash = check_flash.find_all('span')[1].text
# result_flash = f'flash: {status_flash}'

# # Check User-agent
# check_ua = block.find('div', id = "user_agent").text

# print(result_js)
# print(result_flash)
# print(check_ua)


with open("1.html", "w", encoding="utf-8") as file:
    file.write(responce.text)