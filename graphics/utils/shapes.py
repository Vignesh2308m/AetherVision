import numpy as np
import math


class UVSphere:
    def __init__(self, radius=1.0, stacks=32, slices=64, position=(0.0, 0.0, 0.0), color=(1.0, 1.0, 1.0), schema=(True,True,True,True)):
        self.radius = radius
        self.stacks = stacks
        self.slices = slices
        self.center = np.array(position, dtype=np.float32)
        self.color = color
        self.schema = schema
        self.vertex_len = 0
        

        self.vertices = []
        self.indices = []

        self._generate_geometry()

    def _generate_geometry(self):
        r, g, b = self.color
        tx, ty, tz = self.center
        
        schema_val = (3, 3, 2, 3)

        for i in range(4):
            if self.schema[i]:
                self.vertex_len += schema_val[i]
        
        if self.schema[0] == True:
            px = tx
            py = ty + self.radius
            pz = tz 
            self.vertices.extend([px, py, pz])
    
        if self.schema[1] == True:
            nx, ny, nz = 0.0, 1.0, 0.0
            self.vertices.extend([nx, ny, nz]) 

        if self.schema[2] == True:
            u = 0.0
            v = 0.5
            self.vertices.extend([u, v]) 

        if self.schema[3] == True:
            self.vertices.extend([r, g, b]) 


        
        # Top center vertex
        # self.vertices.extend([tx, ty + self.radius, tz, 0.0, 1.0, 0.0, 0.5, 0.0, r, g, b])
        top_index = 0

        # Generate sphere vertices
        for i in range(1, self.stacks):
            theta = i * math.pi / self.stacks
            sin_theta = math.sin(theta)
            cos_theta = math.cos(theta)

            for j in range(self.slices + 1):
                phi = j * 2 * math.pi / self.slices
                sin_phi = math.sin(phi)
                cos_phi = math.cos(phi)

                x = self.radius * sin_theta * cos_phi
                y = self.radius * cos_theta
                z = self.radius * sin_theta * sin_phi


                if self.schema[0] == True:
                    px = x + tx
                    py = y + ty
                    pz = z + tz 
                    self.vertices.extend([px, py, pz])
    
                if self.schema[1] == True:
                    nx, ny, nz = x / self.radius, y / self.radius, z / self.radius
                    self.vertices.extend([nx, ny, nz]) 

                if self.schema[2] == True:
                    u = j / self.slices
                    v = i / self.stacks
                    self.vertices.extend([u, v]) 

                if self.schema[3] == True:
                    self.vertices.extend([r, g, b]) 
        
        if self.schema[0] == True:
            px = tx
            py = ty - self.radius
            pz = tz 
            self.vertices.extend([px, py, pz])
    
        if self.schema[1] == True:
            nx, ny, nz = 0.0, -1.0, 0.0
            self.vertices.extend([nx, ny, nz]) 

        if self.schema[2] == True:
            u = 0.0
            v = 0.5
            self.vertices.extend([u, v]) 

        if self.schema[3] == True:
            self.vertices.extend([r, g, b]) 


        # Bottom center vertex
        bottom_index = len(self.vertices) // self.vertex_len
        # self.vertices.extend([tx, ty - self.radius, tz, 0.0, -1.0, 0.0, 0.5, 1.0, r, g, b])

        # Generate indices for middle quads
        for i in range(self.stacks - 2):
            for j in range(self.slices):
                first = 1 + i * (self.slices + 1) + j
                second = first + self.slices + 1
                self.indices.extend([first, second, first + 1])
                self.indices.extend([second, second + 1, first + 1])

        # Top cap
        for j in range(self.slices):
            first = 1 + j
            next_ = 1 + (j + 1) % (self.slices + 1)
            self.indices.extend([top_index, first, next_])

        # Bottom cap
        base = 1 + (self.stacks - 2) * (self.slices + 1)
        for j in range(self.slices):
            first = base + j
            next_ = base + (j + 1) % (self.slices + 1)
            self.indices.extend([first, bottom_index, next_])

    def get_data(self):
        return (
            np.array(self.vertices, dtype=np.float32),
            np.array(self.indices, dtype=np.uint32)
        )

    def translate(self, position):
        translation = np.array(position, dtype=np.float32) - self.center
        self.center += translation

        for i in range(0, len(self.vertices), self.vertex_len):  # step by vertex structure size
            self.vertices[i] += translation[0]  # x
            self.vertices[i + 1] += translation[1]  # y
            self.vertices[i + 2] += translation[2]  # z

        return self.get_data()

    def rotate(self, axis, angle_degrees):
            angle_radians = math.radians(angle_degrees)
            axis = np.array(axis, dtype=np.float32)
            axis = axis / np.linalg.norm(axis)
            x, y, z = axis
            c = math.cos(angle_radians)
            s = math.sin(angle_radians)
            t = 1 - c
    
            # Rotation matrix (Rodrigues' formula)
            rot = np.array([
                [t*x*x + c,     t*x*y - s*z, t*x*z + s*y],
                [t*x*y + s*z, t*y*y + c,     t*y*z - s*x],
                [t*x*z - s*y, t*y*z + s*x, t*z*z + c    ]
            ], dtype=np.float32)
    
            for i in range(0, len(self.vertices), 12):
                pos = np.array(self.vertices[i:i+3]) - self.center
                rotated = rot @ pos + self.center
                self.vertices[i:i+3] = rotated.tolist()
    
            return self.get_data()