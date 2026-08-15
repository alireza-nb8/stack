import stack

def main():
    stack.init('stack1')
    stack.init('bot_stack')
    stack.init('manager_stack')

    stack.push('stack1', 56)
    stack.push('stack1', 3)

    stack.push('bot_stack', 100)
    stack.push('bot_stack', 105)
    stack.push('bot_stack', 232)

    stack.push('manager_stack', 1)

    assert stack.pop('bot_stack') == 232
    assert stack.pop('bot_stack') == 105

    assert stack.pop('stack1') == 3

    assert stack.pop('manager_stack') == 1
    assert stack.pop('manager_stack') == None

    assert stack.pop('salam') == None
    stack.push('salam', 45)
    assert stack.pop('salam') == None

    stack.init('salam')
    stack.push('salam', 98)
    assert stack.pop('salam') == 98

main()

