from stack import stack

s1 = stack("stack1")
s1.push(9)
s1.push(8)
s1.push(7)
s2 = stack("stack2")
assert s1.pop() == 7
s2.push(6)
s2.push(5)
s2.push(4)
print(s2.pop())



