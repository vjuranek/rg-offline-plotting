import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import Formatter
from RgChart import RgChart
from RgVars import MRT, AT

class LineChart(RgChart):

    def __init__(self, *measurements):
        self._fig, self._ax = plt.subplots()
        self._lines = self._create_base_line(measurements)
        #self._create_plot()
    
    def with_defaults(self):
        self.with_title().with_ylabel().with_grids()
        return self
    
    def with_xticks_names(self, xt_names = None):
        if xt_names is not None:
            formatter = XAxFormatter(xt_names)
            self._ax.xaxis.set_major_formatter(formatter)
            #self.__fig.autofmt_xdate()
        return self

    def add_line(self, *measurements):
        self._lines.append(self._create_line(measurements))
        return self
    
    def _create_line(self, measurements):
        nm = len(measurements)
        ind = np.arange(nm)
        val, xax = [], []
        for i in range(0, len(measurements)):
            val.append(measurements[i]._mrt)
            xax.append(measurements[i]._title)            

        #decide if plot MRT or AT
        if (issubclass(measurements[i]._rg_var, AT)):
            return None #TODO
        elif  (issubclass(measurements[i]._rg_var, MRT)):
            return plt.plot(ind, val, 'bo-')
        else:
            raise ValueError("Unknown variable")
    
    def _create_base_line(self, measurements):
        self._title = measurements[0]._title if measurements[0]._title is not None else ""
        self._ylabel = measurements[0]._rg_var.ylabel if measurements[0]._rg_var is None else ""
        return self._create_line(measurements)

    def _create_plot(self):
        baseline = self._lines[0]
        nm = len(baseline.get_data()[0]) # number of measurements on base line
        self._ax.set_xlim(-0.5, nm - 0.5)
        #plt.xticks(ind)
        plt.setp([self._lines])


class XAxFormatter(Formatter):
    def __init__(self, xvals):
        self._xvals = xvals

    def __call__(self, x, pos=0):
        'Return the label for time x at position pos'
        ind = int(round(x))
        if ind >= len(self._xvals) or ind < 0: return ''

        return self._xvals[ind]
