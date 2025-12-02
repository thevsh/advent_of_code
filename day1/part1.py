
from utils import post_answer, get_input_data

DAY = 1
PART = 1


def solve():
    data = get_input_data(day=DAY)
    data = data.split(sep="\n")[:-1]
    
    max_round_count = 100
    zeros_count = 0
    current_number = 50
    for input_sample in data:
        shift_number = int(input_sample[1:])
        current_number += shift_number if input_sample[0] == "R" else -shift_number
        if not current_number % max_round_count:
            zeros_count += 1
    
    post_answer(day=DAY, part=PART, answer=zeros_count)
