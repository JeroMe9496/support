import os

# File name, mode
# Mods : r+
# https://www.programiz.com/python-programming/methods/built-in/open
f = open("file.txt", "r+")

# ADD TO THE FILE
br = "\n"
f.write("This is snake?" + br)


# STATISTICS
nline = 0
nwords = 0
nchars = 0

for line in f:
  
  line = line.strip("\n")

  words = line.split()

  # Line counting
  nline += 1

  # Word counting
  nwords += len(words)

  # Character counting
  nchars += len(line)

print(f"Number of lines: {nline}")
print(f"Number of words: {nwords}")
print(f"Number of chars: {nchars}")
print(f"\nNumber of lines: {len(f.readlines())}") # Seems to only work when the for loop doesn't exist, unsure why

# os.system("pause") # windows only ?

f.close()