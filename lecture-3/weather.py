import requests
from mcp.server.fastmcp import FastMCP , Context

#server creation
server = FastMCP("weather-server")

#tool
@server.tool()
def get_weather(ctx: Context, city: str = "Delhi") -> str:
    """Get current weather for a given city using Open-Meteo API"""
    coords ={
        "Delhi" : (28.61, 77.23),
        "Mumbai" : (19.07, 72.87),
        "Bangalore" : (12.97, 77.59)
    }
    lat,lon =coords.get(city, (28.61, 77.23))

    url=f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true&timezone=Asia/Kolkata"
    response = requests.get(url).json()

    if "current_weather" in response:
        temp = response["current_weather"]["temperature"]
        wind = response["current_weather"]["windspeed"]
        return f"🌤️ Current weather in {city}: {temp}°C, Wind {wind} km/h"
    else:
      return "no data available"


#test
dummy_ctx=Context()
print(get_weather(dummy_ctx,"Delhi"))
print(get_weather(dummy_ctx,"Mumbai"))
print(get_weather(dummy_ctx,"Bangalore"))
