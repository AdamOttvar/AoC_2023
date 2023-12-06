import lib.AoC_lib as AoC

@AoC.timer
def first_part(input_file):
    result = 0
    with open(input_file, 'r') as input:
        for line in input:
            break
    return result


@AoC.timer
def second_part(input_file):
    result = 0
    with open(input_file, 'r') as input:
        for line in input:
            break
    return result


if __name__ == '__main__':
    DAY = '01'

    print('First solution for day' + DAY + ': ')
    print('Result: ' + str(first_part('input/input'+DAY+'.txt')))

    print('Second solution for day' + DAY + ': ')
    print('Result: ' + str(second_part('input/input'+DAY+'.txt')))