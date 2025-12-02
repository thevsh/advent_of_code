
from utils import post_answer, get_input_data

DAY = 2
PART = 1


def solve():
    data = get_input_data(day=DAY)
    data = data.strip()
    data = data.split(sep=",")
    
    final_sum = 0
    for input_sample in data:
        start, stop = input_sample.split("-")
        
        # exclude not even arrays
        len_start = len(start)
        start_int = int(start) if not len_start & 1 else 10 ** len_start
        start = str(start_int)
        
        len_stop = len(stop)
        stop_int = int(stop) if not len_stop & 1 else 10 ** (len_stop - 1) - 1
        stop = str(stop_int)
        
        if start_int >= stop_int:
            continue
        
        # calculate candidates
        half_index = len(start) // 2
        left_half_start = start[:half_index]
        left_half_stop = stop[:half_index]
        for candidate_sample in range(int(left_half_start), int(left_half_stop) + 1):
            candidate = int(str(candidate_sample) * 2)
            if start_int <= candidate <= stop_int:
                final_sum += candidate
    
    post_answer(day=DAY, part=PART, answer=final_sum)
