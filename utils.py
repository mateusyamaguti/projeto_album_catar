import csv

def save_csv_file(csv_name, data_to_save, header):
    with open(csv_name, 'w', encoding='utf8', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(header)
        for data in data_to_save:
            if type(data) == str:
                csv_writer.writerow([data])
            else:
                csv_writer.writerow(data)