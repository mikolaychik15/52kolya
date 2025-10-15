
import pygame
import random

# Ініціалізація Pygame
pygame.init()

# --- Параметри вікна ---
WIDTH, HEIGHT = 600, 700
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Баскетбол з квадратом 🏀")

# --- Кольори ---
WHITE = (255, 255, 255)
BLUE = (50, 150, 255)
RED = (255, 80, 80)
BLACK = (0, 0, 0)

# --- Звуки ---
move_sound = pygame.mixer.Sound("move.wav")
jump_sound = pygame.mixer.Sound("jump.wav")
score_sound = pygame.mixer.Sound("score.wav")

# --- Ігрові змінні ---
player_size = 40
basket_size = 80
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - player_size - 20
velocity_x = 7
velocity_y = 0
gravity = 0.8
jump = False
score = 0

# Позиція кошика
basket_x = random.randint(50, WIDTH - basket_size - 50)
basket_y = 100

font = pygame.font.SysFont("arial", 36)

# --- Основний цикл ---
run = True
clock = pygame.time.Clock()

while run:
    clock.tick(60)
    win.fill(WHITE)

    # --- Події ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    # Рух вліво/вправо
    if keys[pygame.K_LEFT]:
        player_x -= velocity_x
        move_sound.play()
    if keys[pygame.K_RIGHT]:
        player_x += velocity_x
        move_sound.play()

    # Кидок угору
    if keys[pygame.K_SPACE] and not jump:
        jump = True
        velocity_y = -15
        jump_sound.play()

    # --- Фізика ---
    if jump:
        player_y += velocity_y
        velocity_y += gravity
        if player_y >= HEIGHT - player_size - 20:
            player_y = HEIGHT - player_size - 20
            jump = False

    # --- Перевірка попадання ---
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    basket_rect = pygame.Rect(basket_x, basket_y, basket_size, 20)

    if player_rect.colliderect(basket_rect):
        score += 1
        score_sound.play()
        # Перемістити кошик
        basket_x = random.randint(50, WIDTH - basket_size - 50)
        basket_y = random.randint(80, 200)
        # Повернути гравця вниз
        player_y = HEIGHT - player_size - 20
        jump = False

    # --- Малювання ---
    pygame.draw.rect(win, BLUE, player_rect)    # квадрат-гравець
    pygame.draw.rect(win, RED, basket_rect)     # кошик
    text = font.render(f"Рахунок: {score}", True, BLACK)
    win.blit(text, (20, 20))

    pygame.display.update()

pygame.quit()
