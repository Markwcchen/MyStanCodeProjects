"""
File: mirror_lake.py
Name: Mark
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: str, the file path of the original image (with respect to current directory)
    :return: mirror lake
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    b_img = SimpleImage.blank(original_mt.width, original_mt.height*2)

    for x in range(original_mt.width):
        for y in range(original_mt.height):
            original_mt_pixel = original_mt.get_pixel(x, y)
            # up
            b_img_pixel1 = b_img.get_pixel(x, y)
            b_img_pixel1.red = original_mt_pixel.red
            b_img_pixel1.green = original_mt_pixel.green
            b_img_pixel1.blue = original_mt_pixel.blue
            # down
            b_img_pixel2 = b_img.get_pixel(x, b_img.height-1-y)
            b_img_pixel2.red = original_mt_pixel.red
            b_img_pixel2.green = original_mt_pixel.green
            b_img_pixel2.blue = original_mt_pixel.blue
    b_img.show()
    return 0


def main():
    """
    TODO: reflect the image
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
