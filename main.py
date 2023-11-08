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
    # print(data["temp"])
    # We can get this well formatted dataframe into a data dict
    data_dict = data.to_dict()
    # print(data_dict)
    temperature_list = data["temp"].to_list()
    print(temperature_list)
    # Task: Find the average of the temperatures
    print(sum(temperature_list) / len(temperature_list))
    # There is another way with just pandas
    print(data["temp"].mean())
    # Task: Obtain the max for temperatures
    print(data["temp"].max())
    # Get data from columns
    print(data.day)
    # Get Data from rows
    print(data[data.day == "Monday"])
    # Task: Obtain the max row with the max temperature
    print(data[data.temp == data.temp.max()])
    # To retrieve a specific column for a specified row
    print(data[data.day == "Monday"].condition)
    # Task: convert temps from C -> F
    print([ (x * (9/5)) + 32 for x in data.temp.tolist()])
    # Create a dataframe from scratch
    data_dic = {
        "students": ["James", "Fred", "Amy", "Jenny"],
        "scores": [6, 2, 10, 8]
    }
    data = pandas.DataFrame(data_dic)
    print(data)
#   We can also take this and create a csv file
    data.to_csv("new.csv")


