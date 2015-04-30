import matplotlib.pyplot as plt

#class RgChart(object):
    #__metaclass__ = ABCMeta

class RgChart(object):
    
    def with_grids(self):
        self._ax.xaxis.grid(True)
        self._ax.yaxis.grid(True)
        return self

    def with_ygrid(self):
        self._ax.yaxis.grid(True)
        return self
    
    def with_title(self, title = None):
        if title is None:
            plt.title(self._title)
        else:
            plt.title(title)
        return self

    def with_xlabel(self, xlabel = None):
        if xlabel is None:
            plt.xlabel(self._xlabel)
        else:
            plt.xlabel(xlabel)
        return self

    def with_ylabel(self, ylabel = None):
        if ylabel is None:
            plt.ylabel(self._ylabel)
        else:
            plt.ylabel(ylabel)
        return self

