import requests

# If you want to use classes

# class Place:
# attributes of Place are lat, lon, num
# like a card in blackjack and the place_list would be like a deck


class Place:
    def __init__(self, lat, lon, name):
        self.lat = lat
        self.lon = lon
        self.name = name


# string function tells python how it should print off a coordinates and city report object.  dunder underscore method tells py how to print off the object that's in the parenthesis / same as prev sentence.  the default behavior is that it prints off the memory address to store it in random access memory.

# With no string function this is how random object from a class you defined yourself would print:
# Default print(object):
# <__main__.sample instance at 0x1041caab8

    def __str__(self):
        return (f'{self.name} latitude: {self.lat} longitude: {self.lon}')

place_list = [
    (43.101145, -73.850623, 'Saratoga Springs'),
    (42.2494444, -71.0666667, 'Milton'),
    (39.6402638, -106.3741955, 'Vail'),
    (34.138332, 118.660835, 'Calabasas'),
    (32.076176, -81.088371, 'Savannah'),
    (30.2669444, -97.7427778, 'Austin'),
    (35.691544, -105.944183, 'Santa Fe'),
    (43.6567346, -72.7895468, 'Killington'),
    (18.2736111111, -78.35188889, 'Negril'),
    (48.804722, 2.121782, 'Versailles'),
]


def create_placelist(list):
    places = []
    for city in list:
        place = Place(city[0], city[1], city[2])
        places.append(place)
    return places


# def get_weather_data(place_list):
#     url =
#     "https://api.climacell.co/v3/weather/realtime"
#     for place in place_list:

#       payload = {
#       "apikey": "7MFksKPFxUP6Hv1OE67vAvFBRK74UUew","lat":place[0], "lon":place[1],
#       "fields": ["temp", "precipitation", "wind_gust"], "unit_system":"us",
#     }
#       response = requests.get(url, params=payload)
#       .json()

#create instances of weather report class

payload = {
    "apikey": "7MFksKPFxUP6Hv1OE67vAvFBRK74UUew",
    "lat": place[0],
    "lon": place[1],
    "fields": ["temp", "precipitation", "wind_gust"],
    "unit_system": "us",
}

response = requests.get(url, params=payload).json()