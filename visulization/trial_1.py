import folium
import geopandas as gpd
import pandas as pd
from collections import Counter
import re
from folium import LinearColormap

# Function to extract city names from the location data
def extract_cities(location_str):
    # Use regex to match patterns that resemble cities followed by a state
    city_pattern = re.findall(r'([A-Za-z\s]+), [A-Za-z]+', location_str)
    return city_pattern

# Load the data
csv_file = "D:\\News Project\\all the data sets\\gpt\\wvua_news_gpt_trial_29.csv" # Update to your file path
df = pd.read_csv(csv_file)

# Drop any rows with missing location data
df = df.dropna(subset=['Locations'])

# Extract cities from the 'Locations' column
df['Cities'] = df['Locations'].apply(extract_cities)

# Flatten the list of cities and calculate their frequency
cities_list = [city for sublist in df['Cities'].tolist() for city in sublist]
city_counter = Counter(cities_list)

# Load the comprehensive city shapefile (for the entire US or relevant region)
city_gdf = gpd.read_file("D:\\News Project\\all the data sets\\map_county_data\\cb_2018_01_cousub_500k")  # Adjust to your shapefile

# Create a Folium map centered around a broader area
us_coords = [37.0902, -95.7129]  # Centered on the U.S.
mymap = folium.Map(location=us_coords, zoom_start=5)

# Get the min and max frequencies to set the color scale
min_freq = min(city_counter.values())
max_freq = max(city_counter.values())

# Define a sequential color map (blue gradient) using a linear scale
color_scale = LinearColormap(
    ['#deebf7', '#08306b'],  # Light blue to dark blue
    vmin=min_freq,
    vmax=max_freq,
    caption='Frequency of City Usage'
)

# Initialize lists to track unmapped locations and mapped locations
unmapped_locations = []
mapped_locations = []

# Function to style city polygons based on frequency
def style_function(feature):
    city_name = feature['properties']['NAME']
    frequency = city_counter.get(city_name, 0)

    # Use the color scale to assign a color based on frequency
    fill_color = color_scale(frequency) if frequency > 0 else '#ffffff'
    
    return {
        'fillColor': fill_color,
        'color': 'black',
        'weight': 1,
        'fillOpacity': 0.7,
    }

# Add city boundaries to the map for the entire shapefile
folium.GeoJson(
    city_gdf,
    name='City Boundaries',
    style_function=style_function,
    tooltip=folium.GeoJsonTooltip(fields=['NAME'], aliases=['City:'], localize=True)
).add_to(mymap)

# Process each city to check if it can be mapped
for city, count in city_counter.items():
    # Check if the city is in the GeoDataFrame
    if city in city_gdf['NAME'].values:
        # If it exists, save the coordinates and name for those successfully mapped
        mapped_locations.append({'City': city, 'Frequency': count})
    else:
        # If it doesn't exist, log the unmapped location
        unmapped_locations.append(city)

# Save the unmapped locations to a text file
with open('unmapped_locations.txt', 'w') as file:
    for location in unmapped_locations:
        file.write(f"{location}\n")

# Convert mapped locations to DataFrame for saving
mapped_df = pd.DataFrame(mapped_locations)
# Save the mapped locations to a CSV file
mapped_df.to_csv('mapped_locations.csv', index=False)

# Add the color scale to the map
color_scale.add_to(mymap)

# Add layer control
folium.LayerControl().add_to(mymap)

# Save the map to an HTML file
map_file = 'us_city_frequency_map_gradient.html'
mymap.save(map_file)
print(f"Map saved as {map_file}")

# Output the frequency of each city for verification
print("City Frequencies:")
for city, count in city_counter.items():
    print(f"{city}: {count}")

# Save a file with the total mapped locations and their frequencies
total_mapped_file = 'total_mapped_locations.txt'
with open(total_mapped_file, 'w') as file:
    for city in mapped_locations:
        file.write(f"{city['City']}: {city['Frequency']}\n")

print(f"Unmapped locations saved to 'unmapped_locations.txt'")
print(f"Mapped locations saved to 'mapped_locations.csv'")
print(f"Total mapped locations saved to 'total_mapped_locations.txt'")
