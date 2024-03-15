feet_inches = input("Enter Feet and inches: ")


def convert(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inch = float(parts[1])

    meter = feet * 0.3048 + inch * 0.0254
    return meter


result = convert(feet_inches)

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use the slide.")
