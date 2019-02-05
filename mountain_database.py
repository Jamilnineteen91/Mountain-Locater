import csv
import sqlite3


#Database connection and commands setup
conn= sqlite3.connect('Albanian_mountains.db')
cur=conn.cursor()

#Creates Database
cur.execute("""CREATE TABLE IF NOT EXISTS Albanian_mountains(
            name text,
            latitude FLOAT,
            longitude FLOAT
            )""")
conn.commit()

#Reads/parses mountain csv file
with open('Albania.csv','r') as csv_file:
    csv_reader=csv.reader(csv_file)

    next(csv_reader) #Skips header row

    #Imports csv file contents into the database
    for line in csv_reader:
        cur.execute('INSERT INTO Albanian_mountains VALUES (:name, :latitude, :longitude)',
                    {'name':line[0], 'latitude':line[1], 'longitude':line[2]})

