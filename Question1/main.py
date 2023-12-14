def convertLine(line):
    wordNumbers={'nine': '9','eight': '8','seven': '7','six': '6','five': '5','four': '4','three': '3','two': '2','one': '1'}
    string = ''
    for i in line:
        for word, number in wordNumbers.items():
                if (word in string):
                    line = line.replace(word, number)
        string += i
    return line
with open('puzzle.txt', 'r') as f:
    lines = f.readlines()
numbers = ['1','2','3','4','5','6','7','8','9']
sum = 0
for line in lines:
    first = ''
    last = ''
    line = convertLine(line)
    for i in range(len(line)):
        if first == '':
            if line[i] in numbers:
                first = line[i]
        if line[i] in numbers:
            last = line[i]
    print('Input: ',line, " First: ", first, " Last: ", last)
    sum += int(first + last)
    print(sum)