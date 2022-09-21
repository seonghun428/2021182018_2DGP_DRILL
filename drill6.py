#import os
#os.chdir('C:/Users/shson/Desktop/2-2/2DGP/2021182018_2DGP_DRILL/DRILL06')

from pico2d import *
import math

open_canvas()

grass=load_image('grass.png')
character = load_image('character.png')

def rect_move(x,y):
    while(x<790):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x=x+2
        delay(0.01)
    
    while(y<580):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y=y+2
        delay(0.01)

    while(x>10):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x=x-2
        delay(0.01)

    while(y>90):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y=y-2
        delay(0.01)

    
def circle_move(x,y,r):
    while(r>360):
        y=math.sin(r/360 * 2 * math.pi) * 200 + 300
        x=math.cos(r/360 * 2 * math.pi) * 200 + 300
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        r=r+10
        delay(0.01)


while(True):
    x=10
    y=90
    rect_move(x,y)
    x=400
    y=90
    r=0
    circle_move(x,y,r)