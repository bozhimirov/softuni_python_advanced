expression = input()
s = []
for i in range(len(expression)):
    ch = expression[i]
    if ch == '(':
        s.append(i)
    elif ch == ')':

        startindex = s.pop()
        endindex = i
        print(expression[startindex:endindex + 1])
