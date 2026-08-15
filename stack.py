stack = {}

def init(name):
    stack[name] = []
    #return stack[name]


def push(name , x):
    if name in stack:
        stack[name].append(x)
        return stack
    else:
        return 	None

def pop(name):
    if name in stack:
        if stack[name]:
            last_index = stack[name][-1]
            del stack[name][-1]
            return last_index
        else:
            return None
    else:
        return None
