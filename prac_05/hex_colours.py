COLOUR_CODES = {
    "Absolute Zero": "#0048ba",
    "Acid Green": "#b0bf1a",
    "AliceBlue": "#f0f8ff",
    "Alizarin Crimson": "#e32636",
    "Amaranth": "#e52b50",
    "Amber": "#ffbf00",
    "Amethyst": "#9966cc",
    "AntiqueWhite": "#faebd7",
    "AntiqueWhite1": "#ffefdb",
    "AntiqueWhite2": "#eedfcc"
}

for colour, code in COLOUR_CODES.items():
    print(f"{colour} ")

colour_name = input("Enter a colour name: ").upper()
while colour_name != "":
    if colour_name in COLOUR_CODES:
        print(f"{colour_name} is {COLOUR_CODES[colour_name]}")
    else:
        print("Invalid name")
    colour_name = input("Enter a colour name: ").upper()
