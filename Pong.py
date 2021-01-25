# Implementation of classic arcade game Pong
# Dave DC - Oct 17 2014 - Francis Bui
# Updated January 2021

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
color = 0
direction = "LEFT"

ball_pos = [WIDTH / 2, HEIGHT / 2]
vel = [-1, 1]

paddle1_pos = [PAD_WIDTH /2, HEIGHT / 2]
paddle2_pos = [WIDTH - PAD_WIDTH /2, HEIGHT / 2]

paddle1_vel = 0
paddle2_vel = 0

score_left = 0
score_right = 0
score_left_pos = [425, 50]
score_right_pos = [125, 50]

colorChange = False
ballShrinkFlag = False
padShrinkFlag = False


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
        
    vel[0] = random.randrange(2, 5)
    vel[1] = (random.randrange(1, 4)) *-1
    
    if direction == "LEFT":
        vel[0] *= -1
    
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    
    
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score_left, score_right, direction  # these are ints
    
    score_left = 0
    score_right = 0
    
    start_dir = random.randrange(0, 2)
    if start_dir == 0:
        direction = "LEFT"
    else:
        direction = "RIGHT"
        
    spawn_ball(direction)

def color_change():
    global colorChange, color # boolean flag

    if colorChange == False:
        colorChange = True
    elif colorChange == True:
        colorChange = False
        color = 0

def ball_shrink():
    global ballShrinkFlag, BALL_RADIUS

    if ballShrinkFlag == False:
        ballShrinkFlag = True
    elif ballShrinkFlag == True:
        ballShrinkFlag = False
        BALL_RADIUS = 20

def pad_shrink():
    global padShrinkFlag, PAD_HEIGHT

    if padShrinkFlag == False:
        padShrinkFlag = True
    elif padShrinkFlag == True:
        padShrinkFlag = False
        PAD_HEIGHT = 80

def draw(canvas):
    global score_left, score_right, paddle1_pos, paddle2_pos, ball_pos, ball_vel, direction, color, colorChange, ballShrinkFlag, padShrinkFlag, BALL_RADIUS, PAD_HEIGHT
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # update ball ============================
    ball_pos[0] += vel[0]
    ball_pos[1] += vel[1]
    
    #bounce off ceiling
    if ball_pos[1] - BALL_RADIUS <= 0:
        vel[1] *= -1
     
    #bounce off floor
    if ball_pos[1] + BALL_RADIUS >= HEIGHT:
        vel[1] *= -1
        
    
    # left side
    if ball_pos[0] - BALL_RADIUS <= PAD_WIDTH:
        #check for paddle connect
        if (ball_pos[1] >= (paddle1_pos[1] - HALF_PAD_HEIGHT)) and (ball_pos[1] <= (paddle1_pos[1] + HALF_PAD_HEIGHT)): 
            #reverse horiz direction and speed ball up by 10%
            if colorChange == True:
                color += 1
            if ballShrinkFlag == True:
                BALL_RADIUS -= .5
            if padShrinkFlag == True:
                PAD_HEIGHT -= 4

            vel[0] *= -1.15
            vel[1] *= 1.15
        else:
            #ball hits wall
            score_left += 1
            
            #send the next ball towards the last scorer
            if vel[0] > 0:
                direction = "LEFT"
            else:
                direction = "RIGHT"
                
            spawn_ball(direction)

        
            
    # right side
    if ball_pos[0] + BALL_RADIUS >= WIDTH - PAD_WIDTH:
        #check for paddle connect
        if (ball_pos[1] >= (paddle2_pos[1] - HALF_PAD_HEIGHT)) and (ball_pos[1] <= (paddle2_pos[1] + HALF_PAD_HEIGHT)): 
            #reverse direction and speed up by 10%
            if colorChange == True:
                color +=1
            if ballShrinkFlag == True:
                BALL_RADIUS -= .5
            if padShrinkFlag == True:
                PAD_HEIGHT -= 4

            vel[0] *= -1.15
            vel[1] *= 1.15
        else:
            score_right += 1
            
            #send the next ball towards the last scorer
            if vel[0] > 0:
                direction = "LEFT"
            else:
                direction = "RIGHT"
                
            spawn_ball(direction)
            #ball_pos = [WIDTH / 2, HEIGHT / 2]
        
        
    #==========================================
    
        
    # draw ball
    if color == 0:
        canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")
    if colorChange == True:
        if color == 1:
            canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "Red", "Red")
        elif color == 2:
            canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "Orange", "Orange")
        elif color == 3:
            canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "Yellow", "Yellow")
        elif color == 4:
            canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "Green", "Green")
        elif color == 5:
            canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "Blue", "Blue")
        elif color == 6:
            canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "Purple", "Purple")
        elif color == 7:
            color -= 6


    # update paddle's vertical position, keep paddle on the screen
    pad_acc = 4.0
    global paddle1_vel, paddle2_vel
    if (paddle1_pos[1] + paddle1_vel - HALF_PAD_HEIGHT) >= 0 and (paddle1_pos[1] + paddle1_vel + HALF_PAD_HEIGHT) <= HEIGHT:
        paddle1_pos[1] += paddle1_vel
  
    if (paddle2_pos[1] + paddle2_vel - HALF_PAD_HEIGHT) >= 0 and (paddle2_pos[1] + paddle2_vel + HALF_PAD_HEIGHT) <= HEIGHT:
        paddle2_pos[1] += paddle2_vel
    
    # draw paddles
    canvas.draw_polygon([[paddle1_pos[0] - HALF_PAD_WIDTH, paddle1_pos[1]- HALF_PAD_HEIGHT], 
                         [paddle1_pos[0] + HALF_PAD_WIDTH, paddle1_pos[1]- HALF_PAD_HEIGHT], 
                         [paddle1_pos[0] + HALF_PAD_WIDTH, paddle1_pos[1]+ HALF_PAD_HEIGHT], 
                         [paddle1_pos[0] - HALF_PAD_WIDTH, paddle1_pos[1]+ HALF_PAD_HEIGHT]], 
                        1, "White", "White")
    
    canvas.draw_polygon([[paddle2_pos[0] - HALF_PAD_WIDTH, paddle2_pos[1]- HALF_PAD_HEIGHT], 
                         [paddle2_pos[0] + HALF_PAD_WIDTH, paddle2_pos[1]- HALF_PAD_HEIGHT], 
                         [paddle2_pos[0] + HALF_PAD_WIDTH, paddle2_pos[1]+ HALF_PAD_HEIGHT], 
                         [paddle2_pos[0] - HALF_PAD_WIDTH, paddle2_pos[1]+ HALF_PAD_HEIGHT]], 
                        1, "White", "White")
    
    # draw scores
    canvas.draw_text(str(score_left), score_left_pos, 60, "White")
    canvas.draw_text(str(score_right), score_right_pos, 60, "White")


    
def keydown(key):
    global paddle1_vel, paddle2_vel
    #************************************************
    pad_acc = 7
    if key==simplegui.KEY_MAP["w"]: 
        paddle1_vel -=  pad_acc
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel +=  pad_acc
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel +=  pad_acc
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel -=  pad_acc
   
def keyup(key):
    global paddle1_vel, paddle2_vel
     
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 100)
frame.add_button("Color Change Toggle", color_change, 100)
frame.add_button("Ball Shrink Toggle", ball_shrink, 100)
frame.add_button("Pad Shrink Toggle", pad_shrink, 100)


# start frame
new_game()
frame.start()