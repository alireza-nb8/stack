import stack 

def main():
    stack.nl("ali")
    stack.nl('hamid')
    stack.push('ali',12)
    stack.push('ali',13)
    stack.push(98)

    assert stack.pop() == 98
    assert stack.pop() == 13


main()