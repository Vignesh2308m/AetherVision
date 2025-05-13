from graphics.utils.buffer import Buffer
from graphics.utils.instance import Instance
from graphics.utils.shader import Shader
from graphics.utils.shapes import UVSphere
from graphics.utils.vao import VAO
import moderngl as mgl

class Linear_Regression():
    def __init__(self, ctx, data, model, view, projection):
        self.ctx : mgl.Context = ctx
        self.data = data

        self.shape = UVSphere(radius=0.1, stacks=16,slices=16,position=(0.0, 0.0, 0.0),schema=(True,True,False,True), color=(1.0,0.0,0.1))
        vert, ind = self.shape.get_data()
        self.instances = Instance((10,10,10), (-0.5,-0.5,-0.5), (0.5,0.5,0.5))
        elem = self.instances.get_data()
        self.buffer = Buffer(self.ctx, vert, ind, elem)
        vbo, ibo, ebo = self.buffer.get_buffer()
        self.shader = Shader(self.ctx)
        self.shader.set_mvp(model=model, view=view, projection=projection)
        prog = self.shader.get_shader()
        self.vao = VAO(self.ctx, prog=prog, buffer_format=[(vbo, '3f 3f 3f', 'in_pos', 'in_norm', 'in_color'),
                                                           (ebo, '3f /i', 'in_offset')] ,
                       ibo=ibo, mode=mgl.TRIANGLES)


    def get_vao(self):
        return self.vao.get_vao()

    def _create_graphics(self):
        return