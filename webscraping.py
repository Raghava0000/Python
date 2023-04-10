# requests -- for hutting the endpoint apis
# urllib.request 

# Beautifulsoup

import urllib.request
from bs4 import BeautifulSoup
import csv
data = urllib.request.urlopen('https://www.shine.com/job-search/python-django-jobs-in-hyderabad?q=Python+Django%2C+&loc=Hyderabad')

bs_data = BeautifulSoup(data.read(),'html5lib')

# print(bs_data)

div_parent = bs_data.find('div',class_='parentClass')

# print(div_parent)


child_divs = div_parent.find_all('div',class_='jobCard_jobCard__jjUmu white-box-border jobCard')

with open('webscraping_data.csv','w',newline="") as file_data:
    csv_writer = csv.writer(file_data)
    csv_writer.writerow(['Title','Company Name','Exprience',"Location"])
    for row in child_divs:
        title = row.find('h2').text
        company_name = row.find('div',class_="jobCard_jobCard_cName__mYnow").text
        year_exp = row.find('div',class_="jobCard_jobCard_lists_item__YxRkV jobCard_jobIcon__3FB1t").text
        location = row.find('div',class_="jobCard_jobCard_lists_item__YxRkV jobCard_locationIcon__zrWt2").text
        csv_writer.writerow([title,company_name,year_exp,location])
