import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=13.08&longitude=80.27&current_weather=true"

response = requests.get(url)
data = response.json()

temp = data['current_weather']['temperature']
wind = data['current_weather']['windspeed']

print("Temperature:", temp)
print("Wind Speed:", wind)