class Singleton:
    _instance = None
    def __init__(self):
        if Singleton._instance:
            raise Singleton._instance
        Singleton._instance=self

class A(Singleton):
    pass
