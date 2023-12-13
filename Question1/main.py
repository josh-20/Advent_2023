f = open('puzzle2.txt','r')
lines = f.readlines()

numbers = ['1','2','3','4','5','6','7','8','9','0']
wordNumbers={'one': '1','two': '2','three': '3','four': '4','five': '5','six': '6','seven': '7','eight': '8','nine': '9'}
sum = 0
for line in lines:
    first = ''
    last = ''
    for word in wordNumbers.keys():
        if word in line:
            line = line.replace(word,wordNumbers[word])
    for i in range(len(line)):
        if first == '':
            if line[i] in numbers:
                first = line[i]
        if line[i] in numbers:
            last = line[i]
    # print('Input: ',line, " First: ", first, " Last: ", last)
    sum += int(first + last)
    print(sum)