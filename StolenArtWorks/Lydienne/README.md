# THEFT ALERTS
Lydienne Albertoe and Esmee Ellson.

## Data collection of stolen artworks in the world.

As source is the following url used:

- http://www.theft-alerts.com/

In total the scraping script analyzed **213** stolen art works; found the date, categorie, location, crimeref, title and the images of the art works.

Code source:

- http://codereview.stackexchange.com/questions/60769/scrape-an-html-table-with-python
- http://codereview.stackexchange.com/questions/106457/a-web-crawler-for-scraping-images-from-stock-photo-websites
- http://codereview.stackexchange.com/questions/99300/scraping-a-table-from-texas-dept-of-criminal-justice-website
- http://stackoverflow.com/questions/32343976/python-beautiful-soup-webscraping-pandas-dataframe
- http://stackoverflow.com/questions/36424527/how-to-web-scrape-images-that-are-in-a-link-in-a-table
- http://stackoverflow.com/questions/36885303/how-to-scrape-the-next-pages-link
- http://stackoverflow.com/questions/36885447/how-to-scrape-the-text-by-categories-and-make-a-json-file
- http://stackoverflow.com/questions/37184173/how-to-scrape-the-images-from-the-website

### Results

The result of all the scraping is a map off Images called **`myimages`** and JSON file called **`Theft-alerts-text.json`**. [JSON file](theft-alerts.json)

###### myimage map is a map with *stolen artworks images*. 

Not all images are placed in the map because some images have the same name that gives errors. 


###### The JSON file is a list with *stolen artworks*. 
For each stolen artwork there are the following keys:

- `Location`: the date off each stolen artwork.
	- `lon` the coordinate x.
	- `lat` the coordinate y.
- `Categorie`: the image link of off each stolen artwork.
- `ID`: What kind of artwork and the name who has made it.
- `CrimeRef`: the place where it is stolen and in there:
- `nItemsStolen`: from the person or company that the artwork belongs too.

The `Date`, `lon/lat` and `Title` are not included but it will be soon.

### Process scraping

[Image](Theft-alerts-image.py)

```
#!/usr/bin/python
#Theft-alerts-image

import  requests

from bs4 import BeautifulSoup
from urlparse  import urljoin

def get_pages(start):
        soup = BeautifulSoup(requests.get(start).content, "lxml")
        images = [img["src"] for img in soup.select("div.itemspacingmodified a img")]
        yield  images
        nxt = soup.select("code.resultnav a")[-1]
        #Finds the images on the next pages
        while True:
            soup = BeautifulSoup(requests.get(urljoin(url, nxt["href"])).content)
            nxt = soup.select("code.resultnav a")[-1]
            if nxt.text != "Next":
                break
            yield [img["src"] for img in soup.select("div.itemspacingmodified a img")]
# change to whatever your url is
url = "http://www.theft-alerts.com/"
#Shows the names link of the images
for images in get_pages(url):
    print(images)
#Placed al the images in the map myImages
with open("myimages/{}".format(img), "w") as f:
    f.write(urllib2.urlopen("{}/{}".format(url.rsplit("/", 1)[0], img)).read())

if __name__ == "__main__":
    main()

```	
[Text](Theft-alerts-text.py)

```
#!/usr/bin/python
#Theft-alerts-text

import urllib2
from bs4 import BeautifulSoup
import json

theftalerts = []
for i in range(1, 19):
	# change to whatever your url is
	connection = urllib2.urlopen("http://www.theft-alerts.com/index-%d.html" % i)

	soup = BeautifulSoup(connection.read().replace("<br>","\n"), "html.parser")

	# for the categories we wanted out the text
	for sp in soup.select("table div.itemspacingmodified"):
		theftDict = {}
		for wd in sp.select("div.itemindentmodified"):
			text = wd.text
			if text.startswith("Crime Ref"):
				ref = text.split(":")[1]
				ref = ref.strip()
				ref = ref.strip("\n")
				theftDict['CrimeRef'] = ref
			elif text.startswith("No of items stolen"):
				ref = text.split(":")[1]
				ref = ref.strip()
				ref = ref.strip("\n")
				theftDict['nItemsStolen'] = ref
			elif text.startswith("Location"):
				values = text.split("\n")
				for v in values:
					if v.startswith("Location"):
						ref = v.split(":")[1]
						ref = ref.strip()
						ref = ref.strip("\n")
						theftDict['Location'] = ref
					if v.startswith("Category"):
						ref = v.split(":")[1]
						ref = ref.strip()
						ref = ref.strip("\n")
						theftDict['Category'] = ref
					if v.startswith("ID"):
						ref = v.split(":")[1]
						ref = ref.strip()
						ref = ref.strip("\n")
						theftDict['ID'] = ref
			elif text.startswith("Item ONE"):
				ref = text.split(":")[1]
				ref = ref.strip()
				ref = ref.strip("\n")
				theftDict['ItemONE'] = ref
			elif text.startswith("Contact"):
				ref = text.split(":")[1]
				ref = ref.strip()
				ref = ref.strip("\n")
				theftDict['Contact'] = ref
			elif text.startswith("ID"):
				ref = text.split(":")[1]
				ref = ref.strip()
				ref = ref.strip("\n")
				theftDict['ID'] = ref
			else:
				print text
			if not text.startswith("Images :"):
				pass
		theftalerts.append(theftDict)

#Shows the results
print len(theftalerts)
#Makes a json file in your map
with open("theft-alerts.json", 'w') as outFile:
	json.dump(theftalerts, outFile, indent=2)
    
```	

##License (MIT License)

Apeace Leaflet is released under the MIT license.

Copyright © 2016 Lydienne Albertoe and Esmee Ellson.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.