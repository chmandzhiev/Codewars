# Find the divisors!

def divisors(integer):
    divisors_list = []
    numbers_list = []

    for i in range(2,integer):
        numbers_list.append(i)
        
    for number in numbers_list:
        if (integer % number) == 0:
            divisors_list.append(number)
        
    if divisors_list == []:
        return (f"{integer} is prime")  
    else:
        return divisors_list  
    






