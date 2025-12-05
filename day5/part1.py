
from utils import post_answer, get_input_data

DAY = 5
PART = 1


def solve():
    data = get_input_data(day=DAY)
    
    fresh_ids_ranges, ids = data.split(sep="\n\n")
    ids = ids.strip().split(sep="\n")
    fresh_ids_ranges = fresh_ids_ranges.strip().split(sep="\n")
    fresh_ids_ranges = [pair.split(sep="-") for pair in fresh_ids_ranges]
    for pair in fresh_ids_ranges:
        pair[0] = int(pair[0])
        pair[1] = int(pair[1])
    
    final_count = 0
    
    for index in ids:
        index = int(index)
        for min_, max_ in fresh_ids_ranges:
            if min_ <= index <= max_:
                final_count += 1
                break
    
    post_answer(day=DAY, part=PART, answer=final_count)
