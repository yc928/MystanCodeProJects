"""
File: babygraphics.py
Name: Ian
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
    x_coordinate = GRAPH_MARGIN_SIZE + year_index*(width-2*GRAPH_MARGIN_SIZE)//len(YEARS)
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
    # for i in range(GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, (CANVAS_WIDTH-2*GRAPH_MARGIN_SIZE)//len(YEARS)):
    #     canvas.create_line(i, 0, i, CANVAS_HEIGHT)
    for i in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT)
        canvas.create_text(x+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)


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
    change_height = (CANVAS_HEIGHT - 2*GRAPH_MARGIN_SIZE) / 1000

    for i in range(len(lookup_names)):
        name = lookup_names[i]
        year = str(YEARS[0])
        pre_x = get_x_coordinate(CANVAS_WIDTH, 0)
        # Show first data without drawing line.
        if year in name_data[name].keys():
            pre_y = int(name_data[name][year])*change_height + GRAPH_MARGIN_SIZE
            show_text = name + ' ' + name_data[name][year]
        else:
            pre_y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
            show_text = name + ' *'
        canvas.create_text(pre_x + TEXT_DX, pre_y, text=show_text, anchor=tkinter.SW, fill=COLORS[i % len(COLORS)])
        # Show second to the end and drawing line.
        for j in range(1, len(YEARS)):
            year = str(YEARS[j])
            cur_x = get_x_coordinate(CANVAS_WIDTH, j)
            if year in name_data[name].keys():
                cur_y = int(name_data[name][year])*change_height + GRAPH_MARGIN_SIZE
                show_text = name + ' ' + name_data[name][year]
            else:
                cur_y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                show_text = name + ' *'
            canvas.create_line(pre_x, pre_y, cur_x, cur_y, width=LINE_WIDTH, fill=COLORS[i % len(COLORS)])
            canvas.create_text(cur_x + TEXT_DX, cur_y, text=show_text, anchor=tkinter.SW, fill=COLORS[i % len(COLORS)])
            pre_x, pre_y = cur_x, cur_y


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
