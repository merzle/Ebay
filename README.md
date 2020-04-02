<h1>An Ebay-kleinanzeigen Web scraper using Python and Scrapy</h1>

Adapted from <b>https://github.com/HicBoux/Ebay-kleinanzeigen-scrapy-elastic</b>

The aim here is to extract data from https://www.ebay-kleinanzeigen.de/ automatically and rapidly in order to store the found pictures into a local folder.

<h2>Requirements</h2>
Python 3 <br/>
Elasticsearchb 7.0.2 <br/>
Scrapy 1.6.0 <br/>

<h2>How to set it :</h2>

1) Set the URLs (like https://www.ebay-kleinanzeigen.de/s-berlin/l3331 for example) you want to scrape in JSON file : urls.json
2) Set the directory path to the folder were the pictures should be stored in the ebay_kleinanzeigen.py file.
3) Change your current directory to the Scraper's one and start it through :
```bash
cd .../ebaykleinanzeigen
scrapy crawl ebay_kleinanzeigen
```

NB: The number of concurrent requests and time between has been defined in settings.py respectively to 1 and 30 by default
in order to avoid problems on Ebay-kleinanzeigen's server.

<h2>References</h2>

-[Ebay-kleinanzeigen](https://www.ebay-kleinanzeigen.de/stadt/berlin/) <br/>

<h2>Credits</h2>

Copyright (c) 2019, HicBoux. Work released under Apache 2.0 License. 

(Please contact me if you wish to use my work in specific conditions not allowed automatically by the Apache 2.0 License.)

<h2>Disclaimer</h2>

This solution has been made available for informational and educational purposes only. I hereby disclaim any and all 
liability to any party for any direct, indirect, implied, punitive, special, incidental or other consequential 
damages arising directly or indirectly from any use of this content, which is provided as is, and without warranties.
I also disclaim all responsibility for web scraping at a disruptive rate and eventual damages caused by a such use.
