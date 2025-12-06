
from utils import get_input_data, post_answer

DAY = 5
PART = 2


def solve():
    data = get_input_data(day=DAY)
    
    fresh_ids_ranges, ids = data.split(sep="\n\n")
    fresh_ids_ranges = fresh_ids_ranges.strip().split(sep="\n")
    fresh_ids_ranges = [pair.split(sep="-") for pair in fresh_ids_ranges]
    for pair in fresh_ids_ranges:
        pair[0] = int(pair[0])
        pair[1] = int(pair[1])
    
    fresh_ids_ranges.sort(key=lambda pair: pair[0], reverse=True)
    
    pair = fresh_ids_ranges.pop()
    final_ranges = [pair]
    while fresh_ids_ranges:
        next_pair = fresh_ids_ranges.pop()
        if pair[1] < next_pair[0]:
            pair = next_pair
            final_ranges.append(pair)
        elif pair[1] < next_pair[1]:
            pair[1] = next_pair[1]
    
    final_count = sum(pair[1] - pair[0] + 1 for pair in final_ranges)
    post_answer(day=DAY, part=PART, answer=final_count)
