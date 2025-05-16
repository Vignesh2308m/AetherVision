from dearpygui import dearpygui as dpg
from ai.model_load import Load_AI
from init_ui import ViewPort
from init_graphics import Graphics
from init_ai import AI_Interface
import moderngl as mgl
from functools import partial
from array import array
from graphics.LinearRegression import Linear_Regression

def add_graphics(color_tex):
    with dpg.texture_registry(show=False):
        dpg.add_raw_texture(800,600,color_tex,format=dpg.mvFormat_Float_rgba, tag="img")

    with dpg.window(label="window"):
        dpg.add_image(texture_tag="img",width=800,height=600)

    pass

def main():
    l = Load_AI()
    a = AI_Interface() 
    g = Graphics(800,600,a.data)
    g.render()
    v = ViewPort(800,600)
    
    func = partial(add_graphics, g.data)
    v.add_window("Test", 800, 600,func)
    v.run()
    pass

if __name__ == '__main__':
    main()

