
from utils import post_answer, get_input_data

DAY = 7
PART = 1


def solve():
    data = get_input_data(day=DAY)
    data = data.strip().split(sep="\n")
    
    beams_indexes = set()
    beams_indexes.add(data[0].index("S"))
    data = data[1:]
    
    count = 0
    for line in data:
        for sign_index, sign in enumerate(line):
            if sign == "^" and sign_index in beams_indexes:
                beams_indexes.remove(sign_index)
                beams_indexes.add(sign_index - 1)
                beams_indexes.add(sign_index + 1)
                count += 1
    
    post_answer(day=DAY, part=PART, answer=count)
