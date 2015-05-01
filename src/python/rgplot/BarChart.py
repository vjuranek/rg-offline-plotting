import matplotlib.pyplot as plt
from RgChart import RgChart
from RgVars import MRT, AT

class BarChart(RgChart):
    COLORS = ['r','b','g','y','gray','violet','orange'] #TODO harcoded list for now, autometed list TBD
    BAR_WIDTH = 0.35
    OPACITY = 0.4
    ERROR_CONFIG = {'ecolor': '0.3'}

    def __init__(self, *measurements):
        self._fig, self._ax = plt.subplots()
        self._create_plot(measurements)
    
    def save_as(self, filename):
        self._fig.savefig(filename, bbox_extra_artists=(self._legend,), bbox_inches='tight')
        plt.close(self._fig) # close on save to avoid memory issues

    def with_defaults(self):
        self.with_title().with_legend().with_ylabel().with_ygrid().with_bar_labels().wo_xticks()
        return self
        
    def with_legend(self):
        self._legend = plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), fancybox=True, shadow=True, ncol=5)
        #plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        return self
        
    def with_bar_labels(self):
        self._label_bars()
        return self
    
    def _create_plot(self, measurements):
        self._bars = []
        for i in range(0, len(measurements)):
            self._title = measurements[i]._title #last name wins
            if measurements[i]._rg_var is None:
                self._ylabel = ""
            else:
                self._ylabel = measurements[i]._rg_var.ylabel # TODO check, that _rg_var is not None
                
            #decide if plot MRT or thgroughtpu
            if (issubclass(measurements[i]._rg_var, AT)):
                self._bars.append(self._create_at_bar(measurements[i], i))
            # elif  (issubclass(measurements[i]._rg_var, MRT)):
            # default to MRT
            else:
                self._bars.append(self._create_mrt_bar(measurements[i], i))
                
    def _create_mrt_bar(self, measurement, i):
        bar = plt.bar(i, measurement._mrt, BarChart.BAR_WIDTH,
                      alpha = BarChart.OPACITY,
                      color = BarChart.COLORS[i],
                      yerr = measurement._mrt_std_dev,
                      error_kw = BarChart.ERROR_CONFIG,
                      label = measurement._description)
        return bar

    def _create_at_bar(self, measurement, i):
        bar = plt.bar(i, measurement._at, BarChart.BAR_WIDTH,
                      alpha = BarChart.OPACITY,
                      color = BarChart.COLORS[i],
                      label = measurement._description)
        return bar

    def _label_bars(self):
        for bar in self._bars:
            for ibar in bar:
                height = ibar.get_height()
                self._ax.text(ibar.get_x() + ibar.get_width()/2., 1.05*height, '%1.2f'%float(height), ha='center', va='bottom')
