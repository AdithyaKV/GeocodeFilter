from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import csv
import matplotlib.pyplot as plt
from geopy.geocoders import Nominatim
from random import randint


with open('cleaned_address.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  fields = next(reader)
  
  with open('coords_out_pt2.csv', 'w', newline='') as out_file:
    writer = csv.writer(out_file)
    writer.writerow(["Index","Last Name", "First Name", "Longitude", "Lattitude"])
    
    j = 0
    # Iterate over the rows
    user_agent = 'user_me_{}'.format(randint(10000,99999))
    geolocator = Nominatim(user_agent=user_agent)

    for row in reader:
        j+=1
        if j > 6750:
            ret = []
            ret.append(row[fields.index('Index')])
            ret.append(row[fields.index('Last Name')])
            ret.append(row[fields.index('First Name')])
            if row[fields.index('Address')] == "$INSIDE":
                ret.append(row[fields.index('Address')])
                ret.append(row[fields.index('Address')])
            else:
                address = row[fields.index('Address')]
                location = geolocator.geocode(address)
                if location == None:
                    ret.append(-1)
                    ret.append(-1)
                    print("addr not found")
                else:
                    ret.append(location.latitude)
                    ret.append(location.longitude)
                    print(location.address)
            writer.writerow(ret)
