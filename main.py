import pygame
import random
import time

colors = {
    "red": (255, 0, 0),
    "blue": (0, 0, 255),
    "green": (0, 255, 0)
}

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True

# Track time for color changes
last_color_change = time.time()
current_color = random.choice(list(colors.values()))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Check if a second has passed
    current_time = time.time()
    if current_time - last_color_change >= 1.0:
        last_color = current_color
        while last_color == current_color:
            current_color = random.choice(list(colors.values()))
        last_color_change = current_time

    screen.fill(current_color)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()