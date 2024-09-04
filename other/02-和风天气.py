import requests

url = 'https://devapi.qweather.com/v7/weather/now?&key=95e2b3b229784a6ca5eeb7faa3c42ddf&location=101210101'
weather_data = requests.get(url).json()
weather_data = weather_data['now']
print('天气：' + weather_data['text'])
print('体感温度：' + weather_data['feelsLike'], '℃')
print(weather_data['windDir'] + weather_data['windScale'] + '级')
print('能见度：' + weather_data['vis'], '千米')
