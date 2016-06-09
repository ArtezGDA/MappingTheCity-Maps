# Wiki Births 

## Data collection of all births from jan till dec scraped from wikipedia 
Wikipedia was used as a source to collect all the people (who selected noted by Wikipedia) there birthday is on 1 january till 30 december.

- https://en.wikipedia.org/wiki/ + wikidate
- example:"January_1","January_2","January_3","January_4".

All wikidates are collected in the file: **`wikibirthdata.txt`**

There are two python files: 
<br>**first one** <br>
scraping all births in january. **`Birthscraperjan.py`**

<br>**Second one** <br>
 scraping all births in january till dec **`Birthscraperjandec.py`** 

In total the scraping script analyzed .. births, found .. deathyears, .. birthyears.


### Result

The result of all the scraping of  **first one** is a JSON file called **`wikibirth-jan.json`**.

The result of all the scraping of  **second one** is a JSON file called **`wikibirth-jandec.json`**.



Top level of this JSON is a list with *date* and *birth* . Then for each date we have the following keys:

- `year`: birthyear
- `name`: persons name of birth
- `url`: the url of the wikipedia page of this person
- `description`: the wikipedia description of the person
- `deathyear`: (if there) deathyear of person

Not every `deathyear` is presented in the json file for all births. if wikipedia doesn't have a deathyear presented on the day of birth page it is possible a deathyear is not presented or the person is still alive. 

### Ways of improving/questions
- some deathyears are somewhere(on the web/Wikipedia?), but not presented yet in the list.

- Is there a way to get the..\u00fc away in a json file? (guess not, way of scripting an e with a stripe?)

- Sometimes the datafile is very big to use in a visualisation. Is there a way to improve this by maybe scraping every month on his own? (yes)
