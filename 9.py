# Printer Errors

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m"]

def printer_error(s):
    s1 = 0
    s2 = len(s)
    s = s.lower()
    for i in s:
        if i not in letters:
            s1 +=1
    return f"{s1}/{s2}"

 
