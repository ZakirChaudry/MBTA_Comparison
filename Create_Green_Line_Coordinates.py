# This file was created by Zakir Chaudry on July 8, 2019

import cv2 as cv
import numpy as np
import time
from tkinter import *
import csv

img_rgb = cv.imread('MBTA_Full.jpg')
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
template = cv.imread('Green_Circle.jpg', 0)
w, h = template.shape[::-1]
radius = 27

original_stops = []

res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)
threshold = 0.95
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):
    if pt[0] < 5000 and not (pt[0] > 4800 and pt[1] > 5100):
        original_stops.append(pt)

to_remove = []

for stop in original_stops:
    fake_list = original_stops.copy()
    fake_list.remove(stop)
    if stop not in to_remove:
        for other in fake_list:
            if other[0] + radius > stop[0] > other[0] - radius:
                if other[1] + radius > stop[1] > other[1] - radius:
                    if other not in to_remove:
                        to_remove.append(other)
                    # print("Stop being compared is " + str(stop))
                    # print("Other is " + str(other))

# print(original_stops)

for stop in to_remove:
    # print(str(stop) + "is to be removed")
    original_stops.remove(stop)

width = 500
height = 500

animation = Tk()
canvas = Canvas(animation, width=width, height=height)
canvas.pack()

with open('GreenLine.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(original_stops)

for stop in original_stops:
    new_x = stop[0]/(9600/width)
    new_y = stop[1]/(9600/height)
    new_radius = radius/(9600/height)
    new_stop = canvas.create_oval(new_x - new_radius, new_y - new_radius, new_x + new_radius,
                                  new_y + new_radius)
    animation.update()
    fake = input("x is " + str(new_x) + ", y is " + str(new_y))
    if fake == 'f':
        canvas.delete(new_stop)

time.sleep(100)
