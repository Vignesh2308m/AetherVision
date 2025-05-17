import moderngl as mgl
import glm
import numpy as np



class Scene():
    def __init__(self, ctx, width, height):
        self.ctx : mgl.Context = ctx 
        self.vao_list = []

        # Projection Matrix Parameters
        self.width = width
        self.height = height
        self.fovy = 45
        self.near = 0.1
        self.far = 100

        # View Matrix Parameters
        self.eye = glm.vec3(0.0,0.0,5.0)
        self.center = glm.vec3(0.0,0.0,0.0) 
        self.up = glm.vec3(0.0,1.0,5.0) 

        self._generate_scene() 

    def _generate_scene(self):
        self.color_tex = self.ctx.texture((self.width, self.height), components=4, dtype='f1')
        self.color_tex.filter = (mgl.NEAREST, mgl.NEAREST)
    
        self.fbo = self.ctx.framebuffer(color_attachments=[self.color_tex])

        self.projection = glm.perspective(glm.radians(self.fovy),self.width/self.height,0.1,100) 
        self.view = glm.lookAt(self.eye, self.center , self.up)
        self.model = glm.mat4(1.0)

        self.mvp = self.projection * self.view * self.model

    
    def add_vao(self, v):
        self.vao_list.append(v)
    
    def render(self):
        self.fbo.use()    # Bind framebuffer
        self.ctx.clear(0.0, 0.0, 0.0, 1.0)  # Clear it

        for i in self.vao_list:
            i.render_vao()

        self.pixels = self.fbo.read(components=4)
        self.data = np.frombuffer(self.pixels, dtype=np.uint8).astype(np.float32) / 255.0
