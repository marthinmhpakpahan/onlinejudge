N = input()

for i in range(N):
    S = raw_input()
    iN = input()

    R = ""
    for j in S:
        oj = ord(j)
        rs = oj-iN
        if 90 >= oj >= 65:
            if rs < 65:
                rs = 90-iN+(oj-64)
        elif 122 >= oj >= 97:
            if rs < 97:
                rs = 122-iN+(oj-96)

        R += chr(rs)
    
    print R
    