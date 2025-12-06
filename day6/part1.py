import math

from utils import post_answer, get_input_data

DAY = 6
PART = 1


def solve():
    data = get_input_data(day=DAY)
    
    numbers = []
    for line in data.strip().split(sep="\n"):
        line_numbers = []
        numbers.append(line_numbers)
        for number in line.strip().split(sep=" "):
            if not number:
                continue
            line_numbers.append(number)
    
    operators = numbers.pop()
    final_summ = 0
    for index, operator in enumerate(operators):
        func = sum if operator == "+" else math.prod
        final_summ += func(int(line[index]) for line in numbers)
    
    post_answer(day=DAY, part=PART, answer=final_summ)
