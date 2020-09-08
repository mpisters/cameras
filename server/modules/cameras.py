import csv
import os
import re


def parse_csv_cameras_to_json(path_to_csv):
    cameras = []
    with open(path_to_csv, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            match_error = re.match(r'\bERROR\b', row['Camera'])
            if match_error:
                continue
            match = re.match(r'^\w*-\w*-(\d*)-?', row['Camera'])
            number = match.group(1) if match else None
            row.update({'number': number})
            cameras.append(row)
            line_count += 1
    return cameras


