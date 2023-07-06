# import csv
# with open(r"E:\Programming\Python\python-practice\Weather\weather_data.csv") as data:
#     weathers = csv.reader(data)
#     temps = list()
#     for row in weathers:
#         if row[1] != 'temp':
#             temps.append(int(row[1]))
#         print(row)
# print(temps)
import pandas
datas = pandas.read_csv(
    r"E:\Programming\Python\python-practice\Weather\weather_data.csv")
datas_dict = datas.to_dict()
# print(datas_dict)
# average = float()
# for row in datas["temp"]:
#     average += row
# print(f"average is = {average/len(datas['temp'])}")
# print(datas["temp"].max())
# print(datas[datas.temp == 'Monday'])
print(datas[datas.temp == datas.temp.max()])
