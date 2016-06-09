# Weather of Philadephia 

## Weather data for each month from the last 75 years (1941-2016)

As a source we used wunderground.com. This is the following url: 

- https://www.wunderground.com/history/airport/KPHL/%d/%d/1/MonthlyHistory.html

In total the scraping script analyzed **75** years(1941-2016), with **12** months for every year with a collection of different weather data you can use -- for example **max temperature**, **min temperature**, **wind** etc. 


### Result
The result of all the scraping is a JSON file called **`allData_philly.json`**.

Top level of this JSON is a list with *`months`* and *`year`*. Then within **months** > `weather` the following keys:

- `Cooling Degree Days (base 65)`
- `Gust Wind`
- `Min Temperature`
	- `max`
	- `avg`
	- `min`
- `Heating Degree Days (base 65)`
- `Dew Point`
	- `max`
	- `avg`
	- `min`
- `Growing Degree Days (base 50)`
- `Snowdepth`
- `Sea Level Pressure`
	- `max`
	- `avg`
	- `min`
- `Max Temperature`
	- `max`
	- `avg`
	- `min`
- `Precipitation`
	- `max`
	- `sum`
	- `avg`
	- `min`
- `Wind`
	- `max`
	- `avg`
	- `min`
- `Mean Temperature`
	- `max`
	- `avg`
	- `min`
	
Not all the keys will be present for all the weather, for example `Heating Degree Days` is an empty string (`""`) and this has no data. 
So in processing the JSON file, take into account that some keys are missing data. 

### Process

Our First scraping code of the weather in january 2016

[January_2016](Dirk.version.py)


###License (MIT License)

Apeace Leaflet is released under the MIT license.

Copyright © 2016 Shirin Pfisterer, Sietske Barten and Bella Donna Nag.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 
