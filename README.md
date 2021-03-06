# Keypirinha-Units
A unit conversion plugin for KeyPirinha

# Install

Download the `Units.keypirinha-package` file and move it to the `InstalledPackage` folder located at:

* `Keypirinha\portable\Profile\InstalledPackages` in **Portable mode**

**Or** 

* `%APPDATA%\Keypirinha\InstalledPackages` in **Installed mode** 

  The final path would look like `C:\Users\%USERNAME%\AppData\Roaming\Keypirinha\InstalledPackages`

# Usage

It can take three formats:
### Quick Convert:

`x Units`

Returns units that go hand-in-hand with the input.

Acceptable Inputs:
- Liters -> Gallons
- Gallon -> Liters
- Mile -> Kilometer
- Kilometer -> Mile
- Feet -> Inches
- Inches -> Millimters
- Millimeters -> Inches
- Degrees -> Radians
- Radians -> Degrees

### 4 Words:
`x Units to Units`

Converts from the input Unit to the output unit, and multiplies by x.
- ex: "5 gal to milliliters" = "18927.053 Milliliters"

### 3 Words:
`x Units Units`

Converts from the input Unit to the output unit, and multiplies by x without the word "to" [which can actually be any word]

`Units to Units`

Converts the units without a multiplier.

# Convertable Units: 
[Can only convert between things of the same category. e.g `gal to qrt`]

Liquids:

- "gal", "gallon", "gallons", "quart", "quarts", "qrt", "pint", "pints", "cup", "cups", "floz", "tablespoon", "tablespoons", "tbsp", "teaspoon", "teaspoons", "tsp", "kiloliter", "kiloliters", "kl", "liter", "liters", "l", "li",

Distances:

- "milliliter", "milliliters", "ml", "mile", "miles", "mi", "foot", "feet", "ft", "inch", "inches", "in", "kilometer", "kilometers", "km", "meter", "meters", "m", "centimeter", "centimeters", "cm", "millimeter", "millimeters", "mm",

Angles:	

- "degree", "degrees", "deg", "radian", "radians", "rad"
