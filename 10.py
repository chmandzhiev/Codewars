# Array.diff

def array_diff(a, b):
    result_list = []

    for i in a:
        if i not in b:
            result_list.append(i)
    return result_list

print(array_diff([1,2,2,2,3],[2]))
