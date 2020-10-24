import requests

url = 'https://wttr.in'

weather_parameters = {
    '0': '',
    'T': '',
}

response = requests.get(url, params=weather_parameters)  # передайте параметры в http-запрос

print(response.text)
