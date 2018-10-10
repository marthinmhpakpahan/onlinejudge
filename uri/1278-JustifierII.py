c = 0
while True:
    n = input()

    if n == 0:
        break
    
    c += 1
    if c > 1 and n != 0:
        print ""

    arr = []
    max_len = 0
    for i in range(n):
        in_str = raw_input()
        in_str = in_str.strip()
        temp = ""

        for x in in_str:
            # print temp, x
            if temp == "" and x != " ":
                temp += x
                continue
            if temp != "":
                if x == " ":
                    if temp[-1] != " ":
                        temp += x
                else:
                    temp += x
        temp = temp.strip()
        arr += [temp]
        if len(temp) > max_len:
            max_len = len(temp)

    for i in arr:
        print (max_len-len(i))*" "+i