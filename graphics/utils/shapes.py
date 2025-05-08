import numpy as np


class BaseShape():
    def __init__(self, func, radius, position, u_range, v_range, schema, color):
        self.vertices = []
        self.indices = []

        self.radius = radius
        self.position = position
        self.u_range = u_range
        self.v_range = v_range
        self.schema = schema
        self.color = color
        self.func = func

        self._generate_vertices()    
        self._generate_indices()

    def _generate_vertices(self):
        u_min, u_max, u_step = self.u_range
        v_min, v_max, v_step = self.v_range

        u_line= np.linspace(u_min, u_max, u_step)
        v_line= np.linspace(v_min, v_max, v_step)

        for i in u_line:
            for j in v_line:
                x, y, z = self.func(i,j)

                if self.schema[0] == True:
                    self._add_pos(x,y,z)
                
                if self.schema[1] == True:
                    self._add_norm(x,y,z)
                
                if self.schema[2] == True:
                    self._add_tex(i, j)
                
                if self.schema[3] == True:
                    self._add_color(x,y,z)

    def _generate_indices(self):
        _, _, u_step = self.u_range  # number of rows
        _, _, v_step = self.v_range  # number of columns

        for i in range(u_step - 1):
            for j in range(v_step - 1):
                top_left     = i * v_step + j
                top_right    = top_left + 1
                bottom_left  = (i + 1) * v_step + j
                bottom_right = bottom_left + 1

                # two triangles per quad
                self.indices.extend([
                    top_left, bottom_left, top_right,
                    top_right, bottom_right, bottom_left
                ])

    def _add_pos(self, x, y, z):
        px, py, pz = self.position
        r = self.radius
        self.vertices.extend([(x+px)*r, (y+py)*r, (z+pz)*r])        
        pass

    def _add_norm(self, x, y, z):
        self.vertices.extend([x, y, z])        
        pass
    def _add_tex(self, u, v):
        self.vertices.extend([u, v])        
        pass
    def _add_color(self, x, y, z):
        r, g, b = self.color
        self.vertices.extend([r, g, b])        
        pass

    def get_vertices(self):
        return np.array(
            self.vertices , dtype=np.float32
        )

    def get_indices(self):
        return np.array(
            self.indices , dtype=np.uint32
        )