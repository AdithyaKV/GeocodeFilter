#%%

from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import csv
import matplotlib.pyplot as plt

infilename = "coords_file_here"

points = []
with open(infilename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for coord in csvreader:
        points.append((float(coord[0]), float(coord[1])))

dist_rows = []
fields = []
with open('address.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  fields = next(reader)
  for row in reader:
    dist_rows.append(row)

polygon = Polygon(points)


with open('coords_op.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  fields_a = next(reader)
  
  with open('output.csv', 'w', newline='') as out_file:
    writer = csv.writer(out_file)
    writer.writerow(fields)
    for row in reader:
      ind = int(row[0])
      if row[fields_a.index("Longitude")] == "$INSIDE" or polygon.contains(Point(float(row[fields_a.index("Latitude")]), float(row[fields_a.index("Longitude")]))):
        writer.writerow(dist_rows[ind-1])

# %%
