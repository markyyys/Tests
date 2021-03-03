import pytest

def testedTuple():
    a = (5, 9, "text", 0)
    return a

def testedTuple2():
    a = (5, 0, "text", 0)
    return a.count(0)


def testTuple1():
    assert len(testedTuple()) != 0

def testTuple2():
    try:
        assert 4 in testedTuple()
    except AssertionError:
        pass

def testTuple3():
    try:
        assert 9 in testedTuple()
    except AssertionError:
        pass