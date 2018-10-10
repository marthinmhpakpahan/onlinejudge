n = int(input())

for i in range(n):
    text = raw_input()
    a = text.split(" ")[0]
    b = text.split(" ")[1]

    if len(b) > len(a):
        print "nao encaixa"
    elif a[len(a)-len(b):] == b:
        print "encaixa"
    else:
        print "nao encaixa"
