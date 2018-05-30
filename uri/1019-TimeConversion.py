a = int(input())

h = a/3600
a = a%3600 if a >= 3600 else a
m = a/60
a = a%60
s = a

print "{}:{}:{}".format(h,m,s)
