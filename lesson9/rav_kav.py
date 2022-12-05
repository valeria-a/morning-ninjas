import datetime


class RavKav:

    rides = {'short': {'range': (0, 15), 'price': 5.5},
             'medium': {'range': (16, 40), 'price': 12},
             'long': {'range': (40, 1000), 'price': 40},
             }

    def __init__(self, holder_id, holder_name):
        self.__holder_id = holder_id
        self.__holder_name = holder_name
        self.__balance = 0
        # self.__log = {
        #     'log_dates': {},
        #     'log_types': {}
        # }
        self.__log_date = {}
        self.__log_types = {}

    def get_holder_id(self):
        return self.__holder_id

    def get_holder_name(self):
        return self.__holder_name

    def topup(self, amnt):
        if amnt > 0:
            self.__balance += amnt

    @staticmethod
    def _km2type(km) -> str:
        for ride_type, ride_details in RavKav.rides.items():
            if ride_details['range'][0] <= km <= ride_details['range'][1]:
                return ride_type

    def ride(self, km, date: datetime.date):
        pass


# # d1 = datetime.datetime.now()
# d2 = input("Insert a date dd-mm-yyyy: ")
# date2 = datetime.datetime.strptime(d2, "%d-%m-%Y")
# print(date2.date())










