# Convert Celsius to Fahrenheit
# Set up default values for variables
result = 0.0
temp_c = 0.0
temp_f = 0.0

# Prompt for Celsius
temp_c = float(input('Temperature in C? '))

# Convert Celsius to Fahrenheit
temp_f = (temp_c * (9 / 5)) + 32
result = f'{temp_f} F'

# Print result
print(result)