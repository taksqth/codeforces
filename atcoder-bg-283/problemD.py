def solve():
    s = input()

    stack = []
    box = set()
    for el in s:
        if el == '(':
            stack.append('(')
        elif el == ')':
            while stack[-1] != '(':
                box.remove(stack.pop())
            stack.pop()
        else:
            if el in box:
                print('No')
                return
            stack.append(el)
            box.add(el)
    print('Yes')

solve()