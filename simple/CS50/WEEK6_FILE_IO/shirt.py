import sys
from PIL import Image, ImageOps

# Set the valid file formats
valform = (".jpg", ".jpeg", ".png")

# Checks argv length
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

# Checks input and output files' format
if not sys.argv[1].endswith(valform) and not sys.argv[2].endswith(valform):
    sys.exit("Invalid Output")  

# Checks if the input and output have the same file format
if sys.argv[1].split(".")[1] != sys.argv[2].split(".")[1]:
    sys.exit("Input and output have different extensions")

# Opens the img to be stacked to another img
stack_img = Image.open("shirt.png")
output_name = sys.argv[2]

# Main Logic
try:
    with Image.open(sys.argv[1]) as im:
        im = ImageOps.fit(image=im, size=(600,600))
        im.paste(stack_img, mask=stack_img)
        im.save(output_name)

except FileNotFoundError:
    sys.exit("Input does not exist")
