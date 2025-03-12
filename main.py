import pygame
import time
import random

# Initialize pygame
pygame.init()

# Define window size
WIDTH = 600
HEIGHT = 400

# Define colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (213, 50, 80)
BLUE = (50, 153, 213)
BLACK = (0, 0, 0)

# Snake block size
BLOCK_SIZE = 10
SPEED = 15  # Snake speed

# Create window
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock for controlling game speed
clock = pygame.time.Clock()

# Font for messages
font = pygame.font.SysFont("bahnschrift", 20)

# Function to draw the snake
def draw_snake(block_size, snake_body):
    for block in snake_body:
        pygame.draw.rect(win, GREEN, [block[0], block[1], block_size, block_size])

# Function to display message
def message(msg, color, x, y):
    text = font.render(msg, True, color)
    win.blit(text, [x, y])

# Main function for the game
def game_loop():
    game_over = False
    game_close = False

    # Initial position of the snake
    x, y = WIDTH // 2, HEIGHT // 2
    dx, dy = 0, 0

    # Snake body
    snake_body = []
    snake_length = 1

    # Food position
    food_x = random.randrange(0, WIDTH - BLOCK_SIZE, BLOCK_SIZE)
    food_y = random.randrange(0, HEIGHT - BLOCK_SIZE, BLOCK_SIZE)

    while not game_over:
        while game_close:
            win.fill(BLACK)
            message("Game Over! Press C to Play Again or Q to Quit", RED, WIDTH // 6, HEIGHT // 3)
            pygame.display.update()

            # Event handling for restart or quit
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Handling events for movement
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx == 0:
                    dx, dy = -BLOCK_SIZE, 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx, dy = BLOCK_SIZE, 0
                elif event.key == pygame.K_UP and dy == 0:
                    dx, dy = 0, -BLOCK_SIZE
                elif event.key == pygame.K_DOWN and dy == 0:
                    dx, dy = 0, BLOCK_SIZE

        # Update snake position
        x += dx
        y += dy

        # Game over conditions (collision with boundaries)
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            game_close = True

        # Update screen
        win.fill(BLACK)
        pygame.draw.rect(win, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])  # Draw food

        # Update snake body
        snake_head = [x, y]
        snake_body.append(snake_head)
        if len(snake_body) > snake_length:
            del snake_body[0]

        # Check if snake collides with itself
        for block in snake_body[:-1]:
            if block == snake_head:
                game_close = True

        # Draw snake
        draw_snake(BLOCK_SIZE, snake_body)

        # Display score
        message(f"Score: {snake_length - 1}", WHITE, 10, 10)

        # Update display
        pygame.display.update()

        # Check if snake eats food
        if x == food_x and y == food_y:
            food_x = random.randrange(0, WIDTH - BLOCK_SIZE, BLOCK_SIZE)
            food_y = random.randrange(0, HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
            snake_length += 1

        # Control snake speed
        clock.tick(SPEED)

    pygame.quit()
    quit()

# Run the game
game_loop()