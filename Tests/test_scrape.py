# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from  csv import writer
import re

#Requests country name from user
user_input=input('Enter Country:')
country=user_input[0:1].upper()+user_input[1:].lower()

#URLS needed to retrieve country and mountain coordinates
country_url="https://www.nationmaster.com/country-info/stats/Geography/Geographic-coordinates"
mountain_list_url='https://en.wikipedia.org/wiki/List_of_mountains_in_'+country

#Web scrapper set-up: response requests and HTML parser
response=requests.get(mountain_list_url)
bs=BeautifulSoup(response.text,'html.parser')

region_response=requests.get(country_url)
bs4=BeautifulSoup(region_response.text,'html.parser')



#***---Country coordinate parsing---***

region_table=bs4.find('tbody')
country_coords=[]

#Retrieves the country's coordinates
for row in region_table.find_all('tr'):
    reg_name = row.find('span', class_='full').get_text()
    reg_coords = row.find('td').find_next('td').get_text()
    if reg_name == country:
        country_coords.append(reg_coords)
    else:
        pass

cc=country_coords[0].split(',')
country_lat=cc[0].split(',')
country_lon=cc[1].split(',')
print(country_lat)
print(country_lon)




#***---Mountain coordinate parsing---***

table=bs.find('table',class_='wikitable')

#Creates CSV file from parsed table data
with open(country+'.csv','w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Name', 'Latitude', 'Longitude']
    csv_writer.writerow(headers)

    #Converts DMS coordinates to DD coordinates.
    def dd_calc(deg, min, sec, direc):
        if direc == 'W' or direc == 'S':
            return -1 * (deg + (min / 60) + (sec / 3600))
        else:
            return deg + (min / 60) + (sec / 3600)


    def dms_to_dd(dms):
        parts = re.split('[^\d\w]+', dms)  # Splits all symbols except for integers and unicode characters

        if len(parts) > 4:  # This statement accounts for a parsing of decimals
            return dd_calc(int(parts[0]), int(parts[1]), (int(parts[2]) + (int(parts[3]) / 100)), parts[4])
        else:
            return dd_calc(int(parts[0]), int(parts[1]), int(parts[2]), parts[3])


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
