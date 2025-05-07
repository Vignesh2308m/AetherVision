import moderngl as mgl


class VAO():
    def __init__(self, ctx, prog, vbo, ibo, mode, params =[]):

        self.prog = prog
        self.vbo = vbo
        self.ibo = ibo
        self.mode = mode
        self.ctx : mgl.Context = ctx
        self.params = params
        
        self.vao = None
        self._create_vao()

    def _create_vao(self):


        self.vao = self.ctx.vertex_array(
            self.prog,
            self.vbo, *self.params,
            index_buffer = self.ibo
        ) 

        pass

    def get_vao(self):
        return {
            'vao': self.vao,
            'mode': self.mode
        }

    def update_prog(self, new_prog):
        self.prog = new_prog
        self._create_vao()

    def update_vbo(self, new_vbo):
        self.vbo = new_vbo
        self._create_vao()

    def update_ibo(self, new_ibo):
        self.ibo = new_ibo
        self._create_vao()

    def update_mode(self, new_mode):
        self.mode = new_mode
        self._create_vao()
