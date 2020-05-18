# DOCUMENTATION
# ==================================================================
# https://www.programiz.com/python-programming/variables-datatypes




# NUMBERS
# ==================================================================
# region

# INTEGER: Positive or negative whole number (without decimals)
a = 5


# FLOAT: Positive or negative number with decimals
b = 5.38


# Type Conversion
# ------------------------------------
# Forcing a value to be an int, ex. a = "5" --> int(a) --> 5
a_string = int("5")       # 5
a_float = int(2.32)       # 2
# print("String to int: ", type(a_string))
# print("Float to int: ", type(a_float))

# Forcing a value to be a float, ex. a = "5.38" --> float(a) --> 5.38
b_string = float("5.38")  # 5.38
b_int = float(5)          # 5.0
# print("String to float: ", type(b_string))
# print("Int to float: ", type(b_int))

# endregion




# STRINGS
# ==================================================================
# region

# Single or collection of characters packed in single, double or triple quotes
s = "This is a string"

ss = '''
A multiline
string
'''

# print(f)
# print(ff)


# String methods
# ------------------------------------------
# https://www.programiz.com/python-programming/methods/string


# Count occurences of certains patterns :
# print("Empty spaces:", s.count(" "))


# A string is a list (sequence) of characters
# print("Get the first letter:", s[0])


# Length of a string
# print("The length of the string:", len(s))


# Multiply a string
# print("Hell" + "o" * 5)


# Split a string → return a list with string items
split_word = list("python")     # split a word with list()
# print(split_word)           

split_str_1 = s.split()         # default is splitting at space " "
split_str_2 = s.split('i')      # split at a specific letter "i"
split_str_3 = s.split('i', 1)   # split at a specific letter "i" + how many instances
# print("split default: ", split_str_1)
# print("split with letter 'i': ", split_str_2)
# print("split with letter 'i' once: ", split_str_3)



# Change case
str_capit = "this is a string".capitalize()
# print(str_capit)

str_title = "this is a string".title()
# print(str_title)

str_upper = "this is a string".upper()
# print(str_upper)

str_lower = "This IS A String".lower()
# print(str_lower)

str_replace = "this is a dog".replace("dog", "cat")
# print(str_replace)


# Concatenate. ☝ With the "+" sign you can concatenate only strings
name = "John"
age = 27

concat_1 = name + " is " + str(age) + " years old"  # using plus → have to convert numbers to strings!
concat_2 = "{} is {} years old".format(name, age)   # using placeholders {}
concat_3 = f"{name} is {age} years old"             # using f-strings f"". Nice one!

# print(concat_1)
# print(concat_2)
# print(concat_3)

# endregion




# BOOLEANS & NULLS
# ==================================================================
# region
# Data being one of the two built-in values True or False (case sensitive)
c = True
d = False


# Declare a variable with a None value (equivalent of NULL in other languages)
# Object that denotes the lack of value
e = None

# endregion




# SEQUENCES (or COLLECTIONS)
# ==================================================================
# region
# Python have many ways to do "array like" collections


# LISTS → []
# ------------------------------------------
# region
# Mutable, ORDERED collection of data items (any type)
# When you want a simple array with indexes
# https://www.programiz.com/python-programming/list

l = [0, 1, 2, 3, 4, 5]
# print("list: ", l)
# print(l[3])

l[0] = 54
# print("list after change: ", l)

# endregion



# DICTIONARY → {}
# ------------------------------------------
# region
# Mutable, UNORDERED collection of data of any type in a "key: value" pair form
# When you want freedom and flexibility

d = {
  "surname":  "George",
  "name":     "Marigold",
  "age":      57,
  "job":      "Marksman"
}
# print("dictionary: ", d)
# print(d["name"])

# endregion



# TUPLES → ()
# ------------------------------------------
# region
# Immutable, ORDERED collection of data items (any type)
# When you want a "fixed" list of items or keep values unchanged
# https://www.programiz.com/python-programming/tuple

t = ("tree", "car", "apple")
# print("tuple: ", t)
# print(t[1])

t_mix = ("tree", 23, [52, "Mary"], "apple", False)
# print("tuple mix [3]: ", t_mix[3])

# t_mix[1] = 22 # error → cannot change value in a tuple

# endregion



# SET → {}
# ------------------------------------------
# region
# Immutable, UNORDERED collection of unique items
# When you want to avoid duplicates or/and keep values unchanged
# Like in math, the order is not important
# Usually used with loops
# https://www.programiz.com/python-programming/set

# set of integers
s = {1, 2, 3}
# print("set: ", s)
# print(s[1]) # error → you cannot use index in a set, it's unordered

# set of mixed datatypes
s_mix = {1.0, "Hello", (1, 2, 3)}
# print("set mix: ", s_mix)

s_order = {5,8,1,2,3,3,3,3,4,5}
# print("nice order: ", s_order)  # numbers in order and duplicates removed !

s_rand = {"Marcel", "Jasmine", "James", "Mary", "Mary", "Dolores"}
# print("random order: ", s_rand)  # duplicates removed but the strings are displayed RANDOMLY

# for x in s_rand:
#   print(x)

# endregion

# endregion SEQUENCES
