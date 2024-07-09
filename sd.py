import pygame

# Initialize Pygame
pygame.init()

# Constants
GRID_SIZE = 20  # Adjust this size as needed for your game

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialize a Pygame screen (just for rendering)
screen = pygame.Surface((GRID_SIZE * 3, GRID_SIZE * 3))  # Adjust size as needed

# Head images
head_up = pygame.Surface((GRID_SIZE, GRID_SIZE))
head_up.fill(WHITE)  # Fill with white for visibility
pygame.draw.rect(head_up, GREEN, (0, 0, GRID_SIZE, GRID_SIZE))  # Green rectangle for head
pygame.image.save(head_up, 'head_up.png')

head_down = pygame.Surface((GRID_SIZE, GRID_SIZE))
head_down.fill(WHITE)
pygame.draw.rect(head_down, GREEN, (0, 0, GRID_SIZE, GRID_SIZE))
pygame.image.save(head_down, 'head_down.png')

head_left = pygame.Surface((GRID_SIZE, GRID_SIZE))
head_left.fill(WHITE)
pygame.draw.rect(head_left, GREEN, (0, 0, GRID_SIZE, GRID_SIZE))
pygame.image.save(head_left, 'head_left.png')

head_right = pygame.Surface((GRID_SIZE, GRID_SIZE))
head_right.fill(WHITE)
pygame.draw.rect(head_right, GREEN, (0, 0, GRID_SIZE, GRID_SIZE))
pygame.image.save(head_right, 'head_right.png')

# Body and Tail images
body = pygame.Surface((GRID_SIZE, GRID_SIZE))
body.fill(WHITE)
pygame.draw.rect(body, GREEN, (0, 0, GRID_SIZE, GRID_SIZE))
pygame.image.save(body, 'body.png')

tail = pygame.Surface((GRID_SIZE, GRID_SIZE))
tail.fill(WHITE)
pygame.draw.rect(tail, GREEN, (0, 0, GRID_SIZE, GRID_SIZE))
pygame.image.save(tail, 'tail.png')

# Exit Pygame
pygame.quit()

print("Image files generated successfully!")
