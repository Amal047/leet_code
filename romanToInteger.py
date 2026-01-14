"""
ROMAN TO INTEGER — METHOD 1 (LOOK-BACK)
RULES:
1. Roman numerals are added by default.
2. Subtraction happens when a smaller value appears before a larger value.
3. If current_value > previous_value:
   - The previous value must be subtracted instead of added.
4. Since the previous value was already added, subtract it twice to correct the sum.

APPROACH:
1. Create a dictionary mapping Roman symbols to values.
2. Initialize result = 0.
3. Iterate through the string from left to right.
4. Add the value of the current symbol.
5. If current_value > previous_value:
   - Subtract 2 * previous_value from result.
6. Continue until the end of the string.
7. Return result.

=======================================================

ROMAN TO INTEGER — METHOD 2 (LOOK-AHEAD)
RULES:
1. Compare the current symbol with the next symbol.
2. If current_value < next_value:
   - Subtract current_value.
3. Otherwise:
   - Add current_value.
4. The last symbol is always added.

APPROACH:
1. Create a dictionary mapping Roman symbols to values.
2. Initialize result = 0.
3. Iterate through the string from index 0 to n - 1.
4. For each symbol:
   - If next symbol exists and its value is greater:
     - Subtract current_value.
   - Else:
     - Add current_value.
5. Return result.
"""

def romanToInt(s: str) -> int:
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0

    #Look Back Approach
    # for i in range(len(s)):
    #     if i > 0 and roman_dict[s[i]] > roman_dict[s[i - 1]]:
    #         result += roman_dict[s[i]] - 2 * roman_dict[s[i - 1]]
    #     else:
    #         result += roman_dict[s[i]]
    # return result

    #Look Ahead Approach
    for i in range(len(s)):
        value = roman_dict[s[i]]
        if i + 1 < len(s) and roman_dict[s[i + 1]] > value:
            result -= value
        else:
            result += value
    return result

print(romanToInt("LVIII"))      # Output: 58