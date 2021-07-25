from bokeh.io import output_file, show
from bokeh.models import GMapPlot, GMapOptions, ColumnDataSource, \
    Circle, Range1d, PanTool, WheelZoomTool, BoxSelectTool

import re

API_KEY = "AIzaSyAtt_C5_5WTwW-0bTHYi4aSDmURoU1UzvE"

with open("message_new_pen.txt") as file:
    content = file.read()

# print(content)

coordinates = re.findall(r"[\d]+.[\d]+,-[\d]+.[\d]+", content)
# print(coordinates)

lats = []
longs = []
for coordinate in coordinates:
    lat, long = coordinate.split(",")
    lats.append(lat)
    longs.append(long)

map_options = GMapOptions(lat=0, lng=0, zoom=3)

plot = GMapPlot(x_range=Range1d(), y_range=Range1d(), map_options=map_options)
plot.title.text = "Example Plot"
plot.api_key = API_KEY

source = ColumnDataSource(
    data=dict(
        lat=lats,
        lon=longs,
    )
)
