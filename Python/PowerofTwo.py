def isPowerOfTwo(n: int) -> bool:
    import math
    if n < 0 or n == 0:
        return False
    if n == 1 or (math.log2(n) * 10 % 10) == 0.0:
        return True
    return False
