import numpy as np

class Instance():
    def __init__(self, num_of_instances, start, end):
        self.num_of_instances = num_of_instances
        self.start = start
        self.end = end
        
        self.instances = []
        self._generate_instance()
        pass

    def _generate_instance(self):
        inst_x , inst_y, inst_z = self.num_of_instances

        del_x = (self.end[0] - self.start[0])/inst_x
        del_y = (self.end[1] - self.start[1])/inst_y
        del_z = (self.end[2] - self.start[2])/inst_z


        x, y, z = self.start
        for i in range(inst_x*inst_y*inst_z):
            x += del_x
            if i % (inst_x*inst_y) == 0:
                x , y, _= self.start
                z += del_z
            
            if i % inst_y == 0:
                x, _, _ = self.start
                y += del_y
            
            self.instances.extend([x, y, z])
    
    def get_data(self):
        return np.array(
            self.instances, dtype=np.float32
        )
            