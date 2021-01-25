# Ball motion with an implicit timer

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# Initialize globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

# ball start position
ball_pos = [WIDTH / 2, HEIGHT / 2]

# [xVel, yVel]
vel = [5, 5] # pixels per update (1/60 seconds)

# define event handlers
def draw(canvas):
    
    # Update ball position

    #ball_pos[x] += vel[x]
    #ball_pos[y] += vel[y]
    ball_pos[0] += vel[0]
    ball_pos[1] += vel[1]
    
    # bounce the ball off of the...
    # BOTTOM
    if (ball_pos[1] + BALL_RADIUS >= HEIGHT):
        vel[1] *= -1

    # RIGHT
    if (ball_pos[0] + BALL_RADIUS >= WIDTH):
        vel[0] *= -1
        
    # TOP =======
    if (ball_pos[1] + BALL_RADIUS <= HEIGHT - HEIGHT):
        vel[1] *= -1
    
    # LEFT ========
    if (ball_pos[0] + BALL_RADIUS <= WIDTH - WIDTH):
        vel[0] *= -1
    
   
    # Draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    
# create frame
frame = simplegui.create_frame("Motion", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)

# start frame
frame.start()
