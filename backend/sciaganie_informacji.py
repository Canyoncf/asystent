import datetime
from pyown import OWN

owm = OWM('YOUR_API_KEY')  # Zastąp 'YOUR_API_KEY' kluczem API z OpenWeatherMap
mgr = owm.weather_manager()

observation = mgr.weather_at_place("City, Country")
w = observation.weather

print("Temperature:", w.temperature('celsius')['temp'])
print("Weather status:", w.status)
