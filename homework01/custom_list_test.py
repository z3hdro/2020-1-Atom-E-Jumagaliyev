import pytest
from custom_list import CustomList

def test1():
    x = CustomList(1, 2, 3, 4, 5, 6)
    assert type(x) == CustomList
    assert len(x) == 6
    x.append(10)
    assert len(x) == 7

def test2():
    a = CustomList(5, 1, 3)
    b = CustomList(1, 2, 7, 3)
    assert type(a) == CustomList
    assert type(b) == CustomList
    assert (a + b) == CustomList(6, 3, 10, 3)
    assert (a - b) == CustomList(4, -1, -4, -3)
    assert a == CustomList(5, 1, 3)

def test3():
    a = CustomList(1, 2, 7)
    b = CustomList(1, 2, 7, 3)
    assert (a == b) is False 
    a.append(3)
    assert (a == b) is True
    a.pop()
    assert (a <= b) is True
    assert (a < b) is True
    assert (a == b) is False