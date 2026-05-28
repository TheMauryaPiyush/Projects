#Unit Converter 

#lenght units
def convert_length(value, from_unit, to_unit):
    meters = {
        "centimeter": 0.01,
        "meter": 1,
        "kilometer": 1000,
        "inch": 0.0254,
        "foot": 0.3048,
        "yard": 0.9144,
        "mile": 1609.34
    }

    return (value * meters[from_unit]) / meters[to_unit]

#weight units
def convert_weight(value, from_unit, to_unit):

    grams = {
        "milligram": 0.001,
        "gram": 1,
        "kilogram": 1000,
        "pound": 453.592
    }

    return ((value * grams[from_unit]) / grams[to_unit])

#temperature units
def convert_temperature(value, from_unit, to_unit):

    if from_unit == "Celsius":
        celsius = value

    elif from_unit == "Fahrenheit":
        celsius = (value - 32) * 5 / 9

    else:
        celsius = value - 273.15


    if to_unit == "Celsius":
        return celsius

    elif to_unit == "Fahrenheit":
        return ((celsius * 9 / 5) + 32)

    else:
        return (celsius + 273.15)


while True:

    print("\n===== UNIT CONVERTER =====")

    print("1. Length")
    print("2. Weight")
    print("3. Temperature")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":      #length selected

        print("\nLength Units:")
        print("centimeter")
        print("meter")
        print("kilometer")
        print("inch")
        print("foot")
        print("yard")
        print("mile")

        value = float(input("\nEnter value: "))

        from_unit = input("Convert from: ")
        to_unit = input("Convert to: ")

        result = convert_length(value, from_unit, to_unit)

        print(f"\nConverted Value = {round(result, 4)}")



    elif choice == "2":       #weight selected

        print("\nWeight Units:")
        print("milligram")
        print("gram")
        print("kilogram")
        print("ounce")
        print("pound")

        value = float(input("\nEnter value: "))

        from_unit = input("Convert from: ")
        to_unit = input("Convert to: ")

        result = convert_weight(value, from_unit, to_unit)

        print(f"\nConverted Value = {round(result, 4)}")



    elif choice == "3":       #temperature selected

        print("\nTemperature Units:")
        print("Celsius")
        print("Fahrenheit")
        print("Kelvin")

        value = float(input("\nEnter value: "))

        from_unit = input("Convert from: ")
        to_unit = input("Convert to: ")

        result = convert_temperature(value, from_unit, to_unit)

        print(f"\nConverted Value = {round(result, 4)}")


    elif choice == "4":      #Exiting the program
        print("\nThank You 😇")
        break

    else:
        print("\nInvalid Choice")
