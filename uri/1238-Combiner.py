N = input()

for i in range(N):
    S = raw_input()
    A = S.split(" ")[0]
    B = S.split(" ")[1]

    M = max(len(A), len(B))

    R = ""
    for i in range(M):
        if i < len(A):
            R += A[i]
        if i < len(B):
            R += B[i]

    print R