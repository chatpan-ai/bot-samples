import requests, dateparser

def fetch_weather_amap(city_adcode, date, extensions='all'):
    
    city_adcode = '110000' # Always point to Beijing for testing
    
    date = dateparser.parse(date).strftime('%Y-%m-%d')
    
    url = 'https://restapi.amap.com/v3/weather/weatherInfo'
    params = {
        'key': '<YOUR_AMAP_KEY>', 
        'city': city_adcode,
        'extensions': extensions
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        
        for cast in data['forecasts'][0]['casts']:
            # print(1, cast)
            if date == cast['date']:
                return cast
    
    return None