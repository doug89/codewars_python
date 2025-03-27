"""
RGB To Hex Conversion
5 kyu
https://www.codewars.com/kata/513e08acc600c94f01000001/train/python

The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal
 representation being returned. Valid decimal values for RGB are 0 - 255.
 Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.
Examples (input --> output):

255, 255, 255 --> "FFFFFF"
255, 255, 300 --> "FFFFFF"
0, 0, 0       --> "000000"
148, 0, 211   --> "9400D3"


"""



def rgb(r,g,b):
    colours = [hex(min(255, max(0, colour)))[2:].upper() for colour in (r,g,b)]
    colours = ["0" + colours[i] if len(colours[i]) == 1 else colours[i] for i in range(len(colours))]
    return "".join(colours)

# def rgb(r,g,b):
#     colours = [min(255, max(0, colour)) for colour in (r,g,b)]
#     colours = [hex(colour)[2:].upper() for colour in colours]
#     colours = ["0" + colours[i] if len(colours[i]) == 1 else colours[i] for i in range(len(colours))]
#     return "".join(colours)

# def rgb(r,g,b):
#     colours = [r,g,b]
#     for i, colour in enumerate(colours):
#         if colour < 0:
#             colours[i] = 0
#         if colour > 255:
#             colours[i] = 255
#     colours = [hex(colour)[2:].upper() for colour in colours]
#     for i, colour in enumerate(colours):
#         if len(colour) == 1:
#             colours[i] = "0" + colour
#     return "".join(colours)


# def rgb(*args):
#     binary_colours = (r, g, b)
#     for colour in binary_colours:
#         print(str(hex(colour))[2:].upper())

print(rgb(255,255,255))
print(rgb(0,0,0))
print(rgb(1,2,3))
print(rgb(-20, 275, 125))