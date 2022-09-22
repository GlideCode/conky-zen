#
# Hex Color Coding to RGB 0xaarrgg format
#
#
# September, 2022
#

# Definition of the function hex_to_rgb
def hex_to_rgb(hex_color):
    hex_color = hex_color.replace(" ", "").replace("#", "")
    # 3-digits hex color
    if len(hex_color) == 3:
        r = hex_color[0] * 2
        g = hex_color[1] * 2
        b = hex_color[2] * 2
    # 6-digits hex color
    elif len(hex_color) == 6:
        r = hex_color[0:2]
        g = hex_color[2:4]
        b = hex_color[4:6]
    else:
        return "length error"
    # convert hex to decimal
    r = int(r, 16)
    g = int(g, 16)
    b = int(b, 16)
    # check if in range 0~255
    assert 0 <= r <= 255
    assert 0 <= g <= 255
    assert 0 <= b <= 255
    # write rgb in correct syntax
    rgb_color = "rgb({0},{1},{2})".format(r, g, b)
    return rgb_color


# Variable to define the input color
hex_input = '#453e67'
# Calling of the variable
RGB_output = hex_to_rgb(hex_input)
# Prints output
print('RGB result is:{0}'.format(RGB_output))
