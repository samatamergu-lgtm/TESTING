import sys
import os

# add project root so hello.py can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from hello import Greet

def test_dummy():
    assert False 

