# decouple the subject and observer objects, allowing for better code maintainability and flexibility.

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, **kwargs):
        for observer in self._observers:
            observer.update(**kwargs)


class Observer:
    def update(self, *args, **kwargs):
        raise NotImplementedError


class ConcreteObserver(Observer):
    def update(self, *args, **kwargs):
        print(f"Received update with args: {args} kwargs: {kwargs}")


class ConcreteSubject(Subject):
    def some_business_logic(self):
        print("Subject: I'm doing some work")
        self.notify(data="Some data")
