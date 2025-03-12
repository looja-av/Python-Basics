def celsius_to_fahrenheit(celsius_values):
    return[(c*9/5)+ 32 for c in celsius_values]

def fahrenheit_to_celsius(fahrenheit_values):
    return[(f-32)*5/9 for f in fahrenheit_values]

def main():
    print("Temperature Converter")
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius")

    choice= input("Enter you choice(1 or 2): ")

#map helps to put all the integers into float while split makes the integers converted to small substrings in order to make it readable 
    temperatures= list(map(float,input("Enter temperatures separated by space:").split()))


    if choice=='1':
        converted= celsius_to_fahrenheit(temperatures)
        print("Converted Temperatures (F):" , converted)
    else:
        converted=fahrenheit_to_celsius(temperatures)
        print("Converted Temperature (C):" , converted)

if __name__== "__main__":
    main()




