with open('puzzle.txt', 'r') as f:
    lines = f.readlines()


total_sum = 0

def checkIfValid(round,red,green,blue):
    for set in round:
        set = set.split(' ')
        if '' in set:
            set.remove('')
        if set[1] == 'red':
            if int(set[0]) > red:
                red = int(set[0])
        elif set[1] == 'blue':
            if int(set[0]) > blue:
                blue = int(set[0])
        elif set[1] == 'green':
            if int(set[0]) > green:
                green = int(set[0])
    return red,green,blue

allGames = {}
for line in lines:
    game = line.split(':')
    games = game[1].strip().split(';')
    allGames[game[0]] = games

for game in allGames.keys():
    red = 0
    blue = 0
    green = 0
    for cubes in allGames[game]:
        cubes = cubes.split(',')
        red,green,blue = checkIfValid(cubes,red,green,blue)
    total_sum += (red*blue*green)

print(total_sum)
