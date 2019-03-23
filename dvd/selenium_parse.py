import os
import platform
from random import *
from time import sleep

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

from dvd.model.DvdRes import DvdRes

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

def parse(_url):
    driver.get(_url)
    dvd = DvdRes()
    ##productImage
    productImage: WebElement = driver.find_element_by_xpath(
        """//*[@id="container"]/div[3]/div/div[1]/div[1]/p/img""")
    dvd.productImage = productImage.get_attribute('src')
    ##detailPageImage
    detailPageImage = driver.find_element_by_xpath("""//*[@id="tab_detail2"]/div[2]""")
    images = detailPageImage.find_elements_by_tag_name('img')
    image_list = []
    for image in images:
        image_list.append(image.get_attribute('src'))
    dvd.detailPageImage = "##".join(image_list)

    title = driver.find_element_by_xpath("""//*[@id="container"]/div[3]/div/ul[2]/li[1]""")
    dvd.title = title.text
    originalPrice = driver.find_element_by_xpath(
        """//*[@id="container"]/div[3]/div/div[1]/div[2]/div[1]/table/tbody/tr[1]/td/span[1]""")
    dvd.originalPrice = originalPrice.text

    discountPrice = driver.find_element_by_xpath(
        """//*[@id="container"]/div[3]/div/div[1]/div[2]/div[1]/table/tbody/tr[1]/td/span[2]""")
    dvd.discountPrice = discountPrice.text
    sold = driver.find_element_by_xpath(
        """//*[@id="container"]/div[3]/div/div[1]/div[2]/div[2]""")
    images = sold.find_elements_by_tag_name('img')
    dvd.sold = images[0].get_attribute('alt')
    castMember = driver.find_element_by_xpath(
        """//*[@id="tab_detail1"]/div/table/tbody/tr[1]/td""")
    dvd.castMember = castMember.text
    director = driver.find_element_by_xpath(
        """//*[@id="tab_detail1"]/div/table/tbody/tr[2]/td[1]""")
    dvd.director = director.text

    screenRatio = driver.find_element_by_xpath(
        """//*[@id="tab_detail1"]/div/table/tbody/tr[3]/td""")
    dvd.screenRatio = screenRatio.text
    sound = driver.find_element_by_xpath(
        """//*[@id="tab_detail1"]/div/table/tbody/tr[4]/td""")
    dvd.sound = sound.text
    sound = driver.find_element_by_xpath(
        """//*[@id="tab_detail1"]/div/table/tbody/tr[4]/td""")

    dvd.sound = sound.text
    subtitle = driver.find_element_by_xpath(
        """//*[@id="tab_detail1"]/div/table/tbody/tr[6]/td""")
    dvd.subtitle = subtitle.text
    productionDistribution = driver.find_element_by_xpath(
        """//*[@id="tab_detail1"]/div/table/tbody/tr[2]/td[2]""")
    dvd.productionDistribution = productionDistribution.text
    regionCode = driver.find_element_by_xpath(
        """//*[@id="tab_detail1"]/div/table/tbody/tr[7]/td[1]""")
    dvd.regionCode = regionCode.text
    rating = driver.find_element_by_xpath(
        """//*[@id="tab_detail1"]/div/table/tbody/tr[7]/td[2]""")
    dvd.rating = rating.text
    runningTime = driver.find_element_by_xpath(
        """//*[@id="tab_detail1"]/div/table/tbody/tr[8]/td[1]""")
    dvd.runningTime = runningTime.text
    media = driver.find_element_by_xpath(
        """//*[@id="tab_detail1"]/div/table/tbody/tr[8]/td[2]""")
    dvd.media = media.text

    details = driver.find_element_by_xpath(
        """//*[@id="PROD_DESCR_DIV"]""")
    dvd.details = details.text

    return dvd


url = "http://www.synnara.co.kr/sp/sp121Main.do?categoryId=CT21004401&productId=P000422579#.XJXX9ZgzZPZ"

dvd = parse(url)
print(dvd.title)
driver.quit()
