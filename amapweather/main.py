import json
from fastapi import FastAPI

import amap_api

app = FastAPI()

@app.post("/chatpan/buildPrompt")
async def buildPrompt(request_body: dict):
    print('buildPrompt', request_body)
    
    q = request_body['data']
    
    response_body = {
        "code": 200,
        "msg": "OK",
        "data": [{
            "role": "user",
            "content": f"""please prase text in three backquotes into JSON format, the key is 'location' and 'date'. \n ```{q}```"""
        }]
    }
    return response_body

@app.post("/chatpan/requestWeather")
async def requestWeather(request_body: dict):
    print('requestWeather', request_body)
    
    data = json.loads(request_body['data'])
    
    weather_json = amap_api.fetch_weather_amap(data['location'], data['date'])
    
    weather = ''
    if weather_json:
        weather = f"{data['date']} {data['location']} {weather_json['dayweather']} 最高温度 {weather_json['daytemp']}度， 最低温度 {weather_json['nighttemp']}度"

    
    response_body = {
        "code": 200,
        "msg": "OK",
        "data": {
            "weather": weather,
            "weather_json": weather_json
        }
    }
    return response_body