import os

print("This script will change file case type that are in the same directory\n")

ext = input("Which file extension (without dot): ")

def camel_to_snake(path = os.getcwd()):
  for file in os.listdir(path):
    namechange = file

    for letter in file:
      if letter.isupper():
        upp = letter
        low = letter.lower()
        namechange = namechange.replace(upp, f"_{low}")

    if file.endswith(f".{ext}"):
      os.rename(file, namechange)
      print(f"{file} --> {namechange}")

def snake_to_camel():
  for file in os.listdir():
    namechange = file

    for letter in file:
      if letter.islower():
        low = letter
        upp = letter.upper()
        namechange = namechange.replace(f"_{low}", upp)

    if file.endswith(f".{ext}"):
      os.rename(file, namechange)
      print(f"{file} --> {namechange}")

prompt = input("What do you want? camel or snake: ")
print("")
print("List of changed files:")

if prompt == "camel":
  snake_to_camel()

elif prompt == "snake":
  camel_to_snake()

print("\nChanges done!")
# os.system("Pause")