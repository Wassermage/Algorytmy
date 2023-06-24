from Stack import Stack


def solveRPN(expression):
    s = Stack()

    for element in expression:
        if element.isdigit():
            s.push(int(element))
        else:
            
            operand2 = s.pop()            
            operand1 = s.pop()            

            result = eval(f'{operand1} {element} {operand2}')
    
            s.push(result)

    return s.peek()

print(solveRPN("25+"))
print(solveRPN("25-"))
print(solveRPN("25*"))
print(solveRPN("25/"))
print(solveRPN("73+52-*"))