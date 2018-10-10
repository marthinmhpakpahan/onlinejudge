def bloggoShortcuts(text):
    counterA = -1 # handle _
    counterB = -1 # handle *
    result = ""

    for i in text:
        x = i
        if i == '_':
            counterA += 1
            i = "<i>" if counterA%2 == 0 else "</i>"
        if i == '*':
            counterB += 1
            i = "<b>" if counterB%2 == 0 else "</b>"
        result += i
    print result
while True:
    try:
        bloggoShortcuts(raw_input())
    except EOFError:
        break
