#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_6_6():
    move_right()
    while wall_is_beneath() and wall_is_above():
        move_right()
    while not wall_is_above() and wall_is_beneath():
        while not wall_is_above():
            move_up(1)
            fill_cell()
        while wall_is_above() and wall_is_on_the_left():
            while not wall_is_beneath():
                move_down()


    pass


if __name__ == '__main__':
    run_tasks()
