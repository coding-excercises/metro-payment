# -*- coding: utf-8 -*-
import sys
import os

# add the paths to context so that the project 
# packages are available for running the tests
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

import metropayment
from src.farecalc import FareCalc