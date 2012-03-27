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


My result for this script can be found at cdn.yilmazhuseyin.com/data/iettbus.tar.gz

Output Format
-------------

    {
        "buses": [{"route": "K\\u0130RAZLITEPE-AC  ", "code": "1",
    	      "busstops": {"busstop_id": 0, "descrition": "A0082aaaA0082aaaPARK", "title": "PARK"},
    	      "no": "1"}
    	      ....
    	     ],
    
        "busstops": [{"lat": "41.03738",
    		 "id": 0,
    		 "long": "29.06061"}
    		 ....
    		],

        "errors": [{"code": "_x2",
    	       "error": "Could not find busstop information file"}
    	       ....
    	      ]
    }