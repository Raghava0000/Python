# File operations: Operations that we can perform on the files..

# To Perform anything you have to open the file first..

# opening the file can be done in 2 ways..


# 3 modes
    # reading -r
    # writing - w
    # appending - a

# 1st way
# open(filepath,mode)

# 2nd Way
# """
# with open(filepath,mode) as file_data:
#     statements
# """

# file_data = open('dialogues.txt','r')

# print(file_data)

# print(file_data.closed)

# file_data.close() # This will close the opened file..

# print(file_data.closed)


# with open('dialogues.txt','r') as file_data:
#     pass

# print(file_data.closed)

# with will automatically close the file once the cursor comes outside of with block.

# reading -- 
    # read() -- will read the complete content in the file at once..
    # readline() -- It will read one line at a time..
    # readlines() -- It will read the complete content but line by line format..


# with open('dialogues.txt','r') as file_data:
#     # print(file_data.read())
#     # print(file_data.readline())
#     # print(file_data.readline())
#     data = file_data.readlines()[1:]
#     for ele in data:
#         print(ele)


# writing(w): This will overwrite the data in the file..
    # write()
    # writelines()

# if file is not present it will create the file during writing and appending mode.
# with open('C:/Users/reddy/OneDrive/Desktop/dialogues.txt','w') as file_data:
#     # file_data.write('Seat kadukada assembly gate kuda takanivvavu\n')
#     # file_data.write('Narikakoddi neku alupu vastadi emo naku oopu vastadi.')
#     file_data.writelines(['Seat kadukada assembly gate kuda takanivvavu\n', 'Narikakoddi neku alupu vastadi emo naku oopu vastadi.\n', 'Breaks leni buldozer ni tokkipadestha\n'])



# appending(a) : This is for adding the content to the previous content..
    # write ()
    # writelines()
# with open('C:/Users/reddy/OneDrive/Desktop/dialogues.txt','a') as file_data:
#     file_data.write('Sarvejana sukinobavanthu okka veedu tappa.\n')
#     # file_data.write('Narikakoddi neku alupu vastadi emo naku oopu vastadi.')
#     file_data.writelines(['Seat kadukada assembly gate kuda takanivvavu\n', 'Narikakoddi neku alupu vastadi emo naku oopu vastadi.\n', 'Breaks leni buldozer ni tokkipadestha\n']) 

# first.txt
    # a=5
    # b=6
# second.txt
    # c=a+b 

# third.txt
    # c=???



# File operations on CSV file:-
# CSV:- comma separated values
# CSV:- its for working on CSV file

import csv

# reading of csv:
# with open('first class.csv','r') as file_data:
    # print(file_data)
    # print(file_data.read())
    # csv_data=csv.reader(file_data)

    # next(csv_data)//
    # print(list(csv_data)[1:2])

    # for ele in csv_data:
    #     if ele[1]=='chiranjeevi':
    #         print(ele)


    # writing operations:
    # 1)writerow
    # 2)writerows
# with open('second class.csv','w', newline='') as file_data:
#     csv_write_data = csv.writer(file_data)
#     csv_write_data.writerow(['movie name','actor name'])
#     csv_write_data.writerow(['indra', 'chiru'])
#     csv_write_data.writerows([['indra', 'chiru'],['bahubali','prabhas'],['kushi','pawankalyan']])


# appending:-add new row data to the previous rows in the file.

# with open('second class.csv','a', newline='') as file_data:
#     csv_write_data = csv.writer(file_data)
#     csv_write_data.writerow(['indra', 'chiru'])


# json:-(javascript object notation):
# [
#     {
#     "name": "raghava",
#     "address": "hyderabad",
#     "email": "raghava@gmail.com",
#     "phone": ["9632147785","7412385901"]
#     },
#     {
#     "name": "raghava",
#     "address": "hyderabad",
#     "email": "raghava@gmail.com",
#     "phone": ["9632147785","7412385901"]
#     }
# ]

import json

# sample_data = '{"name": "raghava", "address": "hyderabad"}'
# print(type(sample_data))
# data = json.loads(sample_data)
# print(data)
# print(type(data))

# data=json.loads(sample_data)
# print(type(data))
# print(data)

# data = open('sample_data.json')
# new_data = json.load(data)
# print(new_data)
# print(type(new_data))

# final_data = []

        # print(final_data)

# with open('sample_new.json', 'w') as file_data:
#     json.dump(final_data,file_data,indent=4)

# print((json.dumps(final_data,indent=4)))

print(dir(json))