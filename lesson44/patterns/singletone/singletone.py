class Singleton:
    _instance = None


    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # cls._instance.cache = {}
        return cls._instance

    def __init__(self):
        if not self.__getattribute__('cache'):
            self.cache = {}


    def add_to_cache(self, k, v):
        self.cache[k] = v


if __name__ == '__main__':

    s1 = Singleton()
    s1.add_to_cache(1, "a")
    print(s1)

    s2 = Singleton()
    s2.add_to_cache(2, "b")
    print(s2)

    print(s1.cache)
    print(s2.cache)