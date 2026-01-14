'''
PALINDROME NUMBER (Math Approach)
RULES:
1. Negative numbers are NOT palindromes.
2. Numbers ending with 0 are NOT palindromes (except 0 itself).
3. A palindrome reads the same forward and backward.
4. We do NOT need to reverse the entire number.
5. Reversing only HALF of the number is sufficient.

APPROACH:
1. Reject invalid cases:
   - x < 0
   - x % 10 == 0 and x != 0
2. Initialize reversed_half = 0.
3. While original_number > reversed_half:
   - Extract last digit using x % 10.
   - Append digit to reversed_half using reversed_half * 10 + digit.
   - Remove last digit from x using x // 10.
4. After the loop:
   - If even digits: x == reversed_half
   - If odd digits: x == reversed_half // 10
5. Return True if either condition is satisfied, else False.
'''


def palandrome_number(x:int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    rev = 0
    while x > rev:
        digit = x % 10
        rev = rev * 10 + digit
        x //= 10
    return x == rev or x == rev // 10

print(palandrome_number(1231))