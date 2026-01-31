# with open("weather_data.csv", mode='r') as weather:
#     data.append(weather.readlines())
#     print(data)

# import csv
#
# with open("weather_data.csv", mode='r') as weather:
#     data=(csv.reader(weather))
#     temperatures = []
#     for temperature in data:
#         if temperature[1] == 'temp':
#             continue
#         temperatures.append(int(temperature[1]))
#     print(temperatures)

import pandas
data = pandas.read_csv("weather_data.csv")
# # print(type(data))
# # print(type(data["temp"]))
#
# # data_dict = data.to_dict()
# # print(data_dict)
# # print(data_dict["day"])
# # print(data_dict["temp"])
#
temp_list = data["temp"].to_list()
print(temp_list)
print(type(temp_list))
#
# # avg = data["temp"].mean()
# # print(avg)
#
# data_temp = data["temp"]
# print(data_temp.max())
# # print(data_temp.min())

# 행 데이터 구하기, 월요일
# data_monday = data[data.day == "Monday"]
# print(data_monday)

# 온도가 가장 높은 데어티가 있는 행을 구하기
# data_temp_max = data[data.temp == data.temp.max()]
# print(data_temp_max)

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)

# data_dict = {
#     "students": ["Amy", "Jack", "Mike"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_color = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_color = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_color = len(data[data["Primary Fur Color"] == "Black"])

dict_data = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_color, cinnamon_color, black_color]
}

data_color = pandas.DataFrame(dict_data)
data_color.to_csv("color_data.csv")