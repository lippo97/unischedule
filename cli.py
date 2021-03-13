#!/usr/bin/env python3

import fire
import lib

from config import COURSES_PATH

def today():
    return lib.load_data(COURSES_PATH).today()

def day(name):
    return lib.load_data(COURSES_PATH).day(name)

if __name__ == "__main__":
    fire.Fire()
