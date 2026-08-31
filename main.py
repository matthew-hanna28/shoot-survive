import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Shoot Survive")

player_x = 400
player_y = 300
player_size = 40

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= 5

    if keys[pygame.K_RIGHT]:
        player_x += 5

    if keys[pygame.K_UP]:
        player_y -= 5

    if keys[pygame.K_DOWN]:
        player_y += 5

    player_x = max(0, min(player_x, 760))
    player_y = max(0, min(player_y, 560))

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (0, 255, 255), (player_x, player_y, player_size, player_size))
    pygame.display.flip()

pygame.quit()
