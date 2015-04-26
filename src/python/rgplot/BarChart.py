import matplotlib.pyplot as plt
from RgVars import MRT, AT

class BarChart:
    COLORS = ['r','b','g','y','gray','violet','orange'] #TODO harcoded list for now, autometed list TBD
    BAR_WIDTH = 0.35
    OPACITY = 0.4
    ERROR_CONFIG = {'ecolor': '0.3'}

    def __init__(self, *measurements):
        self.__fig, self.__ax = plt.subplots()
        self.__create_bars(measurements)

    def save_as(self, filename):
        self.__fig.savefig(filename, bbox_extra_artists=(self._legend,), bbox_inches='tight')
        plt.close(self.__fig) # close on save to avoid memory issues

    def with_defaults(self):
        self.with_title().with_legend().with_ylabel().with_ygrid().with_bar_labels().wo_xticks()
        return self
        
    def with_legend(self):
        self._legend = plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), fancybox=True, shadow=True, ncol=5)
        #plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        return self
        
    def with_xlabel(self, xlabel):
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

    def with_ylim(self, lim):
        self.__ax.set_ylim(lim)
        return self

    def with_ygrid(self):
        self.__ax.yaxis.grid(True)
        return self

    def with_bar_labels(self):
        self.__label_bars()
        return self
    
    def wo_xticks(self):
        self.__ax.get_xaxis().set_ticks([])
        return self

    def __create_bars(self, measurements):
        self.__bars = []
        for i in range(0, len(measurements)):
            self.__title = measurements[i]._title #last name wins
            if measurements[i]._rg_var is None:
                self.__ylabel = ""
            else:
                self.__ylabel = measurements[i]._rg_var.ylabel # TODO check, that _rg_var is not None
                
            #decide if plot MRT or thgroughtpu
            if (issubclass(measurements[i]._rg_var, AT)):
                self.__bars.append(self.__create_at_bar(measurements[i], i))
            # elif  (issubclass(measurements[i]._rg_var, MRT)):
            # default to MRT
            else:
                self.__bars.append(self.__create_mrt_bar(measurements[i], i))
                
    def __create_mrt_bar(self, measurement, i):
        bar = plt.bar(i, measurement._mrt, BarChart.BAR_WIDTH,
                      alpha = BarChart.OPACITY,
                      color = BarChart.COLORS[i],
                      yerr = measurement._mrt_std_dev,
                      error_kw = BarChart.ERROR_CONFIG,
                      label = measurement._description)
        return bar

    def __create_at_bar(self, measurement, i):
        bar = plt.bar(i, measurement._at, BarChart.BAR_WIDTH,
                      alpha = BarChart.OPACITY,
                      color = BarChart.COLORS[i],
                      label = measurement._description)
        return bar

    def __label_bars(self):
        for bar in self.__bars:
            for ibar in bar:
                height = ibar.get_height()
                self.__ax.text(ibar.get_x() + ibar.get_width()/2., 1.05*height, '%1.2f'%float(height), ha='center', va='bottom')
