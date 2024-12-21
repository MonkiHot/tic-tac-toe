import pygame
import sys
import pygame_gui

#initalize game
pygame.init()

#sizes
window_size = 300
grid_size = 100
line_width = 5

#color
white = (255,255,255)
black = (0,0,0)
line_color = (0,0,0)


screen = pygame.display.set_mode((window_size,window_size))
pygame.display.set_caption('Tic Tac Toe')
manager = pygame_gui.UIManager((300, 300))

game_board = [[' ' for _ in range(3)] for _ in range(3)]
current_player = "X"

def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all (board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def draw_lines():
    for i in range(1, 3): 
        pygame.draw.line(screen, line_color, (i * grid_size, 0), (i * grid_size, window_size), line_width)
        pygame.draw.line(screen, line_color, (0, i* grid_size), (window_size, i * grid_size), line_width)

def draw_x(row, col):
    offset = grid_size // 4
    pygame.draw.line(screen, line_color, (col * grid_size + offset, row * grid_size + offset),
                      ((col +1)* grid_size - offset, (row +1) * grid_size - offset), line_width)
    pygame.draw.line(screen, line_color, ((col + 1) * grid_size - offset, row* grid_size + offset),
                      (col * grid_size + offset, (row + 1) * grid_size - offset), line_width)
    
def draw_o(row, col):
    offset = grid_size // 4
    pygame.draw.circle(screen, line_color, (col * grid_size + grid_size // 2, row * grid_size + grid_size // 2),
                       grid_size // 2 - offset, line_width)
    


#main loop
running = True
game_over = False

while running:
    screen. fill(white)
    draw_lines()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not game_over and event.type == pygame.MOUSEBUTTONDOWN:
            x,y = event.pos
            row, col = y // grid_size, x // grid_size

            if game_board[row][col] == ' ':
                game_board[row][col] = current_player

                if check_win(game_board, current_player):
                    if not game_over:  # Only create the popup once
                        message_panel = pygame_gui.elements.UIPanel(
                            relative_rect=pygame.Rect((50, 50), (200, 100)),
                            manager=manager
                        )
                        message_label = pygame_gui.elements.UILabel(
                            relative_rect=pygame.Rect(-50, -10, 300, 100),
                            text=f"Player {current_player} wins!",
                            manager=manager,
                            container=message_panel
                        )
                    print(f"player {current_player} wins!")
                    game_over = True
                else:
                    current_player = 'O' if current_player == 'X' else 'X'

    for row in range(3):
        for col in range(3):
            if game_board[row][col] == 'X':
                draw_x(row,col)
            elif game_board[row][col] == 'O':
                draw_o(row, col)

    time_delta = pygame.time.Clock().tick(60) / 1000.0
    manager.update(time_delta)
    manager.draw_ui(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()
