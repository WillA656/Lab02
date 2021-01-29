# File: ab02.py

import karel

# Your code should go immediately below the comment
# in each of the below functions. Remember to tab it
# in (so it lines up with the comment) so that it is
# part of the function "bundle"!  paint_room()


def paint_room():
    """
    Function to paint all 4 walls of the
    room with beepers. You'll need to use
    your below defined functions here to
    achieve the desired goal of painting
    all 4 walls of the room with beepers.
    """
    move_to_corner()
    paint_wall()
    reposition()
    paint_wall()
    reposition()
    paint_wall()
    reposition()
    paint_wall()
    reposition()


def move_to_corner():
    """
    Function to initially move the bot
    into a corner.
    """
    move()
    move()
    turn_left()

def paint_wall():
    """
    Moves along one wall, "painting" it
    by placing beepers along it.
    """
    move()
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()

def reposition():
    """
    Turns and otherwise repositions Karel
    in between walls.
    """
    turn_left()