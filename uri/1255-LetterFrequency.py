N = input()

for i in range(N):
    iN = raw_input();
    iN = iN.lower()

    d = {}
    m = 0
    for j in iN:
        if (97 <= ord(j) <= 122):
            if j not in d:
                d[j] = 1
            else:
                d[j] += 1

            if d[j] > m:
                m = d[j]

    R = ""
    for j in d:
        if d[j] == m:
            R += j
    print "".join(sorted(R))