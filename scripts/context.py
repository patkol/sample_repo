"""
This module allows us to import the `sample` package located in the parent directory:
from context import sample
Taken from https://github.com/navdeep-G/samplemod/blob/master/tests/context.py
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import sample
