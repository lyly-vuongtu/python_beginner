from hello import hello

def test_default():
    assert hello("lyly") == "hello, lyly"
def test_argument():
    assert hello() == "hello, world"
    

