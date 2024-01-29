import pygame
import random
import sys

# Game variables
WIDTH, HEIGHT = 800, 600
RADIUS = 10
MAX_CIRCLES = 10
COLORS = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(MAX_CIRCLES)]
BACKGROUND_COLOR = (173, 216, 230)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def draw_circles(circles):
    for circle in circles:
        pygame.draw.circle(screen, circle['color'], circle['pos'], circle['radius'], 1)

def main():
    circles = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if len(circles) == MAX_CIRCLES:
                    circles.pop(0)

                circles.append({
                    'pos': pygame.mouse.get_pos(),
                    'color': random.choice(COLORS),
                    'radius': RADIUS,
                })

        screen.fill((0, 0, 0))
        draw_circles(circles)
        pygame.display.flip()

if __name__ == "__main__":
    main()