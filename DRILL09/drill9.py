from pico2d import *
import random

open_canvas(1280, 1024)

background = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

chara_x = 600
chara_y = 600

hand_x = 700
hand_y = 700

xframe = 0
yframe = 0

def go_line(p1, p2):
    global xframe
    global yframe

    if p1[0] < p2[0]:
        yframe = 1
    elif  p1[0] > p2[0]:
        yframe = 0

    for i in range(0, 100 + 1, 2):
        t = i / 100
        x = (1-t) * p1[0] + t * p2[0]
        y = (1-t) * p1[1] + t * p2[1]
        clear_canvas()
        background.clip_draw(0, 0, 1280, 1024, 640, 512)
        hand.clip_draw(0, 0, 50, 52, p2[0], p2[1])
        character.clip_draw(xframe * 100, yframe * 100, 100, 100, x, y)
        update_canvas()
        xframe = (xframe + 1) % 8
        delay(0.1)

while(True):
    if chara_x != hand_x or chara_y != hand_y:
        go_line((chara_x, chara_y), (hand_x, hand_y))
        chara_x, chara_y = hand_x, hand_y
        hand_x, hand_y = random.randint(0,1280), random.randint(0,1024)

close_canvas()