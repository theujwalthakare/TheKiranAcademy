# # H.W 
# # check methods like .pop(index/remove ? what is the parameter), .remove( same for this value/index ??) also check return type
# l = [1,2,3,4,5,6]

data = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']

# Determine the number of rows needed
columns = 5
rows = (len(data) + columns - 1) // columns  # Ensures all elements are printed

# Print elements in a formatted way
for row in range(rows):
    for col in range(columns):
        index = row + col * rows  # Calculates correct index for column-wise printing
        if index < len(data):  # Ensures index is within range
            print(data[index], end='\t')  # Tab space for alignment
    print()  # New line after each row