from dearpygui import dearpygui as dpg



class Slider():
    def __init__(self, label, min, max):
        self.label = label
        self.min = min
        self.max = max

        self.value = None

        self._generate_slider()

    def _generate_slider(self):
        dpg.add_slider_float(label=self.label, min_value=self.min, max_value=self.max, callback=self._callback)
    
    def _callback(self, sender, appdata):
        self.value = float(appdata)