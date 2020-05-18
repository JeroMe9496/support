a = 5
b = 5
c = "5"

# Equal to
# if ( a == b ): print("true!")


# Not equal to
# if ( a != b ): print("false!")


# Less than & Less or equal than
# if ( a < b ): print("false!")
# if ( a <= b ): print("true!")


# Greater than & Greater or equal than
# if ( a > b ): print("false!")
# if ( a >= b ): print("true!")


# And / Or

# Requires one of both connditions to be True
# if (a == b or a < b): print("true!")

# Requires both conditions to be True
# if (a == b and a < b): print("false!")


# Strict equality is native. '==' or 'is' will check also if values are the same type

if a is c:
  print("is : checking if 'a' is exactly the same as 'c'!")
elif a == c:
  print("== : checking if 'a' is exactly the same as 'c'!")
else:
  print("values are not the same")


# You can get the type of any value using this native function
val = 5.4
type_v = type(val)
print( type_v )

if type_v == int or type_v == float:
  print("Is a number!")
elif type_v == int:
  print("Is an integer!")
elif type_v == float:
  print("Is a float!")
elif type_v == str:
  print("Is a string!")
elif type_v == list:
  print("Is a list!")
elif type_v == list:
  print("Is a list!")


# Or using this function that returns True/False instead of the type
# Instead of this :
if type_v == int or type_v == float:
  print("val is an integer OR a float!")

# You could use this
if isinstance(val, (int, float)): 
  print("val is an integer OR a float!")

if isinstance(val, float): 
  print("val is a float!")
else: 
  print("val is not a float!")