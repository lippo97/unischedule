#!/usr/bin/env python3

import fire
import lib
import os

COURSES = os.path.join(os.path.expanduser('~'), '.scripts', 'courses.yml')

def today():
    return lib.load_data(COURSES).today()

def day(name):
    return lib.load_data(COURSES).day(name)

if __name__ == "__main__":
    fire.Fire()
