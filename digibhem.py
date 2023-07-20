import pygame
import random
import time


pygame.init()


screen_width = 800
screen_height = 600


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")


black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)


clock = pygame.time.Clock()


snake_img = pygame.Surface((10, 10))
snake_img.fill(white)

food_img = pygame.Surface((10, 10))
food_img.fill(red)

big_food_img = pygame.Surface((20, 20))
big_food_img.fill(blue)


snake_block = 10
snake_speed = 10


def draw_snake(snake_body):
    for block in snake_body:
        screen.blit(snake_img, block)

def display_message(text, size, x, y, color):
    font = pygame.font.SysFont(None, size)
    message = font.render(text, True, color)
    screen.blit(message, [x, y])

def game_loop():
    game_over = False
    game_close = False

    
    snake_x, snake_y = screen_width / 2, screen_height / 2
    snake_x_change, snake_y_change = 0, 0
    snake_body = []
    snake_length = 1

    
    food_x, food_y = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0, round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0

    
    score = 0
    food_count = 0

    while not game_over:

        while game_close:
            screen.fill(black)
            display_message("Game Over! Your Score: " + str(score), 40, 150, 250, white)
            display_message("Press Q-Quit or C-Play Again", 30, 180, 300, white)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_x_change = -snake_block
                    snake_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    snake_x_change = snake_block
                    snake_y_change = 0
                elif event.key == pygame.K_UP:
                    snake_y_change = -snake_block
                    snake_x_change = 0
                elif event.key == pygame.K_DOWN:
                    snake_y_change = snake_block
                    snake_x_change = 0

        
        snake_x += snake_x_change
        snake_y += snake_y_change

        
        if snake_x >= screen_width or snake_x < 0 or snake_y >= screen_height or snake_y < 0:
            game_close = True

        
        snake_head = [snake_x, snake_y]
        snake_body.append(snake_head)
        if len(snake_body) > snake_length:
            del snake_body[0]

        
        for block in snake_body[:-1]:
            if block == snake_head:
                game_close = True

        
        if snake_x == food_x and snake_y == food_y:
            food_x, food_y = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0, round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
            snake_length += 1
            score += 10
            food_count += 1

            
            if food_count == 5:
                food_x, food_y = round(random.randrange(0, screen_width - snake_block * 2) / 10.0) * 10.0, round(random.randrange(0, screen_height - snake_block * 2) / 10.0) * 10.0
                score += 20
                screen.blit(big_food_img, (food_x - 5, food_y - 5))
                food_count = 0
            else:
                screen.blit(food_img, (food_x, food_y))

        
        screen.fill(black)
        draw_snake(snake_body)
        pygame.draw.rect(screen, red, [food_x, food_y, snake_block, snake_block])

        
        pygame.draw.rect(screen, white, [0, 0, screen_width, snake_block])
        pygame.draw.rect(screen, white, [0, 0, snake_block, screen_height])
        pygame.draw.rect(screen, white, [0, screen_height - snake_block, screen_width, snake_block])
        pygame.draw.rect(screen, white, [screen_width - snake_block, 0, snake_block, screen_height])

        
        display_message("Score: " + str(score), 25, 10, 10, white)

        pygame.display.update()
        clock.tick(snake_speed)

    
    screen.fill(black)
    display_message("Congratulations!", 80, 140, 200, white)
    display_message("Your Final Score: " + str(score), 40, 200, 300, white)
    display_message("Press Q-Quit or C-Play Again", 30, 180, 400, white)
    pygame.display.update()

    time.sleep(2)  # Pause for 2 seconds before closing the game

    pygame.quit()
    quit()


game_loop()