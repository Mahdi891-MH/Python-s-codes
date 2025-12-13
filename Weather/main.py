import csv
temperature = []
with open("weather-data.csv") as data_file:
    data = csv.reader(data_file)
    for d in data:
        if d[1] != 'temp':
            temperature.append(int(d[1]))

print(temperature)
