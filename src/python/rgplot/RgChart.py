import matplotlib.pyplot as plt
import constants as const

#class RgChart(object):
    #__metaclass__ = ABCMeta

class RgChart(object):
    
    def with_grids(self):
        self._ax.xaxis.grid(True)
        self._ax.yaxis.grid(True)
        return self

    def save_as(self, filename):
        self._create_plot()
        self._fig.savefig(filename)
        plt.close(self._fig) # close on save to avoid memory issues

    def with_ygrid(self):
        self._ax.yaxis.grid(True)
        return self
    
    def with_title(self, title = None, y_offset = const.TITLE_Y_OFFSET):
        if title is None:
            plt.title(self._title, y = y_offset)
        else:
            plt.title(title, y = y_offset)
        return self

    def with_text(self, text, x_pos, y_pos):
        self._ax.text(x_pos, y_pos, text, transform = self._ax.transAxes)
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

    def with_ylog(self):
        self._ax.set_yscale('log')
        return self
    
    def with_ylim(self, lim):
        self._ax.set_ylim(lim)
        return self

    def with_hline(self, y, color = 'b', style = '-', xmin = 0, xmax = 1):
        line = self._ax.axhline(y, xmin, xmax)
        line.set_color(color)
        line.set_linestyle(style)
        return self
    
    def wo_xticks(self):
        self._ax.get_xaxis().set_ticks([])
        return self

    def wo_yticks(self):
        self._ax.get_yaxis().set_ticks([])
        return self

    def _create_plot(self):
        pass
