import csv

def csv_as_list(csv_file_name, delim = ';'):
    with open(csv_file_name, 'rb') as csv_file:
        data = csv.DictReader(csv_file, delimiter = delim)
        csv_list = []
        for item in data:
            csv_list.append(item)
        return csv_list

