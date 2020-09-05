import re
import random

_PLAYER = "player"
_MACHINE = "machine"

_PLAYER_SYMBOL = "x"
_MACHINE_SYMBOL = "o"

class TicTacToeGame():
  def __init__(self):
    self.board = [None] * 9
    self.turn = _PLAYER
    self.is_game_over = False
    self.winner = None

  def is_over(self): # TODO: Finish this function by adding checks for a winning game (rows, columns, diagonals)
    if self.board[0] == _PLAYER_SYMBOL:
      if self.board[1] == _PLAYER_SYMBOL and self.board[2] == _PLAYER_SYMBOL:
        self.winner = _PLAYER
        return True
      elif self.board[3] == _PLAYER_SYMBOL and self.board[6] == _PLAYER_SYMBOL:
        self.winner = _PLAYER
        return True
      elif self.board[4] == _PLAYER_SYMBOL and self.board[8] == _PLAYER_SYMBOL:
        self.winner = _PLAYER
        return True

    elif self.board[0] == _MACHINE_SYMBOL:
      if self.board[1] == _MACHINE_SYMBOL and self.board[2] == _MACHINE_SYMBOL:
        self.winner = _MACHINE
        return True
      elif self.board[3] == _MACHINE_SYMBOL and self.board[6] == _MACHINE_SYMBOL:
        self.winner = _MACHINE
        return True
      elif self.board[4] == _MACHINE_SYMBOL and self.board[8] == _MACHINE_SYMBOL:
        self.winner = _MACHINE
        return True

    elif self.board[1] == _PLAYER_SYMBOL:
      if self.board[4] == _PLAYER_SYMBOL and self.board[7] == _PLAYER_SYMBOL:
        self.winner = _PLAYER
        return True

    elif self.board[1] == _MACHINE_SYMBOL:
      if self.board[4] == _MACHINE_SYMBOL and self.board[7] == _MACHINE_SYMBOL:
        self.winner = _MACHINE
        return True

    elif self.board[2] == _PLAYER_SYMBOL:
      if self.board[5] == _PLAYER_SYMBOL and self.board[8] == _PLAYER_SYMBOL:
        self.winner = _PLAYER
        return True
      elif self.board[4] == _PLAYER_SYMBOL and self.board[6] == _PLAYER_SYMBOL:
        self.winner = _PLAYER
        return True

    elif self.board[2] == _MACHINE_SYMBOL:
      if self.board[5] == _MACHINE_SYMBOL and self.board[8] == _MACHINE_SYMBOL:
        self.winner = _MACHINE
        return True
      elif self.board[4] == _MACHINE_SYMBOL and self.board[6] == _MACHINE_SYMBOL:
        self.winner = _MACHINE
        return True
    
    elif self.board[3] == _PLAYER_SYMBOL:
      if self.board[4] == _PLAYER_SYMBOL and self.board[5] == _PLAYER_SYMBOL:
        self.winner = _PLAYER
        return True

    elif self.board[3] == _MACHINE_SYMBOL:
      if self.board[4] == _MACHINE_SYMBOL and self.board[5] == _MACHINE_SYMBOL:
        self.winner = _MACHINE
        return True
    
    elif self.board[6] == _PLAYER_SYMBOL:
      if self.board[7] == _PLAYER_SYMBOL and self.board[8] == _PLAYER_SYMBOL:
        self.winner = _PLAYER
        return True

    elif self.board[6] == _MACHINE_SYMBOL:
      if self.board[7] == _MACHINE_SYMBOL and self.board[8] == _MACHINE_SYMBOL:
        self.winner = _MACHINE
        return True

    else:
      return self.board.count(None) == 0

  def play(self):
    if self.turn == _PLAYER:
      self.player_turn()
      self.turn = _MACHINE
    else:
      self.machine_turn()
      self.turn = _PLAYER

  def player_choose_cell(self):
    print("Input empty cell bewtween 0 and 8")

    player_cell = input().strip()
    match = re.search("\d", player_cell)

    if not match:
      print("Input is not a number, please try again")

      return self.player_choose_cell()

    player_cell = int(player_cell)

    if self.board[player_cell] is not None:
      print("Cell is already taken, try again")

      return self.player_choose_cell()

    return player_cell

  def player_turn(self):
    chosen_cell = self.player_choose_cell()

    self.board[chosen_cell] = _PLAYER_SYMBOL

  def machine_turn(self):
    # TODO: Implement this function to make the machine choose a random cell (use random module)
    # The result of this function should be that self.board now has one more random cell occupied
    finished = False
    while not finished:
      a = random.randint(0,8)
      if self.board[a] != _PLAYER_SYMBOL and self.board[a] != _MACHINE_SYMBOL:
        self.board[a] = _MACHINE_SYMBOL
        finished = True

  def format_board(self):
    # TODO: Implement this function, it must be able to print the board in the following format:
    #  x|o| 
    #   | | 
    #   | | 

    x = range(8)
    rows = ""
    for i in x:
      if self.board[i] != None and i < 2:
        rows += self.board[i] + "|"
      elif self.board[i] is None and i < 2:
        rows += " " + "|"
      elif self.board[i] != None and i == 2:
        rows += self.board[i] + "\n"
      elif self.board[i] is None and i == 2:
        rows += " " + "\n"
      elif self.board[i] != None and i > 2  and i < 5:
        rows += self.board[i] + "|"
      elif self.board[i] is None and i > 2  and i < 5:
        rows += " " + "|"
      elif self.board[i] != None and i == 5:
        rows += self.board[i] + "\n"
      elif self.board[i] is None and i == 5:
        rows += " " + "\n"
      elif self.board[i] != None and i > 5 and i < 8:
        rows += self.board[i] + "|"
      elif self.board[i] is None and i > 5 and i < 8:
        rows += " " + "|"
      elif self.board[i] != None and i == 8:
        rows += self.board[i] + "\n"
      else:
        rows += " " + "\n"
    
    return rows

  def print(self):
    print("Player turn:" if self.turn == _MACHINE else "Machine turn:")
    print(self.format_board())
    print()

  def print_result(self):
    # TODO: Implement this function in order to print the result based on the self.winner
    if self.winner == _PLAYER:
      print("Congratulations player!")
    else:
      print("Congratulations machine!")
    pass
