n = input()

for i in range(n):
    ni = input()

    sm = 0
    for j in range(ni):
        nj = raw_input()
        
        for k in range(len(nj)):
            ok = ord(nj[k])
            sm += (ok-65) + j + k

    print sm