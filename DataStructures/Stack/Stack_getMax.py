# You have an empty sequence, and you will be given  queries. Each query is one of these three types:
#
# 1 x  -Push the element x into the stack.
# 2    -Delete the element present at the top of the stack.
# 3    -Print the maximum element in the stack.
# Function Description
#
# Complete the getMax function in the editor below.
#
# getMax has the following parameters:
# - string operations[n]: operations as strings
#
# Returns
# - int[]: the answers to each type 3 query
#
# Input Format
#
# The first line of input contains an integer, . The next  lines each contain an above mentioned query.
#
# Constraints
#
# Constraints
#
#
#
# All queries are valid.
#
# Sample Input
#
# STDIN   Function
# -----   --------
# 10      operations[] size n = 10
# 1 97    operations = ['1 97', '2', '1 20', ....]
# 2
# 1 20
# 2
# 1 26
# 1 20
# 2
# 3
# 1 91
# 3
# Sample Output
#
# 26
# 91
#
# #

def getMax(operations):
    class Stack:
        def __init__(self):
            self.items = []
            self.max_element = None  # Initialize to None

        def isEmpty(self):
            return self.items == []

        def push(self, item):
            self.items.append(item)
            # Update max_element if necessary
            if self.max_element is None or item > self.max_element:
                self.max_element = item

        def pop(self):
            if self.isEmpty():
                print("Error: Stack underflow")
                return None
            popped_item = self.items.pop()
            # Update max_element if the popped item was the current maximum
            if popped_item == self.max_element:
                self.max_element = max(self.items, default=None)  # Find new max efficiently
            return popped_item

        def peek(self):
            if self.isEmpty():
                print("Error: Stack underflow")
                return None
            return self.items[-1]

    stack = Stack()
    type3 = []

    for operation in operations:
        op = int(operation.split()[0])  # Extract the operation type (1, 2, or 3)

        if op == 1:
            value = int(operation.split()[1])  # Extract the value to push
            stack.push(value)
        elif op == 2:
            stack.pop()
        elif op == 3:
            if stack.isEmpty():
                type3.append(-1)  # Append -1 for empty stack on type 3 query
            else:
                type3.append(stack.max_element)

    return type3