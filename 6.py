# String ends with?

def solution(text, ending):
    reverse_1 = "".join(list(text)[::-1])
    reverse_2 = "".join(list(ending)[::-1])

    if reverse_1[0:len(reverse_2)] == reverse_2:
        return True
    else:
        return False
    

print(solution("abcd","cd"))