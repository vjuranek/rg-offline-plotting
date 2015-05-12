import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import Formatter
from RgChart import RgChart
from RgVars import MRT, AT

class LineChart(RgChart):

    def __init__(self, *measurements):
        self._fig, self._ax = plt.subplots()
        self._create_plot(measurements)
    
    def with_defaults(self):
        self.with_title().with_ylabel().with_grids()
        return self
    
    def with_xticks_names(self, xt_names = None):
        if xt_names is not None:
            formatter = XAxFormatter(xt_names)
            self._ax.xaxis.set_major_formatter(formatter)
            #self.__fig.autofmt_xdate()
        return self
    
    def _create_plot(self, measurements):
        nm = len(measurements)
        self._ax.set_xlim(-0.5, nm - 0.5)
        ind = np.arange(nm)
        val = []
        xax = []
        for i in range(0, len(measurements)):
            val.append(measurements[i]._mrt)
            xax.append(measurements[i]._title)            
            self._title = measurements[i]._title #last name wins
            self._ylabel = measurements[i]._rg_var.ylabel if measurements[i]._rg_var is None else ""
                
        plt.xticks(ind)
        #decide if plot MRT or AT
        if (issubclass(measurements[i]._rg_var, AT)):
            pass #TODO 
        elif  (issubclass(measurements[i]._rg_var, MRT)):
            self._ax.plot(ind, val, 'bo-')
        else:
            raise ValueError("Unknown variable")


class XAxFormatter(Formatter):
    def __init__(self, xvals):
        self._xvals = xvals

    def __call__(self, x, pos=0):
        'Return the label for time x at position pos'
        ind = int(round(x))
        if ind >= len(self._xvals) or ind < 0: return ''

        return self._xvals[ind]
