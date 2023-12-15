import re
with open('test.txt', 'r') as f:
    lines = f.readlines()
validNumbers = []
def checkForNumbers(i, j, matrix):
    global validNumbers
    for row in range(-1, 2):
        for col in range(-1, 2):
            value = ''
            new_i = i + row
            new_j = j + col
            if 0 <= new_i < len(matrix) and 0 <= new_j < len(matrix[0]):
                if matrix[new_i][new_j].isdigit():
                    for digit in range(-2, 2):
                        if 0 <= new_i + digit < len(matrix):
                            if( matrix[new_i][new_j + digit].isdigit()):
                                print(matrix[new_i][new_j + digit])
                                value += matrix[new_i + digit][new_j]
                                
                    validNumbers.append(value)
    return validNumbers
matrix = []
for input in lines:
    input = input.strip()
    pattern = r'.'
    result = re.findall(pattern, input)
    matrix.append(result)

valid_symbols = "!@#$%^&*()_-+=/\[]"
print(matrix)
for i in range(len(matrix)):
    print('\n',matrix[i])
    for j in range(len(matrix[i])):
        if (matrix[i][j] in valid_symbols):
            checkForNumbers(i,j,matrix)
print(validNumbers)