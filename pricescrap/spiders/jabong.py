from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
import MySQLdb

class Jabong(BaseSpider):
    name = "jabong"
    allowed_domains = "jabong.com"
    start_urls = [""]
    def parse(self,response):
        self.conn = MySQLdb.connect(user='root', passwd='2361250', db='test', host='localhost', charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()
        hxs = HtmlXPathSelector(response)
        links = hxs.select("//@data-url").extract()
        image = hxs.select("//img[@class='itm-img']//@src").extract()
        content = hxs.select("//div[@class='box box-bgcolor']")
        price = content.select("//strong[@class='fs16 qa-price']/text()").extract()
        title = content.select(".//span[@class='qa-brandName title mt30 c999 prod-ellipsis']/text()").extract()
        title2 = content.select(".//span[@class='qa-brandTitle fs11 c999 prod-ellipsis']/text()").extract()
        l1 = [elem.strip().split(' ') for elem in title2]
        l2 = [elem.strip().split(' ') for elem in title]
        arr = []
        new_links=[]

        i = 0
        for l in links:
            l = "http://www.jabong.com/"+l
            new_links.append(l)
        for l in range(len(l2)):
            text = l2[i]+l1[i]
            arr.append(text)
            i = i+1
        i = 0
        arrnw=[]
        for l in arr:
            arrnw.append(",".join(l))
        arlate=[]
        for l in arrnw:

            l= l.replace (",", " ")

            arlate.append(l)
        formatted_images = [l.encode("utf-8") for l in image]
        formatted_title = [l.encode("utf-8") for l in arlate]
        formatted_price = [l.encode("utf-8") for l in price]
        formatted_links = [l.encode("utf-8") for l in new_links]
        i = 0
        for j in formatted_price:
            self.cursor.execute("""INSERT INTO data (title,price,link,image) VALUES (%s,%s,%s,%s)""", (formatted_title[i]
            ,j,formatted_links[i],formatted_images[i]))
            self.conn.commit()
            i = i+1
