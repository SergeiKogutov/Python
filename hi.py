
import python_weather
import asyncio

async def getweather():
    client = python_weather.Client(format=python_weather.IMPERIAL)

    weather = await client.get ("шелаболиха")
    celsius = (weather.current.temperature - 32) / 1.8
    print(str(round(celsius)) + "'") 
    
    print(weather.current.local_time)

    # for forecast in weather.forecasts:
    #     print(str(forecast.date), forecast.sky_text, forecast.temperature)

    await client.close()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(getweather())