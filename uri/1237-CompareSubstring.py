def compareSubstring(a,b):
    result = 0
    a = list(set(a))
    b = list(set(b))

    result = (len(a)+len(b)) - len(set(a+b))

    print result

while True:
    try:
        a = raw_input()
        b = raw_input()
        compareSubstring(a,b)
    except EOFError:
        break
