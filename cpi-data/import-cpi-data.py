import csv
from pymongo import MongoClient

# ---------------------- Info ---------------------- #

# TODO readme

# Running this script will process and insert CPI data from cpi-raw.csv to MongoDB
# Currently, cpi-raw.csv contains CPI data from 2006-2023

# Data formatted as follows:
# - year            : int
# - annual_cpi      : float
# - half1_cpi       : float
# - half2_cpi       : float
# - {month number}  : object
#     - cpi         : float
#     - rate        : float (where 1.00 is 100%)

# ------------------- Processing Data ------------------- #

file = "cpi-raw.csv"
mapping = [  # mapping columns to dictionary attributes
    'year',
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
    'annual_cpi',
    'half1_cpi',
    'half2_cpi'
]
data = []  # init data


def process_row_to_dict(csv_row):
    """ Process csv row to dictionary using column mappings """
    row_data = {}
    for i in range(len(csv_row)):
        value = csv_row[i]
        if value not in (None, ''):
            if i == 0:
                row_data[mapping[i]] = int(value)               # year is an int
            elif i in range(1, 13):
                row_data[mapping[i]] = {'cpi': float(value)}    # months must be dictionaries with floats
            else:
                row_data[mapping[i]] = float(value)             # additional annual attributes are floats
    return row_data


with open(file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:     # ignore headers
            line_count += 1
            continue
        elif len(row) != 16:    # error if unexpected shape
            raise Exception("Invalid input")
        else:                   # process valid rows
            processed_row = process_row_to_dict(row)
            data.append(processed_row)
            line_count += 1


def process_month_inflation(year_index):
    """ Calculate month to month inflation rate for the given year """
    # !! assumes years in data are in order
    year_data = data[year_index]

    def process_rate(curr_cpi, prev_year_index, curr_month, prev_month):
        prev_cpi = data[prev_year_index][str(prev_month)]['cpi']
        rate = (curr_cpi - prev_cpi) / curr_cpi
        data[year_index][curr_month]['rate'] = rate

    for month in range(1, 13):
        str_month = str(month)
        if str_month not in year_data:  # stops loop once it reaches a missing month
            break

        cpi = year_data[str_month]['cpi']
        if month == 1 and year_index > 0:
            process_rate(cpi, year_index - 1, str_month, 12)
        elif month > 1:
            process_rate(cpi, year_index, str_month, month - 1)


# calculate inflation rates for all data
for i in range(len(data)):
    process_month_inflation(i)
    print(data[i])


# ------------------- Importing Data ------------------- #

client = MongoClient()

# need a db called ds4300
db = client.ds4300
collection = db.cpis

for i in range(len(data)):
    post_id = collection.insert_one(data[i])
    print(post_id)

