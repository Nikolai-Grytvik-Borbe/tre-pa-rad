import pygame
from board import Board

pygame.init()

desktop_display_size = pygame.display.get_desktop_sizes()
WINDOW_SIZE = (
    int(desktop_display_size[0][1] * 0.75),
    int(desktop_display_size[0][1] * 0.75),
)
screen = pygame.display.set_mode(WINDOW_SIZE)

board = Board(WINDOW_SIZE[0], WINDOW_SIZE[1])


def draw(display):
    display.fill("white")
    board.draw(display)
    pygame.display.update()


if __name__ == "__main__":
    running = True
    while running:
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    board.handle_click(mx, my)
        if board.has_tre_pa_rad("C"):
            print("Circle wins!")
            running = False
        elif board.has_tre_pa_rad("X"):
            print("X wins!")
            running = False
        if not board.checkif_more_moves():
            print("Draw!")
            running = False

        draw(screen)
