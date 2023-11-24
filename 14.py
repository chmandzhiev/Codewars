# Vowel Count

def get_count(sentence):
    count = 0
    lst = ["a","e","i","o","u"]
    for i in lst:
        for j in sentence:
            if i == j:
                count +=1
    return count
