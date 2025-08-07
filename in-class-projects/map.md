# FOUR-IN-A-ROW

## board.py

### `init_board()`

Initializes the 6x7 grid

### `show_board()`

Prints the grid

### `deter_bottom(col)`

Determines the bottom of the columns from up to down (It would be more efficient in reverse but I'm too lazy to do that)

### `place(col, turn)`

Places on `col`, `1` if `turn` is equal to `Player 1`, 2 otherwise

### `check_win(side, n)`

`n` is the win condition (so how many in a row to win)

Supports horizontal, vertical, top left to bottom right and top right to bottom left

### `bot_place(n)`

Makes the decisions for the bot

If it is possible to win in the next step, it takes that step

Otherwise it places in a random column

## main.py

Handles the main game logic

Loops until either side of the `check_win()` function returns `True`

## utils.py

### `clear_screen()`

Clears the terminal screen

### `rand_int(a, b)`

Returns a random integer between numbers `a` and `b` using the `random` package (inclusive)