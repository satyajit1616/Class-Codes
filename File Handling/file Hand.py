# import csv
from dataclasses import fields

# import csv
# print(dir(csv))
# import csv
# rows = [["Name","Age","City"],
#         ["Satyajit","23","Bhubaneswar"],
#         ["Abhijit","23","Cuttack"]]
# with open("data.csv","w")as file1:
#     writer = csv.writer(file1)
#     writer.writerows(rows)
#
# with open("data.csv","r") as file2:
#     reader = csv.reader(file2)
#     for i in reader:
#         for j in i:
#             print(j,end='   ')
#         print()
import csv
data = [
    {"Name": "Satya","Age":"23","City":"BBSR"},
    {"Name": "Abhi","Age":"22","City":"CTC"},
    {"Name": "Dibya","Age":"28","City":"KDP"}
]
# with open("data.csv","w",newline='') as file3:
#     fields = ["Name","Age","City"]
#     writer = csv.DictWriter(file3,fieldnames=fields)
#     writer.writeheader()
#     writer.writerows(data)

with open("data.csv","r") as file4:
    reader = csv.DictReader(file4)
    for i in reader:
        print(i)
