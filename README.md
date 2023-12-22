# Python-Palette-Swap
Python script that replaces colors in an image to the closest color in a custom palette via Pythagorean theorem on RGB color space.
### Libraries
Libraries used include:
Python math library
Pillow image library (Under the HPND lisence)

# Usage (v1.0)
Currently, usage is not ideal. The actual script must be edited to determine the file to be edited, the name of the output file, and the color palette. This will be changed with version 2.0.
Additionally: There is no file conversion. Pillow operates primarialy with JPEG files, and most files of other types will result in errors when attempting to run this script. Some non-JPEG files do work, but this rare. It is recommended to convert the file before using this script. The addition of automatic file conversion in the script is planned for verison 2.0.

## Setting input file
Within the script, there is a variable called "Target", which by default has a value of "Input.jpg". This file can be edited to set the file you want to modify, or it can be left the same and the file itself can be renamed.

## Setting color palette
Setting the color palette is currently the most difficult part of the script. There are 3 tuples within the Python script relating to the color palette:
- R_Palette
- G_Palette
- B_Palette
The R_Palette tuple stores the red value of each color in the palette via RGB color space, G_Palette the green value, and so on. To change the color palette, write the RGB values of the color from the top tuple (red) to the bottom tuple (blue). This can be done as decimal (1, 2, 3, etc) integers, or hexadecimal (9, A, B, etc) integers. Hexadecimal is one of the easiest ways to set this, as if you know the hex-code for the color, simply use the first 2 digits for red, the second two digits for green, and the last two digits for blue. If there are 4 pairs (8) of digits, then simply ignore the last 2, as that is the alpha channel and is irrelevant for this script. By default, the script has 16 colors, though the variation in colors has shown to cause lacking detail. It is recommended to have at least 2 different shades of each color to help perserve detail, though no matter what some will be lost as you are reducing the variety of colors from 16 million down to a more easily countable number.

## Setting output file
Setting the output file is as simple as the input file. Within the script, there is a variable called "Output", with a default value of "Output.jpg". This can be changed to more easily rename the file, but it is recommended to have a different name than the input name. 

Now that everything is set, the script can be run. Assuming there are no errors that appear, the image will be processed and colors replaced to match the defined palette via Pythagorean 3D distance on the RGB color space. Conversion may take about a minute for larger files. The script will print "Finished!" to the console when it has finished applying the colors.

# Roadmap
A number of things are going to be changed for version 2.0.
- Comment the script to better explain what everything is doing
- Using more human-readable variable names
- Changing the script to use user-input on the console instead of requiring the script to be edited
- Adding automatic file conversion to make the script a more all-in-one script and easing use.
Version 2.0 will not release until these changes are complete.
