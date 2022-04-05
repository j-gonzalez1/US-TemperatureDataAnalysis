import csv

file_in = 'GlobalLandTemperaturesByCity.csv'
file_out = 'US_LandTempsByCity.csv'
country = 'United States'

with open('GlobalLandTemperaturesByCity.csv', 'rt', encoding="utf8") as f, \
    open(file_out, "a", newline='') as f_output:
    reader = csv.reader(f, delimiter=',')
    writer = csv.writer(f_output)
    for row in reader:
        if country == row[4]:
            writer.writerow(row)