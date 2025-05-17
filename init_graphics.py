import moderngl as mgl
import numpy as np
import math
import glm
from graphics.LinearRegression import Linear_Regression
from PIL import Image


class Graphics():

    def __init__(self, width, height,data):
        self.ctx = mgl.create_standalone_context()
        self.lr = Linear_Regression(self.ctx, [])

    def render(self):
        self.lr.scene.render()
        self.data = self.lr.scene.data

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
