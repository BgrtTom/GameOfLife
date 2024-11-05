import pygame
import numpy as np
import time

# Paramètres de la grille 
WIDTH, HEIGHT = 1600, 800
CELL_SIZE = 10
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (20, 20, 20)
TEXT_COLOR = (200, 200, 200)

# Initialisation de pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu de la Vie")

# Police d'écriture pour l'affichage du numéro d'itération
font = pygame.font.Font(None, 36)


# Fonction pour compter les voisins vivants
def count_alive_neighbors(grid, x, y):
    neighbors = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    count = 0
    for dx, dy in neighbors:
        nx, ny = x + dx, y + dy
        if 0 <= nx < GRID_WIDTH and 0 <= ny < GRID_HEIGHT:
            count += grid[nx, ny]
    return count


# Initialisation de la grille
grid = np.zeros((GRID_WIDTH, GRID_HEIGHT), dtype=int)  # Grille vide
iteration = 0  # Compteur d'itérations
running_simulation = False  # Mode de sélection au départ

# Boucle principale
running = True
while running:
    screen.fill(GRAY) # Affichage de la grille de selection des cellules

    # Événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: # Bar espace
                running_simulation = not running_simulation  # Démarre la simulation ou bien met la simulation en pause
        elif event.type == pygame.MOUSEBUTTONDOWN and not running_simulation:
            # Sélection des cellules avec un clic
            x, y = pygame.mouse.get_pos()
            grid_x, grid_y = x // CELL_SIZE, y // CELL_SIZE
            grid[grid_x, grid_y] = 1 - grid[grid_x, grid_y]  # Inverse l'état de la cellule


    # Si la simulation est en cours
    if running_simulation:
        screen.fill(BLACK) # Enleve la grille de selection des cellules
        # Calcul de la prochaine génération
        new_grid = np.copy(grid)
        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT):
                alive_neighbors = count_alive_neighbors(grid, x, y)
                if grid[x, y] == 1:
                    # Règles de survie
                    if alive_neighbors < 2 or alive_neighbors > 3:
                        new_grid[x, y] = 0
                else:
                    # Règle de naissance
                    if alive_neighbors == 3:
                        new_grid[x, y] = 1

        # Mise à jour de la grille et de l'itération
        grid = new_grid
        iteration += 1


    # Affichage de la grille
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            color = WHITE if grid[x, y] == 1 else BLACK
            pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE - 1, CELL_SIZE - 1))

    # Affichage du texte
    if not running_simulation:
        instruction_text = font.render("Cliquez pour sélectionner les cellules, Espace pour démarrer", True, TEXT_COLOR)
        screen.blit(instruction_text, (10, 10))
    else:
        iteration_text = font.render(f"Itération : {iteration}", True, TEXT_COLOR)
        screen.blit(iteration_text, (10, 10))

    pygame.display.flip()
    time.sleep(0.05)

# Quitter pygame
pygame.quit()
