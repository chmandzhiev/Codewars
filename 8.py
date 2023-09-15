# Sum of two lowest positive integers

def sum_two_smallest_numbers(numbers):
    srt_lst = sorted(numbers)
    return srt_lst[0] + srt_lst[1]


print(sum_two_smallest_numbers([19, 5, 42, 2, 77]))

