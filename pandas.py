# pip install pandas 

import pandas

# names = ["Rajesh","Suresh","Ramesh"]

# df = pandas.DataFrame(names)

# print(df)

data = pandas.read_csv('movie_info.csv')


# data = pandas.read_csv('movie_info.csv',skiprows=[1,2]) # for skipping the rows from reading inside the csv
# print(type(data))

# print(data[2:4])
# 

# data.to_json('movie_info.json',orient='records')

# data.to_json('movie_info.json',orient='index')

data.to_json('movie_info.json',orient='values')
