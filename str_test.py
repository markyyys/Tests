import pytest

def testedStr(f):
    a = "The Answer is "
    return a+f

def testStr1():
    try:
        assert testedStr("42") == "The Answer is 42"
    except SyntaxError:
        pass

def testStr2():
    assert len(testedStr("42")) != 30

def testStr3():
    try:
        assert 42 in (testedStr("42"))
    except TypeError:
        pass


