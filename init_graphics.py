import moderngl as mgl
import numpy as np
import math
import glm
from graphics.LinearRegression import Linear_Regression
from PIL import Image


class Graphics():

    def __init__(self, width, height,data):
        self.ctx = mgl.create_standalone_context()
        
        # Create a color texture
        self.color_tex = self.ctx.texture((width, height), components=4, dtype='f1')
        self.color_tex.filter = (mgl.NEAREST, mgl.NEAREST)
    
       # Attach to framebuffer
        self.fbo = self.ctx.framebuffer(color_attachments=[self.color_tex])

        self.projection = glm.perspective(glm.radians(45),width/height,0.1,100) 
        self.view = glm.lookAt(glm.vec3(0.0,0.0,5.0), glm.vec3(0.0,0.0,0.0), glm.vec3(0.0,1.0,5.0))
        self.model = glm.mat4(1.0)

        self.mvp = self.projection * self.view * self.model

        lr = Linear_Regression(self.ctx, [], self.model, self.view, self.projection)
        
        self.vao_list = []
        
        self.vao_list.append(lr.get_vao())

    def render(self):
        self.fbo.use()    # Bind framebuffer
        self.ctx.clear(0.0, 0.0, 0.0, 1.0)  # Clear it

        
        for i in self.vao_list:
            i['vao'].render(mode=i['mode'], instances = 1000)
        pass

        self.pixels = self.fbo.read(components=4)
        self.data = np.frombuffer(self.pixels, dtype=np.uint8).astype(np.float32) / 255.0

    def save_image(self, data):
        img_data_uint8 = (data * 255).astype(np.uint8)

        im = Image.fromarray(img_data_uint8, mode="L")
        im.save('img.png')
        im.close()
        
        print(self.data)

 
    def add_vao(self, vao, mode):
        self.vao_list.append(
            {
                "vao": vao,
                "mode": mode
            }
        )
