from threading import Lock
import asyncio

import aiohttp


class WeatherData:

    _instance = None
    _lock = Lock()


    @staticmethod
    def get_geo_url(city):
        return f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid=14117d62cad13ac618a2d61bb433197d"

    @staticmethod
    def get_weather_from_api(long, lat):
        return f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid=14117d62cad13ac618a2d61bb433197d"

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls, *args, **kwargs)
                    cls._instance._cache = {}
                    cls._cache_lock = Lock()
        return cls._instance


    async def get_weather(self, city):
        weather_data = self._cache.get(city)
        if not weather_data:
            weather_data = await self.send_requests(city)
        return weather_data

    async def send_requests(self, city):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.get_geo_url(city)) as response:

                geo_json = await response.json()
                long = geo_json[0]['lon']
                lat = geo_json[0]['lat']

                async with session.get(self.get_weather_from_api(long, lat)) as response:
                    weather_json = await response.json()
                    with self._cache_lock:
                        self._cache[city] = weather_json
                    return weather_json

async def main():
    w = WeatherData()
    data = await w.get_weather('London')
    print(data)


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())