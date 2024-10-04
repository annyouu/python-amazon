
# requests ウェブページのコンテンツを取得するためのライブラリ
# BeautifulSoup HTMLを解析し、操作するためのライブラリ
import requests
from bs4 import BeautifulSoup

amazonURL = "https://www.amazon.co.jp/%E7%8B%AC%E7%BF%92Python-%E5%B1%B1%E7%94%B0-%E7%A5%A5%E5%AF%9B/dp/4798163643/ref=sr_1_3_sspa?crid=NF65AAVUBSFL&dib=eyJ2IjoiMSJ9.JNiqW30D3eB8w_7BvJyRdXg6VxIRObtXgxx4FrubshRNvGeMQAJ9CIG6ZDvSsm5nG5y8k0_EY-VyOtXr_nQOOevE0Q9_dAn9geVFXJpwpt1LRu1ggNFmVeg-tSL3Q7fm7r3TgW-jnHtKsav7_bH-kyr_sfGVKtmzIrOMVx5UO1sccNCSpcU9A7ognvXzfylWul1osW4Zbspi9ZKb_-y_4Q.39-Ndlc-t4HwcChK0zUw2EsF7-fkZJpiYMssHXQ0HlA&dib_tag=se&keywords=python&qid=1725427480&sprefix=pyt%2Caps%2C261&sr=8-3-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"

# amazonをトラッキングする関数
# parser 解析
# amazonPage = requests.get(amazonURL)
# amazonURLのウェブページのコンテンツを取得する。それをamazomPageに代入

#soup = BeautifulSoupを使って、取得したHTMLコンテンツを解析し、操作しやすい形に変換 print(soup) 解析されたHTML全体をコンソールに出力する。
def amazonTrackingPrice():
    amazonPage = requests.get(amazonURL)
    soup = BeautifulSoup(amazonPage.content, "html.parser")
    # print(soup)

    title = soup.find(id="titleblock_feature_div").get_text()
    price = soup.find("span", class_="a-price-whole").get_text()
    # convertedPrice = price[1:6]
    convertedPrice = price.replace(",","")
    intPrice = int(convertedPrice)
    print(title)
    print(convertedPrice)

    if (intPrice > 3000):
         sendLineNotify()

def sendLineNotify():
     print("lineに通知がいきました")
     lineNotifyToken = "8fFLBJNaMPkQsNxOYgR03iofvYKRRXcqq7KA7BNKxwY"
     lineNotifyApi = "https://notify-api.line.me/api/notify"
     headers = {"Authorization": f"Bearer {lineNotifyToken}"}
     data = {"message":"今がお買い時です ! https://www.amazon.co.jp/%E7%8B%AC%E7%BF%92Python-%E5%B1%B1%E7%94%B0-%E7%A5%A5%E5%AF%9B/dp/4798163643/ref=sr_1_3_sspa?crid=NF65AAVUBSFL&dib=eyJ2IjoiMSJ9.JNiqW30D3eB8w_7BvJyRdXg6VxIRObtXgxx4FrubshRNvGeMQAJ9CIG6ZDvSsm5nG5y8k0_EY-VyOtXr_nQOOevE0Q9_dAn9geVFXJpwpt1LRu1ggNFmVeg-tSL3Q7fm7r3TgW-jnHtKsav7_bH-kyr_sfGVKtmzIrOMVx5UO1sccNCSpcU9A7ognvXzfylWul1osW4Zbspi9ZKb_-y_4Q.39-Ndlc-t4HwcChK0zUw2EsF7-fkZJpiYMssHXQ0HlA&dib_tag=se&keywords=python&qid=1725427480&sprefix=pyt%2Caps%2C261&sr=8-3-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"}
     requests.post(lineNotifyApi, headers=headers, data=data)

amazonTrackingPrice()

