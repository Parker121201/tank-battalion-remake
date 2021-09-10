import pygame, os, random

pygame.init()

DISPLAY_WIDTH, DISPlAY_HEIGHT = 700, 700
TANK_SIZE = 175
BRICK_SIZE = 100
pygame.display.set_caption("Tank Battalion")
DISPLAY = pygame.display.set_mode((DISPLAY_WIDTH, DISPlAY_HEIGHT))

FPS = 60
PLAYER_VELOCITY = 1
ENEMY_VELOCITY = 1
BULLET_VELOCITY = 2


BLACK = (0, 0, 0)
GOLD = (212, 175, 55)

# Images
PLAYER_TANK = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "player_tank.png")), (TANK_SIZE, TANK_SIZE))
ENEMY_TANK = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "enemy_tank.png")), (TANK_SIZE, TANK_SIZE))
BRICKS = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "bricks.png")), (BRICK_SIZE, BRICK_SIZE))


def player_movement(keys_pressed, player_tank, bricks):
    if keys_pressed[pygame.K_a] and player_tank.x - PLAYER_VELOCITY > 0:  # LEFT
        player_tank.x -= PLAYER_VELOCITY
    if keys_pressed[pygame.K_d] and player_tank.x + PLAYER_VELOCITY + player_tank.width < DISPLAY_WIDTH:  # RIGHT
        player_tank.x += PLAYER_VELOCITY
    if keys_pressed[pygame.K_w] and player_tank.y - PLAYER_VELOCITY > 0:  # UP
        player_tank.y -= PLAYER_VELOCITY
    if keys_pressed[pygame.K_s] and player_tank.y + PLAYER_VELOCITY + player_tank.height < DISPlAY_HEIGHT:  # DOWN
        player_tank.y += PLAYER_VELOCITY


def temp_enemy_movement(keys_pressed, enemy_tank):
    if keys_pressed[pygame.K_LEFT]:
        enemy_tank.x -= ENEMY_VELOCITY
    if keys_pressed[pygame.K_RIGHT]:
        enemy_tank.x += ENEMY_VELOCITY
    if keys_pressed[pygame.K_UP]:
        enemy_tank.y -= ENEMY_VELOCITY
    if keys_pressed[pygame.K_DOWN]:
        enemy_tank.y += ENEMY_VELOCITY


def draw_display(bricks, player_tank, enemy_tank, player_bullets):
    DISPLAY.fill(BLACK)
    # Map
    for i in bricks:
        DISPLAY.blit(BRICKS, (i.x, i.y))

    DISPLAY.blit(PLAYER_TANK, (player_tank.x, player_tank.y))  # Comfortable gap between bricks is 95
    DISPLAY.blit(ENEMY_TANK, (enemy_tank.x, enemy_tank.y))

    for bullet in player_bullets:
        pygame.draw.rect(DISPLAY, GOLD, bullet)

    pygame.display.update()


def main():
    # dif of 40 each way
    # make list and blit with for loop
    brick_dimensions = [[100, 100], [140, 100], [180, 100],[180, 140], [275, 100], [275, 140]]
    bricks = [pygame.Rect(pos[0], pos[1], BRICK_SIZE, BRICK_SIZE) for pos in brick_dimensions]

    player_tank = pygame.Rect(200, 100, TANK_SIZE, TANK_SIZE)
    enemy_tank = pygame.Rect(200, 300, TANK_SIZE, TANK_SIZE)

    player_bullets = []

    clock = pygame.time.Clock()
    playing = True
    while playing:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = pygame.Rect(player_tank.x + player_tank.width,
                                         player_tank.y + player_tank.height // 2 - 2, 5, 10)
                    player_bullets.append(bullet)

        keys_pressed = pygame.key.get_pressed()
        player_movement(keys_pressed, player_tank, bricks)
        temp_enemy_movement(keys_pressed, enemy_tank)

        draw_display(bricks, player_tank, enemy_tank, player_bullets)

    pygame.quit()


if __name__ == "__main__":
    main()