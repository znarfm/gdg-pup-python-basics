# Create a dictionary with initial key-value pairs.
contact_list: dict = {
    "name": "Sparky",
    "age": 25,
}
print(f"Original dictionary: {contact_list}")

# Add a new key-value pair.
contact_list["city"] = "New York"
print(f"Dictionary after adding an item: {contact_list}")

# Update an existing key-value pair.
contact_list["age"] += 1
print(f"Dictionary after updating an item: {contact_list}")

# Remove a key-value pair
contact_list.pop("age")
print(f"Dictionary after removing an item: {contact_list}")
