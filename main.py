import requests

api_key = 'cc6dc6e06b35413b76f55e0482c93bac'

def get_weather_report(api_key, city):
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'appid': api_key}
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        print("Weather data for", city)
        print("Temperature:", data['main']['temp'])
        print("Weather:", data['weather'][0]['description'])
    else:
        print("Error:", response.status_code)

if __name__ == "__main__":
    city = input("Enter the city name: ")
    get_weather_report(api_key, city)
