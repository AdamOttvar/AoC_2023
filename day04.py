import lib.AoC_lib as AoC

@AoC.timer
def first_part(input_file):
    result = 0
    with open(input_file, 'r') as input:
        for line in input:
            card_points = 0
            numbers = line.split(': ')[1]
            winning_numbers, my_numbers = numbers.split('|')
            winning_numbers = ' ' + winning_numbers + ' '
            for number in my_numbers.split():
                if ' '+number.strip()+' ' in winning_numbers:
                    if card_points == 0:
                        card_points=1
                    else:
                        card_points = card_points * 2
            result = result + card_points

    return result


@AoC.timer
def second_part(input_file):
    result = 0
    nbr_of_cards = [1]*198
    print(nbr_of_cards)
    with open(input_file, 'r') as input:
        for line in input:
            break
    return result


if __name__ == '__main__':
    DAY = '04'

    print('First solution for day' + DAY + ': ')
    print('Result: ' + str(first_part('input/input'+DAY+'.txt')))

    print('Second solution for day' + DAY + ': ')
    print('Result: ' + str(second_part('input/input'+DAY+'.txt')))