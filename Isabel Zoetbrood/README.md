# # New York City Crimes 

## Concept 
I found the data of the Crimes which had occured in NYC interesting from the moment we found them. How cool would is be to show in three poster the difference in amount of crimes! Maybe we would find out what crime is most common in what borough of nyc. 

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

## Own Sketches
The first sketch made was in the beginning of the process. We wanted to show the differences between the crimes in different boroughs. 
![Sketch](First_Sketch/poster2.png)

Afterwards I made sketches with plotdevice. We already knew a bar graphs wasn't what we wanted, so I didn't really experiment any further with that. <br>
![Sketch 2](Plotdevice_Schetsen/Analyzing_time_burglary.png)
![Sketch 3](Plotdevice_Schetsen/Analyzing_time_felony.png)
![Sketch 4](Plotdevice_Schetsen/Analyzing_time_motor.png)
![Sketch 5](Plotdevice_Schetsen/Analyzing_time_murder.png)
![Sketch 6](Plotdevice_Schetsen/Analyzing_time_rape.png)
![Sketch 7](Plotdevice_Schetsen/Analyzing_time_robbery.png)

But later we decided to focus on the hour of occurence, so we needed a different visual representation. In the Library we found a book on data visualization in which a really cool circle graph was. Different layers of rounded cornered shapes. After drawing one shape in illustrator I experimented with the rounded corners, <br>
![Sketch 8](Second_sketch/schets-13.png)
![Sketch 9](Second_sketch/schets-14.png)
![Sketch 10](Second_sketch/schets-15.png)
![Sketch 11](Second_sketch/schets-16.png)
But later we realized that coding the rounded corners was too difficult, so I decided to stay put with the existing corners, or else the information wouldn't be completely accurate. 

With the illustrator codes I ended up with 6 different shapes and sizes, which I overlayed fist. <br>
![Sketch 12](Final_Sketch/2_overlay.png)

The difference however between the amount of the larceny and that of murder was so big that when portrayed on true size, the murder was very difficult to see. The amount wasn't good to read anymore. That why I added, smaller underneath the big graph, the smaller graphs with the highest point on that graph in numers. ()I didn't realy really the bargraphs which is why I only used the new shapes.) 

![Sketch 13](Final_Sketch/3_overlay+verschil.png)

I wasn't really content witht he big graph, so I figured out a way to show all the shapes in the same graphs using a logaritm. The logarithm of 2 was fitting the best, so I used 2^3 for the smallest, and 2^9 for the biggest. 
![Sketch 14](Final_Sketch/4_logaritmisch.png)

