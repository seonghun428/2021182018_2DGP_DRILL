from pico2d import *

open_canvas(1280, 1024)

background = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

x = 600
y = 600

dir = 0
# left = 0, right = 1
dirx = 0
# left = -1, right = 1
diry = 0
# up = 1, down = -1

running = False

xframe = 0

yframe = 3

def handle_event():
    global dir
    global dirx
    global diry
    global yframe
    global running

    events = get_events()

    for event in events:
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                running = True
                dir = 0
                dirx -= 1
            elif event.key == SDLK_RIGHT:
                running = True
                dir =1
                dirx += 1
            elif event.key == SDLK_UP:
                running = True
                diry += 1
            elif event.key == SDLK_DOWN:
                running = True
                diry -= 1

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                running = False
                dirx += 1
            elif event.key == SDLK_RIGHT:
                running = False
                dirx -= 1
            elif event.key == SDLK_UP:
                running = False
                diry -= 1
            elif event.key == SDLK_DOWN:
                running = False
                diry += 1


while(True):
    if running == True and dir == 0:
        yframe = 0
    elif running == True and dir == 1:
        yframe = 1
    elif running == False and dir == 0:
        yframe = 2
    elif running == False and dir == 1:
        yframe = 3

    x += dirx * 10
    y += diry * 10

    if x >= 1240:
        x = 1240
    elif x <= 40:
        x = 40

    if y >= 984:
        y = 984
    elif y <= 40:
        y = 40

    clear_canvas()
    background.clip_draw(0, 0, 1280, 1024, 640, 512)
    character.clip_draw(xframe * 100, yframe * 100, 100, 100, x, y)
    update_canvas()
    xframe = (xframe + 1) % 8
    delay(0.1)
    handle_event()

close_canvas()