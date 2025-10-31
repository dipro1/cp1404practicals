COLOUR_NAME_TO_CODE = {
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

for name in COLOUR_NAME_TO_CODE:
    print(f"{name.title()} ")

colour_name = input("Enter a colour name: ").strip()
while colour_name != "":
    if colour_name in COLOUR_NAME_TO_CODE:
        print(f"{colour_name} is {COLOUR_NAME_TO_CODE[colour_name]}")
    else:
        print("Invalid name")
    colour_name = input("Enter a colour name: ").strip()