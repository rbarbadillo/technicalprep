""" Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000. """

# Leetcode: https://leetcode.com/problems/longest-palindromic-substring/solution/
# (1) Longest common substring
# Reverse S and become S′. Find the longest common substring between S and S′, which must also be the longest palindromic substring.
# However is S can contain reverse versions of its substrings and this can lead to errors. For example:
# S = "abacdfgdcaba", S′ = "abacdgfdcaba".
# The longest common substring would be "abacd"

# (2) Brute force
# The obvious brute force solution is to pick all possible starting and ending positions for a substring, and verify if it is a palindrome.
# Time complexity: O(n^3)
# Space complexity O(1)

# (3) Dynamic Programming
# Find "smallest" palindromes and expand on them. 
# Consider the case "ababa". If we already knew that "bab" is a palindrome, it is obvious that "ababa" must be a palindrome since the two left and right end letters are the same.
# Build a matrix such that each element: 
#   P[i,j] == true if substring Si ... Sj is a palindorme
#   P[i,j] == false if not
# P[i,j] = (P[i+1, j-1] and Si == Sj)
# Base cases: P[i,i] = true; P[i, i+1] = (Si == S(i+1))
# We first initialize the one and two letters palindromes, and work our way up finding all three letters palindromes
# Time complexity: O(n^2)
# Space complexity: O(n^2)

# (4) Expand around center
# Palindrome mirrors around its center. How many centers are there?
# Letter not in edges can be centers. (n - 2)
# If palindromes have even number of letters ("abba"), centers are BETWEEN letters. (n - 1)
# Number of centers = 2n - 3
# Time compelxity: O(n^2)
# Space complexity: O(1)

def longestPalindrome(s: str) -> str:
    if s == None or len(s) < 1:
        return ''
    start, end = 0, 0
    length = len(s)
    for i in range(length):
        len1 = expandAroundCenter(s, i, i)
        len2 = expandAroundCenter(s, i, i + 1)
        maxlen = max(len1, len2)
        if (maxlen > end - start):
            start = i - (maxlen - 1) / 2
            end = i + maxlen / 2
    return s.substring(start, end + 1)


def expandAroundCenter(s: str, left: int, right: int) -> int:
    length = len(s)
    while (left >= 0 and right < length and s[left] == s[right]):
        left -= 1
        right += 1
    return right - left -1