from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

angle = 0.0
speed = 2.0  

def init():
    glClearColor(0.5, 0.8, 1.0, 1.0)
    gluOrtho2D(-1, 1, -1, 1)

def draw_house():
   
    glColor3f(0.8, 0.5, 0.3)
    glBegin(GL_QUADS)
    glVertex2f(-0.8, -0.3)
    glVertex2f(-0.5, -0.3)
    glVertex2f(-0.5, 0.05)
    glVertex2f(-0.8, 0.05)
    glEnd()

   
    glColor3f(0.6, 0.1, 0.1)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.85, 0.05)
    glVertex2f(-0.65, 0.2)
    glVertex2f(-0.45, 0.05)
    glEnd()

   
    glColor3f(0.3, 0.2, 0.1)
    glBegin(GL_QUADS)
    glVertex2f(-0.68, -0.3)
    glVertex2f(-0.62, -0.3)
    glVertex2f(-0.62, -0.05)
    glVertex2f(-0.68, -0.05)
    glEnd()

def draw_scene():
    glClear(GL_COLOR_BUFFER_BIT)

   
    glBegin(GL_QUADS)
    glColor3f(0.2, 0.8, 0.2)
    glVertex2f(-1, -1)
    glVertex2f(1, -1)
    glVertex2f(1, -0.3)
    glVertex2f(-1, -0.3)
    glEnd()

   
    draw_house()

   
    glColor3f(0.6, 0.6, 0.6)
    glBegin(GL_QUADS)
    glVertex2f(-0.05, -0.3)
    glVertex2f(0.05, -0.3)
    glVertex2f(0.05, 0.4)
    glVertex2f(-0.05, 0.4)
    glEnd()

  
    glPushMatrix()
    glTranslatef(0, 0.4, 0)
    glRotatef(angle, 0, 0, 1)

    for i in range(4):
        glRotatef(90, 0, 0, 1)
        glBegin(GL_TRIANGLES)
        glColor3f(1.0, 1.0, 1.0)
        glVertex2f(0, 0)
        glVertex2f(0.3, 0.05)
        glVertex2f(0.3, -0.05)
        glEnd()

    glPopMatrix()

    glutSwapBuffers()

def update(value):
    global angle, speed

    angle += speed
    if angle > 360:
        angle = 0

    glutPostRedisplay()
    glutTimerFunc(16, update, 0)

def keyboard(key, x, y):
    global speed

    if key == b's' or key == b'S':
        if speed == 0:
            speed = 2
        elif speed == 2:
            speed = 5
        elif speed == 5:
            speed = 10
        else:
            speed = 0

    print("Current Speed:", speed)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Windmill with House")

    init()
    glutDisplayFunc(draw_scene)
    glutKeyboardFunc(keyboard)
    glutTimerFunc(0, update, 0)

    glutMainLoop()

if __name__ == "__main__":
    main()
