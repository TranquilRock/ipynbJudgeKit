m = 2722458769

# Sample
def Q1_CountNumbers(n: int) -> int:
    res = 1
    if n == 1:
        res = 5
    elif n == 2:
        res = 20
    elif n % 2 != 0:
        res = Q1_CountNumbers(n - 1) * 5
    elif (n // 2) % 2 != 0:
        res = Q1_CountNumbers(n - 2) * 20
    else:
        res = Q1_CountNumbers(n // 2) ** 2
    return res % m
