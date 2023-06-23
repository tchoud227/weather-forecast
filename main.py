import streamlit as st
import plotly.express as px
from backend import get_data

st.set_page_config(layout="wide")
filtered_data = []
# Add title, text input, slider, selectbox, and subheader
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ", )
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    # Get the temperature/sky data
    try:
        filtered_data = get_data(place, days)

        if option == "Temperature":
            # Extract Data
            temperatures = [float(dict["main"]["temp"] / 10 ) for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]

            # Create a temperature plot
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)
        if option == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/clouds.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_condition = [dict["weather"][0]["main"] for dict in filtered_data]
            image_path = [images[condition] for condition in sky_condition]
            print(sky_condition)
            st.image(image=image_path, width=100)

    except KeyError:
        st.write(f"{place} does not exist!")

