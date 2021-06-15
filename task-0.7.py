def celsius_to_fahrenheit_converter(x):
    fahrenheit = (x * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius_converter(y):
    celsius = (y - 32) * 5/9
    return celsius

print(celsius_to_fahrenheit_converter())
print(fahrenheit_to_celsius_converter())
