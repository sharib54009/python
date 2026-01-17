<<<<<<< HEAD
from turtle import *
import colorsys 

speed(0)
bgcolor("black")
colormode(1)   # allow RGB in 0-1 range

h = 0
for i in range(16):
    for j in range(18):
        c = colorsys.hsv_to_rgb(h, 1, 1)
        color(c)
        h += 0.005
        rt(90)
        circle(150 - j * 6, 90)
        lt(90)
        circle(150 - j * 6, 90)
        rt(180)
        circle(40, 2)   # fixed line

done()


=======
from turtle import *
import colorsys 

speed(0)
bgcolor("black")
colormode(1)   # allow RGB in 0-1 range

h = 0
for i in range(16):
    for j in range(18):
        c = colorsys.hsv_to_rgb(h, 1, 1)
        color(c)
        h += 0.005
        rt(90)
        circle(150 - j * 6, 90)
        lt(90)
        circle(150 - j * 6, 90)
        rt(180)
        circle(40, 2)   # fixed line

done()


>>>>>>> ccf339ab26e53daabfa936e12c7d806a11bd917e
