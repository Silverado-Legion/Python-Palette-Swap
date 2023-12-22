from PIL import Image
import math

def Dist_3D(x1, y1, z1, x2, y2, z2):
    return math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2) + pow(z2 - z1, 2))

Target = "Input.jpg"
Output = "Output.jpg"

Im = Image.open(Target)
R_Palette = (0xFF, 0xFF, 0xFF, 0xFF, 0x32, 0x28, 0x00, 0x87, 0x41, 0x80, 0xFF, 0xDC, 0x8B, 0xA9, 0xD3, 0x00)
G_Palette = (0x4F, 0xD7, 0x8C, 0xA0, 0xCD, 0x8B, 0xCE, 0xCE, 0x69, 0x00, 0x69, 0x14, 0x45, 0xA9, 0xD3, 0x00)
B_Palette = (0x4F, 0x00, 0x00, 0x7A, 0x32, 0x22, 0xD1, 0xEB, 0xE1, 0x80, 0xB4, 0x3C, 0x13, 0xA9, 0xD3, 0x00)

I_W, I_H = Im.size

for y in range(I_H):
    for x in range(I_W):
        old_dist = float('inf')
        new_dist = 0
        C_T = 0

        P_X = Im.getpixel((x, y))
        for i in range(len(R_Palette)):
            new_dist = Dist_3D(P_X[0], P_X[1], P_X[2], R_Palette[i], G_Palette[i], B_Palette[i])
            if old_dist > new_dist:
                old_dist = new_dist
                C_T = i
            
        Im.putpixel((x, y), (R_Palette[C_T], G_Palette[C_T], B_Palette[C_T]))

Im.save(Output)
print("Finished!")