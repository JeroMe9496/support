# LISTS
# ==================================================================
# Ordered collection of one or more data items (any type) using square brackets
# https://www.programiz.com/python-programming/methods/list
# https://www.programiz.com/python-programming/list

arr = ["monkey", "dog", "snake", "zebra", "cricket"]
# print("original array: ", arr)


# Append one item to the list
# arr.append("horse")
# print("after append: ", arr)


# Remove the last item
# arr.pop() # removes the last item
# print("after pop: ", arr)


# Remove one item by index
# arr.pop(2) # removes the 2nd index (snake)
# print("after pop index: ", arr)


# Remove one item by index starting at the end
# arr.pop(-1) # removes the last item from the end (cricket)
# print("after pop index end: ", arr)


# Remove one item by value
# arr.remove("dog")
# print("after remove: ", arr)


# Insert to a specific index
# arr.insert(2, "giraffe")
# print("after insert: ", arr)


# Return the length of an array
# print( len(arr) )

# Printing the array
# print(arr)


# Sorting the array in alphabetical order (default is in ascending order)
# arr.sort()
# arr.sort(reverse=True)
# print(arr)


# Returning the number of elements found with specified value
# print( arr.count("snake") )


# Extend a list (by adding another list)
# arr_2 = ["chicken, ruster, duck, pig"]
# arr.extend(arr_2)
# print(arr)


# Get the max and min values in an array
# arr_nums = [52, 12, 87, -54, 154, -3, 23]
# max_val = max(arr_nums)
# min_val = min(arr_nums)
# print("max value: ", max_val)     # 154
# print("min value: ", min_val)     # -54





# TUPLES
# ==================================================================
# Immutable, ordered collection of one or more data items (any type) using parentheses
tup_a = ("tree", "car", "apple")

# Same as above. It's the comma who creates the tuple, not the paranthesis
tup_b = "tree", "car", "apple"    

# print("tuple a: ", tup_a)
# print(tup_a[1])

# print("tuple b: ", tup_b)
# print(tup_b[1])


# Cannot add/remove/change to/from a tuple
# tup_b.append("chicken") # → error
# tup_b.pop()             # → error


# Add to the tuple: have to convert-it into a list first!
# tup_a = list(tup_a)     # convert to list
# tup_a.append("bob")     # add to the list
# tuple(tup_a)            # convert to tuple
# print("after add: ", tup_a)





# DICTIONARIES
# ==================================================================
# Unordered collection of data (any type) in a key:value pair form
dic = {
  "firstname":  "George",
  "name":       "Marigold",
  "age":        57,
  "job":        "Marksman"
}
# print("dictionary: ", dic)
# print("dictionary key: ", dic["name"])


# Changing Dictionary Elements

# Update value
dic['age'] = 27
# print(dic)


# Add item
dic['address'] = 'Downtown'
# print(dic)


# Remove item
# dic.pop("job")
# print(dic)
