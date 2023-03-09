"""
File: fire.py
Name: Ian
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    :param filename: str, the file path of the original image.
    :return: SimpleImage, fire location with red and other are gray scale.
    """
    fire_img = SimpleImage(filename)
    for x in range(fire_img.width):
        for y in range(fire_img.height):
            fire_p = fire_img.get_pixel(x, y)
            avg = (fire_p.red + fire_p.green + fire_p.blue) / 3
            if fire_p.red > (avg * HURDLE_FACTOR):
                fire_p.red = 255
                fire_p.green = 0
                fire_p.blue = 0
            else:
                fire_p.red = avg
                fire_p.green = avg
                fire_p.blue = avg
    return fire_img


def main():
    """
    This program is to find the fire location.
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
