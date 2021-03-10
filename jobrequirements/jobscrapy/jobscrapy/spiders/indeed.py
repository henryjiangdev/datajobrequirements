import scrapy
# import logging
import w3lib.html
from ..items import JobscrapyItem

class IndeedSpider(scrapy.Spider):
    name = "Indeed"
    title = "Data+Engineer"
    pNum = 10
    pNumIncrease = 10
    pNumMax = 750
    mainURL = "https://www.indeed.com{}"
    templateURL = "https://www.indeed.com/jobs?q="+title+"&start={}"
    start_urls = ["https://www.indeed.com/jobs?q="+title+"&start=0"]
    
    def removeHTMLTags(self, text):
        import re
        return re.sub(re.compile('<.*?>'), '', text)
    
    def parse(self, response):
        
        # data gathering
        titles = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "jobtitle", " " ))]').xpath("@title").extract()
        companies = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "company", " " ))]/a/text()').extract()
        locations = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "accessible-contrast-color-location", " " ))]/text()').extract()
        hrefs = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "jobtitle", " " ))]').xpath('@href').extract()
            
        # data storage
        for i in range(len(companies)):
            items = JobscrapyItem()
            items["title"] = titles[i].replace(",", "")
            items["company"] = companies[i].replace("\n", "").replace(",", "")
            items["location"] = locations[i].replace(",", "")
            items["href"] = hrefs[i].replace(",", "")
            yield scrapy.Request(self.mainURL.format(hrefs[i]), callback=self.parse_page2, meta={"items":items})
        
        nextPage = self.templateURL.format(self.pNum)
        if self.pNum <= self.pNumMax:
            self.pNum += self.pNumIncrease
            yield response.follow(nextPage, callback=self.parse)
            
    def parse_page2(self, response):
        html = w3lib.html.remove_tags(response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "jobsearch-JobComponent-description", " " ))]').get()).replace("\n", " | ")
        items = response.meta["items"]
        items["html"] = html
        yield items
           
           
       