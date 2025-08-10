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

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)


class Observer:
    def update(self, message):
        raise NotImplementedError


class EmailNotification(Observer):
    def update(self, message):
        print(f"Sending email notification: {message}")
        # iterate over your users and send email to every user subscribed for updates
        # send_emai()


class TextNotification(Observer):
    def update(self, message):
        print(f"Sending text notification: {message}")


class WeatherStation(Subject):
    def __init__(self):
        super().__init__()
        self._temperature = 0

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        self._temperature = temperature
        self.notify(f"Temperature is now {temperature}")


if __name__ == "__main__":
    station = WeatherStation()
    email_notifier = EmailNotification()
    text_notifier = TextNotification()

    station.attach(email_notifier)
    station.attach(text_notifier)

    station.temperature = 25
    station.temperature = 30

    station.detach(email_notifier)

    station.temperature = 35
