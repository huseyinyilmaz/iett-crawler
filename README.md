IETT Crawler
------------

Crawls harita.iett.gov.tr site and pulls bus route and busstop data with geolocation information. result is printed to standart output stream as json. Result will have

* Bus route list in Istanbul, Turkey
* Busstop list with geo-location information and title in Istanbul, Turkey.

result json format will have

Usage
-----
Unfortunately I could not get busstop geo-location info with script yet. but it is very easy to get with wget.
just run

    wget --mirror 'http://harita.iett.gov.tr'

command. After downloading the site, copy XML directory from site to same location with your crawler.py script.

After this point run

    python3 crawler.py>result.json


script is written for python3 but it should also work for pyhon 2.7.

Requirements
------------

    beautifulsoup4==4.0.1
    requests==0.10.8


my result for this script can be found at cdn.yilmazhuseyin.com/data/iettbus.json
