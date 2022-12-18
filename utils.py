import csv
from os.path import exists


def save_csv_file(csv_name, data_to_save, header):
    with open(csv_name, "w", encoding="utf8", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(header)
        for data in data_to_save:
            if type(data) == str:
                csv_writer.writerow([data])
            else:
                csv_writer.writerow(data)


def read_csv_file(csv_name):
    if not exists(csv_name):
        return
    with open(csv_name, "r", encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file)
        return list(csv_reader)
