import random
import time
"""
    -------BATTLESHIPS-------
    Pre-reqs: Loops, Strings, Arrays, 2D Arrays, Global Variables, Methods
    How it will work:
    1. A 10x10 grid will have 5 ships randomly placed about
    2. You can choose a row and column to indicate where to shoot
    3. For every shot that hits or misses it will show up in the grid
    4. If all ships are shot, game over

    Legend:
    1. "." = water
    2. "S" = ship position
    3. "O" = water that was shot with bullet, a miss because it hit no ship
    4. "X" = ship sunk!
"""
#       -- Global Variables --

# Global variable for grid size
grid_size = 10
# Global variable for grid
grid = [ ['   ']*grid_size for i in range(grid_size) ]
# Global variable for number of ships to place
num_of_ships = 5

#       -- Functions --

def setupBoard(myBoard):
    i = j = 0
    while i < grid_size:
        while j < grid_size:
            myBoard[i][j] = " . "
            j += 1
        j = 0
        i += 1
    ships_placed = 0
    while ships_placed < num_of_ships:
        randomRow = random.randint(0, grid_size - 1)
        randomCol = random.randint(0, grid_size - 1)        
        if myBoard[randomRow][randomCol] == " . ":
            myBoard[randomRow][randomCol] = " S "
            ships_placed += 1
    return myBoard

def drawBoard(myBoard):
    rows = (len(myBoard)) + 2
    for i in range(grid_size):
        print("---".join((["+"]*rows)))
        if i == 0:
            print("|   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |")
            print("---".join((["+"]*rows)))
        row_content = [""]
        for j in range(grid_size):
            if j == 0 :
                row_content.append(f" {i} ") 
            row_content.append(f"{myBoard[i][j]}")
        print("|".join(row_content) + "|") 
    print("---".join((["+"]*rows)))
    return

def hitOrMiss(myBoard, row, col):
    if myBoard[row][col] == " . ":
        print("MISS! Take a look at the board.")
        myBoard[row][col] = " O "
    elif myBoard[row][col] == " S ":
        print("HIT! Argh, nicely done...")
        myBoard[row][col] = " X "
    else:
        print("Shaking my head, are you trying to waste")
        print("cannon ammo on my ship? YAARGH!")
    return myBoard

def isGameOver(myBoard):
    ship_counter = 0
    for i in range(grid_size):
        for j in range(grid_size):
            if myBoard[i][j] == " S ":
                ship_counter += 1
    if ship_counter == 0:
        return True
    else:
        return False

def main(myBoard):
    ready2play = setupBoard(myBoard)
    drawBoard(ready2play)
    print()
    while isGameOver(ready2play) == False:
        while True:
            try:
                row_guess = int(input("Enter your row (x-coordinate): "))
                if 0 <= row_guess <= 9:
                    break
                else:
                    print("Please enter a guess between the numbers 0-9.")
            except ValueError: 
                print("Invalid input. Please enter an integer.")
        while True:
            try:
                col_guess = int(input("Enter your column (y-coordinate): "))
                if 0 <= col_guess <= 9:
                    break
                else:
                    print("Please enter a guess between the numbers 0-9.")
            except ValueError: 
                print("Invalid input. Please enter an integer.")
        hitOrMiss(ready2play, row_guess, col_guess)
        print()
        drawBoard(ready2play)
        print()
    print('Game over!')


#       -- Let's Play the Game! --

print('Welcome to Battleship TM !')
print('Instructions: This is a single-player game where the game board ')
print('is previewed already to you and you will be prompted to enter ')
print('a row and column (between the #s 0-9) to hit the S on the board ')
print('which signifies the ship, . is the water, X is a hit, and O is ')
print('an area of the board that was hit, but was a miss.')
print('ARGH! Best of luck on the wild seas!')
print()

main(grid)

time.sleep(5)
print("...The final enemy ship has been sunk, your pirating group has won.")
time.sleep(5)
print("But, at what cost?")
time.sleep(3)
print("AT WHAT COST?")
time.sleep(2)
print("(the end?)")





