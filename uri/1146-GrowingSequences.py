while True:
    i = input()
    if i == 0:
        break
    s = ""
    for a in range(1, i+1):
        if s != "":
            s += " "
        s += str(a)
    print s