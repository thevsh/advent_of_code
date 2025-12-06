import math

from utils import post_answer, get_input_data

DAY = 6
PART = 2


def solve():
    data = get_input_data(day=DAY)
    lines = data.split(sep="\n")
    lines.pop()
    
    operators = lines.pop()
    operators += " !"
    operators_len = len(operators)
    
    final_summ = 0
    index = 0
    while index != operators_len - 1:
        operator = operators[index]
        func = sum if operator == "+" else math.prod
        assert operator in "*+"
        
        numbers = []
        for column_index in range(index, operators_len):
            if operators[column_index + 1] in "*+!":
                index = column_index + 1
                break
            numbers.append(int("".join(line[column_index] for line in lines)))
        
        final_summ += func(numbers)
    
    post_answer(day=DAY, part=PART, answer=final_summ)
