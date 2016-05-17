#!/usr/bin/env python
"""
Unnecessarily complicated program that prints 'Hello, world!'.

Ruben Naeff
May 2016
"""
from random import random

from meet_world import hello, bye


def main():
    """Randomly says hello or bye."""
    if random() > .5:
        hello()
    else:
        bye()


if __name__ == "__main__":
    main()
