
from utils import post_answer, get_input_data

DAY = 3
PART = 1


def solve():
    data = get_input_data(day=DAY)
    data = data.strip()
    data = data.split(sep="\n")
    
    final_sum = 0
    for digits_array in data:
        largest_tenth = digits_array[0]
        max_number = 0
        
        for digit in digits_array[1:]:
            number = int(largest_tenth+digit)
            if number > max_number:
                max_number = number
            
            if digit > largest_tenth:
                largest_tenth = digit
        
        final_sum += max_number
    
    post_answer(day=DAY, part=PART, answer=final_sum)
