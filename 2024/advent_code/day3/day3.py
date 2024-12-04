import re
from pathlib import Path

DO_NOT_PATTERN = "don\'t\(\)"
DO_PATTERN = "do\(\)"
MUL_PATTERN = "mul\(\d{1,3}\,\d{1,3}\)"
COMBINED_PATTERN = f"(?:{DO_NOT_PATTERN}|{DO_PATTERN}|{MUL_PATTERN})"


def extract_groups(text: str, pattern: str):
    return re.findall(pattern, text)

def get_values():
    INPUT_PATH = Path(__file__).parent / "day3_input.txt"
    with open(INPUT_PATH, "r") as file:
        # can optimize the read portion here
        INPUT_TEXT = file.read()
        return extract_groups(INPUT_TEXT, COMBINED_PATTERN)
    

def combine(items):
    total = 0
    multiply_next = True

    for item in items:
        if re.match(DO_NOT_PATTERN, item):
            multiply_next = False
            continue
        elif re.match(DO_PATTERN, item):
            multiply_next = True
            continue
        if (multiply_next):
            nums = re.findall(r"\d{1,3}", item)
            if len(nums) == 2: 
                num1, num2 = map(int, nums) 
            result = num1 * num2
            total += result
    return total

print(combine(get_values()))

'''
linear time and space, it reads through the text file once then the matches again, so n + m

can optimize the read to do inline calculations and not need to store the data in memory

'''
