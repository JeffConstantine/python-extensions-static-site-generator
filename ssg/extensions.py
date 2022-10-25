import sys
import importlib
from pathlib import path

def load_module(directory, name):
    sys.path.insert(0, directory)
