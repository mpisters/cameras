import csv
import os


def parse_csv_cameras_to_json(path_to_csv):
    cameras = []
    print(os.getcwd())
    with open(path_to_csv, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            row.update({'row_number': line_count})
            cameras.append(row)
            line_count += 1
    return cameras


