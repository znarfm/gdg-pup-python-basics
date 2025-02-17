# Create a list of integers.
numbers: list[int] = list(range(5, 0, -1))
print(f"List: {numbers}")

# Add an element to the list.
numbers.append(6)
print(f"List after adding a number: {numbers}")

# Remove an element from the list.
numbers.remove(3)
print(f"List after removing an element: {numbers}")

# Sort the list in ascending order.
numbers.sort()
print(f"List after sorting: {numbers}")
