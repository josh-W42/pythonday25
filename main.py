# if __name__ == '__main__':
#     with open("weather_data.csv") as file:
#         data = file.readlines()
#     values = data
#     print(values)

# import csv
#
# if __name__ == '__main__':
#     with open("weather_data.csv") as file:
#         data = csv.reader(file)
#         temperatures = []
#         for row in data:
#             if row[1] != "temp":
#                 temperatures.append(int(row[1]))
#         print(temperatures)

import pandas

# When working with csv files or any type of data, Use pandas, it's easier.

if __name__ == '__main__':
    data = pandas.read_csv("weather_data.csv")
    print(data["temp"])

