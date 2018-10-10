n = int(input())

r = []

for i in range(n):
    text = raw_input()

    new_text = ""
    for j in text:
        # each uppercase or lowercase letter must be shifted three positions to the right
        if (j >= 'A' and j <= 'Z') or (j >= 'a' and j <= 'z'):
            new_text += chr(ord(j)+3)
        else:
            new_text += j

    # each line must be reversed
    reversed_text = new_text[::-1]

    updated_text = reversed_text[:len(reversed_text)/2]
    for j in range(len(reversed_text)/2, len(reversed_text)):
        _char = reversed_text[j]
        updated_text += chr(ord(_char)-1)

    r.append(updated_text)

for i in r:
    print i
