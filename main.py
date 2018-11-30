#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from src.tm import Tm

if __name__ == "__main__":
    input_file = sys.stdin

    tm = Tm(input_file)
    while True:
        try:
            tm.compute()
        except KeyError:
            break
