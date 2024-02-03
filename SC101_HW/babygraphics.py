"""
File: babygraphics.py
Name: 
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """

    x_range = width - 2 * GRAPH_MARGIN_SIZE
    interval = x_range / (len(YEARS))
    x_coordinate = GRAPH_MARGIN_SIZE + interval * year_index

    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    bottom_line = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
    top_line = GRAPH_MARGIN_SIZE

    # top and bottom line
    canvas.create_line(GRAPH_MARGIN_SIZE, bottom_line, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, bottom_line, fill='black',
                       width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, top_line, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, top_line, fill='black',
                       width=LINE_WIDTH)

    # left and right
    canvas.create_line(GRAPH_MARGIN_SIZE, top_line, GRAPH_MARGIN_SIZE, bottom_line, fill='black', width=LINE_WIDTH)
    # canvas.create_line(CANVAS_WIDTH - GRAPH_MARGIN_SIZE, top_line, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, bottom_line,
    #                    fill='black', width=LINE_WIDTH)

    for year_index, year in enumerate(YEARS):
        x_coordinate = get_x_coordinate(CANVAS_WIDTH, year_index)

        canvas.create_line(x_coordinate, top_line, x_coordinate, bottom_line, fill='gray', dash=(2, 2),
                           width=LINE_WIDTH)
        canvas.create_text(x_coordinate + TEXT_DX, bottom_line + TEXT_DX, text=str(year), anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    for name in lookup_names:
        if name in name_data:
            color = COLORS[lookup_names.index(name) % len(COLORS)]

            previous_x = None
            previous_rank = None
            first = True

            for year_index, year in enumerate(YEARS):
                x_coordinate = get_x_coordinate(CANVAS_WIDTH, year_index)


                def get_y_coordinate(rank):
                    interval = (CANVAS_HEIGHT - 2*GRAPH_MARGIN_SIZE)/MAX_RANK
                    return rank*interval+GRAPH_MARGIN_SIZE

                if first:
                    first = False
                    previous_x = x_coordinate       # get_x_coordinate(CANVAS_WIDTH, 0)
                    previous_rank = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE if str(YEARS[0]) not in name_data[name] else int(name_data[name][str(YEARS[0])])
                    canvas.create_text(x_coordinate + TEXT_DX, GRAPH_MARGIN_SIZE, text=str(YEARS[0]), anchor=tkinter.NW)
                    t = f"{name} *" if str(YEARS[0]) not in name_data[name] else f"{name} {previous_rank}"
                    canvas.create_text(x_coordinate + TEXT_DX, get_y_coordinate(previous_rank), text=t, anchor=tkinter.SW, fill=color)
                else:
                    x_coordinate = get_x_coordinate(CANVAS_WIDTH, year_index)
                    year_str = str(year)

                    if year_str in name_data[name]:
                        rank = int(name_data[name][year_str])
                        if str(YEARS[year_index-1]) in name_data[name]:  #(990, 990)
                            canvas.create_line(previous_x, get_y_coordinate(previous_rank), x_coordinate, get_y_coordinate(rank), fill=color, width=LINE_WIDTH)
                        else:  #(1100, 990)
                            canvas.create_line(previous_x, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, x_coordinate, get_y_coordinate(rank), fill=color, width=LINE_WIDTH)
                        canvas.create_text(x_coordinate + TEXT_DX, get_y_coordinate(rank), text=f"{name} {rank}", anchor=tkinter.SW, fill=color)
                        previous_x = x_coordinate
                        previous_rank = rank
                    else:
                        if str(YEARS[year_index-1]) in name_data[name]:  #(990, 1100)
                            canvas.create_line(previous_x, get_y_coordinate(previous_rank), x_coordinate, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, fill=color, width=LINE_WIDTH)
                        else:  #(1100, 1100)
                            canvas.create_line(previous_x, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, x_coordinate, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, fill=color, width=LINE_WIDTH)
                        canvas.create_text(x_coordinate + TEXT_DX, get_y_coordinate(MAX_RANK), text=f"{name} *", anchor=tkinter.SW, fill=color)
                        previous_x = x_coordinate
                        previous_rank = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE

                    canvas.create_text(x_coordinate + TEXT_DX, GRAPH_MARGIN_SIZE, text=year_str, anchor=tkinter.NW)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
