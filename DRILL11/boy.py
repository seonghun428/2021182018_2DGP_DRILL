from pico2d import *

# 이벤트 정의
# 0 1 2 3 4 5
RD, LD, RU, LU, TIMER, AD  = range(6)

# 키 입력 확인 단순화
key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYDOWN, SDLK_a): AD
}

class IDLE:
    def enter(self, event): # 상태에 들어갈 때 행하는 액션
        self.dir = 0
        self.timer = 1000

    def exit(self): # 상태를 나올 때 행하는 액션
        pass

    def do(self): # 상태에 있을 때 지속적으로 행하는 액션
        self.frame = (self.frame + 1) % 8
        self.timer -= 2
        if self.timer == 0:
            self.add_event(TIMER)
        delay(0.02)

    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        else:
            if self.face_dir == 1:
                self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
            else:
                self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)

class RUN:
    @staticmethod
    def enter(self, event): # 상태에 들어갈 때 행하는 액션
        # 방향 결정, 어떤 키가 눌려서 RUN으로 들어왔나
        # 키 이벤트 정보가 필요하다
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1

    @staticmethod
    def exit(self): # 상태를 나올 때 행하는 액션
        self.face_dir = self.dir

    @staticmethod
    def do(self): # 상태에 있을 때 지속적으로 행하는 액션
        self.frame = (self.frame + 1) % 8
        self.x += self.dir * 3
        self.x = clamp(0, self.x, 800)
        delay(0.02)

    @staticmethod
    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)

class SLEEP:
    def enter(self, event): # 상태에 들어갈 때 행하는 액션
        pass

    def exit(self): # 상태를 나올 때 행하는 액션
        pass

    def do(self): # 상태에 있을 때 지속적으로 행하는 액션
        self.frame = (self.frame + 1) % 8
        delay(0.02)

    def draw(self):
        if self.face_dir == -1:
            self.image.clip_composite_draw(self.frame * 100, 200, 100, 100, -3.141592 / 2, '', self.x + 25, self.y - 25, 100, 100)
        else: # 오른쪽 눕기
            self.image.clip_composite_draw(self.frame * 100, 300, 100, 100, 3.141592 / 2, '', self.x - 25, self.y - 25, 100, 100)

class AUTO_RUN:
    def enter(self, event): # 상태에 들어갈 때 행하는 액션
        print('A enter')
        self.dir = self.face_dir

    def exit(self): # 상태를 나올 때 행하는 액션
        pass

    def do(self): # 상태에 있을 때 지속적으로 행하는 액션
        self.frame = (self.frame + 1) % 8
        self.x += self.dir * 3
        if self.x >= 800:
            self.dir -= 2
        elif self.x <= 0:
            self.dir += 2
        delay(0.02)

    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y + 40, 200, 200)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y + 40, 200, 200)

next_state = {
    IDLE : {RU : RUN, LU : RUN, RD : RUN, LD : RUN, TIMER: SLEEP, AD: AUTO_RUN},
    RUN : {RU : IDLE, LU : IDLE, RD : IDLE, LD : IDLE, AD: AUTO_RUN},
    SLEEP: {RD: RUN, LD: RUN, RU: RUN, LU: RUN, TIMER: SLEEP, AD: AUTO_RUN},
    AUTO_RUN: {RD: RUN, LD: RUN, RU: RUN, LU: RUN, AD: IDLE}
}

class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')
        self.q = [] # 이벤트 큐 초기화
        self.cur_state = IDLE
        self.cur_state.enter(self, None) # 초기 상태의 엔트리 액션 수행

    def add_event(self, event):
        self.q.insert(0, event)

    def update(self):
        self.cur_state.do(self) # 현재 상태의 do 액션 수행
        
        # .이벤트 확인, 이벤트에 따른 변환 처리
        if self.q: # q에 이벤트가 있으면 == 이벤트가 발생하면
            event = self.q.pop()
            self.cur_state.exit(self)
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)

    def handle_event(self,event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)