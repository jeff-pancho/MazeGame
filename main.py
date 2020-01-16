#Backslash to break the line because the first row won't be lined up in the code
#And that makes me very uncomfortable
#Create a list that has lists inside of it
#The list-in-that-list will have each element as a string to represent objects in the game
#It's called easyMaze so this will be an easy maze :))))))))
easyMaze = [\
["X", ".", "X", "X", "X", "X", "X", "X"],
["X", ".", "X", "X", ".", ".", ".", "X"],
["X", ".", ".", ".", ".", "X", ".", "X"],
["X", ".", "X", "X", "X", "X", ".", "X"],
["X", ".", "X", ".", ".", ".", ".", "X"],
["X", "X", "X", "X", ".", "X", "X", "X"],
["X", "O", ".", ".", ".", ".", ".", "X"],
["X", "X", "X", "X", "X", "X", "X", "X"]]

#A mediumer maze than the easy maze wow very suprising
#It's bigger.
mediumMaze = [\
["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", ],
["X", "O", ".", ".", ".", ".", ".", ".", ".", ".", ".", "X", ],
["X", "X", "X", ".", "X", "X", "X", "X", "X", "X", ".", "X", ],
["X", ".", "X", ".", "X", ".", ".", "X", ".", "X", ".", "X", ],
["X", ".", ".", ".", ".", ".", ".", "X", ".", ".", ".", "X", ],
["X", ".", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", ],
["X", ".", "X", ".", "X", ".", ".", ".", ".", ".", ".", "X", ],
["X", ".", "X", ".", "X", "X", "X", ".", "X", "X", ".", "X", ],
["X", ".", "X", ".", ".", ".", ".", ".", "X", ".", ".", "X", ],
["X", ".", "X", ".", "X", "X", "X", ".", "X", ".", "X", "X", ],
["X", ".", ".", ".", "X", ".", ".", ".", "X", ".", ".", ".", ],
["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", ]
]
#It's a maze that's hard. Bigger and harder than the medium maze :(
hardMaze = [\
["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
["X", ".", ".", ".", ".", ".", ".", "X", ".", ".", ".", "X", ".", ".", ".", "X"],
["X", "X", ".", "X", ".", "X", ".", "X", ".", "X", ".", ".", ".", "X", ".", "X"],
["X", ".", ".", "X", ".", "X", ".", "X", ".", "X", "X", "X", "X", "X", ".", "X"],
["X", ".", "X", "X", ".", "X", ".", "X", ".", "X", ".", ".", ".", "X", ".", "X"],
["X", ".", ".", "X", ".", "X", ".", "X", ".", "X", ".", "X", ".", "X", ".", "X"],
["X", "X", ".", "X", ".", "X", ".", ".", ".", "X", ".", "X", ".", "X", ".", "X"],
["X", "X", "X", "X", ".", "X", "X", "X", "X", "X", ".", "X", ".", "X", ".", "X"],
["X", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "X", ".", "X", ".", "X"],
["X", ".", "X", "X", "X", "X", ".", "X", "X", "X", ".", "X", ".", "X", ".", "X"],
["X", ".", ".", ".", ".", "X", ".", ".", ".", "X", "X", "X", ".", "X", ".", "X"],
["X", "X", "X", "X", ".", "X", "X", "X", ".", "X", ".", ".", ".", "X", ".", "."],
["X", ".", ".", ".", ".", ".", ".", "X", ".", "X", ".", "X", "X", "X", "X", "X"],
["X", "X", ".", "X", ".", "X", ".", "X", ".", "X", "X", "X", ".", ".", ".", "X"],
["X", ".", ".", "X", ".", "X", ".", ".", ".", ".", ".", ".", ".", "X", "O", "X"],
["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"]
]

#Dictionary that stores the maze lists we have
mazes = {
    "easy": easyMaze,
    "medium": mediumMaze,
    "hard": hardMaze
}

#Store the ending coordinates of the mazes
mazeEnd = {
    "easy": [1, 0],
    "medium": [11, 10],
    "hard": [15, 11]
}

#Store the beginning coordinates of the player for each maze
playerBeginning = {
    "easy": [1, 6],
    "medium": [1, 1],
    "hard": [14, 14]
}

#Empty string that will be used to refer to the keys in the maze dictionaries
mazeChosen = ""

#Variables solved (is the maze solved?)
#plrX and plrY refer to the player's position in the maze list
#This value will be different depending on the maze chosen
solved = False
plrX = 0
plrY = 0

#Values that hold the plrX and plrY before they are modified
#So we can move the player back if they collide with a wall
tempX = 0
tempY = 0

#Empty string variable to use raw_input()
choice = ""

#Create a function that prints the whole map. Takes 2d list input x
#The for loop iterates through the input x. i is equal to a list that represents a row
#In the loop, print the row. Each element in the row is separated by a space
def printMaze(x):
    for i in x:
        print " ".join(i)
    #Print a blank line to separate the maze from other things that will be printed
    print

#Function that checks if the player is colliding with a wall
#Well more like checking if the player is inside a wall
def isColliding(x, y, maze):

    #Using x and y inputs, use these as indices for the maze list
    #If the element is "X" then return True else return False
    if maze[y][x] == "X":
        return True
    else:
        return False

#Keep looping while mazeChosen is empty
#The only way to exit the loop is to change mazeChosen
while mazeChosen == "":
    #Print text and set choice to the player input
    #It also sets the player's input into lowercase
    print "Pick a maze to solve. Your options are easy, medium and hard."
    choice = raw_input("Pick a maze: ").lower()

    #If the input is 'easy', 'medium' or 'hard'
    if choice == "easy" or choice == "medium" or choice == "hard":
        #Set mazeChosen to the player's input
        #Then do some funky concatenation with the mazeChosen variable
        mazeChosen = choice
        print "Have fun at the", mazeChosen, "maze!"
        print "Type 'help' for some help that you will probably need."
    else:
        #If the input isn't those three then print stuff
        print "What?"
        print "Type something that I can understand please." 
    #Print new line
    print

#Set the player's beginning coordinates that corresponds with each maze
plrX = playerBeginning[mazeChosen][0]
plrY = playerBeginning[mazeChosen][1]

#Print the chosen maze and some funky text.
#See how mazeChosen is used to refer to the three mazes? Pretty cool stuff
printMaze(mazes[mazeChosen])
print "You find yourself in this deep, dark and dank dungeon."
print "You really want to get out of here. \n"

#While loop that will continue looping until the maze has been solved
while not solved:
    #Take what the user inputs after the prompt and converts it to lowercase
    #Save it to the variable choice
    choice = raw_input("What do you want to do next? ").lower()
    tempX = plrX
    tempY = plrY

    #Take the user input and use it in a bunch of if statements
    if choice == "w":
        #If the player typed 'w' then print and subtract plrX by 1
        print "You go west."
        plrX -= 1
    elif choice == "e":
        #If the player typed 'e' then print and add plrX by 1
        print "You go east."
        plrX += 1
    elif choice == "n":
        #If the player typed 'n' then print and subtract plrY by 1
        print "You go north."
        plrY -= 1
    elif choice == "s":
        #If the player typed 's' then print and add plrY by 1
        print "You go south."
        plrY += 1 
    elif choice == "die":
        #Type 'die' and then you die. Also it breaks the while loop, exiting it
        print "You decide to die so you sit in a fetal position and become one with the maze."
        break;
    elif choice == "help":
        #Type 'help' then you shall recieve help :)
        print "Type 'w', 'e', 'n' or 's' depending on the direction you want to go."
        print "If you need some help then type 'help'."
        print "If you don't like this maze then type 'die' to stop."
    else:
        #If the player types anything else just print
        #The computer doesn't understand :(
        print "You're not sure what that means."

    #Check if the player collides with a wall
    #Use plrX, plrY and the maze chosen as inputs
    if isColliding(plrX, plrY, mazes[mazeChosen]):
        #If true then print
        #Then set plrX and plrY back to their original position using tempX/tempY
        print "You smack yourself into the wall. Oops."
        plrX = tempX
        plrY = tempY
    else:
        #If not colliding then set the element where the player is to "O"
        #Then set the where the old player was to "."
        mazes[mazeChosen][tempY][tempX] = "."
        mazes[mazeChosen][plrY][plrX] = "O"

    #Print a new line then print the maze
    print
    printMaze(mazes[mazeChosen])

    #If the player's position is equal to the coords of the maze's end
    if plrX == mazeEnd[mazeChosen][0] and plrY == mazeEnd[mazeChosen][1]:
        #Print maze, print stuff and set solved to True which exits the while loop
        printMaze(mazes[mazeChosen])
        print "You find your way out."
        print "You're Winner!"
        solved = True