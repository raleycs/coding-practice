# This problem was recently asked by Google.
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?

import timeit

nums = [10, 15, 3, 7]
k = 21

def brute():
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == k:
                return True
    return False

def bonus():
    s = set(nums)
    for i in range(0, len(nums)):
        diff = k - nums[i]
        if diff in s:
            return True
    return False

def main():
    print("k = " + str(k))
    print("Brute force time O(n^2): " + str(timeit.timeit("brute()", setup="from __main__ import brute")))
    print("Optimal time O(n): " + str(timeit.timeit("bonus()", setup="from __main__ import bonus")))

if __name__ == "__main__":
    main()
