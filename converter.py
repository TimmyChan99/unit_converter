# Conversion dictionaries
length_unit_to_meter = {
    'meter': 1,
    'millimeter': 1e-3,    # 1 mm = 0.001 meters
    'centimeter': 1e-2,    # 1 cm = 0.01 meters
    'kilometer': 1e3,      # 1 km = 1000 meters
    'inch': 0.0254,        # 1 inch = 0.0254 meters
    'foot': 0.3048,        # 1 foot = 0.3048 meters
    'yard': 0.9144,        # 1 yard = 0.9144 meters
    'mile': 1609.34        # 1 mile = 1609.34 meters
}

temperature_to_kelvin = {
    'kelvin': lambda t: t,                          # Kelvin stays the same
    'celsius': lambda t: t + 273.15,               # Celsius to Kelvin
    'fahrenheit': lambda t: (t - 32) * 5 / 9 + 273.15  # Fahrenheit to Kelvin
}

weight_to_gram = {
    'gram': 1,                 # 1 gram = 1 gram
    'kilogram': 1e3,           # 1 kilogram = 1000 grams
    'milligram': 1e-3,         # 1 milligram = 0.001 grams
    'microgram': 1e-6,         # 1 microgram = 0.000001 grams
    'tonne': 1e6,              # 1 tonne = 1,000,000 grams
    'pound': 453.592,          # 1 pound = 453.592 grams
    'ounce': 28.3495,          # 1 ounce = 28.3495 grams
    'stone': 6350.29           # 1 stone = 6350.29 grams
}

# Dictionary to validate unit categories
available_converters = {
    'length': length_unit_to_meter,
    'temperature': temperature_to_kelvin,
    'weight': weight_to_gram
}

# Function to validate and return the conversion type
def get_conversion_type():
    while True:
        converter = input(f"Select your converter ({', '.join(available_converters.keys())}): ").lower().strip()
        if converter in available_converters:
            return converter
        print(f"'{converter}' is not a valid converter. Please choose from {list(available_converters.keys())}.")

# Function to validate and return a valid unit
def get_valid_unit(converter, prompt):
    valid_units = available_converters[converter].keys()
    while True:
        unit = input(f"{prompt} ({', '.join(valid_units)}): ").lower().strip()
        if unit in valid_units:
            return unit
        print(f"'{unit}' is not a valid unit for {converter}. Please try again.")

# Function to validate and return a valid numeric input
def get_valid_float(prompt):
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Conversion logic

# Convert length from one unit to another
def convert_length(value, from_unit, to_unit):
    value_in_meters = value * length_unit_to_meter[from_unit]  # Convert to meters
    return round(value_in_meters / length_unit_to_meter[to_unit], 4)  # Convert to target unit

# Convert weight from one unit to another
def convert_weight(value, from_unit, to_unit):
    value_in_grams = value * weight_to_gram[from_unit]  # Convert to grams
    return round(value_in_grams / weight_to_gram[to_unit], 4)  # Convert to target unit

# Convert temperature from one unit to another via Kelvin.
def convert_temperature(value, from_unit, to_unit):
    # Convert from source unit to Kelvin
    value_in_kelvin = temperature_to_kelvin[from_unit](value)
    # Convert from Kelvin to target unit
    if to_unit == 'kelvin':
        return round(value_in_kelvin, 2)
    elif to_unit == 'celsius':
        return round(value_in_kelvin - 273.15, 2)
    elif to_unit == 'fahrenheit':
        return round((value_in_kelvin - 273.15) * 9 / 5 + 32, 2)


if __name__ == '__main__':
    # Main Program
    print("Welcome to the Unit Converter!")

    # Step 1: Choose the conversion type
    conversion_type = get_conversion_type()

    # Step 2: Get user inputs
    value = get_valid_float(f"Enter the value to convert: ")
    from_unit = get_valid_unit(conversion_type, "Choose the unit to convert from")
    to_unit = get_valid_unit(conversion_type, "Choose the unit to convert to")

    # Step 3: Perform the conversion
    if conversion_type == 'length':
        result = convert_length(value, from_unit, to_unit)
    elif conversion_type == 'weight':
        result = convert_weight(value, from_unit, to_unit)
    elif conversion_type == 'temperature':
        result = convert_temperature(value, from_unit, to_unit)

        # Step 4: Display the result
    print(f"{value} {from_unit} is equal to {result} {to_unit}.")
