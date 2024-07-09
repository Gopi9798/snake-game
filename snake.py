import pygame
import random

# Initialize Pygame
pygame.init()

# Game constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE
FPS = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Direction vectors (x, y)
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Snake class
class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = GREEN
        self.score = 0
        self.food_position = self.random_food_position()

        # Snake animation frames
        self.head_up = pygame.image.load('head_up.png').convert_alpha()
        self.head_down = pygame.image.load('head_down.png').convert_alpha()
        self.head_left = pygame.image.load('head_left.png').convert_alpha()
        self.head_right = pygame.image.load('head_right.png').convert_alpha()
        self.tail = pygame.image.load('tail.png').convert_alpha()
        self.body = pygame.image.load('body.png').convert_alpha()

    def get_head_position(self):
        return self.positions[0]

    def random_food_position(self):
        x = random.randint(0, GRID_WIDTH - 1) * GRID_SIZE
        y = random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE
        return (x, y)

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x * GRID_SIZE)) % SCREEN_WIDTH), (cur[1] + (y * GRID_SIZE)) % SCREEN_HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.score = 0
        self.food_position = self.random_food_position()

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()  # Ensure proper exit
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.direction != DOWN:
                    self.direction = UP
                elif event.key == pygame.K_DOWN and self.direction != UP:
                    self.direction = DOWN
                elif event.key == pygame.K_LEFT and self.direction != RIGHT:
                    self.direction = LEFT
                elif event.key == pygame.K_RIGHT and self.direction != LEFT:
                    self.direction = RIGHT

    def draw(self, surface):
        # Draw snake head
        head = self.head_up
        if self.direction == DOWN:
            head = self.head_down
        elif self.direction == LEFT:
            head = self.head_left
        elif self.direction == RIGHT:
            head = self.head_right

        surface.blit(head, self.positions[0])

        # Draw snake body
        for pos in self.positions[1:-1]:
            surface.blit(self.body, pos)

        # Draw snake tail
        tail = self.tail
        if len(self.positions) > 1:
            tail_direction = (self.positions[-2][0] - self.positions[-1][0], self.positions[-2][1] - self.positions[-1][1])
            if tail_direction == UP:
                tail = pygame.transform.rotate(self.tail, 0)
            elif tail_direction == DOWN:
                tail = pygame.transform.rotate(self.tail, 180)
            elif tail_direction == LEFT:
                tail = pygame.transform.rotate(self.tail, 90)
            elif tail_direction == RIGHT:
                tail = pygame.transform.rotate(self.tail, -90)

            surface.blit(tail, self.positions[-1])

    def handle_food(self):
        if self.get_head_position() == self.food_position:
            self.length += 1
            self.score += 1
            self.food_position = self.random_food_position()

    def draw_food(self, surface):
        r = pygame.Rect((self.food_position[0], self.food_position[1]), (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, RED, r)

# Game function
def main():
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    pygame.display.set_caption('Funny Snake')

    
   


    snake = Snake()

    while True:
        snake.handle_keys()
        snake.move()

        if snake.get_head_position() in snake.positions[1:]:
            snake.reset()

        snake.handle_food()

        surface.fill(BLACK)
        snake.draw(surface)
        snake.draw_food(surface)
        screen.blit(surface, (0, 0))
        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
