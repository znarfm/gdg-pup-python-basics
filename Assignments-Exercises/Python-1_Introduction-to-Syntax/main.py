# This program explores Python syntax, variables, data types, and basic operators.

# 1. Declare variables of different types
name: str = "Meinard"  # string
age: int = 21        # integer
height: float = 180     # float
is_student: bool = True  # boolean

# 2. Perform basic arithmetic operations
sum_result: float = age + height
product_result: float = age * height

# 3. Concatenate strings and display outputs
greeting: str = "Hello, " + name + "!"
print(greeting)

# 4. Display results of arithmetic operations
print("Sum of age and height:", sum_result)
print("Product of age and height:", product_result)

# 5. Display the types of each variable
print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of height:", type(height))
print("Type of is_student:", type(is_student))
