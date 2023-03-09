"""
File: mirror_lake.py
Name: Ian
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: str, the file path of the original image.
    :return: SimpleImage, mirror image.
    """
    reflect_img = SimpleImage(filename)
    b_img = SimpleImage.blank(reflect_img.width, reflect_img.height * 2)
    for x in range(reflect_img.width):
        for y in range(reflect_img.height):
            color_p = reflect_img.get_pixel(x, y)

            blank1_p = b_img.get_pixel(x, y)
            blank2_p = b_img.get_pixel(x, ((reflect_img.height * 2) - 1) - y)

            blank1_p.red = color_p.red
            blank1_p.green = color_p.green
            blank1_p.blue = color_p.blue

            blank2_p.red = color_p.red
            blank2_p.green = color_p.green
            blank2_p.blue = color_p.blue
    return b_img


def main():
    """
    This program will generate a mirror image.
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
