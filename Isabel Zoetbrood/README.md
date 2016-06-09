# # New York City Crimes 

## Concept 

## Used information

The result of all the scraping of  **the first time** is a JSON file called [Data Bronx](Data/bronx.json). In this file, there's information about:<br>
	- code of crime (given by NYPD) <br>
	- Occurence day <br>
	- Occurence month<br>
	- Occurence year<br>
	- Occurence hour<br>
	- Kind of Offense <br>
	- Borough (all the Bronx obviously)<br>
	- Location (expressed in coordinates)<br>

The result of all the scraping of  **the second time**, after the first iteration is are 6 seperate JSON files called <br>
[Murder Data] (Data/bronx_MURDER.json).<br>
[Rape Data] (Data/bronx_RAPE.json). <br>
[Burglary Data] (Data/bronx_BURGLARY.json).<br>
[Grand Larceny of Motor Vehicly Data] (Data/bronx_LARCENY.json). <br>
[Felont Data] (Data/bronx_FELONY.json).<br>
[Robbery Data] (Data/bronx_ROBBERY.json). <br>


In these files, there's the same information as in the previous file.

### Ways of improving/questions
- some deathyears are somewhere(on the web/Wikipedia?), but not presented yet in the list.

- Is there a way to get the..\u00fc away in a json file? (guess not, way of scripting an e with a stripe?)

- Sometimes the datafile is very big to use in a visualisation. Is there a way to improve this by maybe scraping every month on his own? (yes)
