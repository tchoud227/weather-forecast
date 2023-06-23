import requests as req
API_key = "c4302f3d4241653ffd74cea1c61948c4"


def get_data(place, forecast_days=None, weather_data=None ):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}"
    response = req.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]

    if weather_data == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    if weather_data == "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]

    return filtered_data


if __name__=="__main__":
    print(get_data(place="Tokyo", forecast_days=3, weather_data="Temperature"))
