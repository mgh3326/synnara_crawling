from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from time import sleep
import os
from random import *
from bs4 import BeautifulSoup
import requests
import platform

from record.model.RecordRes import RecordRes

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# for webdriver chromedriver 2.35 linux64
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('no-sandbox')
chrome_options.add_argument('headless')
# chrome_options.add_argument('window-size=1100x400')
chrome_options.add_argument('disable-gpu')
if platform.system() == "Windows":
    try:
        driver = webdriver.Chrome(os.path.join(
            BASE_DIR, '../chromedriver/chromedriver.exe'), chrome_options=chrome_options)
    except ConnectionResetError:
        sleep(float("{0:.2f}".format(uniform(1, 2))))  # Time in seconds.
        driver = webdriver.Chrome(os.path.join(
            BASE_DIR, '../chromedriver/chromedriver.exe'), chrome_options=chrome_options)
else:
    try:
        driver = webdriver.Chrome(os.path.join(
            BASE_DIR, '../chromedriver/chromedriver'), chrome_options=chrome_options)
    except ConnectionResetError:
        sleep(float("{0:.2f}".format(uniform(1, 2))))  # Time in seconds.
        driver = webdriver.Chrome(os.path.join(
            BASE_DIR, '../chromedriver/chromedriver'), chrome_options=chrome_options)
driver.implicitly_wait(3)


# url에 접근한다.

def RecordParse(_url):
    driver.get(_url)
    record = RecordRes()
    ##productImage
    productImage: WebElement = driver.find_element_by_xpath(
        """//*[@id="container"]/div[3]/div/div[1]/div[1]/p[1]/img""")
    record.productImage = productImage.get_attribute('src')
    ##detailPageImage
    detailPageImage = driver.find_element_by_xpath("""//*[@id="tab_detail2"]/div[2]""")
    images = detailPageImage.find_elements_by_tag_name('img')
    for image in images:
        record.detailPageImage.append(image.get_attribute('src'))
    title = driver.find_element_by_xpath("""//*[@id="container"]/div[3]/div/ul[2]/li[1]""")
    record.title = title.text
    originalPrice = driver.find_element_by_xpath(
        """//*[@id="container"]/div[3]/div/div[1]/div[2]/div[1]/table/tbody/tr[1]/td/span[1]""")
    record.originalPrice = originalPrice.text

    discountPrice = driver.find_element_by_xpath(
        """//*[@id="container"]/div[3]/div/div[1]/div[2]/div[1]/table/tbody/tr[1]/td/span[2]""")
    record.discountPrice = discountPrice.text
    sold = driver.find_element_by_xpath(
        """//*[@id="container"]/div[3]/div/div[1]/div[2]/div[2]""")
    images = sold.find_elements_by_tag_name('img')
    record.sold = images[0].get_attribute('alt')
    artist = driver.find_element_by_xpath(
        """//*[@id="tab_detail1"]/div/table/tbody/tr[1]/td""")
    record.artist = artist.text
    publisher = driver.find_element_by_xpath(
        """//*[@id="tab_detail1"]/div/table/tbody/tr[2]/td[2]""")
    record.publisher = publisher.text
    label = driver.find_element_by_xpath(
        """//*[@id="tab_detail1"]/div/table/tbody/tr[3]/td[2]/a""")
    record.label = label.text
    productCode = driver.find_element_by_xpath(
        """//*[@id="tab_detail1"]/div[1]/table/tbody/tr[4]/td[1]""")
    if productCode.text.find("/") > -1:
        record.productCode = productCode.text.split("/")[0].strip()
        record.barcode = productCode.text.split("/")[1].strip()
    else:
        record.productCode = productCode.text
    releaseDate = driver.find_element_by_xpath(
        """//*[@id="tab_detail1"]/div/table/tbody/tr[4]/td[2]""")
    if releaseDate.text.find('[') > -1:
        record.releaseDate = releaseDate.text.split('[')[0].strip()
        record.weight = releaseDate.text.split('[')[1].split(']')[0].strip()  # [이거 있으면 뒤에 ] 있겠지 에러 안 뜨게 해야 되나
    else:
        record.releaseDate = releaseDate.text
    details = driver.find_element_by_xpath(
        """//*[@id="PROD_DESCR_DIV"]""")
    record.details = details.text

    return record


url = "http://www.synnara.co.kr/sp/sp120Main.do?categoryId=CT22101001&productId=P000422727#_tab02"

record = RecordParse(url)
print(record.productCode)
print(record.barcode)
driver.quit()
