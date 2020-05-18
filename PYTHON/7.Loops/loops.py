# LOOPS
# ==================================================================
# A loop statement allows us to execute a statement or group of statements multiple times.
# This allows us to do repeated tasks in a controlled manner

# Alternatively, if we want a specific amount of loops
# We can use range(num)
for x in range(10):
  print(x)


# WHILE: This loop repeats the executing the code while the condition remains true
a = 3
b = 8
# while (a != b):
#   print("Still true!")
#   a += 1


# FOR: This loop is used to go through a list (array) of items
# x is a placeholder name that will be replaced with the item of an array
list_of_items = [5, 8, "Hello", 7]
# for item in list_of_items:
#   print(item)



# LOOP CONTROL STATEMENTS
# ==================================================================
# BREAK: will exit the current loop entirely
# count = 1
# while True:
#   if count <= 10:
#     print(count)
#     count += 1
#   else:
#     break
  




# CONTINUE: will skip the current loop and start the next loop
# for x in range(12):
#   # Checking if x is an even number
#   if x % 2 == 0:
#     continue
#   print(x)




# MISCELLANEOUS
# ==================================================================
# ELSE: This can be used to execute code when the loop finishes
y = 0
# while(y):
#   y+=1
# else:
#   print("Work done!")