"""
File: blur.py
Name:
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: SimpleImage, original image.
    :return: SimpleImage, blur image,
    """
    # Todo: create a new blank img that is as big as the original one
    new_img = SimpleImage.blank(img.width, img.height)

    # Loop over the picture
    for x in range(img.width):
        for y in range(img.height):
            
            # Todo: get pixel of new_img at x,y

            # Belows are 9 conditions of pixel filling, depending on pixels' x,y orientation.
            
            if x == 0 and y == 0:
                # Get pixel at the top-left corner of the image.
                new_img.get_pixel(x, y).red = (img.get_pixel(x, y).red + img.get_pixel(x+1, y).red + img.get_pixel(x, y+1).red + img.get_pixel(x+1, y+1).red) / 4
                new_img.get_pixel(x, y).green = (img.get_pixel(x, y).green + img.get_pixel(x+1, y).green + img.get_pixel(x, y+1).green + img.get_pixel(x+1, y+1).green) / 4
                new_img.get_pixel(x, y).blue = (img.get_pixel(x, y).blue + img.get_pixel(x+1, y).blue + img.get_pixel(x, y+1).blue + img.get_pixel(x+1, y+1).blue) / 4

            elif x == (img.width - 1) and y == 0:
                # Get pixel at the top-right corner of the image.
                new_img.get_pixel(x, y).red = (img.get_pixel(x, y).red + img.get_pixel(x, y+1).red + img.get_pixel(x-1, y).red + img.get_pixel(x-1, y+1).red) / 4
                new_img.get_pixel(x, y).green = (img.get_pixel(x, y).green + img.get_pixel(x, y+1).green + img.get_pixel(x-1, y).green + img.get_pixel(x-1, y+1).green) / 4
                new_img.get_pixel(x, y).blue = (img.get_pixel(x, y).blue + img.get_pixel(x, y+1).blue + img.get_pixel(x-1, y).blue + img.get_pixel(x-1, y+1).blue) / 4

            elif x == 0 and y == (img.height - 1):
                # Get pixel at the bottom-left corner of the image
                new_img.get_pixel(x, y).red = (img.get_pixel(x, y).red + img.get_pixel(x+1, y).red + img.get_pixel(x, y-1).red + img.get_pixel(x+1, y-1).red) / 4
                new_img.get_pixel(x, y).green = (img.get_pixel(x, y).green + img.get_pixel(x+1, y).green + img.get_pixel(x, y-1).green + img.get_pixel(x+1, y-1).green) / 4
                new_img.get_pixel(x, y).blue = (img.get_pixel(x, y).blue + img.get_pixel(x+1, y).blue + img.get_pixel(x, y-1).blue + img.get_pixel(x+1, y-1).blue) / 4

            elif x == (img.width - 1) and y == (img.height - 1):
                # Get pixel at the bottom-right corner of the image
                new_img.get_pixel(x, y).red = (img.get_pixel(x, y).red + img.get_pixel(x, y-1).red + img.get_pixel(x-1, y).red + img.get_pixel(x-1, y-1).red) / 4
                new_img.get_pixel(x, y).green = (img.get_pixel(x, y).green + img.get_pixel(x, y-1).green + img.get_pixel(x-1, y).green + img.get_pixel(x-1, y-1).green) / 4
                new_img.get_pixel(x, y).blue = (img.get_pixel(x, y).blue + img.get_pixel(x, y-1).blue + img.get_pixel(x-1, y).blue + img.get_pixel(x-1, y-1).blue) / 4
 
            elif y == 0:
                # Get top edge's pixels (without two corners)
                new_img.get_pixel(x, y).red = (img.get_pixel(x, y).red + img.get_pixel(x-1, y).red + img.get_pixel(x+1, y).red + img.get_pixel(x, y+1).red + img.get_pixel(x-1, y+1).red + img.get_pixel(x+1, y+1).red) / 6
                new_img.get_pixel(x, y).green = (img.get_pixel(x, y).green + img.get_pixel(x-1, y).green + img.get_pixel(x+1, y).green + img.get_pixel(x, y+1).green + img.get_pixel(x-1, y+1).green + img.get_pixel(x+1, y+1).green) / 6
                new_img.get_pixel(x, y).blue = (img.get_pixel(x, y).blue + img.get_pixel(x-1, y).blue + img.get_pixel(x+1, y).blue + img.get_pixel(x, y+1).blue + img.get_pixel(x-1, y+1).blue + img.get_pixel(x+1, y+1).blue) / 6

            elif y == (img.height - 1):
                # Get bottom edge's pixels (without two corners)
                new_img.get_pixel(x, y).red = (img.get_pixel(x, y).red + img.get_pixel(x-1, y).red + img.get_pixel(x+1, y).red + img.get_pixel(x, y-1).red + img.get_pixel(x+1, y-1).red + img.get_pixel(x-1, y-1).red) / 6
                new_img.get_pixel(x, y).green = (img.get_pixel(x, y).green + img.get_pixel(x-1, y).green + img.get_pixel(x+1, y).green + img.get_pixel(x, y-1).green + img.get_pixel(x+1, y-1).green + img.get_pixel(x-1, y-1).green) / 6
                new_img.get_pixel(x, y).blue = (img.get_pixel(x, y).blue + img.get_pixel(x-1, y).blue + img.get_pixel(x+1, y).blue + img.get_pixel(x, y-1).blue + img.get_pixel(x+1, y-1).blue + img.get_pixel(x-1, y-1).blue) / 6

            elif x == 0:
                # Get left edge's pixels (without two corners)
                new_img.get_pixel(x, y).red = (img.get_pixel(x, y).red + img.get_pixel(x, y-1).red + img.get_pixel(x, y+1).red + img.get_pixel(x+1, y).red + img.get_pixel(x+1, y-1).red + img.get_pixel(x+1, y+1).red) / 6
                new_img.get_pixel(x, y).green = (img.get_pixel(x, y).green + img.get_pixel(x, y-1).green + img.get_pixel(x, y+1).green + img.get_pixel(x+1, y).green + img.get_pixel(x+1, y-1).green + img.get_pixel(x+1, y+1).green) / 6
                new_img.get_pixel(x, y).blue = (img.get_pixel(x, y).blue + img.get_pixel(x, y-1).blue + img.get_pixel(x, y+1).blue + img.get_pixel(x+1, y).blue + img.get_pixel(x+1, y-1).blue + img.get_pixel(x+1, y+1).blue) / 6

            elif x == (img.width - 1):
                # Get right edge's pixels (without two corners)
                new_img.get_pixel(x, y).red = (img.get_pixel(x, y).red + img.get_pixel(x, y-1).red + img.get_pixel(x, y+1).red + img.get_pixel(x-1, y).red + img.get_pixel(x-1, y-1).red + img.get_pixel(x-1, y+1).red) / 6
                new_img.get_pixel(x, y).green = (img.get_pixel(x, y).green + img.get_pixel(x, y-1).green + img.get_pixel(x, y+1).green + img.get_pixel(x-1, y).green + img.get_pixel(x-1, y-1).green + img.get_pixel(x-1, y+1).green) / 6
                new_img.get_pixel(x, y).blue = (img.get_pixel(x, y).blue + img.get_pixel(x, y-1).blue + img.get_pixel(x, y+1).blue + img.get_pixel(x-1, y).blue + img.get_pixel(x-1, y-1).blue + img.get_pixel(x-1, y+1).blue) / 6

            else:
                # Inner pixels.
                new_img.get_pixel(x, y).red = (img.get_pixel(x, y).red + img.get_pixel(x-1, y).red + img.get_pixel(x+1, y).red + img.get_pixel(x-1, y-1).red + img.get_pixel(x, y-1).red + img.get_pixel(x+1, y-1).red + img.get_pixel(x-1, y+1).red + img.get_pixel(x, y+1).red + img.get_pixel(x + 1, y+1).red) / 9
                new_img.get_pixel(x, y).green = (img.get_pixel(x, y).green + img.get_pixel(x-1, y).green + img.get_pixel(x+1, y).green + img.get_pixel(x-1, y-1).green + img.get_pixel(x, y-1).green + img.get_pixel(x+1, y-1).green + img.get_pixel(x-1, y+1).green + img.get_pixel(x, y+1).green + img.get_pixel(x + 1, y+1).green) / 9
                new_img.get_pixel(x, y).blue = (img.get_pixel(x, y).blue + img.get_pixel(x-1, y).blue + img.get_pixel(x+1, y).blue + img.get_pixel(x-1, y-1).blue + img.get_pixel(x, y-1).blue + img.get_pixel(x+1, y-1).blue + img.get_pixel(x-1, y+1).blue + img.get_pixel(x, y+1).blue + img.get_pixel(x + 1, y+1).blue) / 9

    return new_img


def main():
    """
    This program is to blur the image that user input.
    User can change the main function for loop parameter.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
