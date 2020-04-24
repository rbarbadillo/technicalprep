""" This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass? """

# Approach 1: Brute force


def twoSumBruteForce(list, k):
    for i in range(0, len(list)):
        for j in range(i + 1, len(list)):
            if list[i] + list[j] == k:
                return True
    return False
# Time complexity: O(n^2)
# Space complexity: O(1)

# Approach 2: Two-pass using a dictionary (hashtable)


def twoSumTwoPassHashTable(list, k):
    dictionary = {}
    for i in range(0, len(list)):
        dictionary[list[i]] = i
    for i in range(0, len(list)):
        complement = k - list[i]
        if complement in dictionary:
            return True
    return False
# Time complexity: O(n)
# Space complexity: O(n)

# Approach 3: One-pass using a dictionary (hashtable)


def twoSum(list, k):
    dictionary = {}
    for i in range(0, len(list)):
        dictionary[list[i]] = i
        complement = k - list[i]
        if complement in dictionary:
            return True
    return False
# Time complexity: O(n)
# Lookup (complement in dictionary) is O(1)
# Space complexity: O(n)


print(twoSum([10, 15, 3, 7], 10))
