# Beginner Series #3 Sum of Numbers

def get_sum(a,b):
    s = 0
    if a != b:
        if a < b: 
            for i in range(a,b+1):
                s += i
        if a > b:
            for i in range(a,b-1,-1):
                s += i
        return s
    else:
        return a

