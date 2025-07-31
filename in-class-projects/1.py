import os

def clear_screen():
    """Clears the terminal screen."""
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')

def check_in_borders(n, ship):
    """
    This function makes sure that a ship is within the borders of the grid.
    A ship's starting (x, y) must be on the grid (0 to n-1).
    The entire length of the ship must also fit on the grid.
    """
    x, y, l, orientation = ship.x_pos, ship.y_pos, ship.length, ship.direction

    # Check if starting coordinate is valid
    if not (0 <= x < n and 0 <= y < n):
        return False
    
    # Check if the whole ship fits based on its orientation
    if orientation == 'up':
        return y - l + 1 >= 0
    elif orientation == 'down':
        return y + l - 1 < n
    elif orientation == 'left':
        return x - l + 1 >= 0
    elif orientation == 'right':
        return x + l - 1 < n
    
    return False # Invalid orientation string


class Ship:
    """Represents a ship with its properties and state."""
    # Class-level attribute to assign a unique ID to each ship
    next_id = 1
    
    def __init__(self, length, x_pos, y_pos, direction):
        self.id = Ship.next_id
        Ship.next_id += 1
        self.length = length
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.direction = direction.lower()
        self.hits = 0

    def is_sunk(self):
        """Returns True if the ship has been sunk."""
        return self.hits >= self.length


class Battlefield:
    """Manages the game state for one player, including grids and ships."""
    def __init__(self, length):
        self.length = length
        # Public grid showing hits ('X'), misses ('O'), and unknowns ('?')
        self.grid = self.initialisegrid('?')
        # Private grid tracking the location of ships by their ID
        self.shipgrid = self.initialisegrid(0)
        self.shiplist = []

    def displaygrid(self, grid_to_display):
        """Displays the specified grid with coordinate labels for clarity."""
        print()
        # Print column headers (e.g., 0 1 2 3 4)
        header = "   " + " ".join([str(i) for i in range(self.length)])
        print(header)
        print("  " + "-" * (self.length * 2 + 1))

        # Print each row with its header (e.g., 0| ? ? ? ? ?)
        for i, row in enumerate(grid_to_display):
            row_str = f"{i}| " + " ".join(map(str, row))
            print(row_str)
        print()

    def initialisegrid(self, symbol):
        """Creates and returns a 2D list of size length x length filled with a symbol."""
        return [[symbol for _ in range(self.length)] for _ in range(self.length)]
    
    def check_overlap(self, ship):
        """Checks if a new ship's position overlaps with existing ships."""
        x, y, length, direction = ship.x_pos, ship.y_pos, ship.length, ship.direction
        
        coords_to_check = []
        if direction == 'up':
            for i in range(length): coords_to_check.append((y - i, x))
        elif direction == 'down':
            for i in range(length): coords_to_check.append((y + i, x))
        elif direction == 'left':
            for i in range(length): coords_to_check.append((y, x - i))
        elif direction == 'right':
            for i in range(length): coords_to_check.append((y, x + i))
            
        for r, c in coords_to_check:
            if self.shipgrid[r][c] != 0: # 0 represents empty water
                return True # Overlap detected
        return False # No overlap

    def createships(self, n):
        """Guides the user to create and place n valid ships."""
        for i in range(n):
            print("-" * 20)
            self.displaygrid(self.shipgrid) # Show current ship placements
            while True: # Loop until one valid ship is created and placed
                try:
                    print(f"Placing Ship {i + 1} of {n}")
                    l = int(input(f"Enter length (1-{self.length}): "))
                    x = int(input(f"Enter starting X coordinate (0-{self.length - 1}): "))
                    y = int(input(f"Enter starting Y coordinate (0-{self.length - 1}): "))
                    direction = input("Enter direction (up, down, left, right): ")

                    ship = Ship(l, x, y, direction)

                    # Validate the ship placement
                    if direction.lower() not in ['up', 'down', 'left', 'right']:
                        print("❌ Invalid direction. Please try again.")
                        continue
                    if not check_in_borders(self.length, ship):
                        print("❌ Ship is out of bounds. Please try again.")
                        continue
                    if self.check_overlap(ship):
                        print("❌ Ship overlaps with another ship. Please try again.")
                        continue
                    
                    # If all checks pass, place the ship and break the loop
                    self.shiplist.append(ship)
                    self.placeship(ship)
                    print(f"✅ Ship {i + 1} placed successfully!")
                    break # Exit the while loop for this ship
                except (ValueError, IndexError):
                    print("❌ Invalid input. Please enter valid numbers for length/coordinates.")

    def placeship(self, ship):
        """Places a ship on the shipgrid by marking its location with its ID."""
        x, y, length, direction = ship.x_pos, ship.y_pos, ship.length, ship.direction
        
        if direction == 'up':
            for i in range(length): self.shipgrid[y-i][x] = ship.id
        elif direction == 'down':
            for i in range(length): self.shipgrid[y+i][x] = ship.id
        elif direction == 'left':
            for i in range(length): self.shipgrid[y][x-i] = ship.id
        elif direction == 'right':
            for i in range(length): self.shipgrid[y][x+i] = ship.id
            
    def attack(self, x, y):
        """
        Processes an attack on the given coordinates, updating grids and ship status.
        Returns 'hit', 'sunk', 'miss', or 'repeat'.
        """
        if self.grid[y][x] != '?':
            print("You've already fired there!")
            return 'repeat'

        target_id = self.shipgrid[y][x]
        if target_id == 0:
            self.grid[y][x] = 'O' # Miss
            print("💦 Miss!")
            return 'miss'
        else:
            self.grid[y][x] = 'X' # Hit
            hit_ship = next((s for s in self.shiplist if s.id == target_id), None)
            
            if hit_ship:
                hit_ship.hits += 1
                if hit_ship.is_sunk():
                    print(f"💥 Hit! You sunk a battleship of length {hit_ship.length}!")
                    return 'sunk'
                else:
                    print("💥 Hit!")
                    return 'hit'

    def all_ships_sunk(self):
        """Returns True if all ships on the battlefield are sunk."""
        return all(ship.is_sunk() for ship in self.shiplist)

def setup_player(player_name, grid_size):
    """Guides a player through setting up their battlefield."""
    print(f"\n--- {player_name}, it's time to set up your battlefield. ---")
    player_board = Battlefield(grid_size)

    while True:
        try:
            num_ships = int(input(f"How many ships do you want to place, {player_name}? "))
            if 0 < num_ships <= (grid_size * grid_size) // 5: # Limit ships to prevent overcrowding
                break
            else:
                print("Please enter a reasonable, positive number of ships.")
        except ValueError:
            print("Invalid input. Please enter a number.")
            
    player_board.createships(num_ships)
    
    print(f"\n✅ {player_name}, your ships are placed.")
    player_board.displaygrid(player_board.shipgrid)
    input("Press Enter to hide your board and begin the battle...")
    clear_screen()
    return player_board

def get_attack_coords(grid_size):
    """Helper function to get valid attack coordinates from the user."""
    while True:
        try:
            x = int(input(f"Enter X coordinate for your attack (0-{grid_size-1}): "))
            y = int(input(f"Enter Y coordinate for your attack (0-{grid_size-1}): "))
            if 0 <= x < grid_size and 0 <= y < grid_size:
                return x, y
            else:
                print("❌ Coordinates are out of bounds. Please try again.")
        except ValueError:
            print("❌ Invalid input. Please enter integer coordinates.")

# ===============================================
#                 MAIN GAME LOGIC
# ===============================================
if __name__ == "__main__":
    clear_screen()
    print("🔥 Welcome to Battleship! 🔥")
    
    while True:
        try:
            grid_size = int(input("Please input the side length of the grid (e.g., 5-10):\n"))
            if 2 <= grid_size <= 15:
                break
            else:
                print("Grid size must be between 2 and 15.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # --- Setup Phase ---
    p1_board = setup_player("Player 1", grid_size)
    p2_board = setup_player("Player 2", grid_size)

    # --- Game Loop ---
    game_over = False
    winner = None
    # Player 1 starts
    current_player_board, opponent_board, current_player_name = p1_board, p2_board, "Player 1"

    while not game_over:
        print(f"\n--- {current_player_name}'s Turn ---")
        
        # Display the opponent's grid (the one with '?', 'X', 'O')
        print(f"Your view of { 'Player 2' if current_player_name == 'Player 1' else 'Player 1' }'s grid:")
        opponent_board.displaygrid(opponent_board.grid)

        # Get attack coordinates and handle repeated shots
        while True:
            x, y = get_attack_coords(grid_size)
            result = opponent_board.attack(x, y)
            if result != 'repeat':
                break
        
        print("\nUpdated opponent's grid:")
        opponent_board.displaygrid(opponent_board.grid)

        # Check for win condition
        if opponent_board.all_ships_sunk():
            game_over = True
            winner = current_player_name
        else:
            # Switch turns
            input("Press Enter to end your turn.")
            clear_screen()
            if current_player_name == "Player 1":
                current_player_board, opponent_board, current_player_name = p2_board, p1_board, "Player 2"
            else:
                current_player_board, opponent_board, current_player_name = p1_board, p2_board, "Player 1"

    # --- Announce Winner ---
    print(f"\n🎉 Game Over! 🎉")
    print(f"Congratulations, {winner}! You have won the battle!")