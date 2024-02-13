from player import Player, PlayerAttribs
from scene import Scene
from shader_program import ShaderProgram
from texture import Texture
import pygame as pg

class Engine:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx
        self.num_level = 1
        self.texture = Texture(self)
        self.player_attribs = PlayerAttribs()
        self.player: Player = None
        self.shader_program: ShaderProgram = None
        self.scene: Scene = None

        self.new_game()

    def new_game(self):
        self.player = Player()
        self.shader_program.update()
        self.scene.update()

    def render(self):
        self.scene.render()