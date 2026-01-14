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