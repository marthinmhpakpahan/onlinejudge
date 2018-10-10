N = input()

for i in range(N):
    iN = raw_input()
    A = int(iN.split(" ")[0])
    B = int(iN.split(" ")[1])
    X = len(str(A**B))
    print X