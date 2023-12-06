import lib.AoC_lib as AoC
import re

@AoC.timer
def first_part(input_file):
    result = 1
    with open(input_file, 'r') as input:
        times = [int(x) for x in re.findall(r'\d+',input.readline())]
        distances = [int(x) for x in re.findall(r'\d+',input.readline())]
        for time_idx, time in enumerate(times):
            velocity = 1
            while (time - velocity)*velocity <= distances[time_idx]:
                velocity = velocity + 1
            start_time = velocity
            
            velocity = time - 1
            while (time - velocity)*velocity <= distances[time_idx]:
                velocity = velocity - 1
            end_time = velocity
            
            result = result*(end_time-start_time+1)


    return result


@AoC.timer
def second_part(input_file):
    result = 0
    with open(input_file, 'r') as input:
        time = int(''.join(re.findall(r'\d+',input.readline())))
        distance = int(''.join(re.findall(r'\d+',input.readline())))

        velocity = 1
        while (time - velocity)*velocity <= distance:
            velocity = velocity + 1
        start_time = velocity
        
        velocity = time - 1
        while (time - velocity)*velocity <= distance:
            velocity = velocity - 1
        end_time = velocity
        
        result = end_time-start_time+1

    return result


if __name__ == '__main__':
    DAY = '06'

    print('First solution for day' + DAY + ': ')
    print('Result: ' + str(first_part('input/input'+DAY+'.txt')))

    print('Second solution for day' + DAY + ': ')
    print('Result: ' + str(second_part('input/input'+DAY+'.txt')))