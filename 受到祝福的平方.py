import math


def is_blessed_id(A):
    if math.sqrt(A).is_integer():
        return "Yes"
    for i in range(1, len(str(A))):
        left = int(str(A)[:i])
        right = int(str(A)[i:])
        if math.sqrt(left).is_integer() and is_blessed_id(right) == "Yes":
            return "Yes"
    return "No"


A = int(input())
print(is_blessed_id(A))