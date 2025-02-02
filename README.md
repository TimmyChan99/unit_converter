# Unit Converter

A simple unit conversion tool that supports both **GUI (Tkinter)** and **CLI (Command Line Interface)** modes for converting **length, weight, and temperature** units.

## Features
- Convert between different **length**, **weight**, and **temperature** units.
- GUI mode with **Tkinter**.
- CLI mode with **interactive prompts**.
- Handles invalid input gracefully.

## Installation
Ensure you have Python 3 installed. Clone or download this repository and navigate to its directory.

```sh
# Clone the repository (if applicable)
git clone https://github.com/TimmyChan99/unit_converter.git
cd unit-converter
```

## Usage

### GUI Mode
Run the following command to start the Tkinter-based GUI:

```sh
python3 gui.py
```

### CLI Mode
Run the following command to use the command-line interface:

```sh
python3 converter.py
```

### Example (CLI)
```
Welcome to the Unit Converter!
Select your converter (length, temperature, weight): length
Enter the value to convert: 10
Choose the unit to convert from (meter, millimeter, centimeter, kilometer, inch, foot, yard, mile): meter
Choose the unit to convert to (meter, millimeter, centimeter, kilometer, inch, foot, yard, mile): inch
10 meter is equal to 393.701 inches.
```

## Files Overview
- **gui.py** → Runs the graphical Tkinter-based unit converter.
- **converter.py** → Provides the command-line interface and conversion logic.


