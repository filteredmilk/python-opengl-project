import math
import glm
import pygame as pg

# opengl
MAJOR_VERSION = 3
MINOR_VERSION = 3
DEPTH_SIZE = 24

# RES
WIN_RES = glm.vec2(800, 600)

# controls
KEYS = {
    'FORWARD': pg.K_w,
    'BACK': pg.K_s,
    'UP': pg.K_e,
    'DOWN': pg.K_q,
    'STRAFE_L': pg.K_a,
    'STRAFE_R': pg.K_d,
    'INTERACT': pg.K_f,
    'WEAPON_1': pg.K_1,
    'WEAPON_2': pg.K_2,
    'WEAPON_3': pg.K_3,
    'WEAPON_4': pg.K_4,
}

# camera
ASPECT_RATIO = WIN_RES.x / WIN_RES.y
FOV_DEG = 50
V_FOV = glm.radians(FOV_DEG)
H_FOV = 2 * math.atan(math.tan(V_FOV * 0.5) * ASPECT_RATIO)
NEAR = 0.01
FAR = 2000.0
PITCH_MAX = glm.radians(89)

# player settings
MOUSE_SENSITIVITY = 0.0015
PLAYER_SIZE = 0.15
PLAYER_SPEED = 0.0035
PLAYER_ROT_SPEED = 0.003
PLAYER_HEIGHT = 0.6
PLAYER_POS = glm.vec3(1.5, PLAYER_HEIGHT, 1.5)

# player combat
PLAYER_INIT_HEALTH = 100
PLAYER_INIT_AMMO = 20
MAX_HEALTH_VALUE = 100
MAX_AMMO_VALUE = 999

NUM_LEVELS = 2

# COLORS
BG_COLOR = glm.vec3(0.1, 0.2, 0.25)

# TEX SIZE
TEX_SIZE = 256
TEXTURE_UNIT_0 = 0