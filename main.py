import streamlit as st
import plotly.express as px
from backend import get_data

filtered_data = []
# Add title, text input, slider, selectbox, and subheader
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    # Get the temperature/sky data
    filtered_data = get_data(place, days)

    if option == "Temperature":
        # Extract Data
        temperatures = [dict["main"]["temp"] for dict in filtered_data]
        dates = [dict["dt_txt"] for dict in filtered_data]

        # Create a temperature plot
        figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
        st.plotly_chart(figure)
    if option == "Sky":
        sky_condition = [dict["weather"][0]["main"] for dict in filtered_data]
        print(sky_condition)
        for condition in sky_condition:
            st.image(image=f"images\{condition.lower()}.png", width=115)

