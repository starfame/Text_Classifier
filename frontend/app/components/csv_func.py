import csv


def check_csv_format(file):
    try:
        csv.reader(file)
        return True
    except:
        return False
