# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 15:20:19 2020

@author: USER
"""
import turtle
alex=turtle.Turtle()
def draw_triangle(distance):
    for i in range(3):
        alex.forward(distance)
        alex.left(60)
        
draw_triangle(10)
draw_triangle(15)
turtle.done()