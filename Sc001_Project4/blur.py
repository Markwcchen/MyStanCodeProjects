"""
File: blur.py
Name: Mark
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: str, the file path of the original image (with respect to current directory)
    :return:
    """
    # Todo: create a new blank img that is as big as the original one
    new_img = SimpleImage("images/smiley-face.png")
    new_img = SimpleImage.blank(new_img.width, new_img.height)

    # Loop over the picture
    for x in range(img.width):
        for y in range(img.height):

            # Belows are 9 conditions of pixel filling, depending on pixels' x,y orientation.
            
            if x == 0 and y == 0:
                # Get pixel at the top-left corner of the image.
                new_img_pixel = 0
                for i in range(2):
                    for j in range(2):
                        new_img_pixel += img(x+i, y+j)
                        new_img_pixel -= img(x, y)
            elif x == img.width-1 and y == 0:
                # Get pixel at the top-right corner of the image.
                pass

            elif x == 0 and y == img.height-1:
                # Get pixel at the bottom-left corner of the image
                pass

            elif x == img.width-1 and y == img.height-1:
                # Get pixel at the bottom-right corner of the image
                pass
 
            elif 0 < x < img.width-1 and y == 0:
                # Get top edge's pixels (without two corners)
                pass

            elif 0 < x < img.width-1 and y == img.height-1:
                # Get bottom edge's pixels (without two corners)
                pass

            elif x == 0 and 0 < y < img.height-1:
                # Get left edge's pixels (without two corners)
                pass

            elif x == img.width-1 and 0 < y < img.height-1:
                # Get right edge's pixels (without two corners)
                pass

            else:
                # Inner pixels.
                pass

    return new_img


def main():
    """
    TODO:
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
