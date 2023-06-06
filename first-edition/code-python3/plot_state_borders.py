import re
import matplotlib.pyplot as plt

segments = []
points = []

lat_long_regex = r"<point lat=\"(.*)\" lng=\"(.*)\""

with open("states.txt", "r") as f:
    lines = list(f)

for line in lines:
    if line.startswith("</state>"):
        segments.extend((p1, p2) for p1, p2 in zip(points, points[1:]))
        points = []
    if s := re.search(lat_long_regex, line):
        lat, lon = s.groups()
        points.append((float(lon), float(lat)))

def plot_state_borders(color='0.8'):
    for (lon1, lat1), (lon2, lat2) in segments:
        plt.plot([lon1, lon2], [lat1, lat2], color=color)
