#!/usr/bin/env python

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import argparse
import os
import math

path = os.getcwd()
print(path)
with open("phase-1_Rg_values.log", 'r') as input_file:
    for numbers in input_file:
        a = numbers.strip('\n')
        print (a)
         
