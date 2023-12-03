import lib.AoC_lib as AoC
import re

def get_adjacent_positions(center_pos):
    dCol = [ 0, 1, 0, -1, -1, 1, -1, 1]
    dRow = [ -1, 0, 1, 0, -1, -1, 1, 1]
    adj_pos = []

    # Go to the adjacent cells
    for i in range(len(dRow)):
        adj_pos.append((center_pos[0]+dRow[i], center_pos[1]+dCol[i]))

    return adj_pos

@AoC.timer
def first_part(input_file):
    result = 0

    with open(input_file, 'r') as input:
        schematic = [line.rstrip() for line in input]

    symbols = {}
    digits = {}
    special_char_pattern = re.compile(r"[^A-Za-z0-9.]")
    digit_pattern = re.compile(r"[0-9]+")
    for row_id, row in enumerate(schematic):
        for match in special_char_pattern.finditer(row):
            symbols[(row_id, match.start())] = match.group()
        for match in digit_pattern.finditer(row):
            digits[(row_id, match.start(), match.end()-1)] = match.group()

    for digit_pos in digits:
        adj_pos1 = get_adjacent_positions((digit_pos[0],digit_pos[1]))
        adj_pos2 = get_adjacent_positions((digit_pos[0],digit_pos[2]))
        adj_pos1.extend(adj_pos2)
        adj_pos = set(adj_pos1)
        for pos in adj_pos:
            if pos in symbols:
                result = result + int(digits[digit_pos])

    return result


@AoC.timer
def second_part(input_file):
    result = 0

    with open(input_file, 'r') as input:
        schematic = [line.rstrip() for line in input]

    symbols = {}
    digits = {}
    special_char_pattern = re.compile(r"[^A-Za-z0-9.]")
    digit_pattern = re.compile(r"[0-9]+")
    for row_id, row in enumerate(schematic):
        for match in special_char_pattern.finditer(row):
            if '*' in match:
                symbols[(row_id, match.start())] = 0
        for match in digit_pattern.finditer(row):
            digits[(row_id, match.start(), match.end()-1)] = match.group()
    
    for digit_pos in digits:
        adj_pos1 = get_adjacent_positions((digit_pos[0],digit_pos[1]))
        adj_pos2 = get_adjacent_positions((digit_pos[0],digit_pos[2]))
        adj_pos1.extend(adj_pos2)
        adj_pos = set(adj_pos1)
        for pos in adj_pos:
            if pos in symbols:
                
                result = result + int(digits[digit_pos])
    
    return result


if __name__ == '__main__':
    DAY = '03'

    print('First solution for day' + DAY + ': ')
    print('Result: ' + str(first_part('input/input'+DAY+'.txt')))
    #print('Result: ' + str(first_part('input/test.txt')))

    #print('Second solution for day' + DAY + ': ')
    #print('Result: ' + str(second_part('input/input'+DAY+'.txt')))
    print('Result: ' + str(second_part('input/test.txt')))