import inspect
from RgVars import RgVar

class RgMeasurement:
    REQS_SUFF = ".Requests"
    ERRS_SUFF = ".Errors"
    MEAN_SUFF = ".ResponseTimeMean"
    DEV_SUFF = ".ResponseTimeDeviation"
    MAX_SUFF = ".ResponseTimeMax"
    AT_SUFF = ".ActualThroughput"
    TT_SUFF = ".TheoreticalThroughput"
    
    def __init__(self, variable, measurement_list):
        if inspect.isclass(variable) and issubclass(variable, RgVar):
            self._rg_var = variable
            self._name = variable.rg_name
            self._title = variable.title()
        else:
            self._rg_var = None
            self._name = variable
            self._title = variable
        vn = self._name + "%s"
        self._requests = int(measurement_list[vn%RgMeasurement.REQS_SUFF])
        self._errors = int(measurement_list[vn%RgMeasurement.ERRS_SUFF])
        self._mrt = float(measurement_list[vn%RgMeasurement.MEAN_SUFF])/1e6
        self._mrt_std_dev = float(measurement_list[vn%RgMeasurement.DEV_SUFF])/1e6
        self._mrt_max = float(measurement_list[vn%RgMeasurement.MAX_SUFF])/1e6
        self._at = float(measurement_list[vn%RgMeasurement.AT_SUFF])
        self._tt = float(measurement_list[vn%RgMeasurement.TT_SUFF])

    def with_description(self, description):
        if description is not None:
            self._description = description
        return self
