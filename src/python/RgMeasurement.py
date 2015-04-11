class RgMeasurement:
    REQS_SUFF = ".Requests"
    ERRS_SUFF = ".Errors"
    MEAN_SUFF = ".ResponseTimeMean"
    DEV_SUFF = ".ResponseTimeDeviation"
    MAX_SUFF = ".ResponseTimeMax"
    AT_SUFF = ".ActualThroughput"
    TT_SUFF = ".TheoreticalThroughput"
    
    def __init__(self, var_name, measurement_list):
        vn = var_name + "%s"
        self._requests = int(measurement_list[vn%RgMeasurement.REQS_SUFF])
        self._errors = int(measurement_list[vn%RgMeasurement.ERRS_SUFF])
        self._mrt = float(measurement_list[vn%RgMeasurement.MEAN_SUFF])/1e6
        self._mrt_std_dev = float(measurement_list[vn%RgMeasurement.DEV_SUFF])/1e6
        self._mrt_max = float(measurement_list[vn%RgMeasurement.MAX_SUFF])/1e6
        self._at = float(measurement_list[vn%RgMeasurement.AT_SUFF])
        self._tt = float(measurement_list[vn%RgMeasurement.TT_SUFF])
