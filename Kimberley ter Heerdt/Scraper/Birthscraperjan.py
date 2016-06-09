import requests
import json
import collections

from bs4 import BeautifulSoup as Soup, Tag

wikibirths = []
wikidates = [
        "January_1",
      
]


def parse_text(text):
    cur_data = collections.OrderedDict()
    year = int(text[0:text.index(" ")])
    if "," in text:
        name = text[text.index(" ") + 3:text.index(",")]
        description = text[text.index(",") + 1:text.rindex(" ") - 1]
    else:
        name = text[text.index(" ") + 3:text.rindex(" ") - 1]
        description = ""

    if "(d" in text:
        deathyear = text[text.rindex(" "):-1]
        description = description.replace(" (d", "")
    else:
        deathyear = ""

    name = name.strip()
    description = description.strip()
    if "(d" in name:
        name = name.replace(" (d", "")

    cur_data["year"] = year
    print len (year)
    cur_data["name"] = name
    if " " in name:
        name = name.replace(" ", "_")
    
    cur_data["url"] = "https://en.wikipedia.org/wiki/" + name
    cur_data["description"] = description
    cur_data["deathyear"] = deathyear.replace(" ", "")
    return cur_data


def find_births(wikidate):
    data = {}
    url = "https://en.wikipedia.org/wiki/" + wikidate
    response = requests.get(url)
    soup = Soup(response.content, "html.parser")
    births_span = soup.find("span", {"id": "Births"})
    births_ul = births_span.parent.find_next_sibling()
    current_birth = []
    for item in births_ul.findAll("li"):
        if isinstance(item, Tag):
            cur_data = parse_text(item.text)
        current_birth.append(cur_data)

    data["date"] = wikidate.replace("_", " ")
    data["birth"] = current_birth
    return data


for wikidate in wikidates:
    wikibirths.append(find_births(wikidate))

with open("wikidata.json", "w") as outfile:
    json.dump(wikibirths, outfile, indent=4)
    

