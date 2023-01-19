# BiggerPocketBots
This project includes two bots that scrape information from the BiggerPockets website and perform different actions with that information.

<hr/>

<span id=a1> <h2> BP Users Scraper </h2> </span> 

The first bot, takes in several parameters such as a city name, a "kind of city" value, a workbook, and a file path. It then performs a search on the BiggerPockets website using the provided city name, and sorts the results by date or it sorts by relevance. It then scrapes information such as the name of the topic author, the link to the post, and the date of the post, and stores this information in an excel sheet located at the provided file path.

<hr/>

<span id=a1> <h2> Massages Automation </h2> </span> 

The second bot, is designed to send messages to users on the BiggerPockets website. It takes a file path as an input and opens an excel sheet located at that file path. It then iterates through the sheet, pulling the username of each user and sending them a message via Selenium.

<hr/>

<span id=a1> <h2> Requirements </h2> </span> 

* Python 3
* BeautifulSoup
* requests
* openpyxl
* selenium

<span id=a1> <h2> Limitations </h2> </span> 
* This project is scraping data from the BiggerPockets website, which is against their terms of service. Use it at your own risk.
* The project is also limited by the number of pages it can scrape (currently 20 pages) and the number of items it can scrape from each page.
