__author__ = 'jovin'
import time
from scrapy.spider import BaseSpider
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from scrapy.http import TextResponse
from selenium.webdriver.common.keys import Keys
import MySQLdb
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class Snapdeal(BaseSpider):
    name = "snapdeal1"
    allowed_domains = ["snapdeal.com"]
    start_urls = ["http://www.snapdeal.com//brand/micromax/mobiles-mobile-phones?"]


    def __init__(self):
        self.driver = webdriver.Firefox()
    def parse(self, response):
        self.driver.get(response.url)
        copyright = self.driver.find_element_by_id('seeMoreProducts')
        for i in  range(1,20):
            ActionChains(self.driver).move_to_element(copyright).perform()
            time.sleep(15)
        # delay = 3 # seconds
        # try:
        #     WebDriverWait(self.driver, delay).until(EC.presence_of_element_located(self.driver.find_element_by_id('seeMoreProducts')))
        #     print "Page is ready!"
        # except TimeoutException:
        #     print "Loading took too much time!"
        # self.driver.implicitly_wait(25)
        # self.driver.execute_script("window.scrollTo(0,Math.max(document.documentElement.scrollHeight," + "document.body.scrollHeight,document.documentElement.clientHeight));")
        # time.sleep(25)
        # copyright = self.driver.find_element_by_id('seeMoreProducts')
        # # copyright.send_keys(Keys.NULL)
        # ActionChains(self.driver).move_to_element(copyright).perform()
        # # #
        # while not copyright.is_displayed():
        #     copyright = self.driver.find_element_by_id('seeMoreProducts')
        #     time.sleep(20) #to let page content loading
        #     ActionChains(self.driver).move_to_element(copyright).perform()

        response = TextResponse(url=response.url, body=self.driver.page_source, encoding='utf-8')
        # links = response.xpath("//a[@class='hit-ss-logger somn-track prodLink hashAdded']/@href/text()").extract()
        price = response.xpath("//div[@class='product_list_view_heading']/text()").extract()


        # links = self.driver.find_elements_by_class_name('productWrapper')
        print price

        # images = self.driver.find_element_by_xpath("//div[@class='productWrapper']//div[@class='outerImg']//@hoversrc").text
        # title = self.driver.find_element_by_xpath("//div[@class='productWrapper']//img/@alt").text