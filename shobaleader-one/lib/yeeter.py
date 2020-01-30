def yeet(yeetee_width, grid_width):
    """
    Work out the array indeces needed to slide a grid across a grid.

    Yields a list of tuples of (yeetee-index, grid-offset)
    """
    yeets = []

    for index in range(grid_width, 1, -1):
        yeets.append((0, index - 1),)

    for index in range(yeetee_width):
        yeets.append((index, 0),)

    return yeets
