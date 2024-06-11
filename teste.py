import requests


response = requests.get('https://embed.waze.com/iframe?zoom=13&lat=40.78247&lon=-73.97105&pin=1')
print(response.status_code)