from threading import Lock


class Singleton:
    _instance = None
    _lock = Lock()


    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance


if __name__ == '__main__':

    s1 = Singleton()
    s1.add_to_cache(1, "a")
    print(s1)

    s2 = Singleton()
    s2.add_to_cache(2, "b")
    print(s2)

    print(s1.cache)
    print(s2.cache)