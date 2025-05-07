import moderngl as mgl


class Buffer():
    def __init__(self, ctx, vertices, indices):
        self.ctx :mgl.Context = ctx
        self.vertices = vertices
        self.indices = indices

        self.vbo = None
        self.ibo = None

        self._create_vbo()
        self._create_ibo()

    def get_buffer(self):
        return(
            self.vbo, self.ibo
        )
        
    def _create_vbo(self):
        self.vbo = self.ctx.buffer(
            self.vertices
        ) 
    
    def _create_ibo(self):
        self.ibo = self.ctx.buffer(
            self.indices
        )