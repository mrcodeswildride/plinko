import os
import random

def cls():
  os.system("cls" if os.name == "nt" else "clear")

def print_game_state():
  cls()
  print()

  # print main 10 rows
  for row_num in range(10):
    # all rows start with a |
    row = "|"
    
    if row_num % 2 == 0:
      # even row where openings range from 1 to 9
      for opening in range(1, 10):
        # show either opening or path character
        row += get_opening_character(row_num, opening)

        # all openings followed by a * or |
        row += "*" if opening < 9 else "|"
    else:
      # odd row where openings range from 1.5 to 8.5
      for opening in range(1, 9):
        # adding 0.5 since openings range from 1.5 to 8.5
        opening += 0.5

        # all openings preceded by a *
        row += "*"

        # show either opening or path character
        row += get_opening_character(row_num, opening)

      # last opening followed by a *|
      row += "*|"

    print(row)

  # print bottom row where buckets range from 1 to 9
  row = "|"
  
  for bucket in range(1, 10):
    # show either empty bucket or chip
    row += get_bucket_character(bucket)

    # all buckets followed by a |
    row += "|"

  print(f"{row}\n")

def get_opening_character(row_num, opening):
  if path is None or path[row_num] != opening:
    return " "
  else:
    return "/" if path[row_num + 1] < path[row_num] else "\\"

def get_bucket_character(bucket):
  return "_" if path is None or path[-1] != bucket else "X"

def get_slot():
  while True:
    if prize is None:
      slot = input("Choose a slot [1-9]: ")
    else:
      slot = input(f"You won ${prize}. Choose a slot [1-9]: ")

    if slot == "" or slot not in "123456789":
      print("Choose 1-9.\n")
    else:
      return int(slot)

def drop_chip(chip):
  chip_path = [chip]

  for row_num in range(10):
    if chip == 1:
      direction = 0.5
    elif chip == 9:
      direction = -0.5
    else:
      direction = random.choice([-0.5, 0.5])

    chip += direction
    chip_path.append(chip)

  prizes = [100, 500, 1000, 0, 10000, 0, 1000, 500, 100]

  return chip_path, prizes[int(chip - 1)]

path = None
prize = None

while True:
  print_game_state()

  slot = get_slot()
  path, prize = drop_chip(slot)
