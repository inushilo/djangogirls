import requests
from bs4 import BeautifulSoup

# HTMLの取得(GET)
req = requests.get("https://game-i.daa.jp/?GooglePlay%E3%82%A2%E3%83%97%E3%83%AA%E6%9C%88%E9%96%93%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E6%95%B0%E3%83%A9%E3%83%B3%E3%82%AD%E3%83%B3%E3%82%B0")
req.encoding = req.apparent_encoding # 日本語の文字化け防止

# HTMLの解析
bsObj = BeautifulSoup(req.text,"html.parser")

# 要素の抽出
items = bsObj.find_all("td")
#print(items)

with open("ranking_list.txt", encoding="utf-8", mode="w") as f:
  lank = 1; cnt = 0; flg = False; finish_lank = 999
  for item in items:
    if str(lank) == item.get_text():
      flg = True
    if flg:
      if cnt == 0:
        f.write(item.get_text() + ":")
      elif cnt == 2:
        f.write(item.get_text() + ":")
      elif cnt == 3:
        f.write(item.get_text() + "\n")
      cnt += 1
      if cnt == 4:
        cnt = 0
        flg = False
        lank += 1
    if lank > finish_lank:
      break