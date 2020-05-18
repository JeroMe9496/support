# BUILD-IN FUNCTIONS
# ==================================================================
# region
# https://docs.python.org/3.8/library/functions.html


# ☝ Good to know
# We can create "shortcuts" of functions :
p = print
# p("Hello")


# PRINT FUNCTION
# ------------------------------------------
# print("whatever")
# print("whatever", "and", "ever")
# print("label: ", [1,2,3,4,5])


# MAX, MIN, ROUND ...
# ------------------------------------------
# MAX
# print( max([11,85,4,325,44,8]) )  # -> 325

# MIN
# print( min([11,85,4,325,44,8]) )  # -> 4

# ROUND
# print( round(2.34566666, 2) )     # -> 2.35            #


# INPUT FUNCTION
# ------------------------------------------
# input_val = input("Please enter your birth year: ")
# calc = 2020 - int(input_val)
# print("Your age is: ", calc)
# ==================================================================
# endregion




# CUSTOM FUNCTIONS
# ==================================================================
# region
# Use the "def" keyword followed by a name
# https://www.programiz.com/python-programming/function

# BASIC SYNTAX
# ------------------------------------------
# region
# Basic syntax for a function
def func_basic(arg_1, arg_2):
  return arg_1 - arg_2

# print( func_basic(2020,  1966) )  # 54


# Using default values
def func_basic_defaults(arg_1=2020, arg_2=1966):
  return arg_1 - arg_2

# print( func_basic_defaults() )  # 54


# A custom print function
def printus(data):

  sep_line = '--------------------------------------'
  first_sep = "\n" + sep_line + "\n"  # \n is a break row
  last_sep = "\n" + sep_line

  # add end="" to remove empty lines
  print(first_sep, '→ ', data, last_sep, sep='')


# Test printus()
# printus("bob!")
# printus(58 * 2 + 31 / 4)
# ------------------------------------------
# endregion


# GLOBAL AND LOCAL SCOPES
# ------------------------------------------
# region
# Functions can "see" the global variables (unlike PHP but like JS)
bob = "Bobby"


def test_bob():
  print("global 'bob' var: ", bob)

# test_bob()

# ...HOWEVER...
# If you want to change the value of a global variable you have to use "global" (like in PHP)


def change_global():
  global bob
  bob = "Enough with Bob, let's call it 'Marcel'"
  return bob

# change_global() # call the function to change the value of bob
# print("global 'bob' is now: ", bob)
# ------------------------------------------
# endregion


# HOISTING
# ------------------------------------------
# region
# In Python there is no hoisting, you have to declare the function BEFORE calling it

# This throws an error, the function does not exist yet
# try_hosting()     # NameError: name 'try_hosting' is not defined

def try_hosting():
  print("Working ?")

# This will work fine, the function is declared above
# try_hosting()
# ------------------------------------------
# endregion


# THE REST PARAMETER SYMBOL *
# ------------------------------------------
# region
# Use "rest" parameter * to indicate that you want a list of parameters
def calc_age(*args):
  return args[0] - args[1]

# print(calc_age_variant(2020, 1966))


# You could use min/max functions to detect min/max values in the list of arguments
def calc_age_variant(*args):
  return max(args) - min(args)

# print(calc_age_variant(1966, 2020))


# Loop into arguments
def func_arr(*args):
  for item in args:
    print(item)

# func_arr(1, 2, 4, 88, 64, 465, 320)
# ------------------------------------------
# endregion
# ==================================================================
# endregion CUSTOM FUNCTIONS




# CUSTOM "LAMBDA" FUNCTIONS (anonymus functions)
# ==================================================================
# region
# For simple, one statement, one liner functions
# https://www.afternerd.com/blog/python-lambdas/
# No arguments
def nine(): return 3 * 3  # this is silly, you could do the same with a simple variable
# print(nine())

# One argument (x)


def double(x): return x * 2
# print(double(5))

# Multiple arguments (x, y, etc) and default values


def calculate(x=5, y=5, etc=0): return x * y + etc
# print(calculate())
# ==================================================================
# endregion
