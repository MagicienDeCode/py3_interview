from typing import List

# Create a list test1 with two elements, both set to False.
test1 = [False] * 2
print(test1)

# Create a list test containing a nested list with one element set to True.
test = [[False, True, False]]

print(test)
# Print the element at index 1 of the first list in the test list.
print(test[0][1])

print("===============")

# Create a 3x3 matrix-like list where each element is set to False.
test = [[False]*3 for _ in range(3)]

print(test)
print("===============")

# Perform floating-point division (result is a float).
print(1 / 3)
# Perform integer division (the result is the quotient).
print(1 // 3)  # 商 Quotient
# Calculate the remainder of the division.
print(1 % 3)  # 余数 Remainder

# Convert the string "9" to an integer and print it.
print(int("9"))

"""
row  [row  0 - 8] [0 - 8]
col  [col  0 - 8] [0 - 8]
box  [box  0 - 8] [0 - 8]

box0 box1 box2
box3 box4 box5
box6 box7 box8
box[?] = (i//3)*3 + (j//3)

for example, [5,5] has '5'
row[5][4] = True
col[5][4] = True
box[i] = (5 // 3) * 3 + (5 // 3) = 4

"""
class Solution:
	def isValidSudoku(self, board: List[List[str]]) -> bool:
		# Initialize arrays to keep track of numbers in rows, columns, and boxes
		row = [[False]*9 for _ in range(9)]
		col = [[False]*9 for _ in range(9)]
		box = [[False]*9 for _ in range(9)]

		# Iterate through each cell in the Sudoku board
		for i in range(9):
			for j in range(9):
				currentStr = board[i][j]
				# If the current cell is not empty (contains a number)
				if currentStr != ".":
					# Convert character to integer (subtract 1 for 0-based index)
					v = int(currentStr) - 1
					# Calculate the box index
					box_i = (i//3)*3 + (j//3)
					# Check if the number is already present in the current row, column, or box
					if row[i][v] or col[j][v] or box[box_i][v]:
						return False
					# Mark the number as seen in the current row, column, and box
					row[i][v] = True
					col[j][v] = True
					box[box_i][v] = True
		# If no conflicts are found, the Sudoku is valid
		return True


