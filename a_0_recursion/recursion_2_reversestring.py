def reverseString(string):
    if len(string) == 1:
        return string
    return reverseString(string[1:]) + string[0]


print(reverseString('hello there'))
