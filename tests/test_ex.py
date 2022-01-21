import sys
sys.path.insert(1,"../src")
import ex

def test_ex():
    a=1
    b=2
    c=ex.add(a,b)
    assert c==3
