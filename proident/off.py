# Example dictionary
my_dict = {'a': 1, 'b': 2}

# Data to be appended
new_data = {'c': 3}

# Check if the data exists and then append to the dictionary
if new_data:
    my_dict.update(new_data)

print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}
