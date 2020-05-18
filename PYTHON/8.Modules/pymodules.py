# BUILT-IN MODULES
# ==================================================================
# region

# A module is an external python file that can have any kind of data
# This could allow us to make a module with functions we oftenly use
# Or have constants we use often, or both!


# Modules are either:
# BUILT-IN: They're in the python installation folder
# LOCAL: They're local to the script file we're running


# Here's a few built-in modules:
# datetime    
# os
# sys
# math



# IMPORT: Getting a module
# ----------------------------------------------
import math


# ALIAS: Re-naming a module using an alias
# ----------------------------------------------
import math as m


# ☝
# We can list all available functions and variables inside a module using dir(name_of_the_module):
# print( dir(m) )


# Using a function from the math module
# ----------------------------------------------
mf = m.floor(5.45)
# print(mf)




# FROM: When using modules, we won't necessarily use all of its contents
# Though we'll need recall our import to get another function or variable
# ----------------------------------------------
from math import ceil                   # import only the ceil() function
from math import floor                  # import only the floor() function
from random import randrange, uniform   # import only the randrange() and uniform() functions


mc = ceil(5.45)
# print(mc) # output 6

mf = floor(5.45)
# print(mf) # output 6


# randrange gives you an integral value
irand = randrange(0, 10)
# print(irand)

# uniform gives you a floating-point value
frand = uniform(0, 10)
# print(frand)

# endregion




# CUSTOM MODULES
# ==================================================================
# region

# Creating our own module(s):
# Create a new python file, its name will be the module name (i.e. mod.py)
# ----------------------------------------------
# Import all the contents of your file
import mod

# Import only the hello() function
# from mod import hello


# Use the contents like this
# print(mod.hello("Sorin"))
# print(mod.PI)


# Or, create a schortcut for a function
printus = mod.printus
# printus("Seba", 5, 8, "sssss"*8 + "nek", 5)

# endregion




# EXAMPLES - DATE and TIME
# ==================================================================
# region
# https://www.programiz.com/python-programming/datetime/strftime
# https://strftime.org/



# USING time module
# ------------------------------------------
# region

import time

# Local time → A list of valibles containing time related values
local = time.localtime()

# print(local) # → tm_year=2020, tm_mon=5, tm_mday=17, tm_hour=12, tm_min=28, tm_sec=19, tm_wday=6, tm_yday=138, tm_isdst=1

# Using the valiables :
# print(local.tm_year)
# print(local.tm_month)
# print(local.tm_hour)

# current_time = time.strftime("%H:%M:%S", local) # add %p to show AM/PM time

# A "wait a little" kind of function
# time.sleep(4)
# print("Printed after 4 seconds.")


# Run a basic countdown using time.sleep()
"""
counter = 5
end = 0

while counter >= end:
  # print(counter)
  print(counter, end="", flush=True)  # arguments "end" and "flush" → to remove newlines
  print("\r", end="", flush=True)     # arguments → keeps the same spot
  counter -= 1
  time.sleep(1)
"""

# Run a basic digital clock in the python shell using time.strftime() and time.sleep()
# https://stackoverflow.com/a/37515630
# Use this to stop the clock (using "while True:" will be an infinite loop)
counter = 1
end = 5

while counter <= end:
  clock = time.strftime("%H:%M:%S")
  # clock = f"{local.tm_hour}:{local.tm_min}:{local.tm_sec}"

  # print(clock)
  print(clock, end="", flush=True)
  print("\r", end="", flush=True)

  counter += 1

  time.sleep(1)

# endregion



# USING date module
# ------------------------------------------
# region

from datetime import date

# Complete date with default formatting
current = date.today()
# print(current)
# print(current.year)
# print(current.month)
# print(current.day)


# A function who make use of date module
def calc_age(birthyear):
  year = current.year
  return year - birthyear

# print( calc_age(1966) ) # expected result --> 54

# endregion



# USING datetime module
# ------------------------------------------
# region
from datetime import datetime

# Complete datetime with default formatting
now = datetime.now()
# print(now)

# print( now.strftime("%Y") ) # Year full
# print( now.strftime("%y") ) # Year short

# print( now.strftime("%B") ) # Month literal
# print( now.strftime("%m") ) # Month decimal

# print( now.strftime("%w") ) # Weekday decimal
# print( now.strftime("%A") ) # Weekday literal
# print( now.strftime("%a") ) # Weekday literal short

# print( now )
# print ( now.strftime("%H:%M:%S") )
# endregion


# endregion DATE and TIME
