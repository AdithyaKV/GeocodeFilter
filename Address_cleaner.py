#%%
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import csv
import matplotlib.pyplot as plt
from geopy.geocoders import Nominatim
from random import randint
import re

mailing_state = "state"
mailing_city = "city"
zipcode_list = [1,2,3] #add your zipcodes


with open('address.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  fields = next(reader)
  
  with open('cleaned_address.csv', 'w', newline='') as out_file:
    writer = csv.writer(out_file)
    writer.writerow(["Index","Last Name", "First Name", "Address"])
    
    i = 0
    # Iterate over the rows

    for row in reader:
        i+=1
        if  row[fields.index('Mailing State')] == mailing_state and row[fields.index('Mailing City')] == mailing_city and (row[fields.index('Mailing Zip Code')][:5] in zipcode_list):
            ret = []
            ret.append(i)
            ret.append(row[fields.index('Last Name')])
            ret.append(row[fields.index('First Name')])
            if row[fields.index('Mailing Address Line 1')].isupper():
                ret.append("$INSIDE")
            else:
                address = f"{row[fields.index('Mailing Address Line 1')]} {row[fields.index('Mailing Address Line 2')]} {row[fields.index('Mailing Address Line 3')]} {row[fields.index('Mailing City')]} {row[fields.index('Mailing State')]} {row[fields.index('Mailing Zip Code')][:5]}"
                ret.append(re.sub("Apt \w* | apt \w* | APT \w*", "", address))
            writer.writerow(ret)

# %%
