
from utils import post_answer, get_input_data

DAY = 4
PART = 2


def solve():
    data = get_input_data(day=DAY)
    data = data.strip()
    data = data.split(sep="\n")

    final_count = 0
    
    paper_roll_sign = "@"
    empty_sign = "."
    empty_row = [empty_sign * len(data[0])]
    matrix = empty_row + data + empty_row
    for index, row in enumerate(matrix):
        matrix[index] = [empty_sign] + list(row) + [empty_sign]
    
    while True:
        rolls_to_remove_count = 0
        for row_index, row in enumerate(matrix):
            for column_index, element in enumerate(row):
                if element == empty_sign:
                    continue
                
                nearly_rolls_count = 0
                for y in range(row_index - 1, row_index + 2):
                    for x in range(column_index - 1, column_index + 2):
                        if x == column_index and y == row_index:
                            continue
                        
                        nearly_rolls_count += matrix[y][x] == paper_roll_sign
                        if nearly_rolls_count == 4:
                            break
                    else:
                        continue
                    break
                else:
                    matrix[row_index][column_index] = empty_sign
                    rolls_to_remove_count += 1
                    final_count += 1
        
        if not rolls_to_remove_count:
            break
    
    print("\n".join("".join(row) for row in matrix))
    post_answer(day=DAY, part=PART, answer=final_count)
