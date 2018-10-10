def convert(text):
    converted = ""
    counter = 0
    for i in text:
        if (i >= 'A' and i <= 'Z') or (i >= 'a' and i <= 'z'):
            counter += 1
            if counter%2 == 1:
                converted += i.upper()
            else:
                converted += i.lower()
        else:
            converted += i

    print converted

while True:
    try:
        convert(raw_input())
    except EOFError:
        break
