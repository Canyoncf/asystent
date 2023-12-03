import datetime

# -*- coding: utf-8 -*-
import pywapi
import pprint
pp = pprint.PrettyPrinter(indent=4)
# id stacji stosowany przez Yahoo
result = pywapi.get_weather_from_yahoo('PLXX0028', 'metric')
pp.pprint(result)

# ~nazwa miasta
result = pywapi.get_weather_from_google('Warszawa')
pp.pprint(result)


