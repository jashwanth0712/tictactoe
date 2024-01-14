import sqlite3
import os
import random

coord_mapping = {
    1: 'coord_0_0', 2: 'coord_0_1', 3: 'coord_0_2',
    4: 'coord_1_0', 5: 'coord_1_1', 6: 'coord_1_2',
    7: 'coord_2_0', 8: 'coord_2_1', 9: 'coord_2_2'
}
def clear_screen():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Linux and macOS
    else:
        os.system('clear')
class TicTacToeTable:
    def __init__(self, db_name='tictactoe.db'):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self):
        query = '''
            CREATE TABLE IF NOT EXISTS tictactoe (
                matchid INTEGER PRIMARY KEY,
                player_turn VARCHAR(255),
                player1 VARCHAR(255),
                player2 VARCHAR(255),
                symbol_player1 VARCHAR(255),
                symbol_player2 VARCHAR(255),
                coord_0_0 VARCHAR(255),
                coord_0_1 VARCHAR(255),
                coord_0_2 VARCHAR(255),
                coord_1_0 VARCHAR(255),
                coord_1_1 VARCHAR(255),
                coord_1_2 VARCHAR(255),
                coord_2_0 VARCHAR(255),
                coord_2_1 VARCHAR(255),
                coord_2_2 VARCHAR(255),
                winner_name VARCHAR(255)
            );
        '''
        self.cursor.execute(query)
        self.conn.commit()

    def close_connection(self):
        self.conn.close()

    def insert_new_match(self, matchid, player1, player2, symbol_player1, symbol_player2):
        query = '''
            INSERT INTO tictactoe (matchid, player_turn, player1, player2, symbol_player1, symbol_player2)
            VALUES (?, ?, ?, ?, ?, ?);
        '''
        self.cursor.execute(query, (matchid, random.choice([player1, player2]), player1, player2, symbol_player1, symbol_player2))
        self.conn.commit()

    def update_board(self, matchid, coord, player, symbol):
        query = f'UPDATE tictactoe SET {coord} = ?, player_turn = ? WHERE matchid = ?;'
        self.cursor.execute(query, (symbol, player, matchid))
        self.conn.commit()
    def end_match(self, matchid, winner_name):
        query = f'UPDATE tictactoe SET winner_name = ? WHERE matchid = ?;'
        self.cursor.execute(query, (winner_name, matchid))
        self.conn.commit()
    def get_board_state(self, matchid):
        query = f'SELECT * FROM tictactoe WHERE matchid = ?;'
        self.cursor.execute(query, (matchid,))
        row = self.cursor.fetchone()

        if row:
            columns = [description[0] for description in self.cursor.description]
            return dict(zip(columns, row))
        else:
            return None

    def check_winner(self, board_state):
        lines_to_check = [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)]
        ]

        for line in lines_to_check:
            values = [board_state[f'coord_{i}_{j}'] for i, j in line]
            if all(value == board_state['symbol_player1'] for value in values):
                return board_state['player1']
            elif all(value == board_state['symbol_player2'] for value in values):
                return board_state['player2']

        return None

    def show_leaderboard(self):
        query = 'SELECT matchid, winner_name FROM tictactoe WHERE winner_name IS NOT NULL;'
        self.cursor.execute(query)
        leaderboard = self.cursor.fetchall()

        if leaderboard:
            print("\nLeaderboard:")
            print("{:<10}| {:<20}".format("Match ID", "Winner"))
            print("-" * 30)

            for match in leaderboard:
                print("{:<10}| {:<20}".format(match[0], match[1]))
        else:
            print("No winners found in the leaderboard.")

def print_colored(text, color):
        colors = {
            'red': '\033[91m',
            'green': '\033[92m',
            'blue': '\033[94m',
            'reset': '\033[0m'
        }
        return colors[color]+text+colors['reset']
def print_board(board_state):
    def format_cell(value,num):
        positions=[1,2,3,4,5,6,7,8,9]   
        if value is None:
            return str(positions[num])
        elif value == board_state['symbol_player1']:
            return print_colored(value, 'blue')
        elif value == board_state['symbol_player2']:
            return print_colored(value, 'green')
        else:
            return ""+positions[num]
    print(f"{format_cell(board_state['coord_0_0'],0)} | {format_cell(board_state['coord_0_1'],1)} | {format_cell(board_state['coord_0_2'],2)}")
    print("---------")
    print(f"{format_cell(board_state['coord_1_0'],3)} | {format_cell(board_state['coord_1_1'],4)} | {format_cell(board_state['coord_1_2'],5)}")
    print("---------")
    print(f"{format_cell(board_state['coord_2_0'],6)} | {format_cell(board_state['coord_2_1'],7)} | {format_cell(board_state['coord_2_2'],8)}")
    print("\nPlayer Symbols:")
    print(f"Player 1 ({board_state['player1']}): {board_state['symbol_player1']}")
    print(f"Player 2 ({board_state['player2']}): {board_state['symbol_player2']}")

def create_new_match(table_instance):
    match_id = random.randint(1000, 9999)
    player1 = input("Enter Player 1 name: ")
    player2 = input("Enter Player 2 name: ")
    symbol_player1 = input(f"Enter the symbol for {player1}: ")
    symbol_player2 = input(f"Enter the symbol for {player2}: ")
    table_instance.insert_new_match(match_id, player1, player2, symbol_player1, symbol_player2)
    print(f"\nNew match created with ID: {match_id}")
    return match_id

def fill_boxes(table_instance, match_id, player):
    board_state = table_instance.get_board_state(match_id)
    print("\nCurrent Board State:")
    while True:
        print("\n\n")
        print_board(board_state)
        position = int(input(f"\n{board_state[player]}'s turn \nenter the position (1-9)\n0- Exit \n Enter you move : "))

        if position < 1 or position > 9:
            print("Invalid position. Please choose a number between 1 and 9.")
            continue

        coord = coord_mapping[position]
        if board_state[coord] is not None:
            print("Invalid move. The position is already filled. Try again.")
        else:
            break

    symbol = board_state['symbol_player1'] if player == 'player1' else board_state['symbol_player2']
    table_instance.update_board(match_id, coord, player, symbol)

def open_all_matches(table_instance):
    table_instance.cursor.execute('SELECT * FROM tictactoe ;', ())
    existing_matches = table_instance.cursor.fetchall()

    if existing_matches:
        print("\nAll Matches:")
        print("{:<10} {:<20} {:<20} {:<15}".format("Match ID", "Player 1", "Player 2", "Match Status"))
        print("-" * 65)

        for match in existing_matches:
            match_id, player1, player2, match_status = match[0], match[2], match[3], "Live" if match[13] is None else match[13] + " won"
            print("{:<10} {:<20} {:<20} {:<15}".format(str(match_id), player1, player2, match_status))

    else:
        print("No matches found.")

def open_existing_match(table_instance):
    match_id = input("Enter the match ID to open: ")
    table_instance.cursor.execute('SELECT * FROM tictactoe WHERE matchid = ?;', (match_id,))
    existing_match = table_instance.cursor.fetchone()

    if existing_match:
        print("\nExisting Match Details:")
        print(existing_match)

        player1 = existing_match[2]
        player2 = existing_match[3]
        symbol_player1 = existing_match[4]
        symbol_player2 = existing_match[5]

        while True:
            board_state = table_instance.get_board_state(match_id)

            fill_boxes(table_instance, match_id, 'player1')

            winner = table_instance.check_winner(board_state)
            if winner:
                print(f"\nCongratulations! {winner} wins!")
                table_instance.end_match(match_id, winner)
                break

            fill_boxes(table_instance, match_id, 'player2')

            winner = table_instance.check_winner(board_state)
            if winner:
                print(f"\nCongratulations! {winner} wins!")
                table_instance.end_match(match_id, winner)
                break

    else:
        print(f"Match with ID {match_id} not found.")

if __name__ == "__main__":
    db_name = 'tictactoe.db'
    tictactoe_table = TicTacToeTable(db_name)
    tictactoe_table.create_table()

    while True:

        print("\n1. Create New Match")
        print("2. Open Existing Match")
        print("3. Show All Matches")
        print("4. Show Leaderboard")
        print("5. Exit")

        choice = input("Enter your choice (1, 2, 3, 4, or 5): ")
        if(choice in ['1','3','4','5']):
            clear_screen()  # Clear the terminal screen

        if choice == '1':
            match_id = create_new_match(tictactoe_table)

            while True:
                board_state = tictactoe_table.get_board_state(match_id)
                print("\nCurrent Board State:")
                print_board(board_state)

                fill_boxes(tictactoe_table, match_id, 'player1')

                winner = tictactoe_table.check_winner(board_state)
                if winner:
                    print(f"\nCongratulations! {winner} wins!")
                    break

                fill_boxes(tictactoe_table, match_id, 'player2')

                winner = tictactoe_table.check_winner(board_state)
                if winner:
                    print(f"\nCongratulations! {winner} wins!")
                    break

        elif choice == '2':
            open_existing_match(tictactoe_table)
        elif choice == '3':
            open_all_matches(tictactoe_table)

        elif choice == '4':
            tictactoe_table.show_leaderboard()

        elif choice == '5':
            tictactoe_table.close_connection()
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")
