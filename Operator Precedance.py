prec = {
    "$": 0,
    "a": 1,
    "b": 2,
    "g": 3,
}

stack = ['$']
flag = True
top = int(len(stack) - 1)
inp = input('Enter String: ')
inp = list(inp)                 # aba
for i in inp:
    # print(prec[i])
    # print(stack[top])
    try:
        if prec[stack[top]] < prec[i]:
            stack.append(i)
            top += 1
        else:
            stack.pop()
            stack.append(i)
    except:
        flag = False
    

print('String is accepted') if flag else print('String not accepted')
