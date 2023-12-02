import lib.AoC_lib as AoC
from collections import deque
import re

@AoC.timer
def first_part(input_file):
    result = 0
    calibration_values = []
    with open(input_file, 'r') as input:
        for line in input:
            number_string = re.findall(r'\d{1}',line)[0] + re.findall(r'\d{1}',line)[-1]
            calibration_values.append(int(number_string))
    
    result = sum(calibration_values)
    return result

digits = {'one':'o1e', 'two':'t2o', 'three':'t3e', 'four':'f4r', 'five':'f5e', 'six':'s6x', 'seven':'s7n', 'eight':'e8t', 'nine':'n9e'}
def convert_case(match_obj):
    return digits[match_obj.group(1)]

@AoC.timer
def second_part(input_file):
    result = 0
    calibration_values = []
    with open(input_file, 'r') as input:
        for line in input:
            new_string = re.sub(r"(one|two|three|four|five|six|seven|eight|nine)", convert_case, line)
            newer_string = re.sub(r"(one|two|three|four|five|six|seven|eight|nine)", convert_case, new_string)
            number_string = re.findall(r'\d{1}',new_string)[0] + re.findall(r'\d{1}',newer_string)[-1]

            calibration_values.append(int(number_string))
    
    result = sum(calibration_values)

    return result


if __name__ == '__main__':
    DAY = '01'

    print('First solution for day' + DAY + ': ')
    print('Result: ' + str(first_part('input/input'+DAY+'.txt')))

    print('Second solution for day' + DAY + ': ')
    print('Result: ' + str(second_part('input/input'+DAY+'.txt')))