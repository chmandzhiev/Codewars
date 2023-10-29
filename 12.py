# Shortest Word

def find_short(s):
    lst = sorted(s.split(),key=len)
    return len(lst[0])


print(find_short("bitcoin take over the world maybe who knows perhaps"))