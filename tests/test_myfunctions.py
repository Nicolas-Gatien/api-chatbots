from api_chatbots import myfunctions

def test_say_hello():
    assert myfunctions.say_hello() == "Hello, World!"
