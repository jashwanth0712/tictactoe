# Tic Tac Toe Game 
![](https://github.com/jashwanth0712/tictactoe/blob/main/images/tictactoe_demo.gif?raw=true)
## Installation
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/jashwanth0712/tictactoe.git
   ```
   
2. **Install Dependencies:**
   ```bash
   pip install sqlite3
   ```

3. **Run the Game:**
   ```bash
   python tictactoe.py
   ```
   This will start the Tic Tac Toe game. Follow the on-screen instructions to play the game, create new matches, and view the leaderboard.
![](https://github.com/jashwanth0712/tictactoe/blob/main/images/image2.png?raw=true)

## Database Details

The game uses SQLite to store match information. The database file is named `tictactoe.db`. The database has a table named `tictactoe` with the following columns:

| Column           | Type           | Description                                    |
|------------------|----------------|------------------------------------------------|
| `matchid`        | Integer        | Primary key                                    |
| `player_turn`    | VARCHAR(255)   | Indicates the player's turn in the current match|
| `player1`        | VARCHAR(255)   | Name of Player 1                               |
| `player2`        | VARCHAR(255)   | Name of Player 2                               |
| `symbol_player1` | VARCHAR(255)   | Symbol chosen by Player 1                      |
| `symbol_player2` | VARCHAR(255)   | Symbol chosen by Player 2                      |
| `coord_0_0` to `coord_2_2` | VARCHAR(255) | Represents Tic Tac Toe board coordinates    |
| `winner_name`    | VARCHAR(255)   | Name of the player who won the match           |

## functions details 
<details>
<summary><h3><code>TicTacToeTable</code> Class</h3></summary>

<details>
<summary><code>__init__(self, db_name='tictactoe.db')</code></summary>

- **Parameters:**
  - `db_name` (str, optional): The name of the SQLite database. Defaults to 'tictactoe.db'.
- **Explanation:**
  - Initializes a `TicTacToeTable` object, connecting to the specified SQLite database.

</details>

<details>
<summary><code>create_table(self)</code></summary>

- **Parameters:**
  - None
- **Explanation:**
  - Creates the 'tictactoe' table in the SQLite database if it doesn't already exist. The table structure includes fields for match details and the Tic Tac Toe board.

</details>

<details>
<summary><code>close_connection(self)</code></summary>

- **Parameters:**
  - None
- **Explanation:**
  - Closes the connection to the SQLite database.

</details>

<details>
<summary><code>insert_new_match(self, matchid, player1, player2, symbol_player1, symbol_player2)</code></summary>

- **Parameters:**
  - `matchid` (int): Unique identifier for the match.
  - `player1` (str): Name of Player 1.
  - `player2` (str): Name of Player 2.
  - `symbol_player1` (str): Symbol chosen by Player 1.
  - `symbol_player2` (str): Symbol chosen by Player 2.
- **Explanation:**
  - Inserts a new match into the database with provided match details and randomly assigns the starting player.

</details>

<details>
<summary><code>update_board(self, matchid, coord, player, symbol)</code></summary>

- **Parameters:**
  - `matchid` (int): Unique identifier for the match.
  - `coord` (str): Coordinate on the Tic Tac Toe board (e.g., 'coord_0_0').
  - `player` (str): Name of the player making the move.
  - `symbol` (str): Symbol representing the player's move.
- **Explanation:**
  - Updates the Tic Tac Toe board with the player's move.

</details>

<details>
<summary><code>end_match(self, matchid, winner_name)</code></summary>

- **Parameters:**
  - `matchid` (int): Unique identifier for the match.
  - `winner_name` (str): Name of the player who won the match.
- **Explanation:**
  - Marks the end of a match and records the winner.

</details>

<details>
<summary><code>get_board_state(self, matchid)</code></summary>

- **Parameters:**
  - `matchid` (int): Unique identifier for the match.
- **Explanation:**
  - Retrieves the current state of the Tic Tac Toe board for a given match.

</details>

<details>
<summary><code>check_winner(self, board_state)</code></summary>

- **Parameters:**
  - `board_state` (dict): Dictionary representing the current state of the Tic Tac Toe board.
- **Explanation:**
  - Checks if there is a winner based on the current board state.

</details>

<details>
<summary><code>show_leaderboard(self)</code></summary>

- **Parameters:**
  - None
- **Explanation:**
  - Displays the leaderboard showing match IDs and winners.

</details>

<details>
<summary><code>create_new_match(self)</code></summary>

- **Parameters:**
  - None
- **Explanation:**
  - Creates a new match with a random match ID and prompts users for player names and symbols.

</details>

<details>
<summary><code>open_all_matches(self)</code></summary>

- **Parameters:**
  - None
- **Explanation:**
  - Displays information about all existing matches, including match ID, player names, and match status.

</details>

<details>
<summary><code>open_existing_match(self, match_id=None)</code></summary>

- **Parameters:**
  - `match_id` (int, optional): The match ID to open. If not provided, prompts the user for input.
- **Explanation:**
  - Opens an existing match using the provided match ID or user input. Allows players to take turns making moves until there is a winner.

</details>

<details>
<summary><code>fill_boxes(self, match_id, player)</code></summary>

- **Parameters:**
  - `match_id` (int): Unique identifier for the match.
  - `player` (str): Name of the player making the move.
- **Explanation:**
  - Allows a player to make a move on the Tic Tac Toe board.

</details>

<details>
<summary><code>print_colored(self, text, color)</code></summary>

- **Parameters:**
  - `text` (str): The text to be colored.
  - `color` (str): The color to apply to the text (e.g., 'red', 'green').
- **Explanation:**
  - Adds color to the console output.

</details>

<details>
<summary><code>print_board(self, board_state)</code></summary>

- **Parameters:**
  - `board_state` (dict): Dictionary representing the current state of the Tic Tac Toe board.
- **Explanation:**
  - Prints the current state of the Tic Tac Toe board with formatted symbols and player information.

</details>

</details>

