
from utils import post_answer, get_input_data

DAY = 4
PART = 1


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
        matrix[index] = empty_sign + row + empty_sign
    
    for row_index, row in enumerate(matrix):
        for column_index, element in enumerate(row):
            if element != paper_roll_sign:
                continue
            
            nearly_rolls_count = 0
            for y in range(row_index - 1, row_index + 2):
                for x in range(column_index - 1, column_index + 2):
                    if x == column_index and y == row_index:
                        continue
                    
                    nearly_rolls_count += matrix[y][x] == paper_roll_sign
                    if nearly_rolls_count == 4:
                        break
                if nearly_rolls_count == 4:
                    break
            else:
                final_count += 1
    
    post_answer(day=DAY, part=PART, answer=final_count)
