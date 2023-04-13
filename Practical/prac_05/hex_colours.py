COLOR_CODES = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Aquamarine": "#7fffd4",
    "Azure": "#f0ffff",
    "Beige": "#f5f5dc",
    "Bisque": "#ffe4c4",
    "Black": "#000000",
    "BlanchedAlmond": "#ffebcd",
    "Blue": "#0000ff"
}

while True:
    color_name = input("Enter a color name (or blank to quit): ").lower()
    if not color_name:
        break

    try:
        color_code = COLOR_CODES[color_name.capitalize()]
        print(f"The code for {color_name.capitalize()} is {color_code}")
    except KeyError:
        print(f"{color_name.capitalize()} is not a valid color name")
