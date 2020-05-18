# Basic conditions
a = 5
b = 5

"""
# Equal to
if ( a == b ): print("true!")

# Not equal to
if ( a != b ): print("false!")

# Less than & Less or equal than
if ( a < b ): print("false!")
if ( a <= b ): print("true!")

# Greater than & Greater or equal than
if ( a > b ): print("false!")
if ( a >= b ): print("true!")

# And / Or

# Requires one of both conndition to be True
if (a == b or a < b): print("true!")

# Requires both conndition to be True
if (a == b and a < b): print("false!")
"""



# Practice
# -------------------------------------

c = 2
d = 5
e = 8

if c == d:
  print("A")
  if d > c:
    print("B")
  else:
    print("C")
elif e >= d:
  print("D")
  if c < e:
    print("F")
  else:
    print("G")
else:
  print("E")

# What should be expected the result?
# ...