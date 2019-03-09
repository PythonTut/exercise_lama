from typing import List, Tuple


# Changing a single tile
def change(field: List[List[int]], tile: Tuple[int, int]) -> List[List[int]]:
    # TODO implement function
    pass


# Changing all necessary tiles
def change_tiles_normal(field: List[List[int]], tile: Tuple[int, int]) -> List[List[int]]:
    # TODO implement function
    pass


# Change tiles with special rules
def change_tiles_special(field: List[List[int]], tile: Tuple[int, int]) -> List[List[int]]:
    # TODO implement function
    pass


# String-representation for the field
def construct_str(field: List[List[int]]) -> str:
    # TODO implement function
    pass


# Checks whether the game is won or not
def check_solved(field: List[List[int]]) -> bool:
    # TODO implement function
    pass


# Normal game
def lights_out(start: List[Tuple[int, int]]):
    pass


# game with custom grid size
def custom_lights_out(height: int, width: int, start: List[Tuple[int, int]]):
    pass


# game with custom grid size and special rules
def lights_out_variant(height: int, width: int, start: List[Tuple[int, int]]):
    pass
