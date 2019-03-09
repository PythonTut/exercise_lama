from typing import List, Tuple


# Changing a single tile
def change(field: List[List[int]], tile: Tuple[int, int]) -> List[List[int]]:
    if field[tile[0]][tile[1]] == 0:
        field[tile[0]][tile[1]] = 1
    else:
        field[tile[0]][tile[1]] = 0
    return field


# Changing all necessary tiles
def change_tiles_normal(field: List[List[int]], tile: Tuple[int, int]) -> List[List[int]]:
    field = change(field, tile)
    if tile[1] > 0:
        # can go left
        field = change(field, (tile[0], tile[1] - 1))

    if tile[1] < len(field[0]) - 1:
        # can go right
        field = change(field, (tile[0], tile[1] + 1))

    if tile[0] > 0:
        # can go up
        field = change(field, (tile[0] - 1, tile[1]))

    if tile[0] < len(field) - 1:
        # can go down
        field = change(field, (tile[0] + 1, tile[1]))

    return field


# Change tiles with special rules
def change_tiles_special(field: List[List[int]], tile: Tuple[int, int]) -> List[List[int]]:
    for i in range(tile[0] + 1):
        for j in range(tile[1] + 1):
            field = change(field, (i, j))
    return field


# String-representation for the field
def construct_str(field: List[List[int]]) -> str:
    ret_str = ''
    for row in field:
        temp_str = ''
        for cell in row:
            temp_str += " {}".format(cell)
        ret_str += temp_str.strip() + "\n"
    return ret_str.strip()


# Checks whether the game is won or not
def check_solved(field: List[List[int]]) -> bool:
    for i in range(len(field)):
        for j in range(len(field[0])):
            if field[i][j] == 1:
                return False
    return True


# Normal game
def lights_out(start: List[Tuple[int, int]]):
    field = []
    for i in range(5):
        field.append([0 for _i in range(5)])

    for lamps in start:
        field[lamps[0]][lamps[1]] = 1
    print(construct_str(field))
    won = check_solved(field)
    while not won:
        input_x = input("X-Koordinate: ")
        while int(input_x) >= 5:
            input_x = input("Bitte geben sie eine korrekte Koordinate ein: ")
        input_y = input("Y-Koordinate: ")
        while int(input_y) >= 5:
            input_y = input("Bitte geben sie eine korrekte Koordinate ein: ")
        tile = (int(input_x), int(input_y))
        field = change_tiles_normal(field, tile)
        won = check_solved(field)
        print(construct_str(field))
    pass


# game with custom grid size
def custom_lights_out(height: int, width: int, start: List[Tuple[int, int]]):
    field = []
    for i in range(height):
        rowlist = []
        for j in range(width):
            rowlist.append(0)
        field.append(rowlist)
    for lamps in start:
        field[lamps[0]][lamps[1]] = 1
    print(construct_str(field))
    won = check_solved(field)
    while not won:
        input_x = input("X-Koordinate: ")
        while int(input_x) >= height:
            input_x = input("Bitte geben sie eine korrekte Koordinate ein: ")
        input_y = input("Y-Koordinate: ")
        while int(input_y) >= width:
            input_y = input("Bitte geben sie eine korrekte Koordinate ein: ")
        tile = (int(input_x), int(input_y))
        field = change_tiles_normal(field, tile)
        won = check_solved(field)
        print(construct_str(field))
    pass


# game with custom grid size and special rules
def lights_out_variant(height: int, width: int, start: List[Tuple[int, int]]):
    field = []
    for i in range(5):
        rowlist = []
        for j in range(5):
            rowlist.append(0)
        field.append(rowlist)
    for lamps in start:
        field[lamps[0]][lamps[1]] = 1
    print(construct_str(field))
    won = check_solved(field)
    while not won:
        input_x = input("X-Koordinate: ")
        while int(input_x) >= height:
            input_x = input("Bitte geben sie eine korrekte Koordinate ein: ")
        input_y = input("Y-Koordinate: ")
        while int(input_y) >= width:
            input_y = input("Bitte geben sie eine korrekte Koordinate ein: ")
        tile = (int(input_x), int(input_y))
        field = change_tiles_special(field, tile)
        print(construct_str(field))
        won = check_solved(field)
    pass
