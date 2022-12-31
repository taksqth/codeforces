# Without any bad expression handling
def convert_infix_to_postfix(tokens):
    precedence = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
        "^": 3,
    }
    stack = []
    converted = []
    for token in tokens:
        if token.isnumeric():
            converted.append(token)
        elif token == "(":
            stack.append(token)
        elif token == ")":
            while stack[-1] != "(":
                converted.append(stack.pop())
            stack.pop()
        else:
            while (
                len(stack) > 0
                and stack[-1] != "("
                and precedence[stack[-1]] >= precedence[token]
            ):
                converted.append(stack.pop())
            stack.append(token)
    while len(stack) > 0:
        converted.append(stack.pop())
    return converted


print(
    convert_infix_to_postfix(
        [
            "2",
            "+",
            "32",
            "^",
            "2",
            "-",
            "4",
            "+",
            "(",
            "2",
            "-",
            "4",
            "*",
            "5",
            "/",
            "3",
            ")",
        ]
    )
)
