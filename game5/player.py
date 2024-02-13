from camera import Camera
from settings import *

class PlayerAttribs:
    def __init__(self):
        self.health = PLAYER_INIT_HEALTH
        self.num_level = 1

    def update(self, player):
        self.health = player.health

class Player(Camera):
    def __init__(self, eng, position=PLAYER_POS, yaw=0, pitch=0):
        self.app = eng.app
        self.eng = eng

        super().__init__(position, yaw, pitch)

    def update(self):
        self.mouse_control()
        self.keyboard_control()
        super().update()

    def mouse_control(self):
        mouse_dx, mouse_dy = pg.mouse.get_rel()
        if mouse_dx:
            self.rotate_yaw(delta_x = mouse_dx * MOUSE_SENSITIVITY)

        if mouse_dy:
            self.rotate_pitch(delta_y = mouse_dy * MOUSE_SENSITIVITY)

    def keyboard_controls(self):
        key_state = pg.key.get_pressed()
        vel = PLAYER_SPEED * self.app.delta_time
        next_step = glm.vec2()

        if key_state[KEYS['FORWARD']]:
            next_step += self.move_forward(vel)
        if key_state[KEYS['BACK']]:
            next_step += self.move_back(vel)
        if key_state[KEYS['STRAFE_L']]:
            next_step += self.move_left(vel)
        if key_state[KEYS['STRAFE_R']]:
            next_step += self.move_right(vel)

        self.move(next_step = next_step)

    def move(self, next_step):
        self.position.x += next_step[0]
        self.position.z += next_step[1]