from turtle import *
import random as r
width(5)
speed(10)
for i in range(100000000000000):
    dist = i * 5 / 3 
    color('blue')
    fd(dist)
    color('red')
    fd(dist)
    color('green')
    fd(dist)
    rt(89)
input()
