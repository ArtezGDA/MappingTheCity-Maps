from bs4 import BeautifulSoup
import urllib
import json
import os
jaren = [str("2012"),str("2010"),str("2006"),str("2003"),str("2002"),str("1998"),str("1994"),str("1989"),str("1986")]
DESIRED_COLUMNS = {1, 2, 5} #scrapes only afk, aantal & zetels
verkiezingsData = []

filename = raw_input('Enter a filename: ') or 'data.json'

#open file and open json array
with open(filename, "w") as file:
    file.write("[{")
for Jaargetal in jaren:
    #url source 
    r = urllib.urlopen("http://www.nlverkiezingen.com/TK" + Jaargetal +".html").read()
    soup = BeautifulSoup(r, "html.parser")
    tables = soup.find_all("table")
    for table in tables:
        header = soup.find_all("h1")[0].getText()
        #print header
        with open(filename, "a+") as file:
            file.write("\"%s\": [" % header)
        trs = table.find_all("tr")[0].getText()
        #print '\n'

        del verkiezingsData[:] #clear list before adding new data
        #add the 3 columns to a list
        for tr in table.find_all("tr")[:22]: 
            for index, val in enumerate(tr.find_all('td')):
                 if index in DESIRED_COLUMNS:
                    verkiezingsData.append(val.getText().strip())

        #grab 3 values and write json array
        for a, b, c in zip(verkiezingsData[::3], verkiezingsData[1::3], verkiezingsData[2::3]):
    		data2 = {'afk':a,"aantal":b, "zetels":c}
    		with open(filename, 'a') as outfile:
      		    json.dump(data2, outfile)
                    outfile.write(",")

        #open file, delete last comma and close array
        with open(filename, 'ab+') as file:
            file.seek(-1, os.SEEK_END)
            file.truncate()
            file.write("],")

#open file, delete last comma, and close array
with open(filename, 'r+b') as file:
    file.seek(-1, os.SEEK_END)
    file.truncate()
    file.write("}]")
#open file and pretty print json data
with open(filename, 'r') as file:
    prettydata = json.load(file)
with open(filename, 'w') as file:
    json.dump(prettydata, file, sort_keys=True, indent=4, separators=(',', ': '))