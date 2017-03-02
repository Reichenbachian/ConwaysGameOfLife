import os, time, random

xSize = 30
ySize = 40
timesteps = 1000
numberOfRandom = 100
board = [[0 for y in range(xSize)] for x in range(ySize)]

if numberOfRandom > xSize * ySize:
	print("You can't have numberOfRandom > xSize * ySize")

for i in range(numberOfRandom):
	y = int(random.random()*ySize)
	x = int(random.random()*xSize)
	while board[y][x] == 1:
		y = int(random.random()*ySize)
		x = int(random.random()*xSize)
	board[y][x] = 1


for i in range(timesteps):
	os.system('cls' if os.name == 'nt' else 'clear')
	for y in range(ySize):
		for x in range(xSize):
			surroundedByCells = 0
			for xOffset in [-1, 0, 1]:
				for yOffset in [-1, 0, 1]:
					xTest = (xOffset + x) % xSize
					yTest = (yOffset + y) % ySize
					surroundedByCells += board[yTest][xTest]
			if board[y][x] == 1:
				surroundedByCells -= 1
			#Overpopulation
			if surroundedByCells > 3:
				board[y][x] = 0
			#Underpopulation
			if surroundedByCells < 2:
				board[y][x] = 0
			#Reproduction
			if board[y][x] == 0 and surroundedByCells == 3:
				board[y][x] = 1
			printString = str(board[y][x]);
			if printString == "0":
				printString = " "
			if board[y][x] == 1:
				printString = "\033[94m" + printString + "\x1b[0m"

			print(printString, end=" ")
		print("")
	time.sleep(.25)