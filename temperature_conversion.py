def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def main():
    choice = input("Enter 'C' for Celsius to Fahrenheit conversion or 'F' for Fahrenheit to Celsius conversion: ").upper()

    if choice == 'C':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius:.2f} degree Celsius is equal to {fahrenheit:.2f} degree Fahrenheit.")
    elif choice == 'F':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit:.2f} degree Fahrenheit is equal to {celsius:.2f} degree Celsius.")
    else:
        print("Invalid choice. Please enter 'C' or 'F'.")

if __name__ == "__main__":
    main()
