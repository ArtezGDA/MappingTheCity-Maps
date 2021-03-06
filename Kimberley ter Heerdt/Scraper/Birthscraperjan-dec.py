import requests
import json
import collections

from bs4 import BeautifulSoup as Soup, Tag

wikibirths = []
wikidates = [
    "January_1",
    "January_2",
    "January_3",
    "January_4",
    "January_5",
    "January_6",
    "January_7",
    "January_8",
    "January_9",
    "January_10",
    "January_11",
    "January_12",
    "January_13",
    "January_14",
    "January_15",
    "January_16",
    "January_17",
    "January_18",
    "January_19",
    "January_20",
    "January_21",
    "January_22",
    "January_23",
    "January_24",
    "January_25",
    "January_26",
    "January_27",
    "January_28",
    "January_29",
    "January_30",
    "January_31",
    "February_1",
    "February_2",
    "February_3",
    "February_4",
    "February_5",
    "February_6",
    "February_7",
    "February_8",
    "February_9",
    "February_10",
    "February_11",
    "February_12",
    "February_13",
    "February_14",
    "February_15",
    "February_16",
    "February_17",
    "February_18",
    "February_19",
    "February_20",
    "February_21",
    "February_22",
    "February_23",
    "February_24",
    "February_25",
    "February_26",
    "February_27",
    "February_28",
    "February_29",
    "March_1",
    "March_2",
    "March_3",
    "March_4",
    "March_5",
    "March_6",
    "March_7",
    "March_8",
    "March_9",
    "March_10",
    "March_11",
    "March_12",
    "March_13",
    "March_14",
    "March_15",
    "March_16",
    "March_17",
    "March_18",
    "March_19",
    "March_20",
    "March_21",
    "March_22",
    "March_23",
    "March_24",
    "March_25",
    "March_26",
    "March_27",
    "March_28",
    "March_29",
    "March_30",
    "March_31",
    "April_1",
    "April_2",
    "April_3",
    "April_4",
    "April_5",
    "April_6",
    "April_7",
    "April_8",
    "April_9",
    "April_10",
    "April_11",
    "April_12",
    "April_13",
    "April_14",
    "April_15",
    "April_16",
    "April_17",
    "April_18",
    "April_19",
    "April_20",
    "April_21",
    "April_22",
    "April_23",
    "April_24",
    "April_25",
    "April_26",
    "April_27",
    "April_28",
    "April_29",
    "April_30",
    "May_1",
    "May_2",
    "May_3",
    "May_4",
    "May_5",
    "May_6",
    "May_7",
    "May_8",
    "May_9",
    "May_10",
    "May_11",
    "May_12",
    "May_13",
    "May_14",
    "May_15",
    "May_16",
    "May_17",
    "May_18",
    "May_19",
    "May_20",
    "May_21",
    "May_22",
    "May_23",
    "May_24",
    "May_25",
    "May_26",
    "May_27",
    "May_28",
    "May_29",
    "May_30",
    "May_31",
    "June_1",
    "June_2",
    "June_3",
    "June_4",
    "June_5",
    "June_6",
    "June_7",
    "June_8",
    "June_9",
    "June_10",
    "June_11",
    "June_12",
    "June_13",
    "June_14",
    "June_15",
    "June_16",
    "June_17",
    "June_18",
    "June_19",
    "June_20",
    "June_21",
    "June_22",
    "June_23",
    "June_24",
    "June_25",
    "June_26",
    "June_27",
    "June_28",
    "June_29",
    "June_30",
    "July_1",
    "July_2",
    "July_3",
    "July_4",
    "July_5",
    "July_6",
    "July_7",
    "July_8",
    "July_9",
    "July_10",
    "July_11",
    "July_12",
    "July_13",
    "July_14",
    "July_15",
    "July_16",
    "July_17",
    "July_18",
    "July_19",
    "July_20",
    "July_21",
    "July_22",
    "July_23",
    "July_24",
    "July_25",
    "July_26",
    "July_27",
    "July_28",
    "July_29",
    "July_30",
    "July_31",
    "August_1",
    "August_2",
    "August_3",
    "August_4",
    "August_5",
    "August_6",
    "August_7",
    "August_8",
    "August_9",
    "August_10",
    "August_11",
    "August_12",
    "August_13",
    "August_14",
    "August_15",
    "August_16",
    "August_17",
    "August_18",
    "August_19",
    "August_20",
    "August_21",
    "August_22",
    "August_23",
    "August_24",
    "August_25",
    "August_26",
    "August_27",
    "August_28",
    "August_29",
    "August_30",
    "August_31",
    "September_1",
    "September_2",
    "September_3",
    "September_4",
    "September_5",
    "September_6",
    "September_7",
    "September_8",
    "September_9",
    "September_10",
    "September_11",
    "September_12",
    "September_13",
    "September_14",
    "September_15",
    "September_16",
    "September_17",
    "September_18",
    "September_19",
    "September_20",
    "September_21",
    "September_22",
    "September_23",
    "September_24",
    "September_25",
    "September_26",
    "September_27",
    "September_28",
    "September_29",
    "September_30",
    "October_1",
    "October_2",
    "October_3",
    "October_4",
    "October_5",
    "October_6",
    "October_7",
    "October_8",
    "October_9",
    "October_10",
    "October_11",
    "October_12",
    "October_13",
    "October_14",
    "October_15",
    "October_16",
    "October_17",
    "October_18",
    "October_19",
    "October_20",
    "October_21",
    "October_22",
    "October_23",
    "October_24",
    "October_25",
    "October_26",
    "October_27",
    "October_28",
    "October_29",
    "October_30",
    "October_31",
    "November_1",
    "November_2",
    "November_3",
    "November_4",
    "November_5",
    "November_6",
    "November_7",
    "November_8",
    "November_9",
    "November_10",
    "November_11",
    "November_12",
    "November_13",
    "November_14",
    "November_15",
    "November_16",
    "November_17",
    "November_18",
    "November_19",
    "November_20",
    "November_21",
    "November_22",
    "November_23",
    "November_24",
    "November_25",
    "November_26",
    "November_27",
    "November_28",
    "November_29",
    "November_30",
    "December_1",
    "December_2",
    "December_3",
    "December_4",
    "December_5",
    "December_6",
    "December_7",
    "December_8",
    "December_9",
    "December_10",
    "December_11",
    "December_12",
    "December_13",
    "December_14",
    "December_15",
    "December_16",
    "December_17",
    "December_18",
    "December_19",
    "December_20",
    "December_21",
    "December_22",
    "December_23",
    "December_24",
    "December_25",
    "December_26",
    "December_27",
    "December_28",
    "December_29",
    "December_30",
    "December_31"
]


def parse_text(text):
    cur_data = collections.OrderedDict()
    inx = 0
    for i in text:
        if not i.isdigit(): break
        inx += 1

    year = int(text[0:inx])
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
