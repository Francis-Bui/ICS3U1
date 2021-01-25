# Lesson 5 - Graphics in Codeskulptor
# DDC- Jan 2021

# example of drawing operations in simplegui
# standard HMTL color such as "Red" and "Green"
# note later drawing operations overwrite earlier drawing operations

# try catch for use in python 3.0 shell outside of codeskulptor3
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


# Handler to draw on canvas
def draw(canvas):
    
    # circle - center points (x,y), radius, line thickess, oustide colour, inside colour (optional)
    canvas.draw_circle([200, 400], 200, 2, "Red", "Red")
    canvas.draw_circle([200, 400], 190, 2, "Orange", "Orange")
    canvas.draw_circle([200, 400], 180, 2, "Yellow", "Yellow")
    canvas.draw_circle([200, 400], 170, 2, "Green", "Green")
    canvas.draw_circle([200, 400], 160, 2, "Blue", "Blue")
    canvas.draw_circle([200, 400], 150, 2, "Violet", "Violet")
    canvas.draw_circle([200, 400], 140, 2, "Aqua", "Aqua")

    # line - start point (x,y), end point, line width, colour
    
    canvas.draw_circle([323, 75], 40, 2, "Orange", "Yellow")
    
    canvas.draw_polygon([[150, 350], [150, 400], [250, 400], [250, 350]], 2, "Blue", "Aqua")
    canvas.draw_polygon([[190, 375], [190, 400], [210, 400], [210, 375]], 2, "Blue", "Aqua")
        
    #Triangular Polygon = 3 sides - left, right, top, in this case)
    canvas.draw_polygon([(125, 350), (275, 350), (200, 300)], 2, 'Blue', 'Aqua')
    
    canvas.draw_text("Look at my amazing house", [75, 150], 26, "Blue")
    
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 400, 400)
frame.set_draw_handler(draw)
frame.set_canvas_background("Aqua")


# Start the frame animation
frame.start()
