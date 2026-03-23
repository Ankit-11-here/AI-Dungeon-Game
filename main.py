import pygame
import sys
from ga import create_population
from enemy import bfs_next_step
from ga import generate_solvable_grid

pygame.init()

WIDTH, HEIGHT = 600, 600
ROWS, COLS = 10, 10
CELL_SIZE = WIDTH // COLS

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AI Dungeon Game")

font = pygame.font.SysFont(None, 30)

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,200,0)
RED = (200,0,0)
BLUE = (0,0,200)
YELLOW = (255,255,0)

#Difficulty
difficulty = "easy"
enemy_speed = 10

# Wrap-around navigation
enable_wrap = True

def set_difficulty():
    global enemy_speed
    if difficulty == "easy":
        enemy_speed = 15
    elif difficulty == "medium":
        enemy_speed = 8
    else:
        enemy_speed = 4

# Button UI
def draw_button(text, x, y, w, h, color, hover_color):
    rect = pygame.Rect(x, y, w, h)
    mouse = pygame.mouse.get_pos()

    if rect.collidepoint(mouse):
        pygame.draw.rect(screen, hover_color, rect)
    else:
        pygame.draw.rect(screen, color, rect)

    pygame.draw.rect(screen, BLACK, rect, 2)

    txt = font.render(text, True, WHITE)
    screen.blit(txt, txt.get_rect(center=rect.center))

    return rect

# Generate map
population = create_population(20)
from ga import generate_solvable_grid
grid = generate_solvable_grid()

player = [0,0]
enemy = [9,9]
second_enemy = None
goal = [9,9]

steps = 0
clock = pygame.time.Clock()
enemy_timer = 0
game_timer = 0  # Track total time in game
SECOND_ENEMY_SPAWN_TIME = 70  # Approximately 7 seconds (at 10 FPS)

game_state = "menu"

def draw_grid():
    for r in range(ROWS):
        for c in range(COLS):
            rect = pygame.Rect(c*CELL_SIZE, r*CELL_SIZE, CELL_SIZE, CELL_SIZE)

            if grid[r][c] == '#':
                pygame.draw.rect(screen, BLACK, rect)
            else:
                pygame.draw.rect(screen, WHITE, rect)

            pygame.draw.rect(screen, (200,200,200), rect, 1)

    pygame.draw.rect(screen, GREEN, (player[1]*CELL_SIZE, player[0]*CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, YELLOW, (enemy[1]*CELL_SIZE, enemy[0]*CELL_SIZE, CELL_SIZE, CELL_SIZE))
    
    # Draw second enemy if it exists
    if second_enemy is not None:
        pygame.draw.rect(screen, YELLOW, (second_enemy[1]*CELL_SIZE, second_enemy[0]*CELL_SIZE, CELL_SIZE, CELL_SIZE))
    
    pygame.draw.rect(screen, RED, (goal[1]*CELL_SIZE, goal[0]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

def draw_menu():
    screen.fill(WHITE)

    title = pygame.font.SysFont(None, 50).render("AI Dungeon Game", True, BLACK)
    screen.blit(title, (150, 80))

    easy = draw_button("EASY", 150, 200, 100, 50, GREEN, (0,255,0))
    med = draw_button("MEDIUM", 260, 200, 100, 50, BLUE, (0,0,255))
    hard = draw_button("HARD", 370, 200, 100, 50, RED, (255,0,0))

    # Wrap-around navigation toggle
    wrap_color = (100, 200, 100) if enable_wrap else (200, 100, 100)
    wrap_text = "WRAP: ON" if enable_wrap else "WRAP: OFF"
    wrap_button = draw_button(wrap_text, 200, 270, 200, 40, wrap_color, (150, 255, 150) if enable_wrap else (255, 150, 150))

    start = draw_button("START", 230, 340, 140, 60, (100,100,255), (50,50,200))

    return start, easy, med, hard, wrap_button

def restart():
    global player, enemy, second_enemy, steps, game_state, game_timer
    player = [0,0]
    enemy = [9,9]
    second_enemy = None
    steps = 0
    game_timer = 0
    game_state = "playing"
    set_difficulty()

#  GAME LOOP
while True:
    screen.fill(WHITE)

    if game_state == "menu":
        start_btn, easy_btn, med_btn, hard_btn, wrap_btn = draw_menu()

    elif game_state == "playing":
        draw_grid()

        step_text = font.render(f"Steps: {steps}", True, BLACK)
        screen.blit(step_text, (10, 10))
        
        # Display countdown for second enemy
        if second_enemy is None:
            remaining_ticks = SECOND_ENEMY_SPAWN_TIME - game_timer
            remaining_seconds = max(0, (remaining_ticks + 9) // 10)  # Round up
            countdown_text = font.render(f"2nd Enemy in: {remaining_seconds}s", True, RED)
            screen.blit(countdown_text, (10, 40))
        else:
            second_active_text = font.render("2nd Enemy ACTIVE! ⚠️", True, RED)
            screen.blit(second_active_text, (10, 40))
        
        # Increment game timer
        game_timer += 1
        
        # Spawn second enemy after ~7 seconds (70 ticks at 10 FPS)
        if second_enemy is None and game_timer >= SECOND_ENEMY_SPAWN_TIME:
            second_enemy = [0, 0]  # Spawn at top-left corner

        # Move both enemies with same timer
        enemy_timer += 1
        if enemy_timer >= enemy_speed:
            enemy[:] = bfs_next_step(grid, enemy, player)
            
            # Move second enemy too
            if second_enemy is not None:
                second_enemy[:] = bfs_next_step(grid, second_enemy, player)
            
            enemy_timer = 0

        if player == goal:
            game_state = "win"

        if player == enemy or (second_enemy is not None and player == second_enemy):
            game_state = "lose"

    elif game_state == "win":
        txt = font.render("YOU WIN 🎉", True, GREEN)
        screen.blit(txt, (250, 250))
        restart_btn = draw_button("RESTART", 230, 320, 140, 50, BLUE, (0,0,255))

    elif game_state == "lose":
        txt = font.render("YOU LOST 😢", True, RED)
        screen.blit(txt, (250, 250))
        restart_btn = draw_button("RESTART", 230, 320, 140, 50, BLUE, (0,0,255))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()

            if game_state == "menu":
                if start_btn.collidepoint(mx, my):
                    restart()
                elif easy_btn.collidepoint(mx, my):
                    difficulty = "easy"
                elif med_btn.collidepoint(mx, my):
                    difficulty = "medium"
                elif hard_btn.collidepoint(mx, my):
                    difficulty = "hard"
                elif wrap_btn.collidepoint(mx, my):
                    enable_wrap = not enable_wrap

            elif game_state in ["win", "lose"]:
                if restart_btn.collidepoint(mx, my):
                    restart()

        if event.type == pygame.KEYDOWN and game_state == "playing":
            dr, dc = 0, 0
            if event.key == pygame.K_UP: dr = -1
            if event.key == pygame.K_DOWN: dr = 1
            if event.key == pygame.K_LEFT: dc = -1
            if event.key == pygame.K_RIGHT: dc = 1

            if enable_wrap:
                nr = (player[0] + dr) % ROWS   #  Wrap-around enabled
                nc = (player[1] + dc) % COLS
            else:
                nr = player[0] + dr  # No wrap-around
                nc = player[1] + dc
                # Check boundaries
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
                    nr, nc = player[0], player[1]  # Stay in place

            if grid[nr][nc] != '#':
                player = [nr, nc]
                steps += 1

    clock.tick(10)