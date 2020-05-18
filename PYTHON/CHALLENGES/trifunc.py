# Basic syntax for a function
def func(args):
  return args * 2

# We can make a list out of the arguments given using * before the argument
def func_arr(*args):
  for item in args:
    print(item)

# Also we can return a list of items instead of a single value
def func_mult_ret(arg):
  return [arg*1, arg*2, arg*4, arg*8]




# Practice
# -------------------------------------

# Create the stupid operator function
def stupid_operator(a, b):
  if isinstance(a, int) and isinstance(b, int):
    print(str(a)+str(b))
  elif isinstance(a, str) and isinstance(b, str):
    print(int(a)+int(b))
  else:
    print("False")

# Expected results
# stupid_operator("5", "4")  --> 9
# stupid_operator(8, 6)      --> "86"
# stupid_operator("2", 3)    --> False


# Returns true if the bridge is safe to walk on
s = "abcdef"
print(s.count("de"))

def is_safe_bridge(s):
  count = s.count(" ")
  return False if(count > 0) else True

def is_safe_bridge_compact(s):
	return not s.count(" ")




# Expected results
is_safe_bridge_compact("###")      # --> True
is_safe_bridge_compact("#######")  # --> True
is_safe_bridge_compact("### ##")   # --> False

print(is_safe_bridge('###'))


# There are 3 programmers, you've paid all 3 of them by hourly wage (arguments)
# return the difference between the most paid and least paid programmer
def programmers(one, two, three): 
	progs = [one, two, three]
	return max(progs) - min(progs)
# def programmers(*args): 
  # return max(args) - min(args)

# Expected results
# programmers(84, 50, 400)  --> 350
# programmers(354, 55, 21)  --> 333
# programmers(18, 136, 23)  --> 118