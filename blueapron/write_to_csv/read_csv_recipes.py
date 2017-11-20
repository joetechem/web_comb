# https://pythonspot.com/en/files-spreadsheets-csv/

import csv

title = []

filename = 'next_week_recipes.csv'
with open(filename, 'rb') as f:
    reader = csv.reader(f)

# store rows into list
    rowNr = 1
    for row in reader:
            if rowNr >= 1:
                title.append(row)

            rowNr = rowNr + 1

print title
            
