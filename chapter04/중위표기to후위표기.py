def precedence(op): #연산자의 우선순위 반환
    if op == '(' or op ==')':
        return 0
    elif op == '+' or op =='-':
        return 1
    elif op == '*' or op == '/':
        return 2
    else:
        return -1

def Infix2Postfix(expr):
    s = Stack()
    output = []
    for term in expr:
        if term in '(':
            s.push('(')
        elif term in ')':          #왼쪽 괄호가 나올 때 까지 스택에서 연산자를 꺼내 출력
            while not s.isEmpty():
                op = s.pop()
                if op == '(':
                    break
                else:
                    output.append(op)
        elif term in '+-*/':       #연산자이면 우선순위가 높거나 같은 연산자를 스택에서 모두 꺼내 출력
            while not s.isEmpty():
                op = s.peek()
                if (precedence(term) <= precedence(op)):
                    output.append(op)
                    s.pop()
                else:
                    break
            s.push(term)         #마지막으로 현재 연산자 스택에 삽입
        else:                    #피연산이면 바로 출력
            output.append(term)

    while not s.isEmpty():      #처리가 끝났으면 스택에 남은 항목을 모두 출력
        output.append(s.pop())

    return output
