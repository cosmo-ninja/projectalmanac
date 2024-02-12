import pygame
import sys

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BALL_RADIUS = 20
GRAVITY = 9.8  # m/s^2

# Initialize Pygame
pygame.init()

# Set up the window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Free Falling Ball")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Clock
clock = pygame.time.Clock()

# Ball parameters
ball_x = WINDOW_WIDTH // 2
ball_y = BALL_RADIUS  # Start from the top of the window
ball_velocity_y = 0  # Initial velocity in the y-direction

# Timer parameters
elapsed_time = 0
font = pygame.font.SysFont(None, 36)
ball_reached_bottom = False
# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update timer
    if not ball_reached_bottom:
        elapsed_time += clock.get_time() / 1000  # Convert milliseconds to seconds
    
    # Update ball position
    ball_velocity_y += GRAVITY * (clock.get_time() / 1000)  # Convert milliseconds to seconds
    ball_y += ball_velocity_y * (clock.get_time() / 1000)  # Convert milliseconds to seconds
    
    # Check if the ball has reached the bottom of the window
    if ball_y >= WINDOW_HEIGHT - BALL_RADIUS:
        ball_y = WINDOW_HEIGHT - BALL_RADIUS
        ball_velocity_y = 0
        ball_reached_bottom = True
    
    # Clear the window
    window.fill(WHITE)
    
    # Draw the ball
    pygame.draw.circle(window, RED, (ball_x, int(ball_y)), BALL_RADIUS)
    
    # Draw the timer
    timer_text = font.render(f'Time: {elapsed_time:.2f} seconds', True, (0, 0, 0))
    window.blit(timer_text, (10, 10))
    
    # Update the display
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()