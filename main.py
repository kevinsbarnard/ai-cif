# main.py
# Main application

from board import *
import time
import algorithm

WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 1000
DISPLAY_WIDTH = 1920
DISPLAY_HEIGHT = 1080

BOARD_ROWS = 20
BOARD_COLS = 20

names = ['Breadth-first search', 'Depth-first search', 'Greedy search', 'A* search']
algs = [algorithm.bfs, algorithm.dfs, algorithm.greedy, algorithm.a_star]
selected_alg_i = 0
alg_texts = []


def main():
    global selected_alg_i
    window = GraphWin('AI Maze Solver', WINDOW_WIDTH, WINDOW_HEIGHT)
    window.setBackground('white')
    board = Board(BOARD_ROWS, BOARD_COLS)
    board.draw(window)

    palette = {
        (0, BOARD_COLS + 1): 'gray',
        (1, BOARD_COLS + 1): 'black',
        (2, BOARD_COLS + 1): 'blue',
        (3, BOARD_COLS + 1): 'yellow'
    }

    # Set up RUN button
    run_button = Rectangle(
        Point((BOARD_COLS + 2) * SIDE_LENGTH, (BOARD_ROWS - 3) * SIDE_LENGTH),
        Point((BOARD_COLS + 6) * SIDE_LENGTH, (BOARD_ROWS - 1) * SIDE_LENGTH)
    )
    run_button.setFill('red')
    run_button.draw(window)
    run_text = Text(Point((BOARD_COLS + 4) * SIDE_LENGTH, (BOARD_ROWS - 2) * SIDE_LENGTH), 'RUN')
    run_text.setSize(24)
    run_text.draw(window)

    # Set up algorithm selection texts
    for i, alg in enumerate(algs):
        alg_text = Text(
            Point((BOARD_COLS + 4) * SIDE_LENGTH,
                  (BOARD_ROWS - 14 + i) * SIDE_LENGTH),
            '{}: {}'.format(i+1, names[i])
        )
        alg_text.setSize(24)
        alg_text.setTextColor('red' if i == selected_alg_i else 'black')
        alg_texts.append(alg_text)
        alg_text.draw(window)

    # Cost text + field
    cost_text = Text(
        Point((BOARD_COLS + 2) * SIDE_LENGTH,
              (BOARD_ROWS - 8) * SIDE_LENGTH),
        'Cost: '
    )
    cost_text.setTextColor('black')
    cost_text.setSize(24)
    cost_text.draw(window)
    cost_field = Text(
        Point((BOARD_COLS + 4) * SIDE_LENGTH,
              (BOARD_ROWS - 8) * SIDE_LENGTH),
        ''
    )
    cost_field.setTextColor('black')
    cost_field.setSize(36)
    cost_field.draw(window)

    for (row, col), color in palette.items():
        button = Rectangle(
            Point(col * SIDE_LENGTH, row * SIDE_LENGTH),
            Point((col + 1) * SIDE_LENGTH, (row + 1) * SIDE_LENGTH)
        )
        button.setFill(color)
        button.draw(window)

    fill = 'black'
    while True:
        if window.isClosed():
            break

        mouse_click = window.checkMouse()
        if mouse_click:
            row = int(mouse_click.getY() // SIDE_LENGTH)
            col = int(mouse_click.getX() // SIDE_LENGTH)
            if row < BOARD_ROWS and col < BOARD_COLS:
                click_cell = board.get_cell(row, col)
                if board.n_rows - 1 > row > 0 and board.n_cols - 1 > col > 0:
                    if fill in ('blue', 'yellow'):
                        board.reset_color(fill)
                    click_cell.set_color(fill)
            elif BOARD_ROWS - 3 <= row < BOARD_ROWS - 1 and BOARD_COLS + 2 <= col < BOARD_COLS + 6:  # Start button
                run_button.setFill('red4')
                goal_node = algs[selected_alg_i](board, delay=0.05)
                if not goal_node:
                    print('No path found!')
                else:
                    tb = algorithm.traceback(goal_node)[1:-1]
                    cost_field.setText(str(len(tb)+1))
                    for path_cell in tb:
                        path_cell.set_color('red')
                time.sleep(4)  # Wait before clearing
                board.reset_color('red')
                board.reset_color('blue4')
                run_button.setFill('red')
            else:
                for (b_row, b_col), color in palette.items():
                    if b_row == row and b_col == col:
                        fill = color

        key = window.checkKey()
        if key:
            if key == 'Escape':
                break
            elif key in [str(idx+1) for idx in range(len(algs))]:
                alg_texts[selected_alg_i].setTextColor('black')
                selected_alg_i = int(key)-1
                alg_texts[selected_alg_i].setTextColor('red')

    window.close()


if __name__ == '__main__':
    main()
