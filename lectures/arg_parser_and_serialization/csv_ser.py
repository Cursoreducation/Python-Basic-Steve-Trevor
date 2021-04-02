import csv

with open('2020_june_mini.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        current_row = row
        print(row)

with open('2020_june_mini.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerows('iterable')