""" This problem was asked by Amazon.

Run-length encoding is a fast and simple method of encoding strings. 
The basic idea is to represent repeated successive characters as a single count and character. 
For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. 
You can assume the string to be encoded have no digits and consists solely of alphabetic characters. 
You can assume the string to be decoded is valid. """


# Naïve approach

def encoding(string):
    # We know the string will contain only alphabetic characters but not if they're going to be uppercase or lowercase so we convert it to one or the other.
    string = string.upper()
    # Auxiliary variables to store result and temporary searching values
    result = []
    currentrepetition = 0
    currentletter = string[0]
    for letter in string:
        if letter == currentletter:
            currentrepetition += 1
        elif letter != currentletter:
            result.append(str(currentrepetition))
            result.append(currentletter)
            currentrepetition = 1
            currentletter = letter
    result.append(str(currentrepetition))
    result.append(currentletter)
    return ''.join(result)
# Linear time complexity: O(n)


def decoding(string):
    # Assume valid input
    result = []
    for i in range(0, len(string), 2):
        repetitions = int(string[i])
        for _ in range(0, repetitions):
            result.append(string[i+1])
    return ''.join(result)
# Time complexity O(n/2*(sum of the letter repetitions indexes))

import itertools
import re

def encode(string):
    return ''.join(
        str(len(list(group))) + c 
        for c, group in itertools.groupby(string.upper())
    )
def decode(string):
    regex = "([0-9]+)([A-Za-z]+)"
    return ''.join(int(count) * char 
    for count, char in re.findall(regex, string))


print(encode("AAAABBBCCDAa"))
print(decoding("4A3B2C1D2A"))

