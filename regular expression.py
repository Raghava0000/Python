# Regualr expressions:

# 445 784-7484

# re - regular expression

import re

# {} - for representing the length.

# \d - digits

# pattern - pattern of which format you want to perform operation..

pattern = r'\d{3} \d{3}-\d{4}'

sample_str = " My mobile 543 647-7484number is 435 657-8494"

# match -- Match can find the content matching with the pattern inside the string, if it find the pattern at the starting of the string..
# search -- Search can find the content matching with the pattern inside the string, if it find the pattern at the starting of the string
# findall

# match_data = re.match(pattern,sample_str)

# print(match_data)


# search_data = re.search(pattern,sample_str)

# print(search_data)

# findall -- it will return all the values which are matching with the pattern inside the string...

# findall_data = re.findall(pattern,sample_str)

# print(findall_data)

# print(dir(re))
# import csv
# with open('sample_csv.csv','r') as file_obj:
#     csv_data = csv.reader(file_obj)
#     for row in csv_data:
#         if re.search(pattern,row[1]):
#             print(row)
