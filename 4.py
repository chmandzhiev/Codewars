# String ends with?

def solution(string, ending):
    string_list = list(string)
    ending_list = list(ending)

    z = 0

    string_list.reverse()
    ending_list.reverse()

    if len(ending_list) <= len(string_list):
        for i in range(len(ending_list)):
            if ending_list[i] == string_list[i]:
                z +=1
    else:
        return False
    
    if ending == "":
        return True
    elif z == len(ending_list):
        return True
    else:
        return False 


print(solution("abc", "abcd"))
