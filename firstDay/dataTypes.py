# data Types in Python
# Python has the following data types built-in by default, in these categories:
# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# Getting the Data Type
# You can get the data type of any object by using the type() function:
# Example
x = 5
print(type(x))
# Output: <class 'int'>

x = "Hello World"
print(type(x))
# Output: <class 'str'>

y = 6.6 
print(type(y))
# Output: <class 'float'>

z = 1j
print(type(z))
# Output: <class 'complex'>

a = ["apple", "banana", "cherry"]
print(type(a))
# Output: <class 'list'>

b = ("apple", "banana", "cherry")
print(type(b))
# Output: <class 'tuple'>

c = range(6)
print(type(c))
# Output: <class 'range'>

d = {"name" : "John", "age" : 36}
print(type(d))
# Output: <class 'dict'>

e = {"apple", "banana", "cherry"}
print(type(e))
# Output: <class 'set'>

f = frozenset({"apple", "banana", "cherry"})
print(type(f))
# Output: <class 'frozenset'>

g = True
print(type(g))
# Output: <class 'bool'>

h = b"Hello"
print(type(h))
# Output: <class 'bytes'>

i = bytearray(5)
print(type(i))
# Output: <class 'bytearray'>

j = memoryview(bytes(5))
print(type(j))

# Output: <class 'memoryview'>

# Setting the Data Type
# In Python, the data type is set when you assign a value to a variable:
# Example
x = "Hello World" # str
x = 20 # int
x = 20.5 # float
x = 1j # complex
x = ["apple", "banana", "cherry"] # list
x = ("apple", "banana", "cherry") # tuple
x = range(6) # range
x = {"name" : "John", "age" : 36} # dict
x = {"apple", "banana", "cherry"} # set
x = frozenset({"apple", "banana", "cherry"}) # frozenset
x = True # bool
x = b"Hello" # bytes
x = bytearray(5) # bytearray
x = memoryview(bytes(5)) # memoryview



