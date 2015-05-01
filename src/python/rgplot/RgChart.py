import matplotlib.pyplot as plt

#class RgChart(object):
    #__metaclass__ = ABCMeta

class RgChart(object):
    
    def with_grids(self):
        self._ax.xaxis.grid(True)
        self._ax.yaxis.grid(True)
        return self

    def save_as(self, filename):
        self._fig.savefig(filename)
        plt.close(self._fig) # close on save to avoid memory issues

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

    def with_ylim(self, lim):
        self._ax.set_ylim(lim)
        return self

    def wo_xticks(self):
        self._ax.get_xaxis().set_ticks([])
        return self

    def wo_yticks(self):
        self._ax.get_yaxis().set_ticks([])
        return self
