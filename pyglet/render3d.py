import pyglet
from pyglet.gl import *

# Set up the window
window = pyglet.window.Window(width=800, height=600, resizable=True)
glEnable(GL_DEPTH_TEST)

# Define vertices and indices for a cube
vertices = [
    -50, -50, -50,  # bottom-left-back
    50, -50, -50,   # bottom-right-back
    50, 50, -50,    # top-right-back
    -50, 50, -50,   # top-left-back
    -50, -50, 50,   # bottom-left-front
    50, -50, 50,    # bottom-right-front
    50, 50, 50,     # top-right-front
    -50, 50, 50     # top-left-front
]

indices = [
    0, 1, 2, 3,  # back face
    3, 2, 6, 7,  # top face
    7, 6, 5, 4,  # front face
    4, 5, 1, 0,  # bottom face
    1, 5, 6, 2,  # right face
    4, 0, 3, 7   # left face
]

# Convert vertices and indices to OpenGL-compatible format
vertices = (GLfloat * len(vertices))(*vertices)
indices = (GLuint * len(indices))(*indices)

# Define color for the cube
color = (GLubyte * 12)(255, 0, 0, 255,  # red
                        0, 255, 0, 255,  # green
                        0, 0, 255, 255,  # blue
                        255, 255, 0, 255)  # yellow

# Set up the scene
@window.event
def on_draw():
    window.clear()
    
    glLoadIdentity()
    glTranslatef(window.width/2, window.height/2, -200)  # Move the cube to the center of the window and back
    
    glRotatef(30, 1, 0, 0)  # Rotate the cube around the x-axis
    glRotatef(45, 0, 1, 0)  # Rotate the cube around the y-axis
    
    glEnableClientState(GL_VERTEX_ARRAY)
    glEnableClientState(GL_COLOR_ARRAY)
    
    glVertexPointer(3, GL_FLOAT, 0, vertices)
    glColorPointer(4, GL_UNSIGNED_BYTE, 0, color)
    
    glDrawElements(GL_QUADS, len(indices), GL_UNSIGNED_INT, indices)
    
    glDisableClientState(GL_VERTEX_ARRAY)
    glDisableClientState(GL_COLOR_ARRAY)

# Run the application
pyglet.app.run()