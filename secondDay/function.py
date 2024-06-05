# how to create a function in python
# syntax:

# def functionName():
#     code block
#     code block

# Example:


def addTwoNumbers():
      a = 5
      b = 6
      c = a + b
      print(c)

# calling the function
# addTwoNumbers() 
# output: 11

# Example 2:
def addTwoNum(a, b):
      c = a + b
      print(c)

# calling the function
# addTwoNum(5, 5)

# Example 3:

def sum(a,b,c):
      s = a + b + c
      return s

# calling the function
# mind = sum(5, 5, 5)
# print(mind)
print(sum(5, 5, 5)) # output: 15