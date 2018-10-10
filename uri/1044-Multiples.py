text = raw_input()

arr = text.split(" ")
a = int(arr[0])
b = int(arr[1])

r = 0
if a > b:
    r = a%b
else:
    r = b%a

print "Sao Multiplos" if r == 0 else "Nao sao Multiplos"
