import pytest
from converter import Currency

def test1():
    a = Currency(100)
    assert type(a) is Currency
    assert a.value is 100
    assert a.currency is 'RUB'

def test2():
    a = Currency(100)
    b = Currency(250, 'USD')
    c = Currency(400, 'EUR')
    assert type(a + b) is Currency
    assert (a + b).value == 18607.5
    assert (a + b).currency == 'RUB'
    assert (b + a).value == 251.4
    assert (b + a).currency == 'USD'
    assert (a + c).value == 33564.0
    assert (a + 1320).value == 1420
    assert (a + 1320).currency == 'RUB'

def test3():
    a = Currency(400, 'EUR')
    assert a.value == 400
    assert a.currency == 'EUR'
    a.currency = 'RUB'
    assert a.value == 33464
    assert a.currency == 'RUB'