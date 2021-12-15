import random
random.seed(0xC8763)
m = 2722458769
def Q1_CountNumbers(n: int) -> int:
  def recur(n: int) -> int:
    return 1 if n == 0 else (recur(n//2)**2 * (20 if n & 1 else 1) % m)
  return recur(n//2) * (5 if n & 1 else 1) % m # n & 1 means the last bit of n

count = -1
def gen_data():
    """Generate function inputs as array"""
    global count
    count = count + 1
    return [random.randint(1, int(1e12))]
