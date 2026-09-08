from stack import Stack

S1 = Stack("stack1")
S1.push(9)
S1.push(8)
S1.push(7)
S2 = Stack("stack2")
assert S1.pop() == 7
S2.push(6)
S2.push(5)
S2.push(4)
print(S2.pop())



