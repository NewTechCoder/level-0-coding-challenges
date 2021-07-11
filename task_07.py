def celsius_to_fahrenheit(celsuis):
    return (9/5 * celsuis) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

if __name__ == "__main__":
    print(celsius_to_fahrenheit(0))
    print(fahrenheit_to_celsius(32))
