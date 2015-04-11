import csv
from RgMeasurement import RgMeasurement

class RgReport:
    DELIM = ';'
    
    def __init__(self, csv_file_name):
        self.csv_file_name = csv_file_name
        self.records = self.__csv_as_list()

    def total(self, variable = None):
        if variable is None:
            return self.records[len(self.records)-1]
        else:
            return self.records[len(self.records)-1][variable]

    def total_in_mu(self, variable):
        '''Radar Gun stores results in nanoseconds. Typical scale is however microsecond.'''
        try:
            return float(self.records[len(self.records)-1][variable])/1000
        except ValueError:
            return 0 # TODO throws custom exception?

    def measurement_of(self, variable):
        return RgMeasurement(variable, self.total())

    def __csv_as_list(self):
        with open(self.csv_file_name, 'rb') as csv_file:
            data = csv.DictReader(csv_file, delimiter = RgReport.DELIM)
            csv_list = []
            for item in data:
                csv_list.append(item)
            return csv_list
