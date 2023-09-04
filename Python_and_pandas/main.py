# try:
#     file = open("order.txt", "r")
#     file_line_list = [file.readline()]
#     for line in file_line_list:
#         for str in line.split(", "):
#             print(str)
#     file.close()
# except FileNotFoundError as msg:
#     print("File Does Not Exist")
# This above uses file open and file close

# with open command below

# try:
#     with open("order.txt") as file:
#         file_line_list = [file.readline()]
#         for line in file_line_list:
#             for str in line.split(", "):
#                 print(str)
# except FileNotFoundError as msg:
#     print("File Does Not Exist")

import csv

with open("user_details.csv", newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # print(csvreader)
    # for row in csvreader:
    #     print(row)
    # iterable_csv = iter(csvreader) # removing the header row
    # next(iterable_csv)
    # for row in iterable_csv:
    #     print(row)
    print(list(csvreader)[0][1])
# removes first row which is usually the header row
