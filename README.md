# Little Blue Zebra

# Weather Data Dashboard

This is a weather data dashboard project that uses Streamlit to create an interactive interface. It extracts current weather and forecast information from an external API, stores the data in a SQLite database, and displays it in a visually appealing manner. The app.py is hosted [here](https://antonioc4r10s-little-blue-zebra-app-zkxhf2.streamlit.app/).

## Features

- **Metrics Display:** Shows important metrics such as temperature, wind, and humidity for the selected city.
- **Weather Forecast:** Presents weather forecast data for the chosen city over a specific period.
- **Rainfall Amount:** Displays the total amount of rainfall forecasted for the upcoming days.
- **Live Traffic:** Embeds an interactive Waze map showing real-time traffic in the selected city.
- **Forecast Charts:** Presents line charts for temperature and apparent temperature over time.

## Installation

1. Clone the repository:
- git clone (https://github.com/AntonioC4r10s/little_blue_zebra.git)

2. Install the dependencies:
- pip install -r requirements.txt


## Usage

1. Run the `main.py` script:
- streamlit run main.py


2. The dashboard will open automatically in your default web browser.

## Configuration

- **Available Cities:** The available cities are defined in the `model.py` file.
- **API Key:** You need to obtain a valid API key to access external weather data (http://api.openweathermap.org).

## Contribution

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](https://github.com/your-username/your-repository/blob/main/LICENSE).

---
