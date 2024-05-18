import requests

link = "https://data.binance.vision/?prefix=data/spot/daily/aggTrades/"
link2 = "https://icanhazip.com/"
link3 = "https://browser-info.ru/"


responce = requests.get(link2)

print(responce.status_code)
print(responce.text)
## responce.content - если нужно получить байты записываете байты в файл

responce = requests.get(link3)

with open("1.html", "w", encoding="utf-8") as file:
    file.write(responce.text)