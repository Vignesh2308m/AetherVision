import dearpygui.dearpygui as dpg


class ViewPort():
    def __init__(self, width, height):
        dpg.create_context()
        dpg.create_viewport(title="AI Game", width= width, height= height)
        pass

    def run(self):
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()
    
    def add_window(self, label, width, height, win_func):
        win_func()    
        pass