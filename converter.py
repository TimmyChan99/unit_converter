# Convert length
length_unit_to_meter = {
    'meter': 1,
    'millimeter': pow(10, -3),  # 1 mm = 0.001 meters
    'centimeter': pow(10, -2),  # 1 cm = 0.01 meters
    'kilometer': pow(10, 3),    # 1 km = 1000 meters
    'inch': 0.0254,             # 1 inch = 0.0254 meters
    'foot': 0.3048,             # 1 foot = 0.3048 meters
    'yard': 0.9144,             # 1 yard = 0.9144 meters
    'mile': 1609.34             # 1 mile = 1609.34 meters
}

def is_valid_unit(unit):
    return unit in length_unit_to_meter

def convert_to_meter(value, unit):
    return value * length_unit_to_meter[unit]

def convert_to_unit(value, from_unit, to_unit):
    # Convert to meters first, then to the desired unit
    value_in_meter = convert_to_meter(value, from_unit)
    return round(value_in_meter / length_unit_to_meter[to_unit], 4)

def get_valid_unit(prompt):
    while True:
        unit = input(prompt).lower().strip()
        if is_valid_unit(unit):
            return unit
        print(f"'{unit}' is not a valid unit. Please try again.")

def get_valid_float(prompt):
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Main Program
print("Welcome to the Length Converter!")
print("Available units: " + ", ".join(length_unit_to_meter.keys()))

length_value = get_valid_float('Enter length: ')
convert_from = get_valid_unit(f"Choose unit to convert from (e.g., meter, inch): ")
convert_to = get_valid_unit(f"Choose unit to convert to (e.g., kilometer, yard): ")

result = convert_to_unit(length_value, convert_from, convert_to)
print(f"{length_value} {convert_from} is equal to {result} {convert_to}.")

# Convert temperature
