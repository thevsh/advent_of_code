
from utils import post_answer, get_input_data

DAY = 1
PART = 2


def solve():
    data = get_input_data(day=DAY)
    data = data.split(sep="\n")[:-1]
    
    full_round_count = 100
    zeros_count = 0
    current_number = 50
    for input_sample in data:
        shift_number = int(input_sample[1:])
        zeros_count += shift_number // full_round_count
        shift_number = shift_number % full_round_count

        should_count_zero_click = bool(current_number)
        current_number += shift_number if input_sample[0] == "R" else -shift_number
        zeros_count += should_count_zero_click and not 0 < current_number < full_round_count
        current_number = current_number % full_round_count
    
    post_answer(day=DAY, part=PART, answer=zeros_count)
