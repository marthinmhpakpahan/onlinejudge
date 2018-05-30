a = raw_input()

aArr = a.split(" ")

a1 = int(aArr[0])
a2 = int(aArr[1])
a3 = int(aArr[2])

print "{} eh o maior".format(a1 if a2 < a1 > a3 else a2 if a1 < a2 > a3 else a3)
