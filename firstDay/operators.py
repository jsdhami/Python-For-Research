# Operators In Python
# Operators are used to perform operations on variables and values.
# Python divides the operators in the following groups:
# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators

# Arithmetic Operators
# Arithmetic operators are used with numeric values to perform common mathematical operations:
# Operator	Name	Example
# +	Addition	x + y
# -	Subtraction	x - y
# *	Multiplication	x * y
# /	Division	x / y
# %	Modulus	x % y
# **	Exponentiation	x ** y
# //	Floor division	x // y

# Examples
x = 5
y = 3
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

# Assignment Operators
# Assignment operators are used to assign values to variables:
# Operator	Example	Same As
# =	       x = 5	 x = 5
# +=	       x += 3	 x = x + 3
# -=	       x -= 3	 x = x - 3
# *=	       x *= 3	 x = x * 3
# /=	       x /= 3	 x = x / 3
# %=	       x %= 3	 x = x % 3
# //=	      x //= 3	 x = x // 3
# **=	      x **= 3	 x = x ** 3
# &=	       x &= 3	 x = x & 3
# |=	       x |= 3	 x = x | 3
# ^=	       x ^= 3	 x = x ^ 3
# >>=	      x >>= 3	 x = x >> 3
# <<=	      x <<= 3	 x = x << 3

# Examples
x = 5
x += 3
print(x)
x -= 3
print(x)
x *= 3
print(x)
x /= 3
print(x)
x %= 3
print(x)
x //= 3
print(x)
x **= 3
print(x)
x = 5
x &= 3
print(x)
x |= 3
print(x)

# Comparison Operators
# Comparison operators are used to compare two values:
# Operator	Name	Example
# ==	     Equal	x == y
# !=	     Not equal	x != y
# >	     Greater than	x > y
# <	     Less than	x < y
# >=	     Greater than or equal to	x >= y
# <=	     Less than or equal to	x <= y

# Examples
x = 5
y = 3
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

# Logical Operators
# Logical operators are used to combine conditional statements:
# Operator	Description	Example
# and 	Returns True if both statements are true	x < 5 and  x < 10
# or	Returns True if one of the statements is true	x < 5 or x < 4
# not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)

# Examples
x = 5
print(x < 5 and x < 10)
print(x < 5 or x < 4)
print(not(x < 5 and x < 10))

# Identity Operators
# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
# Operator	Description	Example
# is 	Returns True if both variables are the same object	x is y
# is not	Returns True if both variables are not the same object	x is not y  

# Examples
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
print(x is y)
print(x == y)
print(x is not z)

# Membership Operators
# Membership operators are used to test if a sequence is presented in an object:
# Operator	Description	Example
# in	Returns True if a sequence with the specified value is present in the object	x in y
# not in	Returns True if a sequence with the specified value is not present in the object	x not in y

# Examples
x = ["apple", "banana"]
print("banana" in x)
print("pineapple" not in x)

# Bitwise Operators
# Bitwise operators are used to compare (binary) numbers:
# Operator	Name	Description
# & 	AND	Sets each bit to 1 if both bits are 1
# |	OR	Sets each bit to 1 if one of two bits is 1
# ^	XOR	Sets each bit to 1 if only one of two bits is 1
# ~ 	NOT	Inverts all the bits
# <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
# >>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

# Examples
x = 5
y = 3
print(x & y)
print(x | y)
print(x ^ y)
print(~x)
print(x << y)
print(x >> y)

# Python Collections (Arrays)
# There are four collection data types in the Python programming language:
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered and unindexed. No duplicate members.
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.




