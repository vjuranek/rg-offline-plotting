import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import Formatter
from RgVars import MRT, AT

class LineChart:

    def __init__(self, *measurements):
        self.__fig, self.__ax = plt.subplots()
        self.__create_lines(measurements)


    def save_as(self, filename):
        self.__fig.savefig(filename)
        plt.close(self.__fig) # close on save to avoid memory issues

    def with_defaults(self):
        self.with_title().with_ylabel().with_grids()
        return self
    
    def with_grids(self):
        self.__ax.xaxis.grid(True)
        self.__ax.yaxis.grid(True)
        return self

    def with_xticks_names(self, xt_names = None):
        if xt_names is not None:
            formatter = XAxFormatter(xt_names)
            self.__ax.xaxis.set_major_formatter(formatter)
            #self.__fig.autofmt_xdate()
        return self
    
    def with_xlabel(self, xlabel = None):
        if xlabel is None:
            plt.xlabel(self.__xlabel)
        else:
            plt.xlabel(xlabel)
        return self
    
    def with_ylabel(self, ylabel = None):
        if ylabel is None:
            plt.ylabel(self.__ylabel)
        else:
            plt.ylabel(ylabel)
        return self

    def with_title(self, title = None):
        if title is None:
            plt.title(self.__title)
        else:
            plt.title(title)
        return self
        
    def __create_lines(self, measurements):
        nm = len(measurements)
        self.__ax.set_xlim(-0.5, nm - 0.5)
        ind = np.arange(nm)
        val = []
        xax = []
        for i in range(0, len(measurements)):
            val.append(measurements[i]._mrt)
            xax.append(measurements[i]._title)
            
            self.__title = measurements[i]._title #last name wins
            if measurements[i]._rg_var is None:
                self.__ylabel = ""
            else:
                self.__ylabel = measurements[i]._rg_var.ylabel # TODO check, that _rg_var is not None
                
        plt.xticks(ind)
        #decide if plot MRT or thgroughtpu
        if (issubclass(measurements[i]._rg_var, AT)):
            pass
        # elif  (issubclass(measurements[i]._rg_var, MRT)):
        # default to MRT
        else:
            self.__ax.plot(ind, val, 'bo-')
                


class XAxFormatter(Formatter):
    def __init__(self, xvals):
        self._xvals = xvals

    def __call__(self, x, pos=0):
        'Return the label for time x at position pos'
        ind = int(round(x))
        if ind >= len(self._xvals) or ind < 0: return ''

        return self._xvals[ind]
