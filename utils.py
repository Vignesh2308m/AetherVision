import numpy as np

def model_matrix(translation, rotation, scale):
    # Translation
    T = np.eye(4)
    T[:3, 3] = translation

    # Rotation around Y axis (can be extended)
    theta = np.radians(rotation[1])
    R = np.array([
        [np.cos(theta), 0, np.sin(theta), 0],
        [0, 1, 0, 0],
        [-np.sin(theta), 0, np.cos(theta), 0],
        [0, 0, 0, 1]
    ])

    # Scale
    S = np.eye(4)
    S[0, 0], S[1, 1], S[2, 2] = scale

    return T @ R @ S

def view_matrix(eye, target, up):
    f = target - eye
    f = f / np.linalg.norm(f)

    u = up / np.linalg.norm(up)
    s = np.cross(f, u)
    s = s / np.linalg.norm(s)
    u = np.cross(s, f)

    M = np.eye(4)
    M[0, :3] = s
    M[1, :3] = u
    M[2, :3] = -f

    T = np.eye(4)
    T[:3, 3] = -eye

    return M @ T

def projection_matrix(fov, aspect, near, far):
    f = 1.0 / np.tan(np.radians(fov) / 2)
    P = np.zeros((4, 4))
    P[0, 0] = f / aspect
    P[1, 1] = f
    P[2, 2] = (far + near) / (near - far)
    P[2, 3] = (2 * far * near) / (near - far)
    P[3, 2] = -1
    return P

# Example usage
model = model_matrix(translation=[0, 0, -5], rotation=[0, 45, 0], scale=[1, 1, 1])
view = view_matrix(eye=np.array([0, 0, 5]), target=np.array([0, 0, 0]), up=np.array([0, 1, 0]))
projection = projection_matrix(fov=60, aspect=16/9, near=0.1, far=100)

mvp = projection @ view @ model
