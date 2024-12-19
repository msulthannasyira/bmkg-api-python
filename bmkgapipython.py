import pandas as pd
import matplotlib.pyplot as plt
import json
from datetime import datetime

# Input date for the forecast
forecast_date = input("Enter the forecast date (YYYY-MM-DD): ")

# Sample weather data (reference structure)
weather_data = {
    'lokasi': {
        'provinsi': 'Jawa Barat',
        'kotkab': 'Bogor',
        'kecamatan': 'Citeureup',
        'desa': 'Sukahati',  # Changed to Sukahati
        'lon': 110.0881778385,
        'lat': -6.9688421952,
        'timezone': 'Asia/Jakarta'
    },
    'data': [
        {
            'lokasi': {
                'provinsi': 'Jawa Barat',
                'kotkab': 'Bogor',
                'kecamatan': 'Citeureup',
                'desa': 'Sukahati',  # Changed to Sukahati
                'lon': 110.0881778385,
                'lat': -6.9688421952,
                'timezone': '+0700',
                'type': 'adm4'
            },
            'cuaca': [
                {'datetime': f'{forecast_date}T00:00:00Z', 't': 26, 'weather_desc': 'Berawan', 'ws': 2.6, 'hu': 84, 'vs': 5995},
    {'datetime': f'{forecast_date}T01:00:00Z', 't': 27, 'weather_desc': 'Cerah', 'ws': 3.0, 'hu': 80, 'vs': 6100},
    {'datetime': f'{forecast_date}T02:00:00Z', 't': 28, 'weather_desc': 'Hujan', 'ws': 4.5, 'hu': 90, 'vs': 5800},
    {'datetime': f'{forecast_date}T03:00:00Z', 't': 26, 'weather_desc': 'Berawan', 'ws': 2.6, 'hu': 84, 'vs': 5995},
    {'datetime': f'{forecast_date}T04:00:00Z', 't': 27, 'weather_desc': 'Cerah', 'ws': 3.0, 'hu': 80, 'vs': 6100},
    {'datetime': f'{forecast_date}T05:00:00Z', 't': 28, 'weather_desc': 'Hujan', 'ws': 4.5, 'hu': 90, 'vs': 5800},
    {'datetime': f'{forecast_date}T06:00:00Z', 't': 26, 'weather_desc': 'Berawan', 'ws': 2.6, 'hu': 84, 'vs': 5995},
    {'datetime': f'{forecast_date}T07:00:00Z', 't': 27, 'weather_desc': 'Cerah', 'ws': 3.0, 'hu': 80, 'vs': 6100},
    {'datetime': f'{forecast_date}T08:00:00Z', 't': 28, 'weather_desc': 'Hujan', 'ws': 4.5, 'hu': 90, 'vs': 5800},
    {'datetime': f'{forecast_date}T09:00:00Z', 't': 26, 'weather_desc': 'Berawan', 'ws': 2.6, 'hu': 84, 'vs': 5995},
    {'datetime': f'{forecast_date}T10:00:00Z', 't': 27, 'weather_desc': 'Cerah', 'ws': 3.0, 'hu': 80, 'vs': 6100},
    {'datetime': f'{forecast_date}T11:00:00Z', 't': 28, 'weather_desc': 'Hujan', 'ws': 4.5, 'hu': 90, 'vs': 5800},
    {'datetime': f'{forecast_date}T12:00:00Z', 't': 26, 'weather_desc': 'Berawan', 'ws': 2.6, 'hu': 84, 'vs': 5995},
    {'datetime': f'{forecast_date}T13:00:00Z', 't': 27, 'weather_desc': 'Cerah', 'ws': 3.0, 'hu': 80, 'vs': 6100},
    {'datetime': f'{forecast_date}T14:00:00Z', 't': 28, 'weather_desc': 'Hujan', 'ws': 4.5, 'hu': 90, 'vs': 5800},
    {'datetime': f'{forecast_date}T15:00:00Z', 't': 26, 'weather_desc': 'Berawan', 'ws': 2.6, 'hu': 84, 'vs': 5995},
    {'datetime': f'{forecast_date}T16:00:00Z', 't': 27, 'weather_desc': 'Cerah', 'ws': 3.0, 'hu': 80, 'vs': 6100},
    {'datetime': f'{forecast_date}T17:00:00Z', 't': 28, 'weather_desc': 'Hujan', 'ws': 4.5, 'hu': 90, 'vs': 5800},
    {'datetime': f'{forecast_date}T18:00:00Z', 't': 26, 'weather_desc': 'Berawan', 'ws': 2.6, 'hu': 84, 'vs': 5995},
    {'datetime': f'{forecast_date}T19:00:00Z', 't': 27, 'weather_desc': 'Cerah', 'ws': 3.0, 'hu': 80, 'vs': 6100},
    {'datetime': f'{forecast_date}T20:00:00Z', 't': 28, 'weather_desc': 'Hujan', 'ws': 4.5, 'hu': 90, 'vs': 5800},
    {'datetime': f'{forecast_date}T21:00:00Z', 't': 26, 'weather_desc': 'Berawan', 'ws': 2.6, 'hu': 84, 'vs': 5995},
    {'datetime': f'{forecast_date}T22:00:00Z', 't': 27, 'weather_desc': 'Cerah', 'ws': 3.0, 'hu': 80, 'vs': 6100},
    {'datetime': f'{forecast_date}T23:00:00Z', 't': 28, 'weather_desc': 'Hujan', 'ws': 4.5, 'hu': 90, 'vs': 5800},
                # Add more forecast entries as needed
            ]
        }
    ]
}

# Extract the weather data from the structure
forecast_data = weather_data['data'][0]['cuaca']
time_series = []
temperature_series = []
weather_desc_series = []
wind_speed_series = []
humidity_series = []
visibility_series = []

# Iterate over the forecast data and extract values
for forecast in forecast_data:
    forecast_time = datetime.strptime(forecast['datetime'], "%Y-%m-%dT%H:%M:%SZ")
    time_series.append(forecast_time)
    temperature_series.append(forecast['t'])
    weather_desc_series.append(forecast['weather_desc'])
    wind_speed_series.append(forecast['ws'])
    humidity_series.append(forecast['hu'])
    visibility_series.append(forecast['vs'])

# Step 4: Create DataFrame if data is available
if time_series:
    weather_df = pd.DataFrame({
        'Time': time_series,
        'Temperature': temperature_series,
        'Weather Description': weather_desc_series,
        'Wind Speed (m/s)': wind_speed_series,
        'Humidity (%)': humidity_series,
        'Visibility (m)': visibility_series
    })

    # Convert the Time column to string format to be JSON serializable
    weather_df['Time'] = weather_df['Time'].dt.strftime('%Y-%m-%dT%H:%M:%SZ')

    # Step 5: Plot the data (Temperature and Humidity for example)
    output_graph_path = 'weather_forecast.png'
    plt.figure(figsize=(10, 5))
    plt.plot(weather_df['Time'], weather_df['Temperature'], label='Temperature (\u00b0C)', marker='o')
    plt.plot(weather_df['Time'], weather_df['Humidity (%)'], label='Humidity (%)', marker='o')
    plt.xlabel('Time')
    plt.ylabel('Values')
    plt.title(f'Temperature and Humidity Forecast for {forecast_date}')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()

    # Save the plot
    plt.savefig(output_graph_path)

    # Step 6: Save JSON
    output_json_path = 'weather_forecast_data.json'
    with open(output_json_path, 'w') as json_file:
        json.dump(weather_df.to_dict(orient='records'), json_file, indent=4)

    print(f"Files saved as '{output_graph_path}' and '{output_json_path}'")
else:
    print("No valid weather data available.")
