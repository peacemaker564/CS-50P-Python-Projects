from bank import hello_eval

def test_hello():
    assert hello_eval("Hello, Avi.") == 0
    assert hello_eval("hello, brah!56") == 0

def test_h():
    assert hello_eval("Hi, Avi.") == 20
    assert hello_eval("hi, brah!56") == 20
    assert hello_eval("How are you? , Avi.") == 20
    assert hello_eval("Hohooho, brah!56") == 20

def test_non():
    assert hello_eval("Sup ? Avi.") == 100
    assert hello_eval("Yoo, mate.!") == 100





