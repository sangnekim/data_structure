def checkBrackets(statement):
    stack = Stack()
    for ch in statement:
        if ch in ('{','[','('):
            stack.push(ch)
        elif ch in ('}', ']',')'):
            if stack.isEmpty():
                return False     #조건 2 위반
            else:
                left = stack.pop()
                if (ch == '}' and left != '{') or\
                    (ch == ']' and left != '[') or\
                    (ch == ')' and left != '('):
                    return False   #조건 3 위반

    return stack.isEmpty() #False 이면 조건 1위반
