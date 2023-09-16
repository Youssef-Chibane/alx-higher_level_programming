#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    prev_value = 0

    for char in roman_string[::-1]:
        if char in roman_values:
            current_value = roman_values[char]

            if current_value >= prev_value:
                total += current_value
            else:
                total -= current_value

            prev_value = current_value

    return total
