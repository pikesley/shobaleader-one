def yeet(yeetee_width, grid_width, enter_from="right"):
    """
    Work out the array indeces needed to slide a grid across a grid.

    Yields a list of tuples of (yeetee-index, grid-offset)
    """
    yeets = []

    if enter_from == "right":
        for index in range(grid_width, 1, -1):
            yeets.append((0, index - 1),)

        for index in range(yeetee_width):
            yeets.append((index, 0),)

    elif enter_from == "left":
        for index in range(yeetee_width, 1, -1):
            yeets.append((index - 1, 0))

        for index in range(grid_width):
            yeets.append((0, index))

    return yeets
