import requests

# If you want to use classes

# class WeatherReport:
# attributes of Place are lat, lon, num
# like a card in blackjack and the place_list would be like a deck

# Class gives the template and the object is the actual implementation of that template.
# place, temp, precip


class WeatherReport:
    def __init__(self, place, temp, precip):
        self.place = place
        self.temp = temp
        self.precip = precip

# string function -- in this particular replit -- tells python how it should print off a coordinates and city report object.  dunder underscore method tells py how to print off the object that's in the parenthesis / same as prev sentence.  the default behavior is that it prints off the memory address to store it in random access memory.

# With no string function this is how random object from a class you defined yourself would print:
# Default print(object):
# <__main__.sample instance at 0x1041caab8

    def __str__(self):
        return f"the weather report in {self.place} has a high temp for the day of {self.temp}"

#TODO construct alist of places that are tuples lat and long (lat, long, 'Place')
# get lats and longs from tuples

place_list = [(43.101145, -73.850623, 'Saratoga Springs'), (42.2494444, -71.0666667, 'Milton'), (39.6402638, -106.3741955, 'Vail'), (34.138332, 118.660835, 'Calabasas'), (32.076176, -81.088371, 'Savannah'), (30.2669444, -97.7427778, 'Austin'), (35.691544, -105.944183, 'Santa Fe'), (43.6567346, -72.7895468, 'Killington'), (18.2736111111, -78.35188889, 'Negril'), (48.804722, 2.121782, 'Versailles')]

# def get_weather_data(place_list):
#     url =
#     "https://api.climacell.co/v3/weather/realtime"
#     for place in place_list:

#       payload = {
#       "apikey": "7MFksKPFxUP6Hv1OE67vAvFBRK74UUew","lat":place[0], "lon":place[1],
#       "fields": ["temp", "precipitation", "wind_gust"], "unit_system":"us",
#   }

def get_weather_data(place_list):
    url = "https://api.climacell.co/v3/weather/realtime"
    for place in place_list:
    
      payload = {
      "apikey": "7MFksKPFxUP6Hv1OE67vAvFBRK74UUew","lat": place[0],
      "lon": place[1],
      "fields": ["temp", "precipitation", "wind_gust"],
      "unit_system": "us",
    }
     
# response = requests.get(url, params=payload).json()

      response = requests.get(url, params=payload).json()

#create instances of weather report class
# give me temp and precip for a location, given lat and long
   
      report = WeatherReport( place, response["temp"]["value"], response["precipitation"]["value"])

# print(report)

      print(report)

# below will make a request to the 'realtime' url that we used above



get_weather_data(place_list)    

    

   

    