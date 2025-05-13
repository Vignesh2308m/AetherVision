import numpy as np
import time


class BaseShape():
    def __init__(self, func, radius, position, u_range, v_range, schema, color):
        self.vertices = []
        self.indices = []
        self.elements = []

        self.radius = radius
        self.position = position
        self.u_range = u_range
        self.v_range = v_range
        self.schema = schema
        self.color = color
        self.func = func

        start = time.time() 
        self._generate_vertices()    
        self._generate_indices()
        print("Time taken to create shape", time.time()-start)

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

    def get_element(self):
        return np.array(
            self.elements , dtype=np.float32
        )




class UVSphere():
    def __init__(self, radius, stacks, slices, position, schema, color):
        uv_sphere = BaseShape(func= self.func, radius=radius,
                              u_range=[0,np.pi,stacks], 
                              v_range=[0,2*np.pi,slices],
                              position=position, 
                              schema= schema, color=color)
        
        self.vert_func = uv_sphere.get_vertices
        self.ind_func = uv_sphere.get_indices

    @staticmethod
    def func(u, v):
        return [
        np.sin(u) * np.cos(v),
        np.sin(u) * np.sin(v),
        np.cos(u)
    ]

    def get_data(self):
        return self.vert_func(), self.ind_func() 


class Line():
    def __init__(self, pos1, pos2, color):
        self.pos1 = pos1
        self.pos2 = pos2

        self.color = color

    def get_data(self):

        pass