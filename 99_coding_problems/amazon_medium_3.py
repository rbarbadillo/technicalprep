""" Given a string, find the length of the longest substring without repeating characters. """
a = "abcabcbb"
b = "bbbbb"
c = "pwwkew"

# (1) Brute force approach


def bruteForce(s: str) -> str:
    aux = {}
    maxlength = 0
    i = 0
    keepgoing = True
    while keepgoing:
        for j in range(i, len(s)):
            if s[j] not in aux:
                aux[s[j]] = j
            else:
                if (j == len(s)):
                    keepgoing = False
                if len(aux) > maxlength:
                    maxlength = len(aux)
                i = + 1
                aux = {}
                break

    return maxlength


print(bruteForce(a))
print(bruteForce(b))
print(bruteForce(c))


# (2) Sliding window approach
def longestUniqueSubsttr(s: str) -> int:

    # Creating a set to store the last positions of occurrence
    seen = {}
    maximum_length = 0

    # Starting the inital point of window to index 0
    start = 0

    for end in range(len(s)):

        # Checking if we have already seen the element or not
        if s[end] in seen:

            # If we have seen the number, move the start pointer
            # to position after the last occurrence
            start = max(start, seen[s[end]] + 1)

        # Updating the last seen value of the character
        seen[s[end]] = end
        maximum_length = max(maximum_length, end-start+1)
    return maximum_length

# Time complexity: O(2n) = O(n)
# Space complexity: O(min(m, n))
