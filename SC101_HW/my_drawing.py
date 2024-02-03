"""
File: 
Name: Mark
----------------------
TODO: draw the 2020 olympic logo for TOKYO
"""

from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    TODO: draw the olympic logo
    """
    window = GWindow(width=1000, height=500, title='Olympic')
    first = GOval(150, 150, x=250, y=150)
    first.color = 'blue'
    first.filled = True
    first.fill_color = 'blue'
    window.add(first)
    first_mid = GOval(120, 120, x=265, y=165)
    first_mid.color = 'white'
    first_mid.filled = True
    first_mid.fill_color = 'white'
    window.add(first_mid)
    second = GOval(150, 150, x=425, y=150)
    window.add(second)
    second.filled = True
    second.fill_color = 'black'
    second.color = 'black'
    second_mid = GOval(120, 120, x=440, y=165)
    second_mid.color = 'white'
    second_mid.filled = True
    second_mid.fill_color = 'white'
    window.add(second_mid)
    third = GOval(150, 150, x=600, y=150)
    window.add(third)
    third.color = 'red'
    third.filled = True
    third.fill_color = 'red'
    third_mid = GOval(120, 120, x=615, y=165)
    third_mid.color = 'white'
    third_mid.filled = True
    third_mid.fill_color = 'white'
    window.add(third_mid)
    forth = GOval(150, 150, x=325, y=200)
    window.add(forth)
    forth.color = 'orange'
    forth.filled = True
    forth.fill_color = 'orange'
    forth_mid = GOval(120, 120, x=340, y=215)
    forth_mid.color = 'white'
    forth_mid.filled = True
    forth_mid.fill_color = 'white'
    window.add(forth_mid)
    fifth = GOval(150, 150, x=500, y=200)
    window.add(fifth)
    fifth.color = 'green'
    fifth.filled = True
    fifth.fill_color = 'green'
    fifth_mid = GOval(120, 120, x=515, y=215)
    fifth_mid.color = 'white'
    fifth_mid.filled = True
    fifth_mid.fill_color = 'white'
    window.add(fifth_mid)

    label_1 = GLabel('TOKYO', x=250, y=450)
    label_1.font = '-70'
    label_1.color = 'black'
    window.add(label_1)

    label_2 = GLabel('2020', x=580, y=450)
    label_2.font = '-70'
    label_2.color = 'black'
    window.add(label_2)

    japan = GOval(60, 60, x=500, y=380)
    window.add(japan)
    japan.color = 'red'
    japan.filled = True
    japan.fill_color = 'red'



if __name__ == '__main__':
    main()
