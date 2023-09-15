# Closure Counter

def countdown(n):
    def step():
        nonlocal n
        r = n
        n -= 1
        return r
    return step

do_step = countdown(10)

print(do_step())