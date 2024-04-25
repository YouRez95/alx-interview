#!/usr/bin/python3
"""
  function:
    minOperations
"""


def minOperations(n: int) -> int:
    """
      method that calculates the fewest number of operations needed
      to result in exactly n H characters in the file.
    """
    if n < 0:
        return 0
    if n == 1:
        return 0

    for i in range(2, n + 1):
        if n % i == 0:
            m = int(n / i)
            return i + minOperations(m)
