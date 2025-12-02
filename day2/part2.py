import math

from utils import post_answer, get_input_data

DAY = 2
PART = 2


def solve():
    data = get_input_data(day=DAY)
    data = data.strip()
    data = data.split(sep=",")
    
    final_sum = 0
    for input_sample in data:
        start, stop = input_sample.split("-")
        
        start_int = int(start) if not len(start) == 1 else 10
        start = str(start_int)
        len_start = len(start)

        stop_int = int(stop) if not len(stop) == 1 else 10
        stop = str(stop_int)
        len_stop = len(stop)
        
        if start_int == stop_int:
            continue

        candidates_collection = set()
        # calculate candidates
        left_half_start = int(start[:len_start // 2])
        left_half_stop = int(stop[:math.ceil(len_stop / 2)])
        lens_range = list(range(len_start, len_stop + 1))
        for candidate_half_sample in range(left_half_start, left_half_stop + 1):
            candidate_half_sample_str = str(candidate_half_sample)
            
            for candidate_sample_len in range(1, len(candidate_half_sample_str) + 1):
                candidate_sample = candidate_half_sample_str[:candidate_sample_len]
                
                multipliers = set(full_len // candidate_sample_len for full_len in lens_range)
                for multiplier in multipliers:
                    candidate = int(str(candidate_sample) * multiplier)
                    if candidate in candidates_collection:
                        continue
                    
                    candidates_collection.add(candidate)
                    if start_int <= candidate <= stop_int:
                        final_sum += candidate
    
    post_answer(day=DAY, part=PART, answer=final_sum)
