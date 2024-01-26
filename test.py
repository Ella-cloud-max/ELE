# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 09:55:16 2024

@author: Eric van Huizen
"""

from iteratief2 import create_rotate_options, create_pull_options, mutate_direction_pull, mutate_direction_rotate
import random
from code.classes.amino import Amino
from code.classes.protein import Protein
from code.algorithms import randomise
from code.visualisation.visualisation import *
from typing import Any
import copy
import time

def h_bond_combinations(protein):
    