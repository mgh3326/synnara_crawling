import requests
from bs4 import BeautifulSoup
from record.model.RecordRes import RecordRes

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}


def get_html(url):  # 날씨 코드를 받아오기
    _html = ""
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        _html = resp.text
    return _html


def findImageSrc(input):
    return str(input).split("src=\"")[1].split("\"/>")[0].replace('&amp;', '&')


def parse(_url):
    html = get_html(_url)  # html로 문자열 반환 자료값을 받기
    # print(html)
    soup = BeautifulSoup(html, 'html.parser')  # beautiful함수로 실행

    product_image = soup.find('p', {'class': 'view_img'})
    record = RecordRes()
    record.productImage = findImageSrc(product_image)
    title = soup.find('li', {'class': 'de_tit'})
    record.title = str(title.get_text()).replace("\n", '').strip()
    product_thum = soup.find('div', {'class': 'product_thum', 'align': 'center'})
    print(html)
    return record


result = parse("http://www.synnara.co.kr/sp/sp120Main.do?categoryId=CT22101001&productId=P000422727#_tab02")
# print(result.productImage)
