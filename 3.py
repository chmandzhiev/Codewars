# Don't give me five!

def dont_give_me_five(start, end):
    numbers = []
    new_list = []
    num = "5"    
    j = 0

    for i in range (start, end + 1):
        numbers.append(i)
    for f in numbers:
        str_number = str(f)
        if  num in str_number:
            continue
        else:
            new_list.append(f)
        j +=1
    return j
