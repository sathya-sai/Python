import pytest
from DataStructure.utility import LinkedList
t1 = LinkedList()

def test_add():
    assert t1.addnode(3) == None

def test_diaplay():
    assert t1.disply() == None

def test_search():
    assert t1.search1(3)

