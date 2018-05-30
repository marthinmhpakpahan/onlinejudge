n = int(input())

led = [2,5,5,4,5,6,3,7,6,6]
res = []

for i in range(n):
    num = raw_input()
    sum = 0
    for i in range(len(num)):
        sum += led[int(num[i])-1]
    res.append(sum)

for i in res:
    print "{} leds".format(i)
