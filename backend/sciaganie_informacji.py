import datetime
import requests

#api_key = str(5cf8ca022bbd767f66f72ce76fab5766)
latitude = 51.750000
longitude = 19.466669
url = f'http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid=3d5297ba44a4a0ac40fc66c1d9a19fc2'

response = requests.get(url)
data = response.json()
print(url)
print("Temperature:", data['main']['temp'])
print("Weather status:", data['weather'][0]['main'])



