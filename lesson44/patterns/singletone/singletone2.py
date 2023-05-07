class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        else:
            raise ValueError("Singleton instance already exists.")
        return cls._instance

