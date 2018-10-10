n = input()

for i in range(n):
    ni = raw_input()
    t = ""
    for j in range(len(ni)):
        if j == 0 and ni[j] != ' ':
            t += ni[j]
        else:
            if ni[j] != ' ':
                if ni[j-1] == ' ':
                    t += ni[j]
    print t
