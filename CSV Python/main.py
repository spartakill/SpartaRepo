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
import csv


# with open command below

# try:
#     with open("order.txt") as file:
#         file_line_list = [file.readline()]
#         for line in file_line_list:
#             for str in line.split(", "):
#                 print(str)
# except FileNotFoundError as msg:
#     print("File Does Not Exist")

# import csv
#
# with open("user_details.csv", newline='') as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=",")
    # print(csvreader)
    # for row in csvreader:
    #     print(row)
    # iterable_csv = iter(csvreader) # removing the header row
    # next(iterable_csv)
    # for row in iterable_csv:
    #     print(row)
    # print(list(csvreader)[0][1])
# removes first row which is usually the header row

# import csv
#
# def transform_user_details(csv_file_name):
#     new_user_data = []
#     with open(csv_file_name, newline='') as csvfile:
#         user_details_csv = csv.reader(csvfile, delimiter=",")
#
#         for user in user_details_csv:
#             transformation = []
#             transformation.append(user[1]) # first name
#             transformation.append(user[2]) # last name
#             transformation.append(user[-1]) # email
#             new_user_data.append(transformation)
#
#     return new_user_data
#
# # print(transform_user_details("user_details.csv"))
#
# def create_new_user_details(old_file_name="user_details.csv", new_file_name="new_user_details.csv"):
#     new_user_data = transform_user_details(old_file_name)
#     with open(new_file_name, "w", newline='') as new_file:
#         csv_writer = csv.writer(new_file)
#         csv_writer.writerows(new_user_data)
#
# create_new_user_details()

# IMDB Data Transformation

import csv
def transform_imdb_data(csv_file_name):
    new_imdb_data = []
    with open(csv_file_name, newline='') as csvfile:
        imdb_data_csv = csv.reader(csvfile, delimiter=",")

        for movie in imdb_data_csv:
            transformation = []
            if movie[0] == 'movie': # iterates through list of titles selecting only movie related titles
                if movie[4] >= "2010": # selects movies from year 2010 onwards
                    transformation.append(movie[0]) # title type
                    transformation.append(movie[1]) # primary title
                    transformation.append(movie[4]) # start year
                    transformation.append(movie[6]) # runtime
                    transformation.append(movie[7]) # genres
                    new_imdb_data.append(transformation)

    return new_imdb_data

# print(transform_imdb_data("imdbtitles.csv"))

def create_new_imdb_data(old_file_name="imdbtitles.csv", new_file_name="new_imdb_data.csv"):
    new_imdb_data = transform_imdb_data(old_file_name)
    with open(new_file_name, "w", newline='') as new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerows(new_imdb_data)

create_new_imdb_data()