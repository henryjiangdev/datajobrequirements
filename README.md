# datajobrequirements
Figuring out what data analyst, scientist, and engineers want.
Description: Gather data from indeed.com to show common list of languages/tools needed for Data Analyst(750 jobs scraped), Data Science(around 500), Data Engineer(around 500). Mostly for me targeting internships.

![image](https://user-images.githubusercontent.com/78574889/110703445-a5bc4500-81a8-11eb-87ab-6078b031134a.png)
In order for the job Data Analyst, the requirement tier is SQL, Excel, PowerBI, Tableau, Python, R, SAS, Hadoop, Java, NoSQL, and Spark.
![image](https://user-images.githubusercontent.com/78574889/110703461-ab198f80-81a8-11eb-901e-6c7b910b7c03.png)
In order for the job Data Scientist, the requirement tier is Python, SQL, R, Spark, PowerBI, Tableau, SAS, Excel, Hadoop, NoSQL, Java, C/C++.
![image](https://user-images.githubusercontent.com/78574889/110703500-b8367e80-81a8-11eb-87fa-4dbff085d0de.png)
In order for the job Data Engineer, the requirement tier is SQL, Python, PowerBI, Spark, Java, NoSQL, Tableau, Hadoop, Excel, R, C/C++, and SAS

Learned some scrapy framework for this. Yield and generator were quite tough to understand, eventually cracked it took quite a while though. I will most likely use scrapy to scrape things from now on, instead of requests and beautifulsoup4. It is really effecient once you build the bot.

Problems I found were quite difficult were, some understanding of yield and generator. Other than that data cleaning was quite difficult for html. Had to remove all the tags, then format the data in a certain way, instead of using spaces I used | to deliminate paragraphs/sentences, since using spaces can cause words to be combined after a sentence/paragraph ends.
