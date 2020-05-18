# for loop - will stop once x goes through all the values of range() or an array, range being a function that makes an array of numbers
"""
for x in range(5):
  print(x)

print("")

# while loop - will stop once a reaches the same value as b
a = 3
b = 8
while (a != b):
  print("Still true!")
  a += 1

print("")

## break & continue statements
# break will exit any kind of loops
count = 0
while True:
  print(count)
  count += 1
  if count >= 3:
    break

print("")

# whereas continue will skip the current loop and go back to the for or while statement
for x in range(12):
  # Checking if x is an even number
  if x % 2 == 0:
    continue
  print(x)

print("")
"""

# Loops
# -------------------

# While
condition = True
while(condition):
  print("True!")
else:
  print("Not True anymore...")

