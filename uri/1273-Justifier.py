c = 0
while True:
    n = input()

    if n == 0:
        break
    
    c += 1
    if c > 1 and n != 0:
        print ""

    arr = []
    max_len = 0
    for i in range(n):
        in_str = raw_input()
        arr += [in_str]
        if len(in_str) > max_len:
            max_len = len(in_str)

    for i in arr:
        print (max_len-len(i))*" "+i