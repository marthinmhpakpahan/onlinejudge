ar = [4.00, 4.50, 5.00, 2.00, 1.50]

a = raw_input()

arr = a.split(" ")

a1 = int(arr[0])
a2 = int(arr[1])

print "Total: R$ %.2f" % (ar[a1-1]*a2)
