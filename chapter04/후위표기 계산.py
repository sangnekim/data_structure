def evalPostfifx(expr):
    s = Stack()
    for token in expr:
        if token in "+-*/": #항목이 연산자이면 연산 수행 -> 결과 저장
            val2 = s.pop()
            val1 = s.pop()
            if (token == '+'):
                s.push(val1 + val2)
            elif (token == '-'):
                s.push(val1 - val2)
            elif (token == '*'):
                s.push(val1 * val2)
            elif (token == '/'):
                s.push(val1 / val2)
        else:               #항목이 피연산자이면 실수로 변경해서 스택에 저장
            s.push(float(token))

    return s.pop()
