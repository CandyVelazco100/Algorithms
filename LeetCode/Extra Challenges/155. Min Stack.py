Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.

class MinStack:
    
    def __init__(self):
        # Initialize the main stack and a stack to keep track of the minimum values
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        # Push the value onto the main stack
        self.stack.append(val)
        # If min_stack is empty or the current value is less than or equal to the top of min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        # Pop the value from the main stack
        if self.stack:
            val = self.stack.pop()
            # If the popped value is the same as the top of the min_stack, pop from min_stack as well
            if self.min_stack and val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        # Return the top value from the main stack
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        # Return the top value from the min_stack (the current minimum)
        return self.min_stack[-1] if self.min_stack else None
