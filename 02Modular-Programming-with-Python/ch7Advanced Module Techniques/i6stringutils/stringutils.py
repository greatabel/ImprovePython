import re

def extract_numbers(s):
    pattern = r'[+-]?\d+(?:\.\d+)?'
    numbers = []
    for match in re.finditer(pattern, s):
        number = s[match.start():match.end()]
        numbers.append(number)
    return numbers


if __name__ == "__main__":
    extract = extract_numbers("I like 2018 06 26 11:47, future is coming!")
    print(extract)