import glm

class Light:
    def __init__(self, position=(3, 3, -3), color=(1, 1, 1)):
        self.position = glm.vec3(position)
        self.color = glm.vec3(color)
        self.direction = glm.vec3(0, 0, 0)

        # light intensities
        # ambient, diffuse, specular
        self.Ia = 0.1 * self.color
        self.Id = 0.8 * self.color
        self.Is = 1.0 * self.color

        self.m_view_light = self.get_view_matrix()

    def get_view_matrix(self):
        return glm.lookAt(self.position, self.direction, glm.vec3(0, 1, 0))
