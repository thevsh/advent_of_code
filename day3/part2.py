
from utils import post_answer, get_input_data

DAY = 3
PART = 2


def solve():
    data = get_input_data(day=DAY)
    data = data.strip()
    data = data.split(sep="\n")
    
    needed_digits = 12
    final_sum = 0
    
    clean_digit = "0"
    for digits_array in data:
        found_digits = [clean_digit] * needed_digits
        overflow_index = len(digits_array) - needed_digits
        
        for index, digit in enumerate(digits_array):
            min_index_for_found = max(0, index - overflow_index)
            need_to_clean = False
            for candidate_index in range(min_index_for_found, needed_digits):
                if need_to_clean:
                    found_digits[candidate_index] = clean_digit
                    continue
                
                if digit > found_digits[candidate_index]:
                    found_digits[candidate_index] = digit
                    need_to_clean = True
        
        final_sum += int("".join(found_digits))
    
    post_answer(day=DAY, part=PART, answer=final_sum)
