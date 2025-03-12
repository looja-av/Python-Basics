def celsius_to_fahrenheit(celsius_values):
    return [(c * 9/5) + 32 for c in celsius_values]

def fahrenheit_to_celsius(fahrenheit_values):
    return [(f - 32) * 5/9 for f in fahrenheit_values]

def main():
    print("Temperature Convetor is here")
    print("1. Convert Celsius to  Fahrenheit")
    print("2.Convert Fahrenheit to Celsius")

    choice=input("Enter your choice,(1 or 2)")

    temperature=list(map(float,input("Enter the temperature with a space").split()))

    if choice=="1":
        convert=celsius_to_fahrenheit(temperature)
        print("Converted Temperature", convert)

    if choice=="2":
        convert=fahrenheit_to_celsius(temperature)
        print("Converted Temperature:", convert)

if __name__=="__main__":
    main()