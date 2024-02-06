import pygame as pg
import moderngl as mgl
import glm

class Texture:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx
        self.textures = {}
        self.textures[0] = self.get_texture(path='textures/desert.png')
        self.textures[1] = self.get_texture(path='textures/test.png')
        self.textures[2] = self.get_texture(path='textures/desert.png')
        self.textures[3] = self.get_texture(path='textures/metal.png')
        self.textures['robot'] = self.get_texture(path='objects/robot/robot.png')

        self.textures['skybox'] = self.get_texture_cube(dir_path='textures/skybox/', ext='png')

        self.textures['depth_texture'] = self.get_depth_texture()

    def get_depth_texture(self):
        depth_texture = self.ctx.depth_texture(self.app.WIN_SIZE)
        depth_texture.repeat_x = False
        depth_texture.repeat_y = False
        return depth_texture

    def get_texture(self, path):
        texture = pg.image.load(path).convert()
        texture = pg.transform.flip(texture, flip_x=False, flip_y=True)
        texture = self.ctx.texture(size=texture.get_size(), components=3,
                                   data=pg.image.tostring(texture, 'RGB'))

        
        texture.build_mipmaps()
        texture.filter = (mgl.NEAREST_MIPMAP_LINEAR, mgl.NEAREST)

        texture.anisotropy = 32.0
        return texture

    def get_texture_cube(self, dir_path, ext='png'):
        faces = ['right', 'left', 'top', 'bottom'] + ['front', 'back'][::-1]
        textures = []
        for face in faces:
            texture = pg.image.load(dir_path + f'{face}.{ext}').convert()
            if face in ['right', 'left', 'front', 'back']:
                texture = pg.transform.flip(texture, flip_x=True, flip_y=False)
            else:
                texture = pg.transform.flip(texture, flip_x=False, flip_y=True)
            textures.append(texture)
        size = textures[0].get_size()
        texture_cube = self.ctx.texture_cube(size=size, components=3, data=None)

        for i in range(6):
            texture_data = pg.image.tostring(textures[i], 'RGB')
            texture_cube.write(face=i, data=texture_data)

        return texture_cube

    def destroy(self):
        [tex.release() for tex in self.textures.values()]

"""class AnimatedTexture(Texture):
    def __init__(self, ctx, speedx, speedy):
        super().__init__(ctx)

        self.speed = [speedx, speedy]"""
