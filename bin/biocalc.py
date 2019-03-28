#!/usr/bin/python
# coding=utf-8

#__author__ = "Shuo Liu"
#__date__ = 2018-02-16 12:30:21

import os
import sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(base_dir)
sys.path.append(base_dir)

from core import main

if __name__ == '__main__':
    main.run()