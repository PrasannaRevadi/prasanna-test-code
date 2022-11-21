def numberToBase(n,3):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % 3))
        n //= 3
    return digits[::-1]
