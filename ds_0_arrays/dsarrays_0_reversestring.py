def reverseString(string):
    # Check input
    notValidInput = not string or type(string) is not str or len(string) == 0
    if notValidInput:
        return False

    if len(string) == 1:
        return string
    return reverseString(string[1:]) + string[0]


def reverse(stri):
    mylist = []
    for i in range(len(stri)-1, -1, -1):
        mylist.append(stri[i])
    return ''.join(mylist)


print(reverseString('reverse string'))
print(reverseString(''))
