import lib.AoC_lib as AoC

@AoC.timer
def first_part(input_file):
    result = 0
    with open(input_file, 'r') as input:
        for line in input:
            validGame = True
            game, plays = line.split(': ')
            game_id = line.split(' ')[1].strip(':')
            for play in plays.split(';'):
                for cubes in play.strip().split(', '):
                    nbr, color = cubes.split(' ')
                    if 'red' in color and int(nbr) > 12:
                        validGame = False
                    elif 'green' in color and int(nbr) > 13:
                        validGame = False
                    elif 'blue' in color and int(nbr) > 14:
                        validGame = False
            
            if validGame:
                result = result + int(game_id)

    return result


@AoC.timer
def second_part(input_file):
    with open(input_file, 'r') as input:
        powers = []
        for line in input:
            minRed, minGreen, minBlue = 0,0,0
            game, plays = line.split(': ')
            game_id = line.split(' ')[1].strip(':')
            for play in plays.split(';'):
                for cubes in play.strip().split(', '):
                    nbr, color = cubes.split(' ')
                    if 'red' in color and int(nbr) > minRed:
                        minRed = int(nbr)
                    elif 'green' in color and int(nbr) > minGreen:
                        minGreen = int(nbr)
                    elif 'blue' in color and int(nbr) > minBlue:
                        minBlue = int(nbr)
            
            powers.append(minRed*minGreen*minBlue)

    return sum(powers)


if __name__ == '__main__':
    DAY = '02'

    print('First solution for day' + DAY + ': ')
    print('Result: ' + str(first_part('input/input'+DAY+'.txt')))

    print('Second solution for day' + DAY + ': ')
    print('Result: ' + str(second_part('input/input'+DAY+'.txt')))