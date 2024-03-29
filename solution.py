import random
from typing import List

M = 2722458769


def Q1_CountNumbers(n: int) -> int:
    def recur(n: int) -> int:
        return 1 if n == 0 else (recur(n // 2) ** 2 * (20 if n & 1 else 1) % M)

    return recur(n // 2) * (5 if n & 1 else 1) % M  # n & 1 means the last bit of n


count = -1


def gen_data() -> List[int]:
    """Generate function inputs as array"""
    global count
    count = count + 1
    random.seed(0xC8763 + count)
    return [random.randint(int(1e3), int(1e4))]


def data_reset() -> None:
    global count
    count = -1
