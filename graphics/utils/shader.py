import moderngl as mgl
import glm




class Shader:
    def __init__(self, ctx, expr_list=[], func_list=[]):
        self.ctx :mgl.Context = ctx
        self.expr_list = expr_list
        self.func_list = func_list

        self.vert_shader = ""
        self.frag_shader = ""

        self._vert_shader()
        self._frag_shader()

        print(self.vert_shader)
        print(self.frag_shader)

        self.prog = None

        self._gen_shader()

    
    def _gen_shader(self):

        self.prog = self.ctx.program(
            vertex_shader=self.vert_shader,fragment_shader=self.frag_shader
        )
        
    def _vert_shader(self):
        self.vert_shader = """
            #version 330 core

            in vec3 in_pos;
            in vec3 in_color;
            in vec3 in_norm;
            
            out vec3 v_pos;
            out vec3 v_color;
            out vec3 v_norm;
            
            uniform mat4 model;
            uniform mat4 view;
            uniform mat4 projection;
            
            void main() {
                vec4 world_pos = model * vec4(in_pos, 1.0);
                v_pos = vec3(world_pos);
                v_color = in_color;
                v_norm = mat3(transpose(inverse(model))) * in_norm; // normal transformation
                gl_Position = projection * view * world_pos;
            }

        """

    def _frag_shader(self):
        self.frag_shader = """
            #version 330 core

            in vec3 v_pos;
            in vec3 v_color;
            in vec3 v_norm;
            
            out vec4 FragColor;
            
            uniform vec3 lightPos = vec3(1.0, 2.0, 1.0);
            uniform float ambientStrength = 0.1;
            
            void main() {
                vec3 norm = normalize(v_norm);
                vec3 lightDir = normalize(lightPos - v_pos);
            
                float diff = max(dot(norm, lightDir), 0.0);
                vec3 color = v_color * (ambientStrength + diff);
                
                FragColor = vec4(color, 1.0);
            }
            

        """


    def get_shader(self):
        return self.prog

    def set_mvp(self, model:glm.mat4, view:glm.mat4, projection:glm.mat4):

        self.prog['model'].write(
            model.to_bytes()
        )

        self.prog['view'].write(
            view.to_bytes()
        )
        
        self.prog['projection'].write(
            projection.to_bytes()
        )

        pass