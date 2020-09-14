#Rainbow.py
from turtle import *
pensize(2)
bgcolor("black")
colors = ['red','yellow','blue','green','orange','purple']
for i in range(200):
    pencolor(colors[i & 6])
    fd(1.5*i)
    left(61)
done()
