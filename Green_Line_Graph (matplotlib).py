# This file was created by Zakir Chaudry on July 8, 2019
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline, BSpline
import numpy as np
import csv

green_line_csv = open('GreenLineStops.csv', 'r')
labels = False

x_values = []
y_values = []

all_stops = list(csv.reader(green_line_csv))
# print(all_stops)
stops = {}
for stop in all_stops:
    stops[stop[2]] = {'x': float(stop[0]), 'y': 9000 - float(stop[1]),
                      'next': stop[3]}
# print(stops)
for stop in stops:
    # plt.plot(line[0], line[1], 'go-')
    x = stops[stop]['x']
    y = stops[stop]['y']
    next = stops[stop]['next']
    x_values.append(x)
    y_values.append(y)
    if labels:
        plt.annotate(stop, (x, y), (x + 60, y - 150))
    plt.plot([x, stops[next]['x']], [y, stops[next]['y']], linewidth=7, color='Green', zorder=1)

x = np.array(x_values)
y = np.array(y_values)

# xnew = np.linspace(x.min(), x.max(), 300)
# spl = make_interp_spline(x, y, k=3)
# power_smooth = spl(xnew)
# plt.plot(xnew, power_smooth)
plt.scatter(x_values, y_values, edgecolors='green', c='w', marker='o', zorder=2)
plt.show()
