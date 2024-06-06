import os
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item, print_messages=True):
        self.items.append(item)
        if print_messages:
            print(f"Pushed {item} into the stack. Current stack: {self.items}")

    def pop(self, print_messages=True):
        if not self.is_empty():
            item = self.items.pop()
            if print_messages:
                print(f"Popped {item} from the stack. Current stack: {self.items}")
            return item
        else:
            if print_messages:
                print("Error: Stack is empty!")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Error: Stack is empty!")

    def size(self):
        return len(self.items)


def postfix_to_infix(postfix, print_messages=True):
    stack = Stack()
    if print_messages:
        print("Converting postfix to infix:")
        print("Postfix expression:", postfix)
    for char in postfix:
        if char.isalnum():
            stack.push(char, print_messages)
        else:
            operand2 = stack.pop(print_messages)
            operand1 = stack.pop(print_messages)
            expression = '(' + operand1 + char + operand2 + ')'
            stack.push(expression, print_messages)
    result = stack.pop(print_messages)
    if print_messages:
        print("Infix expression:", result)
    return result


def postfix_to_prefix(postfix, print_messages=True):
    stack = Stack()
    if print_messages:
        print("Converting postfix to prefix:")
        print("Postfix expression:", postfix)
    for char in postfix:
        if char.isalnum():
            stack.push(char, print_messages)
        else:
            operand2 = stack.pop(print_messages)
            operand1 = stack.pop(print_messages)
            expression = char + operand1 + operand2
            stack.push(expression, print_messages)
    result = stack.pop(print_messages)
    if print_messages:
        print("Prefix expression:", result)
    return result


def infix_to_postfix(infix_expression, print_messages=True):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    stack = Stack()
    if print_messages:
        print("Converting infix to postfix:")
        print("Infix expression:", infix_expression)
    for char in infix_expression:
        if char.isalnum():
            output.append(char)
        elif char == '(':
            stack.push(char, print_messages)
        elif char == ')':
            while not stack.is_empty() and stack.peek() != '(':
                output.append(stack.pop(print_messages))
            stack.pop(print_messages)  # Discard the '('
        else:
            while not stack.is_empty() and precedence.get(char, 0) <= precedence.get(stack.peek(), 0):
                output.append(stack.pop(print_messages))
            stack.push(char, print_messages)

    while not stack.is_empty():
        output.append(stack.pop(print_messages))

    result = ''.join(output)
    if print_messages:
        print("Postfix expression:", result)
    return result


def infix_to_prefix(infix_expression, print_messages=True):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    output = []
    stack = Stack()
    if print_messages:
        print("Converting infix to prefix:")
        print("Infix expression:", infix_expression)
    for token in infix_expression[::-1]:
        if token.isalnum():
            output.append(token)
        elif token == ')':
            stack.push(token, print_messages)
        elif token == '(':
            while not stack.is_empty() and stack.peek() != ')':
                output.append(stack.pop(print_messages))
            stack.pop(print_messages)  # Discard the ')'
        else:
            while not stack.is_empty() and precedence.get(token, 0) < precedence.get(stack.peek(), 0):
                output.append(stack.pop(print_messages))
            stack.push(token, print_messages)

    while not stack.is_empty():
        output.append(stack.pop(print_messages))

    result = ''.join(output[::-1])
    if print_messages:
        print("Prefix expression:", result)
    return result


def prefix_to_postfix(prefix_expression):
    stack = Stack()
    operators = set(['+', '-', '*', '/'])
    result = ''
    for char in reversed(prefix_expression):
        if char not in operators:
            stack.push(char)
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            expression = operand1 + operand2 + char
            stack.push(expression)
    result = stack.pop()
    return result


def prefix_to_infix(prefix, print_messages=True):
    stack = Stack()
    if print_messages:
        print("Converting prefix to infix:")
        print("Prefix expression:", prefix)
    for char in prefix[::-1]:
        if char.isalnum():
            stack.push(char, print_messages)
        else:
            operand1 = stack.pop(print_messages)
            operand2 = stack.pop(print_messages)
            expression = '(' + operand1 + char + operand2 + ')'
            stack.push(expression, print_messages)
    result = stack.pop(print_messages)
    if print_messages:
        print("Infix expression:", result)
    return result


# Example usage
infix_expression = "(A+B)*C-D"
postfix_expression = infix_to_postfix(infix_expression)
prefix_expression = infix_to_prefix(infix_expression)
os.system('cls')
print("\n\n\nInfix expression:", infix_expression)
print("Postfix expression:", postfix_expression)
print("Prefix expression:", prefix_expression)


print("\n\n\nPostfix to Infix:\n")
postfix2infix = postfix_to_infix(postfix_expression)
print("\n\n\nPostfix to Prefix:\n")
postfix2prefix = postfix_to_prefix(postfix_expression)
print("\n\n\nPrefix to Infix:\n")
prefix2infix = prefix_to_infix(prefix_expression)
print("\n\n\nPrefix to Postfix:\n")
prefix2postfix = prefix_to_postfix(prefix_expression)
print("\n\n\nIntfix to Postfix:\n")
infix2postfix = infix_to_postfix(infix_expression)
print("\n\n\nInfix to Prefix:\n")
infix2prefix = infix_to_prefix(infix_expression)

print("\n\n\nPostfix expression from infix:", infix2postfix)
print("Postfix expression from prefix:", prefix2postfix)
print("Prefix expression from postfix:", postfix2prefix)
print("Prefix expression from infix:", infix2prefix)
print("Infix expression from prefix:", prefix2infix)
print("Infix expression from postfix:", postfix2infix)
