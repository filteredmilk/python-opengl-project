from model import *

class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.load()
        # skybox
        self.skybox = AdvancedSkybox(app)

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self):
        app = self.app
        add = self.add_object

        # ground
        n = 30
        s = 2
        for x in range(-n, n, s):
            for z in range(-n, n, s):
                add(Cube(app, pos=(x, -s, z)))

        # pillars
        for i in range(9):
            add(Cube(app, pos=(15, i * s, -9 + i), tex_id=2))
            add(Cube(app, pos=(15, i * s, 5 - i), tex_id=2))
        # moving cube
        #self.moving_cube = MovingCube(app, pos=(0, 8, 8), scale=(2, 2, 2), tex_id=3)
        #add(self.moving_cube)

        
        #add(Cube(app, tex_id=1, pos=(0, 1, 0), rot=(45, 0, 45)))
        # robots
        add(Robot(app, pos=(0, 1, 0), scale=(1, 1, 1)))

    def update(self):
        pass
        #self.moving_cube.rot.xyz = self.app.time
