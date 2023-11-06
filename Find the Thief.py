
string1 = input("")
string2 = input("")
# Convert the strings to lowercase and then into sets of characters
set1 = set(string1)
set2 = set(string2)

# Find the common elements between the two sets
common_elements = set1.intersection(set2)

# Convert the result back to a sorted list if needed
common_elements_list = sorted(list(common_elements))

# Print the common elements

print(len(common_elements_list))
