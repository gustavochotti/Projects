# import the necessary library
import requests

# paste the API and Base Url:
API_KEY = "your API key here"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# put city name and request data
city = input("Enter a city name: ")
requests_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(requests_url)

# create a condition and put the commands
if response.status_code == 200:
    data = response.json()
    main_weather = data['weather'][0]['main'] 
    description_weather = data['weather'][0]['description']
    temperature = round(data['main']['temp']-273.15, 0)
    temperature_maximum = round(data['main']['temp_max']- 273.15, 0) # -273.15 to convert from Kelvin to Celsius
    temperature_minimum = round(data['main']['temp_min'] - 273.15, 0)
    temperature_feels = round(data['main']['feels_like'] - 273.15, 0)

    # show the weather
    print(main_weather, '-', description_weather)
    print('Temperature:', temperature)
    print(f'Max: {temperature_maximum}c / Min: {temperature_minimum}c - Feels Like: {temperature_feels}c')

# if an error appears during the execution
else:
    "An error has ocurred! :("
