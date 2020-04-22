# Google Question

# Given an array = [2,5,1,2,3,5,1,2,4]:
# It should return 2

# Given an array = [2,1,1,2,3,5,1,2,4]:
# It should return 1

# Given an array = [2,3,4,5]:
# It should return undefined

# Given an array [2,5,5,2,3,5,1,2,4]
# It should return 5 because the pairs are before 2, 2


def func(mylist):
    for i in range(0, len(mylist)):
        for j in range(i+1, len(mylist)):
            if mylist[i] == mylist[j]:
                return mylist[i]
    return 0
# O (n^2)


def findrecurring(mylist):
    hashtable = {}
    for i in range(0, len(mylist)):
        if mylist[i] in hashtable:
            return mylist[i]
        else:
            hashtable[mylist[i]] = i
    return False
# O (n) time complexity
# trade-off -> space complexity now O(n) as well


a = [2, 5, 1, 2, 3, 5, 1, 2, 4]
b = [2, 1, 1, 2, 3, 5, 1, 2, 4]
c = [2, 3, 4, 5]
d = [2, 5, 5, 2, 3, 5, 1, 2, 4]
print(findrecurring(a))
print(findrecurring(b))
print(findrecurring(c))
print(findrecurring(d))
