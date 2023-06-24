from Stack import Stack


opening_chars = ["(", "[", "{", "<"]
closing_chars = [")", "]", "}", ">"]


def pairChecker(symbolStr):
    s = Stack()
    balanced = True
    index = 0

    while index < len(symbolStr) and balanced:
        symbol = symbolStr[index]
        if symbol in opening_chars:
            s.push(symbol)
        elif symbol in closing_chars:
            if s.isEmpty():
                balanced = False
            elif opening_chars.index(s.peek()) == closing_chars.index(symbol):
                s.pop()
        index += 1

    return balanced and s.isEmpty()


print(pairChecker("(()()()())"))
print(pairChecker("())))))"))
print(pairChecker("[<>(){}()]"))
