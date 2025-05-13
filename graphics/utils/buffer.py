import moderngl as mgl


class Buffer():
    def __init__(self, ctx, vertices, indices, element):
        self.ctx :mgl.Context = ctx
        self.vertices = vertices
        self.indices = indices
        self.element = element

        self.vbo = None
        self.ibo = None
        self.ebo = None

        self._create_vbo()
        self._create_ibo()
        self._create_ebo()

    def get_buffer(self):
        return(
            self.vbo, self.ibo, self.ebo
        )
        
    def _create_vbo(self):
        self.vbo = self.ctx.buffer(
            self.vertices
        ) 
    
    def _create_ibo(self):
        self.ibo = self.ctx.buffer(
            self.indices
        )
     
    def _create_ebo(self):
        self.ebo = self.ctx.buffer(
            self.element
        )