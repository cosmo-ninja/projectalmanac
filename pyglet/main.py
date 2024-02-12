import pyglet

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BALL_RADIUS = 2
GRAVITY = 9.8  # m/s^2
INITIAL_HEIGHT = 100  # meters
TIME_STEP = 1 / 60.0  # seconds

# Ball parameters
ball_x = WINDOW_WIDTH // 2
ball_y = INITIAL_HEIGHT
ball_velocity_y = 0  # Initial velocity in the y-direction

# Timer parameters
elapsed_time = 0

# Create a window
window = pyglet.window.Window(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

# Create a ball sprite
ball = pyglet.shapes.Circle(x=ball_x - BALL_RADIUS, y=ball_y, radius = BALL_RADIUS, color=(255, 255, 255, 255))

# Create a label for the timer
timer_label = pyglet.text.Label(text='Time: 0.0 seconds',
                                 x=10, y=WINDOW_HEIGHT - 30,
                                 font_size=16, color=(255, 255, 255, 255))

# Update function
def update(dt):
    global ball_y, ball_velocity_y, elapsed_time
    
    # Update timer
    elapsed_time += dt
    
    # Update ball position
    ball_velocity_y += GRAVITY * dt
    ball_y -= ball_velocity_y * dt
    
    # Check if the ball has hit the ground
    if ball_y <= BALL_RADIUS:
        ball_y = BALL_RADIUS
        ball_velocity_y = 0
        pyglet.clock.unschedule(update)

# Draw function
@window.event
def on_draw():
    window.clear()
    ball.y = ball_y
    ball.draw()
    timer_label.text = f"Time: {elapsed_time:.3f} seconds"
    timer_label.draw()

# Schedule update function
pyglet.clock.schedule_interval(update, TIME_STEP)

# Run the application
pyglet.app.run()