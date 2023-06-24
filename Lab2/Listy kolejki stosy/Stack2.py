from Stack import Stack


def pairChecker(symbolStr):
    s = Stack()
    balanced = True
    index = 0

    while index < len(symbolStr) and balanced:
        symbol = symbolStr[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        index += 1

    return balanced and s.isEmpty()


print(pairChecker("(()()()())"))
print(pairChecker("())))))"))
print(pairChecker("(()()()())"))
