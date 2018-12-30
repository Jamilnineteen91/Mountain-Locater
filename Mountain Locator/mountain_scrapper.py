# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from  csv import writer
import re

#Requests country name from user
user_input=input('Enter Country:')
country=user_input[0:1].upper()+user_input[1:].lower()


country_url='https://en.wikipedia.org/wiki/List_of_mountains_in_'+country

response=requests.get(country_url)
bs=BeautifulSoup(response.text,'html.parser')

#Creates table
table=bs.find('table',class_='wikitable')

#Creates CSV file from parsed table data
with open(country+'.csv','w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Name', 'Latitude', 'Longitude']
    csv_writer.writerow(headers)

    #Converts DMS coordinates to DD coordinates.
    def dms_to_dd(dms):
        parts = re.split('[^\d\w]+', dms)#Splits all symbols except for integers and unicode characters
        if len(parts) > 4:
            deg = int(parts[0])
            min = int(parts[1])
            sec = int(parts[2]) + (int(parts[3]) / 100)#Correction from a decimal split
            if parts[4] == 'W' or parts[4] == 'S':
                return -1 * (deg + (min / 60) + (sec / 3600))
            else:
                return deg + (min / 60) + (sec / 3600)

        else:
            deg = int(parts[0])
            min = int(parts[1])
            sec = int(parts[2])
            if parts[3] == 'W' or parts[3] == 'S':
                return -1 * (deg + (min / 60) + (sec / 3600))
            else:
                return deg + (min / 60) + (sec / 3600)


    #Parses through the data of interest in table
    for row in table.find_all('tr')[1:]:
        name=row.find('td').find_next('td').get_text()
        lat=row.find('span',class_='latitude').get_text()
        long=row.find('span',class_='longitude').get_text()
        #Converts DMS coordinates to DD coordinates
        latitude=dms_to_dd(lat)
        longitude=dms_to_dd(long)

        #Writes data to csv
        csv_writer.writerow([name, latitude, longitude])

