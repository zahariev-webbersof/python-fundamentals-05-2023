import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Крадеца на стотачки")

# Load the player image
player_image = pygame.image.load("player.png")
player_size = player_image.get_rect().size
player_x = width // 2 - player_size[0] // 2
player_y = height - player_size[1] - 10
player_speed = 5

# Load the item image
item_image = pygame.image.load("item.png")
item_size = item_image.get_rect().size
item_x = random.randint(0, width - item_size[0])
item_y = -item_size[1]
item_speed = 3

# Set up the score
score = 0
font = pygame.font.Font(None, 36)

# Set up game over message
game_over_font = pygame.font.Font(None, 72)
game_over_text = game_over_font.render("Време е да влизаш в затвора!", True, (255, 0, 0))
game_over_text_pos = (width // 2 - game_over_text.get_width() // 2, height // 2 - game_over_text.get_height() // 2)

# Set up new game button
button_font = pygame.font.Font(None, 36)
button_text = button_font.render("New Game", True, (0, 0, 255))
button_text_pos = (width // 2 - button_text.get_width() // 2, height // 2 + game_over_text.get_height() // 2 + 20)
button_rect = pygame.Rect(button_text_pos[0], button_text_pos[1], button_text.get_width(), button_text.get_height())

# Game states
STATE_PLAYING = 1
STATE_GAME_OVER = 2
state = STATE_PLAYING

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if state == STATE_GAME_OVER and button_rect.collidepoint(event.pos):
                # Start a new game
                state = STATE_PLAYING
                score = 0
                item_speed = 3
                player_x = width // 2 - player_size[0] // 2
                item_x = random.randint(0, width - item_size[0])
                item_y = -item_size[1]

    if state == STATE_PLAYING:
        # Move the player
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < width - player_size[0]:
            player_x += player_speed

        # Move the items
        item_y += item_speed

        # Check for collision
        if player_x < item_x + item_size[0] and player_x + player_size[0] > item_x and player_y < item_y + item_size[1] and player_y + player_size[1] > item_y:
            score += 1
            item_x = random.randint(0, width - item_size[0])
            item_y = -item_size[1]

            # Increase speed after every 5 points
            if score % 5 == 0:
                item_speed += 1

        # Check if item goes off the screen
        if item_y > height:
            state = STATE_GAME_OVER

    # Clear the screen
    window.fill((255, 255, 255))

    # Draw the player
    window.blit(player_image, (player_x, player_y))

    # Draw the item
    window.blit(item_image, (item_x, item_y))

    # Draw the score
    score_text = font.render("Откраднах: " + str(score) + '00', True, (255, 0, 0))
    window.blit(score_text, (10, 10))

    if state == STATE_GAME_OVER:
        # Draw the game over message
        window.blit(game_over_text, game_over_text_pos)

        # Draw the new game button
        pygame.draw.rect(window, (0, 0, 255), button_rect)
        window.blit(button_text, button_text_pos)

    # Update the display
    pygame.display.update()

    # Set the frames per second
    clock.tick(60)

# Quit the game
pygame.quit()
sys.exit()