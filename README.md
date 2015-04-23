# RadarGun offline plotting utility

This is small set of tools to create plots using [matplotlib](http://matplotlib.org/) from CSV files create by [RadaGun](https://github.com/radargun/radargun).

Add `rgplot` module into your `PYTHONPATH`, e.g. `export PYTHONPATH=$PYTHONPATH:/opt/lib/python/rg-offline-plotting/src/python`, assuming that the repo was checked out into `/opt/lib/python`

Example usage can looks like this:
```python
from rgplot import *

filename1 = 'data/ISPN-server-with-listeners.csv'
filename2 = 'data/ISPN-server-without-listeners.csv'


measure1 = RgReport(filename1).with_description("With listeners").measurement_of(GET_NULL)
measure2 = RgReport(filename2).with_description("Without listeners").measurement_of(GET_NULL)

BarChart(measure1, measure2).with_defaults().with_ylim([-10,11]).save_as('./test.eps')
```
