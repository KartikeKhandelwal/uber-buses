import numpy
import os

# Base coordinate : 1.290542 , 103.781539 

r = open("test.txt", "r+")
w = open("test2.txt", "w+")
lines = r.readlines()

for line in lines:
    line = line[6:]
    w.write(line)

w.close()