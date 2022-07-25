import os
class Stack:
    def __init__(self, size):
        self.items = []
        self.size = size

    def is_empty(self):
        # Write code here
        if len(self.items)==0:
            return true
        else:
            return false

    def is_full(self):
        # Write code here
        if len(self.items)>100:
            return true
        else :
            retrun false
            
              
    def push(self, data):
        if not self.is_full():
            # Write code here
            items.append(data)
            return (self.items)
               

    def pop(self):
        if not self.is_empty():
            # Write code here
            items .pop()
            return (self.items)

    def status(self):
        # Write code here
        while true: 
            return stack 
        
        

# Do not change the following code
size, queries = map(int, input().rstrip().split())
stack = Stack(size)
for line in range(queries):
    values = list(map(int, input().rstrip().split()))
    if values[0] == 1:
        stack.push(values[1])
    elif values[0] == 2:
        stack.pop()
stack.status()
