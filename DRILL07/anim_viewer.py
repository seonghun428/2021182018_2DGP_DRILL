from pico2d import *

open_canvas()

character = load_image('sprites.png')

for a in range(4):
    xframe = 0
    yframe = 0
    for i in range(4):
        for j in range(50):
            clear_canvas()
            character.clip_draw(xframe * 96 , yframe * 104, 96, 104, 400, 300)
            update_canvas()
            xframe = (xframe+1) % 10
            delay(0.05)
            get_events()
        yframe += 1
    
    xframe = 0
    
    
    for j in range(15):
        clear_canvas()
        character.clip_draw(xframe * 96 , yframe * 104, 96, 104, 400, 300)
        update_canvas()
        xframe = (xframe+1) % 3
        delay(0.05)
        get_events()
    yframe += 1
    
    xframe = 0
    for j in range(5):
        clear_canvas()
        character.clip_draw(xframe * 96 , yframe * 104, 96, 104, 400, 300)
        update_canvas()
        delay(0.05)
        get_events()
    yframe += 1
    
    xframe = 0
    for i in range(2):
        for j in range(15):
            clear_canvas()
            character.clip_draw(xframe * 96 , yframe * 104, 96, 104, 400, 300)
            update_canvas()
            xframe = (xframe+1) % 3
            delay(0.05)
            get_events()
        yframe += 1

close_canvas()