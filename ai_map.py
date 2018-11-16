import sys
import random



def getMap():
    global prob
    global nrows
    global ncolmuns

    pacman = (random.randint(1, nrows - 2), random.randint(1, ncolmuns - 2))
    food = (random.randint(1, nrows - 2), random.randint(1, ncolmuns - 2))
    while (pacman == food):
        food = (random.randint(1, nrows - 2), random.randint(1, ncolmuns - 2))
    for i in range(nrows):
        for j in range (ncolmuns):
            if (i,j) == pacman:
                sys.stdout.write('P')
            elif (i,j) == food:
                sys.stdout.write('.')
            elif random.random() < prob:
                sys.stdout.write('%')
            elif i == 0 or j == 0 or i == nrows - 1 or j == ncolmuns - 1:
                sys.stdout.write('%')
            else:
                sys.stdout.write(' ')
        sys.stdout.write('\n')

if __name__ == '__main__':

    if len(sys.argv) < 5:
        sys.exit()

    nrows = int(sys.argv[1])
    ncolmuns = int(sys.argv[2])
    prob = float(sys.argv[3])
    seed = int(sys.argv[4])
    random.seed(a=seed)

    getMap()
