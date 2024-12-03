def f1(a,b):
    if a < 10:
        return 0
    return a*b

def f2(a):
    return f1(f1(a, a+1), 5)

print(f2(5))
print(f2(10))