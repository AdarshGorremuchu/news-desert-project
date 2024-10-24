import folium
import geopandas as gpd
from geopy.geocoders import GoogleV3
import pandas as pd

# Insert your Google Maps API Key here
API_KEY = ''  # Add your Google API Key

# Initialize the geocoder
geolocator = GoogleV3(api_key=API_KEY)

# Function to safely read a CSV file
def read_csv_file(file_path):
    try:
        df = pd.read_csv(file_path, encoding='ISO-8859-1', on_bad_lines='skip')
        return df
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None

# Read the CSV file
csv_file = "D:\\News Project\\all the data sets\\gpt\\wvua_news_gpt_trial_27.csv"
df = read_csv_file(csv_file)

# Check if the dataframe was loaded successfully
if df is not None:
    locations = df['Locations'].dropna().tolist()
else:
    print("Error: Dataframe could not be loaded.")
    locations = []

# Function to geocode a location using Google Maps API
def geocode_location(city, state):
    try:
        location_data = geolocator.geocode(f"{city}, {state}")
        if location_data:
            return (location_data.latitude, location_data.longitude)
        else:
            print(f"Location not found: {city}, {state}")
            return None
    except Exception as e:
        print(f"Error geocoding {city}, {state}: {e}")
        return None

# Add shapefile for county and city boundaries
county_gdf = gpd.read_file("D:\\News Project\\all the data sets\\map_county_data\\cb_2018_us_county_500k")  # Load the shapefile for counties
city_gdf = gpd.read_file("D:\\News Project\\all the data sets\\map_county_data\\cb_2018_01_cousub_500k")  # Load the shapefile for cities

# Create a Folium map centered around Alabama
alabama_coords = [33.5186, -86.8104]
map = folium.Map(location=alabama_coords, zoom_start=6, tiles="Cartodb Positron")

# Add county boundaries to the map
folium.GeoJson(
    county_gdf,
    name='County Boundaries',
    style_function=lambda x: {
        'fillColor': '#FFFAFA',
        'color': 'black',
        'weight': 1,
        'fillOpacity': 0.5,
    }
).add_to(map)

# Add city boundaries to the map
folium.GeoJson(
    city_gdf,
    name='City Boundaries',
    style_function=lambda x: {
        'fillColor': '#FFFAFA',
        'color': 'black',
        'weight': 1,
        'fillOpacity': 0.5,
    }
).add_to(map)

# Lists to track geocoding results
successful_geocodes = []
failed_geocodes = []

# Process and geocode locations
geocoded_locations = []
if locations:
    for loc_group in locations:
        loc_list = loc_group.split('/')
        
        for loc in loc_list:
            parts = loc.strip().rsplit(',', 1)  # Split by the last comma
            if len(parts) == 2:
                city = parts[0].strip()
                state = parts[1].strip()
                lat_lon = geocode_location(city, state)  # Geocode the city/state
                
                # Track geocoding results
                if lat_lon:
                    successful_geocodes.append((city, state, lat_lon))
                    geocoded_locations.append({'city': city, 'state': state, 'lat': lat_lon[0], 'lon': lat_lon[1]})
                else:
                    failed_geocodes.append((city, state))

# Create a DataFrame from geocoded locations
geocoded_df = pd.DataFrame(geocoded_locations)

# Now let's add a Choropleth to color the map based on the number of occurrences of locations
location_count = geocoded_df.groupby(['city']).size().reset_index(name='count')

# Add the Choropleth layer
folium.Choropleth(
    geo_data=city_gdf,
    data=location_count,
    columns=['city', 'count'],   
    key_on='feature.properties.NAME',  # This depends on your geojson structure
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Location Frequency'
).add_to(map)

# Add markers for geocoded locations
for _, row in geocoded_df.iterrows():
    folium.Marker(
        location=[row['lat'], row['lon']],
        tooltip=f"{row['city']}, {row['state']}",
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(map)

# Save the map to an HTML file
map_file = 'news_locations_map.html'
try:
    map.save(map_file)
    print(f"Map has been saved as '{map_file}'")
except Exception as e:
    print(f"Error saving the map: {e}")

# Output geocoding results
print("Geocoding Results:")
print(f"\nSuccessfully geocoded locations ({len(successful_geocodes)}):")
for city, state, lat_lon in successful_geocodes:
    print(f"- {city}, {state}: {lat_lon}")

print(f"\nFailed to geocode locations ({len(failed_geocodes)}):")
for city, state in failed_geocodes:
    print(f"- {city}, {state}")

# Save failed geocodes to a text file for review
with open('failed_geocodes.txt', 'w') as f:
    for city, state in failed_geocodes:
        f.write(f"{city}, {state}\n")

print("Failed geocodes saved to 'failed_geocodes.txt'")

# Save successfully geocoded locations with coordinates to a CSV file
geocoded_df.to_csv('successful_geocodes.csv', index=False)
print(f"Successfully geocoded locations saved to 'successful_geocodes.csv'")
