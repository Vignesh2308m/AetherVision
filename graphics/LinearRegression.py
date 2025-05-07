from graphics.utils.buffer import Buffer
from graphics.utils.shader import Shader
from graphics.utils.shapes import UVSphere
from graphics.utils.vao import VAO
import moderngl as mgl

class Linear_Regression():
    def __init__(self, ctx, data, model, view, projection):
        self.ctx : mgl.Context = ctx
        self.data = data

        self.shape = UVSphere(stacks=360,slices=360,schema=(True,True,False,True))
        vert, ind = self.shape.get_data()
        self.buffer = Buffer(self.ctx, vert, ind)
        vbo, ibo = self.buffer.get_buffer()
        self.shader = Shader(self.ctx)
        self.shader.set_mvp(model=model, view=view, projection=projection)
        prog = self.shader.get_shader()
        self.vao = VAO(self.ctx, prog=prog, vbo=vbo, ibo=ibo, mode=mgl.TRIANGLES, params= ['in_pos', 'in_norm','in_color'])


    def get_vao(self):
        return self.vao.get_vao()

    def _create_graphics(self):
        return