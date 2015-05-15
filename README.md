# RadarGun offline plotting utility

This is small set of tools to create plots using [matplotlib](http://matplotlib.org/) from CSV files create by [RadaGun](https://github.com/radargun/radargun).

Add `rgplot` module into your `PYTHONPATH`, e.g. `export PYTHONPATH=$PYTHONPATH:/opt/lib/python/rg-offline-plotting/src/python`, assuming that the repo was checked out into `/opt/lib/python`

### Usage
##### Loading the data
Probably the first thing you need to do is to load the data. RadarGun by default stores the results in CSV files. You can load the report by creating an instance of
`RgReport` and passing path to the CSV file in its constructor:
```python
measure1 = RgReport(filename1).measurement_of(GET)
```
Here you also specify a vaiable, which you are interested in.

### Examples
##### Bar chart
A bar chart can be create e.g. in this way:
```python
from rgplot import *

filename1 = 'data/ISPN-server-with-listeners.csv'
filename2 = 'data/ISPN-server-without-listeners.csv'


measure1 = RgReport(filename1).with_description("With listeners").measurement_of(GET_NULL)
measure2 = RgReport(filename2).with_description("Without listeners").measurement_of(GET_NULL)

BarChart(measure1, measure2).with_defaults().with_ylim([-10,11]).save_as('./test_bar.eps')
```

##### Line chart
```python
c1w = RgReport('client1w.csv').measurement_of(GET)
c2w = RgReport('client2w.csv').measurement_of(GET)
c3w = RgReport('client3w.csv').measurement_of(GET)

c1wo = RgReport('client1wo.csv').measurement_of(GET)
c2wo = RgReport('client2wo.csv').measurement_of(GET)
c3wo = RgReport('client3wo.csv').measurement_of(GET)


line1 = LineChart(c1w,c2w,c3w).with_defaults().with_xlabel("Number of Hot Rod clients")
line1.with_line('r',c1wo,c2wo,c3wo).save_as('./test_line.eps')
```
