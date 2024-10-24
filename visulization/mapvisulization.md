```python
import requests
import folium
import pandas as pd
from geopy.geocoders import GoogleV3
import geopandas as gpd

# File path to your CSV file
csv_file = "D:\\News Project\\all the data sets\\gpt\\wvua_news_gpt_trial_28.csv"

# Insert your Google Maps API Key here
API_KEY = 'AIzaSyChg3ArAuJhYKEY2mv_CVOWHYYJ1tFHhvA'  # Add your Google API Key

# Initialize the geocoder
geolocator = GoogleV3(api_key=API_KEY)

# Function to safely read a CSV file
def read_csv_file(file_path):
    try:
        # Use on_bad_lines='skip' to ignore problematic lines
        df = pd.read_csv(file_path, encoding='ISO-8859-1', on_bad_lines='skip')
        return df
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None

# Read the CSV file
df = read_csv_file(csv_file)

# Check if the dataframe was loaded successfully
if df is not None:
    locations = df['Locations'].dropna().tolist()
else:
    print("Error: Dataframe could not be loaded.")
    locations = []

# Function to geocode a location using Google Maps API
def geocode_location(location):
    try:
        location_data = geolocator.geocode(location)
        if location_data:
            return (location_data.latitude, location_data.longitude)
        else:
            print(f"Location not found: {location}")
            return None
    except Exception as e:
        print(f"Error geocoding {location}: {e}")
        return None

# Create a Folium map centered around Alabama
alabama_coords = [33.5186, -86.8104]
map = folium.Map(location=alabama_coords, zoom_start=6)

# Path to the GeoJSON file containing county boundaries
geojson_file = "C:\\Users\\ADARSH G\\Downloads\\updated_geojson_file.geojson"

# Load GeoJSON data
try:
    gdf = gpd.read_file(geojson_file)
except Exception as e:
    print(f"Error loading GeoJSON file: {e}")
    gdf = None

# Plot the locations on the map if the GeoJSON file is loaded
if gdf is not None and locations:
    for location in locations:
        lat_lon = geocode_location(location)
        if lat_lon:
            for _, region in gdf.iterrows():
                # Check if the location is within the region's geometry
                if region.geometry.contains(gpd.points_from_xy([lat_lon[1]], [lat_lon[0]])[0]):
                    # Add the region as a blue polygon to the map
                    folium.GeoJson(
                        region.geometry,
                        style_function=lambda x: {'fillColor': 'blue', 'color': 'blue', 'weight': 2, 'fillOpacity': 0.5},
                        tooltip=location
                    ).add_to(map)
                    break
else:
    print("Error: No locations to plot or GeoJSON data not available.")

# Save the map to an HTML file
map_file = 'news_locations_map_2.html'
try:
    map.save(map_file)
    print(f"Map has been saved as '{map_file}'")
except Exception as e:
    print(f"Error saving the map: {e}")



```

    Unexpected exception formatting exception. Falling back to standard exception
    

    Traceback (most recent call last):
      File "C:\Users\ADARSH G\anaconda3\envs\adarsh_trial\Lib\site-packages\IPython\core\interactiveshell.py", line 3577, in run_code
        exec(code_obj, self.user_global_ns, self.user_ns)
      File "C:\Users\ADARSH G\AppData\Local\Temp\ipykernel_5968\3062520611.py", line 2, in <module>
        import folium
    ModuleNotFoundError: No module named 'folium'
    
    During handling of the above exception, another exception occurred:
    
    Traceback (most recent call last):
      File "C:\Users\ADARSH G\anaconda3\envs\adarsh_trial\Lib\site-packages\IPython\core\interactiveshell.py", line 2168, in showtraceback
        stb = self.InteractiveTB.structured_traceback(
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "C:\Users\ADARSH G\anaconda3\envs\adarsh_trial\Lib\site-packages\IPython\core\ultratb.py", line 1457, in structured_traceback
        return FormattedTB.structured_traceback(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "C:\Users\ADARSH G\anaconda3\envs\adarsh_trial\Lib\site-packages\IPython\core\ultratb.py", line 1348, in structured_traceback
        return VerboseTB.structured_traceback(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "C:\Users\ADARSH G\anaconda3\envs\adarsh_trial\Lib\site-packages\IPython\core\ultratb.py", line 1195, in structured_traceback
        formatted_exception = self.format_exception_as_a_whole(etype, evalue, etb, number_of_lines_of_context,
                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "C:\Users\ADARSH G\anaconda3\envs\adarsh_trial\Lib\site-packages\IPython\core\ultratb.py", line 1110, in format_exception_as_a_whole
        frames.append(self.format_record(record))
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "C:\Users\ADARSH G\anaconda3\envs\adarsh_trial\Lib\site-packages\IPython\core\ultratb.py", line 992, in format_record
        frame_info.lines, Colors, self.has_colors, lvals
        ^^^^^^^^^^^^^^^^
      File "C:\Users\ADARSH G\anaconda3\envs\adarsh_trial\Lib\site-packages\IPython\core\ultratb.py", line 804, in lines
        return self._sd.lines
               ^^^^^^^^^^^^^^
      File "C:\Users\ADARSH G\AppData\Roaming\Python\Python312\site-packages\stack_data\utils.py", line 145, in cached_property_wrapper
        value = obj.__dict__[self.func.__name__] = self.func(obj)
                                                   ^^^^^^^^^^^^^^
      File "C:\Users\ADARSH G\AppData\Roaming\Python\Python312\site-packages\stack_data\core.py", line 734, in lines
        pieces = self.included_pieces
                 ^^^^^^^^^^^^^^^^^^^^
      File "C:\Users\ADARSH G\AppData\Roaming\Python\Python312\site-packages\stack_data\utils.py", line 145, in cached_property_wrapper
        value = obj.__dict__[self.func.__name__] = self.func(obj)
                                                   ^^^^^^^^^^^^^^
      File "C:\Users\ADARSH G\AppData\Roaming\Python\Python312\site-packages\stack_data\core.py", line 677, in included_pieces
        scope_pieces = self.scope_pieces
                       ^^^^^^^^^^^^^^^^^
      File "C:\Users\ADARSH G\AppData\Roaming\Python\Python312\site-packages\stack_data\utils.py", line 145, in cached_property_wrapper
        value = obj.__dict__[self.func.__name__] = self.func(obj)
                                                   ^^^^^^^^^^^^^^
      File "C:\Users\ADARSH G\AppData\Roaming\Python\Python312\site-packages\stack_data\core.py", line 614, in scope_pieces
        scope_start, scope_end = self.source.line_range(self.scope)
                                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "C:\Users\ADARSH G\AppData\Roaming\Python\Python312\site-packages\stack_data\core.py", line 178, in line_range
        return line_range(self.asttext(), node)
                          ^^^^^^^^^^^^
    AttributeError: 'Source' object has no attribute 'asttext'
    

    Location not found: Princeton, Walker
    Location not found: Gordo, Northport
    Location not found: Gordo, Northport
    Location not found: beach, Gulf Coast
    Location not found: Hay Court Apartments
    Location not found: Hay Court Apartments
    Location not found: Selma, Montgomery
    Location not found: Prichard
    Location not found: Jackson
    Location not found: UAB Hospital
    Location not found: Fosters
    Location not found: Hoover
    Location not found: University Medical Center
    Location not found: Post Home
    Location not found: Jackson, Southern, James Madison
    Location not found: WVUA, Farmer's Market
    Location not found: City1, County1
    Location not found: Meridian
    Location not found: Hoover
    Location not found: Gordo
    Location not found: City1
    Location not found: SEC
    Location not found: Gordo
    Location not found: Fairfield, Selma
    Location not found: Mobile
    Location not found: none
    Location not found: Fountain, Limestone, Bullock
    Location not found: Northside
    Location not found: Jasper
    Location not found: Brookwood
    Location not found: D.C.
    Location not found: Urban Cookhouse
    Location not found: Marion
    Location not found: Woodstock
    Location not found: Kentuck, Hotel Indigo
    Location not found: Brookwood
    Location not found: Gordo
    Location not found: RISE Center
    Location not found: Brookwood
    Location not found: Brookwood, Warrior Met Coal
    Location not found: Bessemer
    Location not found: Brookwood
    Location not found: Hightown, Bicentennial Square, Government Plaza
    Location not found: Fayette, Berry
    Location not found: Brookwood
    Location not found: UAB Hospital
    Location not found: Montgomery, Mobile
    Location not found: Gordo Elementary
    Location not found: Winfield
    Location not found: Weeping Mary, Holt
    Location not found: Bessemer
    Location not found: Helena
    Location not found: University Medical Center
    Location not found: University Mall
    Location not found: Bessemer
    Location not found: City1
    Location not found: 67 counties
    Location not found: University Medical Center
    Location not found: CVS Pharmacy
    Location not found: MONTGOMERY, Lee County
    Location not found: Reform
    Location not found: Midtown
    Location not found: Bookwood
    Location not found: UAB, Stanford
    Location not found: University Medical Center
    Location not found: Winfield
    Location not found: MOBILE
    Location not found: Notre Dame, Northwestern, Tulane
    Location not found: Austin, Jackson
    Location not found: Clay
    Location not found: Allen
    Location not found: Mobile
    Location not found: University Medical Center
    Location not found: Bessemer
    Location not found: Reform
    Location not found: University, Conference
    Location not found: Mobile
    Location not found: Jackson
    Location not found: City1
    Location not found: Montgomery County, Jefferson County
    Location not found: Mobile
    Location not found: Charlotte, Monroe
    Location not found: University Medical Center
    Location not found: Helena
    Location not found: City1, County1
    Location not found: UAB Hospital
    Location not found: City1
    Location not found: Marion
    Location not found: Weeping Mary A.M.E Zion
    Location not found: Northport, Holt
    Location not found: Jasper
    Location not found: WVUA 23 News studio
    Location not found: Marion
    Location not found: UAB Hospital
    Location not found: City1
    Location not found: City1
    Location not found: UAB Hospital
    Location not found: D.C.
    Location not found: Cadillac, Chevrolet, GMC
    Location not found: Estero
    Location not found: GasBuddy
    Location not found: MOBILE
    Location not found: City1
    Location not found: Mobile
    Location not found: Mobile
    Location not found: Hoover
    Location not found: UAB Hospital
    Location not found: Montgomery, Mobile, Baldwin, Monroe
    Location not found: Brookwood
    Location not found: Jackson
    Location not found: Hurricane Zeta, Gulf Coast
    Location not found: Halloweentown
    Location not found: Foley
    Location not found: Gordo, Oak Grove
    Location not found: Meridian
    Location not found: Mobile
    Location not found: Mobile
    Location not found: University Medical Center
    Location not found: UA
    Location not found: JACKSON
    Location not found: Sanford
    Location not found: MOBILE
    Location not found: Limestone
    Location not found: UAB Hospital
    Location not found: University Medical Center
    Location not found: D.C.
    Location not found: D.C.
    Location not found: Oakman, Shoal Creek Mine
    Location not found: Troy, Montgomery County
    Location not found: Jackson, Howard
    Location not found: World of Beer, Moe's Original Barbeque
    Location not found: Jackson
    Location not found: Kindred
    Location not found: Northport, Brookwood
    Location not found: Columbia
    Location not found: Mobile
    Location not found: Brookwood
    Location not found: Jackson
    Location not found: Guin
    Location not found: Rockies, East
    Location not found: Bradley, Hamilton
    Location not found: Morning Pointe
    Location not found: South
    Location not found: Jackson
    Location not found: Crunch Fitness
    Location not found: Isidore Newman School, Baton Rouge
    Location not found: Miramar, Jasper
    Location not found: Tannehill
    Location not found: JACKSON
    Location not found: Wages
    Location not found: Wenonah, Beauregard, Pinson Valley
    Location not found: JACKSON
    Location not found: Jackson
    Location not found: Sun Belt
    Location not found: JACKSON
    Location not found: Hoover
    Location not found: Wilder, Wallace
    Location not found: Jackson
    Location not found: Crimson Tide
    Location not found: Brookwood
    Location not found: Raymond Steele, Latasha Johnson, Chandra Mayes, Valarie Watkins, LaJeffery Carpenter, Larrie Coleman, Jacquline Stewart
    Location not found: Beulah, Westside
    Location not found: UAB Medicine
    Location not found: JACKSON
    Location not found: Woodstock
    Location not found: Holy Spirit Catholic School
    Location not found: City1
    Location not found: County
    Location not found: Jackson
    Location not found: JACKSON
    Location not found: Montgomery, Mobile
    Location not found: Montgomery, Jackson County
    Location not found: JACKSON
    Location not found: Mission
    Location not found: Ohio State, Penn State
    Location not found: Crowley
    Location not found: Mount Pilgrim Baptist Church
    Location not found: 55 schools
    Location not found: JACKSON
    Location not found: Treasure Island
    Location not found: Jackson
    Location not found: City1
    Location not found: JACKSON
    Location not found: Jackson
    Location not found: JACKSON
    Location not found: Jackson
    Location not found: Mobile
    Location not found: UA
    Location not found: Liberty
    Location not found: Hurricane Creek
    Location not found: Children's Hospital
    Location not found: Montgomery, Jackson County
    Location not found: Strawberry, Marshall County
    Location not found: Clinton
    Location not found: Bear Creek Road, University Blvd. E.
    Location not found: Beulah, Maude Whatley Health Services
    Location not found: Hoover
    Location not found: Mobile
    Location not found: Reform
    Location not found: Jackson
    Location not found: Daystar Church
    Location not found: Bonita Terrace, Morrow
    Location not found: City1
    Location not found: Jefferson, Auburn
    Location not found: Jackson
    Location not found: Johns Hopkins University, Baylor College of Medicine
    Location not found: Jackson
    Location not found: Ozark
    Location not found: Jefferson, Mobile, Lee
    Location not found: Jackson
    Location not found: McMiller's barbershop
    Location not found: JACKSON
    Location not found: Jaycee Fairgrounds
    Location not found: Stephenson
    Error geocoding Richmond, Wilmington, Rehoboth Beach, Jakarta, Rijeka, Johannesburg, Cairo, Luxor, Berlin, Tokyo, Melbourne, Bangkok: HTTPSConnectionPool(host='maps.googleapis.com', port=443): Read timed out.
    Location not found: Jasper
    Location not found: Goodwater, Point Clear
    Location not found: Jackson
    Location not found: Crescent East
    Location not found: Homewood, Shorter
    Location not found: JACKSON
    Location not found: JACKSON
    Location not found: Jackson
    Location not found: Alabaster
    Location not found: Shelton
    Location not found: Mobile, Jefferson, Lee
    Location not found: Elmore
    Location not found: Mobile
    Location not found: JACKSON
    Location not found: MONTGOMERY, St. Clair
    Location not found: Mobile
    Location not found: Northport, Fayette
    Location not found: Druid City, Oz Music
    Location not found: Alabaster
    Location not found: Petal
    Location not found: HSWA
    Location not found: Montgomery, Montgomery County, Mobile
    Location not found: Montgomery, Washington County
    Location not found: Jackson
    Location not found: Jupiter
    Location not found: City1, City2
    Location not found: MOBILE
    Location not found: Samantha, Northport
    Location not found: Temerson Square
    Location not found: City, County
    Location not found: UAB Hospital
    Location not found: Alpha Tau chapter, Bridge Builder Foundation
    Location not found: City1
    Location not found: Capstone Dental Care, DCH Health System, DCH Regional Medical Center
    Location not found: Holy Spirit
    Location not found: Shelton
    Location not found: D.C.
    Location not found: Shelton
    Location not found: St. John
    Location not found: University Medical Center
    Location not found: Butler, Mobile, Marshall, Franklin
    Location not found: JACKSON
    Location not found: University Medical Center
    Location not found: Jasper
    Location not found: New Creations Salon
    Location not found: Gordo
    Location not found: Half Shell Oyster House
    Location not found: Circlewood
    Location not found: Hoover
    Location not found: Gary, Tide
    Location not found: Walker
    Location not found: University Medical Center
    Location not found: Fosters
    Location not found: MOBILE
    Location not found: Jasper
    Location not found: 1225
    Location not found: Vance
    Location not found: Southern Ale House, FIVE, Chuck's Fish, Habitat for Humanity, Wells family
    Location not found: City1
    Location not found: Temerson Square
    Location not found: City1
    Location not found: Vance
    Location not found: Montgomery, St. Clair, Bullock
    Location not found: City1
    Location not found: City1
    Location not found: Beulah
    Location not found: Walker, Jefferson
    Location not found: JACKSON
    Location not found: Woodstock
    Location not found: Bessemer
    Location not found: Black Belt
    Location not found: Palmetto, Orange County
    Location not found: Vista Farms, Fayette County
    Location not found: JACKSON
    Location not found: Jasper
    Location not found: City1
    Location not found: Vance
    Location not found: Southview
    Location not found: UAB Hospital
    Location not found: UA
    Location not found: City1
    Location not found: Clayton
    Location not found: Northport, Fayette
    Location not found: Bessemer
    Location not found: Jamison
    Location not found: Northstar, DCH
    Location not found: Shelton
    Location not found: City
    Location not found: Shelton
    Location not found: Bessemer
    Location not found: Jackson County, Jefferson County
    Location not found: Brian W. Whitfield Memorial Hospital
    Location not found: City1
    Location not found: Shelton
    Location not found: Ozark
    Location not found: Montgomery, Mobile
    Location not found: Mobile
    Location not found: city
    Location not found: Mobile
    Location not found: Five, Chuck's Fish
    Location not found: Dr. Edward Hillard Drive
    Location not found: Jackson, Clinton
    Location not found: Alabaster, Thompson
    Location not found: Montgomery, Trussville, Mobile
    Location not found: Brookwood
    Location not found: JACKSON
    Location not found: Warrior, Kimberly
    Location not found: Capitol School
    Location not found: Jackson
    Location not found: Matthews
    Location not found: Westlawn
    Location not found: Bessemer
    Location not found: Brandon
    Location not found: Christ Episcopal Church
    Location not found: Mobile
    Location not found: Boaz
    Location not found: Auburn, LSU, Texas A&M
    Location not found: Lakeland
    Location not found: South East
    Location not found: Park Manor Health and Rehabilitation Center
    Location not found: Selma, Montgomery
    Location not found: Kimberly
    Location not found: Brookwood
    Error geocoding Birmingham: HTTPSConnectionPool(host='maps.googleapis.com', port=443): Max retries exceeded with url: /maps/api/geocode/json?sensor=false&address=Birmingham&key=AIzaSyChg3ArAuJhYKEY2mv_CVOWHYYJ1tFHhvA (Caused by ReadTimeoutError("HTTPSConnectionPool(host='maps.googleapis.com', port=443): Read timed out. (read timeout=1)"))
    Location not found: Mobile
    Location not found: Bryant
    Location not found: City1, County1
    Location not found: Hoover
    Location not found: Hillcrest
    Location not found: Watson, George, Belcher, Steven George, Chylli Bruce
    Location not found: Farah Majid, WVUA 23
    Location not found: Mobile
    Location not found: Post 6022
    Location not found: Holman
    Location not found: Elmore
    Location not found: Lafayette
    Location not found: MOBILE
    Location not found: Shelton, Turning Point
    Location not found: Davis-Emerson
    Location not found: Boaz
    Location not found: Jefferson, Auburn
    Location not found: Christ Episcopal Church, Randall Hall
    Location not found: University Mall, Coleman Coliseum
    Location not found: Foley
    Location not found: MOBILE
    Location not found: Yellowhammer
    Location not found: Salvation Army
    Location not found: Bethel
    Location not found: Hillcrest
    Location not found: Mobile
    Location not found: Jasper
    Location not found: Temerson Square
    Location not found: Walker Elementary School
    Location not found: Ozark, Montgomery
    Location not found: Central, Avenue Pub
    Location not found: Ozark, Montgomery
    Location not found: Shelby
    Location not found: Jackson
    Location not found: Mobile
    Location not found: Plains
    Location not found: City1, City2
    Location not found: Moody
    Location not found: Myrtlewood
    Location not found: LSU, Bryant-Denny Stadium, Quad, Lloyd Hall, Moore Hall, University Boulevard, Colonial Drive, Reese Phifer Hall
    Location not found: Juul Labs
    Location not found: Jasper
    Location not found: Jasper
    Location not found: Mobile
    Location not found: Walker Elementary
    Location not found: 9th Street
    Location not found: Parrish, Baker Creek
    Location not found: Parrish, Baker Creek
    Location not found: Northport, Holt
    Location not found: Clayton, Marshall County
    Location not found: Jackson
    Location not found: Saint Mark United Methodist Church
    Location not found: City
    Location not found: Bryant, Hillcrest, Hueytown, James Clemens
    Location not found: Hercules, Northport
    Location not found: Woodstock
    Location not found: Calvary Baptist Church, District 4
    Location not found: Auburn, Alabaster
    Location not found: Montgomery, Alabaster, Troy
    Location not found: Camden, Selma
    Location not found: Cooper
    Location not found: Bowlero Bowling Alley
    Location not found: Smith Lake
    Location not found: City1
    Location not found: Northport, Fayette
    Location not found: Northport, Fayette
    Location not found: Cocoa
    Location not found: Bryant-Denny Stadium, Ole Miss
    Location not found: 15th Street, Greensboro Avenue, McFarland Boulevard, Paul W. Bryant Drive, Sixth Street, Seventh Street, Eighth Street, Stillman Boulevard, 11th Street, 25th Avenue, 14th Street
    Location not found: D.C.
    Location not found: Shelton, WVUA
    Location not found: Crossing Points, Shirley
    Location not found: Jackson
    Error geocoding Troy: HTTPSConnectionPool(host='maps.googleapis.com', port=443): Read timed out.
    Location not found: Turning Point
    Location not found: UA
    Location not found: Meridian
    Location not found: Mobile
    Location not found: City1
    Location not found: MOBILE
    Location not found: Watkins
    Location not found: Meridian
    Location not found: Boaz
    Location not found: Mobile, Axis
    Location not found: Mobile
    Location not found: Mobile
    Location not found: Crimson Tide, quad
    Location not found: Mobile
    Location not found: Annie Lavender, Ellen Potts
    Location not found: Bessemer
    Location not found: Jasper
    Location not found: Jasper, Montgomery
    Location not found: Jasper, Smith Lake
    Location not found: Carroline Shines Edwards
    Location not found: Jasper
    Location not found: Enterprise
    Location not found: Gordo
    Location not found: Montgomery, Mobile
    Location not found: The Townes, Edwards Circle
    Location not found: Morton
    Location not found: Hanceville, Black Warrior River
    Location not found: Mobile
    Location not found: City1, County1
    Location not found: WVUA 23
    Location not found: Osher Lifelong Learning Institute, WVUA 23
    Location not found: Shelton
    Location not found: Huffman, Jefferson County
    Location not found: Mobile
    Location not found: Lurleen Wallace Boulevard, University Boulevard, Hugh Thomas Bridge
    Location not found: Coker, Northport
    Location not found: Hoover
    Location not found: Montgomery, Mobile
    Location not found: Anderson, Hillcrest
    Location not found: Shelton, WVUA23
    Location not found: Matthews, Collins-Riverside
    Location not found: Baltimore, Jacksonville
    Location not found: WVUA 23
    Location not found: Bethel
    Location not found: Northport, Brookwood
    Location not found: City1
    Location not found: Hillcrest
    Location not found: Shelton, WVUA
    Location not found: Lafayette
    Location not found: Jasper
    Location not found: Shelton
    Location not found: Franklin, Marion, Walker, Winston
    Location not found: Smith Lake
    Location not found: Brookwood
    Location not found: The Zone, DCH
    Location not found: Shelton, WVUA
    Location not found: Thomasville
    Location not found: Bethel
    Location not found: Pelham, Indian Hills
    Location not found: University Mall
    Location not found: WVUA23
    Location not found: Jasper
    Location not found: Bowers Park
    Location not found: Samson
    Location not found: Independence
    Location not found: Jasper
    Location not found: Hoover
    Location not found: Rosedale
    Location not found: Coker, Druid City
    Location not found: Springbrook
    Location not found: Brookwood
    Location not found: Lakeland
    Location not found: Mobile
    Location not found: Shelton, WVUA23
    Location not found: Shelton
    Location not found: Hackensack, Villanova
    Location not found: Goodwater
    Location not found: Jasper
    Location not found: Ozark
    Location not found: Crunch Fitness
    Location not found: Shelton, WVUA23
    Location not found: Auburn, D.C.
    Location not found: City
    Location not found: Clifford Madison, Emmett Kyzer, Ed Stephens road
    Location not found: Lurleen B. Wallace Boulevard, University Boulevard, Paul W. Bryant Drive, 11th Street, 12th Street
    Location not found: none
    Location not found: Holy Spirit Catholic High School
    Location not found: City1
    Location not found: Northport, Coker
    Location not found: WVUA 23
    Location not found: Bryant
    Location not found: University Boulevard, Lurleen Wallace Boulevard, Midtown Village
    Location not found: Shelton
    Location not found: University Blvd, Red Drew Avenue, The Hub Apartment Complex
    Location not found: Shelton
    Location not found: Panama City, Pike County
    Location not found: Montgomery, Mobile
    Location not found: Locust Fork, Black Warrior River basin
    Location not found: Bibb, Dallas, Hale, Perry, Wilcox
    Location not found: Crestmont, Northport
    Location not found: county
    Location not found: Montgomery, Mobile
    Location not found: Bar 17, West Park Florist
    Location not found: Montgomery, Mobile
    Location not found: Shelton
    Location not found: Bryant
    Location not found: Montgomery, Washington County
    Location not found: McFarland Boulevard, Meadowbrook Shopping Center, Wright Plaza South, Skyland boulevards
    Location not found: Target
    Location not found: Turning Point
    Location not found: Jefferson State
    Location not found: Arcadia, Midtown Village
    Location not found: Montgomery, Mobile
    Location not found: Marion
    Location not found: Foley
    Location not found: Mobile
    Location not found: City1
    Location not found: Bryant High School
    Location not found: Bryant
    Location not found: Walker, Northport
    Location not found: Montgomery, Mobile
    Location not found: Capitol School
    Location not found: Walker Elementary School
    Location not found: Bryant, Crimson Village, Ollie
    Location not found: Mobile
    Location not found: Hillcrest High School, Community Soup Bowl
    Location not found: Wilhagen's Bar and Grill
    Location not found: Jackson County, Harrison County, Hancock County
    Location not found: Shelton, WVUA
    Location not found: Sipsey Valley
    Location not found: Pickwick Lake, Sardis, Arab
    Location not found: Shelton, Englewood
    Location not found: Romulus
    Location not found: Eagle's Wings, Indian Hills Country Club
    Location not found: Jupiter
    Location not found: Shelton, Central High
    Location not found: Eastwood
    Location not found: Capitol School
    Location not found: Hillcrest
    Location not found: MONTGOMERY, Range
    Location not found: Hillcrest High School, Mercedes-Benz, Shelton State Community College
    Location not found: Woodstock
    Location not found: Holt
    Location not found: Loxley, Mobile
    Location not found: North River
    Location not found: Parrish
    Location not found: Hurricane Creek, Holt Peterson, Jack Warner Parkway, Highway 216
    Location not found: Brookwood
    Location not found: Mount Pilgrim Baptist Church, Braxton
    Location not found: Shelton
    Location not found: Montgomery, Range
    Location not found: Shelton, Martin
    Location not found: Mobile
    Location not found: Atmore, St. Clair, Holman
    Location not found: Leland
    Location not found: Alex Trebek
    Location not found: Montgomery, Mobile
    Location not found: City1
    Location not found: none
    Location not found: Central Elementary
    Location not found: Hamilton
    Location not found: Montgomery, Lee High School
    Location not found: Fosters
    Location not found: D.C.
    Location not found: Montgomery, Lee High School
    Location not found: Shelton, WVUA
    Location not found: Central Elementary
    Location not found: Seventh Street, Vance
    Location not found: Linden, Montgomery
    Location not found: Jasper, Little Rock
    Location not found: Shelton
    Location not found: Sipsey Valley, Coker, Mt. Olive
    Location not found: Manderson
    Location not found: Valley View, Shelton
    Location not found: Shelton, WVUA
    Location not found: Stone Creek
    Location not found: Montgomery, Autauga, Chilton, Elmore
    Location not found: Hoover, Montgomery, Birmingham
    Location not found: Studio, Kentuck Art Center
    Location not found: WVUA 23
    Location not found: Mobile
    Location not found: Big Sandy
    Location not found: Vance
    Location not found: North River, Shelton
    Location not found: Decorrin Johnson
    Location not found: Montgomery, St. Clair
    Location not found: D.C.
    Location not found: Summit
    Location not found: Mobile, West Mobile
    Location not found: Washington Street
    Location not found: Mobile
    Location not found: City1
    Location not found: Shelton, WVUA
    Location not found: Studio
    Location not found: Holt
    Location not found: Grace Presbyterian Church, Community Soup Bowl
    Location not found: Winfield, Jasper, Wise
    Location not found: Bessemer
    Location not found: Bagley, Jefferson County
    Location not found: Mobile, Baldwin
    Location not found: Auburn, Texas A&M
    Location not found: Montgomery, Mobile
    Location not found: University Programs, Ferguson Student Center, UA
    Location not found: Mobile
    Location not found: Fosters
    Location not found: Hoover
    Location not found: Hoover
    Location not found: Oakdale, Northport
    Location not found: City1
    Location not found: Capitol Park
    Location not found: Sanford
    Location not found: Betty Shirley, Rise Center, Friends at Bryce, Mental Health Board
    Location not found: Gordo
    Location not found: Shelton
    Location not found: Shelton
    Location not found: Northport, Smith Lake
    Location not found: University Mall
    Location not found: Buele
    Location not found: Shelton, WVUA
    Location not found: Morning Pointe
    Location not found: Sprayberry
    Location not found: Hoover
    Location not found: Mobile
    Location not found: University Mall
    Location not found: Mobile
    Location not found: Chuck's Fish
    Location not found: Jasper
    Location not found: Beulah, Brascomb, Forrester Gardens, Bonita Terrace
    Location not found: City1
    Location not found: Brown's Nursery
    Location not found: Shelton
    Location not found: Sipsey Valley
    Location not found: Oakman, Pike County
    Location not found: City1
    Location not found: Bryant
    Location not found: Shelton, WVUA
    Location not found: Holt
    Location not found: Veterans Memorial Park, University Mall
    Location not found: City1
    Location not found: Sipsey Valley High School
    Location not found: Brookwood
    Location not found: Jasper, St. James, Birmingham
    Location not found: Shelton
    Location not found: Mobile
    Location not found: Tannehill
    Location not found: Lantana
    Location not found: City1
    Location not found: Mobile
    Location not found: Westwood
    Location not found: Tannehill
    Location not found: Crimson Bar
    Location not found: Jasper
    Location not found: Black Warrior
    Location not found: Shelton
    Location not found: Northport, Clear Creek Colony
    Location not found: Sonya Kemp
    Location not found: Shelton
    Location not found: Jasper
    Location not found: University Mall
    Location not found: Myrtlewood
    Location not found: Skyland Boulevard, Exit 76
    Location not found: Shelton
    Location not found: Maxwell
    Location not found: Woodstock, Ace Park
    Location not found: City1, County1
    Location not found: Brookwood
    Location not found: Parrish, Jasper, Dora, Walker
    Location not found: Shelton
    Location not found: Brookwood
    Location not found: Carolinas
    Location not found: City1
    Location not found: Angel Eaton, Dairy Queen
    Location not found: Jasper
    Location not found: Amazon
    Location not found: Jasper
    Location not found: Brookwood
    Location not found: Shelton
    Location not found: Westlawn
    Location not found: Carolina
    Location not found: Stillman College, Hay Center
    Location not found: Shelton
    Location not found: TheKentuck Art Center
    Location not found: City1, County1
    Location not found: Pickens, Fayette, Reform
    Location not found: Shelton
    Location not found: Culverhouse
    Location not found: Reform
    Location not found: Labor Day
    Location not found: JACKSON
    Location not found: Brookwood
    Location not found: Hoover
    Location not found: Moundville, Prince
    Location not found: Summit
    Location not found: Arab
    Location not found: Brookwood
    Location not found: Crestmont, Northport
    Location not found: Vance
    Location not found: Northside, Phillips, Bigham
    Location not found: Unity Grove, Reform
    Location not found: Perry, Wilcox
    Location not found: Keller Williams
    Location not found: Parrish, Oakman, Cordova
    Location not found: Palmetto
    Location not found: Shelton
    Location not found: District 21, District 89
    Location not found: Post 6022, Moose Lodge
    Location not found: Northport, Clear Creek
    Location not found: Holt, Forest Lake
    Location not found: Skyy Boxing Gym
    Location not found: Coker
    Location not found: Central Church of Christ
    Location not found: Jason's Deli
    Location not found: Parrish, Montgomery
    Location not found: Bessemer
    Location not found: Douglas, Crump
    Location not found: Los Gatos
    Location not found: Shelton
    Location not found: Holt
    Location not found: Shelton
    Location not found: United
    Location not found: 23rd Street, DCH Regional Hospital
    Location not found: Capitol School
    Location not found: Henry's Burgers, Craw Daddy Dave's
    Location not found: Ave Maria
    Location not found: Parrish, Adamsville
    Location not found: Shelton, The Dome
    Location not found: 11th Circuit Court
    Location not found: Shelton, Martin
    Location not found: Vance
    Location not found: Ralph
    Location not found: Central, Westlawn
    Location not found: Maylene, Auburn
    Location not found: Selma, Mobile
    Location not found: Midtown
    Location not found: Brookwood
    Location not found: City1
    Location not found: Shelton, Bevill
    Location not found: Montgomery, Jackson County
    Location not found: Jasper
    Location not found: Hillcrest High School, Druid City Hospital
    Location not found: Shelton
    Location not found: Montgomery, Mobile
    Location not found: Holt
    Location not found: Shelton
    Location not found: Brookwood
    Location not found: Brookwood, Collins-Riverside
    Location not found: Collins-Riverside, University Boulevard, Gene Stallings Avenue, Black Warrior River
    Location not found: City1
    Location not found: Gravy Train, Kibbles "N Bits, Ol' Roy, Skippy
    Location not found: Elizabeth
    Location not found: Samantha
    Location not found: Matthews
    Location not found: Montgomery, Oxford
    Location not found: UA
    Location not found: Holt
    Location not found: Parrish
    Location not found: Hillcrest, Northside, Midtown
    Location not found: Jasper
    Location not found: Oz Music
    Location not found: Donna Smith, Nick's Kids, Habitat for Humanity
    Location not found: Woodstock
    Location not found: Woodstock
    Location not found: City1
    Location not found: Brookwood, Stone Ridge Subdivision
    Location not found: Gordo
    Location not found: City1, County1
    Location not found: Vance
    Location not found: Hillcrest High School, Valley View
    Location not found: Super 7
    Location not found: Vance
    Location not found: JACKSON
    Location not found: Creekwood Village Apartments, Stillman College
    Location not found: Malaya, Shane
    Location not found: UA
    Location not found: Vance
    Location not found: Bryant, Indian Hills
    Location not found: Coker
    Location not found: Oak Hill, Westlawn
    Location not found: 18th Street, Crescent Ridge Road, DCH Medical Center
    Location not found: Martin Luther King Jr. Elementary, Beulah Baptist Church, public library, Boys and Girls Club, First United Methodist Church
    Location not found: Jasper, Northport
    Location not found: Capitol Park
    Location not found: Capitol Park
    Location not found: Fayette, Pickens, Bibb, Reform
    Location not found: Hurricane Harvey
    Location not found: TPD, DCH
    Location not found: Harvey
    Location not found: Hurricane Creek
    Location not found: Bowers Park
    Location not found: Central High School, Jeff Sessions
    Location not found: Fayette, Lamar, Pickens
    Location not found: Ashland, Vincent
    Location not found: Summit, Shelton, Lawson
    Location not found: University Medical Center
    Location not found: Shelton
    Location not found: Moshi
    Location not found: Mobile
    Location not found: Bryant
    Location not found: WVUA
    Location not found: Jasper, Birmingham
    Location not found: Charles Sexton, Stacey Waldman, Nicol
    Location not found: Jasper, Carbon Hill
    Location not found: Bessemer
    Location not found: Woodstock
    Location not found: Turner
    Location not found: Brookwood
    Location not found: Highway 69 North
    Location not found: University of Alabama, Ferguson Center Theater, Ferguson Student Center, Bryant Denny Stadium
    Location not found: Christian Clay Perkins
    Location not found: Philadelphia, Samantha
    Location not found: Northport, Samantha
    Location not found: Bear Creek
    Location not found: Gordo, Durham
    Location not found: Sipsey Valley
    Location not found: WVUA 23
    Location not found: Gordo, Durham
    Location not found: Jasper
    Location not found: Holt
    Location not found: Selma, Montgomery
    Location not found: UA
    Location not found: District 63
    Location not found: Romulus, Northport
    Location not found: Selma, Montgomery
    Location not found: Animal Butter, Epiphany Farm-to-Fork
    Location not found: Alberta, University Boulevard, Bel Air Motel, Wrights Restaurant, Advanced Auto Parts
    Location not found: Brown's Nursery
    Location not found: Dora
    Location not found: Jasper
    Location not found: City1, County1
    Location not found: Crimson Student Living, Central High School
    Location not found: Big Sandy Elementary School
    Location not found: Sipsey Valley
    Location not found: Highway 82, 26th Avenue, Highway 69
    Location not found: Albany, McFarland Blvd
    Location not found: Skyland Boulevard, Highway 69, Cobb Hollywood 16, Hillcrest High School
    Location not found: Jasper
    Location not found: Big Sandy
    Location not found: Westlawn
    Location not found: Bessemer
    Location not found: Jackson Hewitt
    Location not found: City1
    Location not found: Meadowbrook Apartments, Taco Casa
    Location not found: Northport, Willowbrook
    Location not found: Mobile
    Location not found: Maxwell
    Location not found: WVUA 23
    Location not found: Fosters
    Location not found: Spencer
    Location not found: Jasper
    Location not found: Jasper
    Location not found: Fields Crossing, Braelinn Village
    Location not found: University Strip
    Location not found: MOBILE
    Location not found: Montgomery, Lee County
    Location not found: CHILI
    Location not found: WVUA 23
    Location not found: Midtown Village, Northport
    Location not found: Helena
    Location not found: Alabaster, Midfield
    Location not found: Fosters, Benevola, Pickens, Gordo, Auburn
    Location not found: Brookwood
    Location not found: Montgomery, Lee County
    Location not found: Skyland
    Location not found: Snead
    Location not found: Selma, Safford
    Location not found: Mount Olive, Brookwood
    Location not found: Black Belt
    Location not found: Campus
    Location not found: Grand at Rum Creek
    Location not found: Cheddar's Scratch Kitchen
    Location not found: Crescent East
    Location not found: Brunswick
    Location not found: Manhattan, Linden, Chelsea, Elizabeth
    Location not found: Brookwood
    Location not found: Northport, Brent
    Location not found: City
    Location not found: City
    Location not found: Starbucks
    Location not found: Angel Eaton, Kim, Florida Georgia Line, Monk
    Location not found: Northside High School
    Location not found: Midtown
    Location not found: Brookwood, Gordo
    Location not found: Brookwood
    Location not found: Hoover
    Location not found: Montgomery, Walker County
    Location not found: Montgomery, Greene County
    Location not found: Central Elementary School
    Location not found: Jasper
    Location not found: Vance
    Location not found: Northport, Grand Pointe
    Location not found: 51st Street East
    Location not found: Northridge, Munny Sokol Park
    Location not found: Brandon, B-F Goodrich
    Location not found: Mobile
    Location not found: Paul Bryant Drive, 12th street
    Location not found: Montgomery, Lee County
    Location not found: Holt
    Location not found: Mobile
    Location not found: Montgomery, Lee County
    Location not found: Shelton
    Location not found: Exit 79
    Location not found: University Mall
    Location not found: Daphne
    Location not found: City1
    Location not found: Mercedes
    Location not found: Montgomery, Mobile
    Location not found: University of Alabama, Bryant-Denny Stadium, Phi Kappa Psi house, Butler Field
    Location not found: Montgomery, Mobile
    Location not found: Decatur, Courtland
    Location not found: Gordo
    Location not found: Hoover
    Location not found: 15th Street, Hackberry Lane
    Location not found: Spring
    Location not found: Monroe
    Location not found: Montgomery, Mobile
    Location not found: Capitol School, Capitol Park
    Location not found: Gordo, Durham
    Location not found: Hillcrest
    Location not found: Springbrook, McFarland Boulevard, Albright Road
    Location not found: BLG Academy
    Location not found: Central Elementary School
    Location not found: Catfish County
    Location not found: Westwood, Bama
    Location not found: Montgomery, Leni Young
    Location not found: Bryant, Jackson
    Location not found: College Hill, Alberta, University Church of Christ, Belk Activity Center
    Location not found: Rosedale Court, Rosedale Apartments
    Location not found: Montgomery, Mobile
    Location not found: Gordo, Durham
    Location not found: Alabama's Museum of Natural History
    Location not found: Jasper, Sipsey
    Location not found: City
    Location not found: Cordova
    Location not found: Maxwell
    Location not found: Northwoods Crossing Shopping Center
    Location not found: Brookside
    Location not found: Mobile
    Location not found: Creekwood Village Apartments, DCH Regional Medical Center
    Location not found: Romulus
    Location not found: Gary, Crimson Tide
    Location not found: Crimson Tide, New England, Philadelphia
    Location not found: Verner Elementary
    Location not found: Governor Bentley, Spencer Collier, Mike Hubbard, Mason
    Location not found: Spencer, Bentley
    Location not found: Perry County, Francis Marion
    Location not found: Montgomery, Range
    Location not found: Jefferson, Shelby, Morgan
    Location not found: Jasper
    Location not found: Bessemer
    Location not found: Clayton, HMT, Inc.
    Location not found: Fosters
    Location not found: city, county
    Location not found: Hoover
    Location not found: Midtown Village, Northport
    Location not found: County
    Location not found: Dothan, Perry County, Marion County
    Location not found: Hoover
    Location not found: Mobile
    Location not found: Oxford, Ranburne
    Location not found: Brookwood
    Location not found: Brookwood
    Location not found: Cynthia Almond
    Location not found: Jasper
    Location not found: Brookwood
    Location not found: Brookwood
    Location not found: Mobile
    Location not found: Selma, Forkland, Linden
    Location not found: Brookwood
    Location not found: Stevenson
    Location not found: City1
    Location not found: Brookwood
    Location not found: Northport, Coker
    Location not found: Montgomery, Mobile
    Location not found: 11th Avenue, Aspen Village
    Location not found: Title Town
    Location not found: City1
    Location not found: Vance
    Location not found: Alberta, University Boulevard
    Location not found: City Council
    Location not found: Holidays on the River
    Location not found: Jim Walter Resources
    Location not found: Beulah
    Location not found: Brookwood
    Location not found: Hoover
    Location not found: Green Village
    Location not found: Trinity, Lawrence County
    Location not found: Mobile
    Location not found: Prichard
    Location not found: Fosters, Northport
    Location not found: Bessemer
    Location not found: Bessemer
    Location not found: Stillman College, Hay Hall Dorm
    Location not found: Montgomery, Mobile, Pike Road
    Location not found: Mobile
    Location not found: Montgomery, Lee, Russell
    Location not found: Style Connection, 23rd avenue
    Location not found: Honda, Takata
    Location not found: University Boulevard
    Location not found: Brookwood
    Location not found: Vance
    Location not found: Broadmoore Gardens, James I Harrison Parkway
    Location not found: Coker
    Location not found: Moulton, Sipsey Wilderness
    Location not found: Northport, Coker
    Location not found: City1
    Location not found: Brookwood
    Location not found: Oak Hill
    Location not found: Coker
    Location not found: Opp
    Location not found: Mobile
    Location not found: University Boulevard
    Location not found: UA, Crimson Tide
    Location not found: Hoover
    Location not found: Brookwood
    Location not found: Jasper
    Location not found: Brookwood
    Location not found: town
    Location not found: Columbia
    Location not found: Northport, Valley
    Location not found: Stillman, Lane College
    Location not found: North River Christian Academy, Charger Park
    Location not found: City1
    Location not found: Brookwood
    Location not found: City
    Location not found: Holt
    Location not found: Dora
    Location not found: Bessemer
    Location not found: Bessemer
    Location not found: Rice Mine Road, Old Colony Road, Bryant Bridge, Cypress Inn
    Location not found: WVUA 23
    Location not found: Jackson Avenue
    Location not found: Alberta, Leland Lanes
    Location not found: Southern Ale House, Children's Hospital
    Location not found: Woodstock
    Location not found: Central Elementary School
    Location not found: Ralph, Fosters
    Location not found: City, County
    Location not found: City Council Meeting
    Location not found: Coker
    Location not found: Union Springs, Montgomery County, Calhoun County
    Location not found: Northport, Berry
    Location not found: City1
    Location not found: Virginia Essary Durden, Lee Wilson Durden
    Location not found: Gordo, Perrigan
    Location not found: Buffalo Rock
    Location not found: Montgomery, Elmore, Madison
    Location not found: Montgomery, Montgomery County, Ferguson
    Location not found: MOBILE
    Location not found: District One
    Location not found: Jasper
    Location not found: Joseph Brown, WVUA
    Location not found: Hoover, Brookwood
    Location not found: Shelton, WVUA
    Location not found: MOBILE
    Location not found: City1
    Location not found: City1
    Location not found: Green Pond
    Location not found: Holt Elementary School, County
    Location not found: Seller's Auditorium, Bryant Conference Center
    Location not found: James I. Harrison Jr. Parkway
    Location not found: Fosters
    Location not found: Yellowstone National Park, Biscuit Basin, Old Faithful Geyser, Mary Bay, Black Diamond Pool, Sapphire Pool, Hebgen Lake, Helena, Billings
    Location not found: City1
    Location not found: Los Gatos
    Location not found: Arlington, Redding, Dallas, Boston
    Location not found: Paris, West London
    Location not found: ConocoPhillips, Marathon Oil
    Location not found: D.C.
    Location not found: Boston, Dallas, Allen
    Location not found: Merrimack
    Location not found: Stanford, Lund
    Location not found: Mark Hotel, The Metropolitan Museum of Art
    Location not found: Norwich, Baltimore
    Location not found: Johns Hopkins, Baylor University, Weill Cornell Medical College
    Error geocoding Malm, Liverpool: Non-successful status code 400
    Error geocoding Paris, Besanon: Non-successful status code 400
    Location not found: Peterborough, London
    Location not found: Cybertruck
    Location not found: Philadelphia, Phoenix
    Location not found: Dallas, Mount Sinai
    Location not found: Montgomery, Mobile
    Location not found: Hershey
    Location not found: Kansas City, San Francisco
    Location not found: Neptune
    Location not found: Amazon, Target, Walmart
    Location not found: Concord
    Location not found: Starbucks
    Location not found: One Medical
    Location not found: Georgetown, Central Park
    Location not found: Shiloh
    Location not found: Concord
    Location not found: Concord
    Location not found: Concord
    Location not found: Ford, General Motors, Stellantis
    Location not found: JACKSON
    Location not found: Buffalo, Dallas, Kansas City
    Location not found: Hostess, J.M. Smucker
    Location not found: Lee
    Location not found: Digital World
    Location not found: JACKSON
    Location not found: Pittsburgh, Cleveland
    Location not found: Brunswick
    Location not found: Homestead
    Location not found: Joint Base Myer-Henderson Hall
    Location not found: D.C.
    Location not found: McDonald's
    Location not found: Microsoft, Activision Blizzard
    Location not found: United Methodist Church, Global Methodist Church
    Location not found: JetBlue, Spirit Airlines, American Airlines
    Location not found: Titanic
    Location not found: North Atlantic
    Location not found: North Atlantic
    Location not found: Delta, Coca-Cola, Walmart, Bud Light, Target, Kohl's, Lego, Southwest Airlines
    Location not found: Silicon Valley, Signature, First Republic
    Location not found: Concord
    Location not found: Leeds, Birmingham
    Location not found: Columbia
    Location not found: Valhalla
    Location not found: Starks
    Location not found: Hyundai, Kia
    Location not found: Dallas, Allen, Cleveland
    Location not found: Helena
    Location not found: Bergdorf Goodman
    Location not found: Pittsburgh, Dallas
    Location not found: Liberty
    Location not found: Cambridge Analytica
    Location not found: Wynne
    Location not found: Congress
    Location not found: Silicon Valley, Signature
    Location not found: JACKSON
    Location not found: JACKSON
    Location not found: Columbia
    Location not found: Bowie
    Location not found: Plains
    Location not found: JACKSON
    Location not found: Google, YouTube
    Location not found: Beijing, Tokyo
    Location not found: JACKSON
    Location not found: Southwest Airlines
    Location not found: Goodyear
    Location not found: Boston, Dallas
    Location not found: Oklahoma City, Dallas
    Location not found: O?wi?cim
    Location not found: Jackson, Brookhaven, Oxford
    Location not found: JACKSON
    Location not found: JACKSON
    Location not found: Pontiac
    Location not found: Penn Biden Center
    Location not found: D.C.
    Location not found: Jackson, Charleston
    Location not found: Mission
    Location not found: JACKSON
    Location not found: Earle
    Location not found: Hudson
    Location not found: JACKSON
    Location not found: Spring Valley, Durand
    Location not found: Twitter
    Location not found: Twitter, Coca-Cola, Nike, Apple
    Location not found: Meta
    Location not found: CVS Health, Walgreens, Walmart
    Location not found: Jackson
    Location not found: Twitter
    Location not found: Aspen
    Location not found: Greenwood
    Location not found: Jackson
    Location not found: JAY
    Location not found: Jackson
    Location not found: JACKSON
    Location not found: Fairmead, San Joaquin Valley
    Location not found: Jackson
    Location not found: JACKSON
    Location not found: Jackson
    Location not found: Jackson
    Location not found: Jackson
    Location not found: Jackson
    Location not found: Jackson
    Location not found: Jackson
    Location not found: Weldon, Regina, James Smith Cree Nation
    Location not found: Jackson
    Location not found: Jackson
    Location not found: Jackson
    Location not found: Jackson
    Location not found: Cadillac, Chevrolet, GMC
    Location not found: Edgewater
    Location not found: Brunswick
    Location not found: Jackson
    Location not found: Greenwood, Seymour
    Location not found: JACKSON
    Location not found: Jackson
    Location not found: Surfside
    Location not found: Hawkins
    Location not found: JACKSON
    Location not found: Jackson
    Location not found: Jackson
    Location not found: JACKSON
    Location not found: Mission
    Location not found: JACKSON
    Location not found: Jackson
    Location not found: Walker
    Location not found: Brandon
    Location not found: Hoover
    Location not found: Jupiter
    Location not found: none
    Location not found: WVUA 23
    Location not found: Manhattan, Lake Tahoe
    Location not found: Montgomery, Mobile, Monroe County
    Location not found: MOBILE, Montgomery
    Location not found: Montgomery, Mobile
    Location not found: D.C.
    Location not found: D.C.
    Location not found: Jefferson, Auburn
    Location not found: Mobile, Jefferson, Lee
    Location not found: Mobile, Jefferson, Lee
    Location not found: City1
    Location not found: Studio
    Location not found: Northport, Holt
    Location not found: Bear Creek
    Location not found: Mercer, Norman
    Location not found: Mobile, Baldwin
    Location not found: Mobile
    Location not found: Montgomery, Mobile
    Location not found: Montgomery, Mobile
    Location not found: Chilton, Coosa, Marengo
    Location not found: Hoover
    Location not found: Jefferson, Bount, Etowah, St. Clair
    Location not found: Winston, Cullman
    Location not found: Richard Scott
    Location not found: Montgomery, Mobile
    Location not found: Montgomery, Cherokee County, Centre
    Location not found: Montgomery, Mobile, Monroe County
    Location not found: MOBILE, Montgomery
    Location not found: Mobile
    Location not found: Area
    Location not found: MONTGOMERY, Kenneth Smith, Terry Jarvis, Lee Holdbrooks, Scott Yancy
    Location not found: Mobile, Knight Complex
    Location not found: Montgomery, Mobile
    Location not found: Selma, Montgomery
    Location not found: Montgomery, Mobile
    Location not found: Montgomery, Limestone
    Location not found: Montgomery, Mobile
    Location not found: City1, County1
    Location not found: State of the State Address
    Location not found: WVUA23
    Location not found: IRS, Federal Trade Commission
    Location not found: Neptune
    Location not found: City1
    Location not found: ALDOR
    Location not found: Leeds, Birmingham
    Location not found: MONTGOMERY, Casey McWhorter
    Location not found: Concord
    Location not found: Concord
    Location not found: Decatur, Clay
    Location not found: Mobile
    Location not found: Bessemer
    Location not found: Ozark
    Location not found: Bessemer
    Location not found: Mobile, Creola, Jackson, Prichard
    Location not found: Columbia
    Location not found: Montgomery, Livingston
    Location not found: Selma, Montgomery
    Location not found: Moody, Trussville
    Location not found: Selma, Montgomery
    Location not found: Limestone
    Location not found: 7th District
    Location not found: Bessemer
    Location not found: Limestone
    Location not found: Verbena
    Location not found: Holman
    Location not found: Limestone
    Location not found: Mobile, Theodore, Jackson County
    Location not found: MONTGOMERY, Clotilda
    Location not found: MONTGOMERY, Terry Jarvis, Lee Holdbrooks, Scott Yancy
    Location not found: MOBILE
    Location not found: Daphne, Mobile
    Location not found: Mobile
    Location not found: Mobile
    Location not found: MOBILE
    Location not found: MOBILE, Evergreen
    Location not found: Ozark
    Location not found: UAB Hospital
    Location not found: Thomasville
    Location not found: Mobile
    Location not found: Jasper
    Location not found: Mobile
    Location not found: Hixson
    Location not found: Bessemer
    Location not found: Mobile
    Location not found: Mobile
    Location not found: Texas A&M, LSU, Vanderbilt
    Location not found: City1
    Location not found: Selma, Montgomery
    Location not found: Mobile
    Location not found: Mobile
    Location not found: MOBILE, Kearney
    Location not found: Evergreen
    Location not found: Montgomery, St. Clair, Ventress
    Location not found: MONTGOMERY, Corfman
    Location not found: MOBILE
    Location not found: Marion
    Location not found: MOBILE
    Location not found: Prichard
    Location not found: Mobile
    Location not found: Marion
    Location not found: Mobile
    Location not found: Montgomery, Mobile
    Location not found: Selma, Montgomery
    Location not found: Mobile, Jefferson, Lee
    Location not found: Mobile, Jefferson, Lee
    Location not found: Mobile
    Location not found: Mississippi State, Auburn
    Location not found: Foley
    Location not found: Mobile
    Location not found: Hoover
    Location not found: WVUA23
    Location not found: Goodwater
    Location not found: Montgomery, Mobile
    Location not found: Florence, Arab
    Location not found: Studio
    Location not found: Arab
    Location not found: Prichard
    Location not found: Mobile
    Location not found: Montgomery, Montgomery County, Ferguson
    Location not found: Phil Campbell
    Location not found: Madison, Vanderbilt, LSU, Auburn
    Location not found: Duke
    Location not found: Columbia
    Location not found: Stillwater
    Location not found: Stillwater
    Location not found: Hoover, Auburn, LSU
    Location not found: Hoover, Auburn, LSU
    Location not found: Mississippi State, LSU, Auburn, Texas A&M, Ole Miss, Vanderbilt
    Location not found: Auburn, LSU
    Location not found: Crumson Tide, Tennessee Titans
    Location not found: Porter
    Location not found: Crimson Tide
    Location not found: Columbia
    Location not found: Sipsey Valley, McKenzie
    Location not found: Ramsey
    Location not found: Mississippi State, Auburn
    Location not found: Big Ten, Southeastern Conference
    Location not found: Hoover
    Location not found: Auburn, LSU
    Location not found: Coleman
    Location not found: LSU, Auburn
    Location not found: Liberty
    Location not found: LSU, Auburn
    Location not found: Flint
    Location not found: UCLA, Cal, Auburn
    Location not found: Texas A&M, Mississippi State, Clemson, Vanderbilt, LSU, Auburn
    Location not found: LSU, Mississippi State
    Location not found: Stillman, Voorhees, Rust
    Location not found: Coleman Coliseum, Morehead
    Location not found: Ole Miss, Georgia Tech, Memphis, Tulane
    Location not found: USF, Notre Dame, Ole Miss
    Location not found: Anderson Green, Northridge High School
    Location not found: Brookwood
    Location not found: Memphis, Villanova
    Location not found: Arlington, Rice
    Location not found: Helena
    Location not found: Villanova, Northridge
    Location not found: Lithia
    Location not found: Carolina
    Location not found: Lithia
    Location not found: Nicholls, Troy
    Location not found: Grayson, Rhodes Stadium
    Location not found: Haclensack, Villanova
    Location not found: Hoover
    Location not found: Stillman College, Faulkner University
    Location not found: Gary, Henry Ruggs, John Metchie, Crimson Tide, Montana Fouts
    Location not found: Carolina
    Location not found: IMG Academy
    Location not found: Southern Miss, Auburn
    Location not found: City1, County1
    Location not found: Crimson Tide, Kansas State, LSU
    Location not found: Princeton, Furman
    Location not found: Mizzou, Mississippi State, LSU
    Location not found: LSU, Auburn
    Location not found: Thompson, Alabaster, Clemson
    Location not found: Ole Miss, Austin Peay
    Location not found: Oxford, LSU, Ole Miss
    Location not found: TCU, Ohio State
    Location not found: Harry Pritchett Course, Crimson Tide
    Location not found: Texas A&M, Bryant-Denny, App State, Kyle Field
    Location not found: Tyler
    Location not found: Gary, ULM, Vanderbilt
    Location not found: Gary, ULM
    Location not found: Ohio State, Clemson
    Location not found: Auburn, Mercer, LSU
    Location not found: Crimson Tide
    Location not found: Crimson Tide
    Location not found: Windsor
    Location not found: Crimson Tide
    Location not found: Crimson Tide
    Location not found: Georgetown, Gonzaga
    Location not found: Brookwood
    Location not found: Calhoun
    Location not found: Crimson Tide
    Location not found: Stillman, Mobile
    Location not found: Hoover
    Location not found: Hoover
    Location not found: Hoover
    Location not found: Buffalo, St. Bonaventure
    Location not found: Jackson State, Auburn
    Location not found: Notre Dame, Gonzaga, Baylor, Vanderbilt, LSU
    Location not found: Lawrence
    Location not found: Duke, Villanova
    Location not found: Villanova, Notre Dame
    Location not found: Texas A&M, Ole Miss, Vanderbilt
    Location not found: Gonzaga, Saint Mary?s, Auburn, Baylor, Texas Tech, TCU, Michigan State, Purdue
    Location not found: Northridge, Shelton
    Location not found: Ohio State, Clemson
    Location not found: WVUA, Ronnell Foreman Jr
    Location not found: Stillman College, William Carey University, Loyola, Dalton State
    Location not found: Ole Miss, Auburn
    Location not found: Mobile
    Location not found: Auburn, Oxford
    Location not found: Texas A&M, Miami, LSU, Notre Dame
    Location not found: LSU, Mizzou
    Location not found: Indian Hills
    Location not found: Indian Hills
    Location not found: Bryant-Denny Stadium, Ole Miss
    Location not found: Carolina
    Location not found: City Invitational
    Location not found: Indian Hills
    Location not found: Jacksonville, Buffalo
    Location not found: Houston, Baltimore
    Location not found: Brookwood, LSU, Mississippi State
    Location not found: Brookwood, Hillcrest
    Location not found: Gary, LSU, Ole Miss
    Location not found: D.C.
    Location not found: Crimson Tide
    Location not found: Gary, Tide, John Metchie, Julio Jones, Tampa Bay, Buccaneers
    Location not found: Hillcrest
    Location not found: Clemson, Ohio State
    Location not found: Thomas-Drew Practice Fields
    Location not found: Bowling Green, Plum
    Location not found: Stillwater
    Location not found: Mobile
    Location not found: Mobile
    Location not found: Mobile
    Location not found: University of Alabama, Crimson Tide, Rose Bowl, Notre Dame
    Location not found: Texas A&M, Ole Miss
    Location not found: Columbia
    Location not found: Columbia
    Location not found: Texas A&M, LSU, Mississippi State
    Location not found: Ohio State, Clemson, LSU
    Location not found: Sewell-Thomas Stadium, LSU
    Location not found: Hoover
    Location not found: Theodore
    Location not found: Mercer
    Location not found: The Citadel
    Location not found: Crimson Tide
    Location not found: Crimson Tide
    Location not found: Gary, Bradley, Levi, Rodney
    Location not found: Crimson Tide, 1992
    Location not found: Gary, Vanderbilt
    Location not found: Crimson Tide
    Location not found: Gary, Kent
    Location not found: Centrals, McAdory, Aliceville
    Location not found: Holt, Brookwood
    Location not found: Gordo, Ellisville, Montgomery, Sipsey Valley
    Location not found: Holt, Brookwood
    Location not found: Northridge, Oak Mountain
    Location not found: Pelham, Northridge, Alma Bryant
    Location not found: Eastwood, Echols
    Location not found: Sipsey Valley
    Location not found: Thompson
    Location not found: Sipsey Valley, Gordo
    Location not found: Holt, Brookwood
    Location not found: Bryant, Hillcrest, Brookwood, McAdory
    Location not found: ACA, Sipsey Valley
    Location not found: October 4, 2019
    Location not found: August 30
    Location not found: Gordo
    Location not found: Hoover, Northridge, Pelham, Thompson
    Location not found: Gordo
    Location not found: American Christian Academy, Millsaps College
    Location not found: Hillcrest, Pike Road, Faith Academy
    Location not found: Holt, Sipsey Valley
    Location not found: Jackson, American Christian Academy
    Location not found: Brookwood, Hillcrest
    Location not found: Central
    Location not found: Northridge, Auburn
    Location not found: Gordo, Houston Academy
    Location not found: Gordo, Phil Campbell
    Location not found: Daphne, T.R. Miller
    Location not found: Gordo
    Location not found: American Christian Academy, Gordo
    Location not found: Northridge, Paul Bryant
    Location not found: Paul Bryant High School, Marion Military Institute
    Location not found: Samantha, Northside
    Location not found: Brookwood
    Location not found: Brookwood, Holt
    Location not found: Hoover
    Location not found: Holy Spirit, Skyline
    Location not found: Gordo, Montevallo
    Location not found: Hillcrest, Faith Academy, Helena High School, Stanhope Elmore High School
    Location not found: Hillcrest, McAdory
    Location not found: Hillcrest, Paul W. Bryant, Northridge, Brookwood
    Location not found: American Christian Academy, Crimson Tide, Patriots
    Location not found: Gordo, Columbia
    Location not found: Gordo, Huntsville
    Location not found: Gordo, Oakman
    Location not found: Hillcrest, Oxford, Shades Valley
    Location not found: Calhoun, Midfield
    Location not found: Sipsey Valley, Paul W. Bryant, Holt, Brookwood
    Location not found: Central, Jasper, Sipsey Valley
    Location not found: Gordo, Northridge, Hamilton
    Location not found: Paul Bryant, Holt, Central High School, American Christian Academy
    Location not found: Northridge, Brookwood, Gordo, Sipsey Valley
    Location not found: Shelton
    Location not found: Shelton
    Location not found: Chipola College, Jones College
    Location not found: Stillman College, County High School, Hillcrest High School
    Location not found: Mobile
    Location not found: Stillman College, Talladega College
    Location not found: Vigor
    Location not found: Gary, Auburn
    Location not found: Mercer
    Location not found: Gary, Rodney
    Location not found: Gary, Rodney
    Location not found: UA Campus, Ramsay High School
    Location not found: Gary, Rodney
    Location not found: Gary, Orr
    Location not found: Gary, Tide
    Location not found: Gary, Rodney
    Location not found: Gary, Tide
    Location not found: Gary, Rodney, Tide
    Location not found: Crimson Tide
    Location not found: Crimson Tide
    Location not found: Gary, Orr
    Location not found: Gary, Tide, Tigers
    Location not found: Crimson Tide
    Location not found: Hoover
    Location not found: Gary, Rodney
    Location not found: Crimson Tide
    Location not found: City1
    Location not found: Gary, Rodney
    Location not found: Gary, Rodney
    Location not found: Crimson Tide
    Location not found: Crimson Tide
    Location not found: Gary, Baylor
    Location not found: Mobile
    Location not found: Gary, Auburn
    Location not found: LSU, Mississippi State
    Location not found: Ole Miss, Texas A&M
    Location not found: Gary, Rodney
    Location not found: Gary, Rodney
    Location not found: Gary, Orr
    Location not found: Gary, Orr
    Location not found: Gary, Orr
    Location not found: Gary, Orr
    Location not found: Mobile
    Location not found: Gary, Auburn
    Location not found: Gary, Rodney
    Location not found: Gary, Orr
    Location not found: LSU, Mississippi State
    Location not found: Vanderbilt, Ole Miss
    Location not found: Crimson Tide
    Location not found: Hoover
    Location not found: Hoover
    Location not found: Gary, Crimson Tide
    Location not found: Brandon, Rodney
    Location not found: LSU, Mississippi State, Texas A&M
    Location not found: Crimson Tide
    Location not found: Ole Miss, Kent State
    Location not found: Crimson Tide
    Location not found: Gary, Crimson Tide
    Location not found: Crimson Tide
    Location not found: Gary, Orr
    Location not found: Gary, Rodney
    Location not found: Crimson Tide
    Location not found: Gary, Orr
    Location not found: Brandon, Rodney
    Location not found: Gary, Crimson Tide
    Location not found: Gary, Crimson Tide
    Location not found: Crimson Tide
    Location not found: Gary, Crimson Tide
    Location not found: Gary, Crimson Tide
    Location not found: Gary, Crimson Tide
    Location not found: Gary, Crimson Tide
    Location not found: Crimson Tide
    Location not found: Gary, Crimson Tide
    Location not found: Brandon, Rodney
    Location not found: Crimson Tide
    Location not found: City1
    Location not found: Gary, Crimson Tide
    Location not found: Gary, Crimson Tide
    Location not found: Crimson Tide
    Location not found: Crimson Tide
    Location not found: Gary, Orr
    Location not found: Gary, Orr
    Location not found: Gary, Crimson Tide
    Location not found: Gary, Orr
    Location not found: Ole Miss, ULM
    Location not found: City1
    Location not found: University Medical Center
    Location not found: University Medical Center
    Location not found: University Medical Center
    Location not found: University Medical Center
    Location not found: University Medical Center
    Location not found: University Medical Center
    Location not found: University Medical Center
    Location not found: University Medical Center
    Location not found: University Medical Center
    Location not found: University Medical Center
    Location not found: University Medical Center
    Location not found: Metro Animal Shelter
    Location not found: local animal shelter
    Location not found: Winn-Dixie
    Location not found: Simon, humanesocietyofwa
    Location not found: Brookwood
    Location not found: wa
    Location not found: WVUA23
    Location not found: WVUA23
    Location not found: South Central Counties, Eastern Counties
    Location not found: WVUA23
    Location not found: WVUA23
    Location not found: Carolinas
    Location not found: Carolina
    Location not found: WVUA23
    Location not found: WVUA23
    Location not found: Southern counties, Central areas
    Location not found: WVUA23
    Location not found: WVUA23
    Location not found: WVUA23
    Location not found: WVUA23
    Location not found: WVUA23
    Location not found: WVUA23
    Location not found: WVUA23
    Location not found: WVUA23
    Location not found: WVUA23
    Location not found: local counties
    Location not found: WVUA23
    Location not found: WVUA23
    Location not found: City1
    Location not found: WVUA23
    Location not found: Jacob Woods
    Location not found: Jacob Woods
    Location not found: City
    Location not found: WVUA23
    Location not found: WVUA23
    Location not found: western side
    Location not found: WVUA23
    Location not found: City
    Location not found: WVUA23
    Location not found: WVUA23
    Location not found: none
    Location not found: WVUA23
    Location not found: WVUA23
    Location not found: WVUA23
    Location not found: WVUA23
    Location not found: WVUA23
    Location not found: WVUA23
    Location not found: WVUA23
    Location not found: Gulf Coast
    Location not found: WVUA23
    Location not found: Vernon, Jasper
    Location not found: area
    Location not found: Thomasville
    Location not found: WVUA23
    Location not found: Gulf Coast
    Location not found: WVUA23
    Location not found: WVUA23
    Location not found: WVUA23
    Location not found: WVUA23
    Location not found: WVUA23
    Location not found: area
    Location not found: WVUA23
    Location not found: WVUA23
    Location not found: WVUA23
    Location not found: WVUA
    Location not found: WVUA
    Location not found: WVUA
    Location not found: WVUA
    Location not found: WVUA
    Location not found: WVUA
    Location not found: WVUA
    Location not found: WVUA
    Location not found: WVUA
    Location not found: WVUA
    Location not found: WVUA
    Location not found: WVUA
    Location not found: WVUA
    Location not found: WVUA
    Location not found: WVUA
    Location not found: WVUA
    Location not found: WVUA 23
    Location not found: Atlantic
    Location not found: WVUA
    Location not found: WVUA
    Location not found: WVUA23
    Location not found: Heartland, Gulf Coast
    Map has been saved as 'news_locations_map_2.html'
    


```python
pip install pandas folium geopy geopandas chardet
```

    Defaulting to user installation because normal site-packages is not writeable
    Requirement already satisfied: pandas in c:\users\adarsh g\appdata\roaming\python\python39\site-packages (2.2.2)
    Requirement already satisfied: folium in c:\users\adarsh g\appdata\roaming\python\python39\site-packages (0.17.0)
    Requirement already satisfied: geopy in c:\users\adarsh g\appdata\roaming\python\python39\site-packages (2.4.1)
    Requirement already satisfied: geopandas in c:\users\adarsh g\appdata\roaming\python\python39\site-packages (1.0.1)
    Requirement already satisfied: chardet in c:\users\adarsh g\appdata\roaming\python\python39\site-packages (3.0.4)
    Requirement already satisfied: numpy>=1.22.4 in c:\users\adarsh g\appdata\roaming\python\python39\site-packages (from pandas) (2.0.2)
    Requirement already satisfied: python-dateutil>=2.8.2 in d:\anaconda3\lib\site-packages (from pandas) (2.8.2)
    Requirement already satisfied: pytz>=2020.1 in c:\users\adarsh g\appdata\roaming\python\python39\site-packages (from pandas) (2024.2)
    Requirement already satisfied: tzdata>=2022.7 in c:\users\adarsh g\appdata\roaming\python\python39\site-packages (from pandas) (2024.1)
    Requirement already satisfied: branca>=0.6.0 in c:\users\adarsh g\appdata\roaming\python\python39\site-packages (from folium) (0.7.2)
    Requirement already satisfied: jinja2>=2.9 in c:\users\adarsh g\appdata\roaming\python\python39\site-packages (from folium) (3.1.4)
    Requirement already satisfied: requests in c:\users\adarsh g\appdata\roaming\python\python39\site-packages (from folium) (2.32.3)
    Requirement already satisfied: xyzservices in c:\users\adarsh g\appdata\roaming\python\python39\site-packages (from folium) (2024.9.0)
    Requirement already satisfied: geographiclib<3,>=1.52 in c:\users\adarsh g\appdata\roaming\python\python39\site-packages (from geopy) (2.0)
    Requirement already satisfied: pyogrio>=0.7.2 in c:\users\adarsh g\appdata\roaming\python\python39\site-packages (from geopandas) (0.9.0)
    Requirement already satisfied: packaging in d:\anaconda3\lib\site-packages (from geopandas) (21.3)
    Requirement already satisfied: pyproj>=3.3.0 in c:\users\adarsh g\appdata\roaming\python\python39\site-packages (from geopandas) (3.6.1)
    Requirement already satisfied: shapely>=2.0.0 in c:\users\adarsh g\appdata\roaming\python\python39\site-packages (from geopandas) (2.0.6)
    Requirement already satisfied: MarkupSafe>=2.0 in d:\anaconda3\lib\site-packages (from jinja2>=2.9->folium) (2.0.1)
    Requirement already satisfied: certifi in d:\anaconda3\lib\site-packages (from pyogrio>=0.7.2->geopandas) (2021.10.8)
    Requirement already satisfied: six>=1.5 in d:\anaconda3\lib\site-packages (from python-dateutil>=2.8.2->pandas) (1.16.0)
    Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in d:\anaconda3\lib\site-packages (from packaging->geopandas) (3.0.4)
    Requirement already satisfied: charset-normalizer<4,>=2 in d:\anaconda3\lib\site-packages (from requests->folium) (2.0.4)
    Requirement already satisfied: idna<4,>=2.5 in c:\users\adarsh g\appdata\roaming\python\python39\site-packages (from requests->folium) (2.10)
    Requirement already satisfied: urllib3<3,>=1.21.1 in d:\anaconda3\lib\site-packages (from requests->folium) (1.26.9)
    Note: you may need to restart the kernel to use updated packages.
    


```python
import json
import requests

# Constants
GEO_API_KEY = 'AIzaSyChg3ArAuJhYKEY2mv_CVOWHYYJ1tFHhvA'  # Replace with your API key
GEO_API_URL = 'https://maps.googleapis.com/maps/api/geocode/json'

# Load existing GeoJSON
with open("C:\\Users\\ADARSH G\\Downloads\\counties.geojson", 'r') as f:
    geojson_data = json.load(f)

# Function to fetch coordinates from a geocoding API
def fetch_coordinates(location_name):
    params = {
        'address': location_name,
        'key': GEO_API_KEY
    }
    try:
        response = requests.get(GEO_API_URL, params=params)
        response.raise_for_status()
        data = response.json()
        if data['status'] == 'OK':
            result = data['results'][0]
            location = result['geometry']['location']
            return location['lat'], location['lng']
        else:
            print(f"Geocoding API error: {data['status']} for location: {location_name}")
            return None, None
    except requests.RequestException as e:
        print(f"Request error: {e}")
        return None, None

# Function to add new location to GeoJSON
def add_new_location(geojson_data, name, lat, lng):
    new_feature = {
        "type": "Feature",
        "properties": {
            "NAME": name
        },
        "geometry": {
            "type": "Point",
            "coordinates": [lng, lat]
        }
    }
    geojson_data['features'].append(new_feature)

# List of locations that were not found
missing_locations = [
    "West Side", "Shelton", "Magic Moments, Sokol Park", "Mercer, Norman",
    "Montgomery, Greene County", "City1", "Mobile", "Fosters", "Indian Hills","Nauvoo", "Walker County",
"Tuscaloosa", "Tuscaloosa County",
"Hale County", "Greensboro", "Sawyerville", "Akron", "Moundville",
"Auburn", "Central-Phenix City",
"Brookwood", "Hoover",
"West Alabama",
"Nauvoo",
"Bibb County", "Fayette County", "Greene County", "Hale County", "Pickens County", "Tuscaloosa County", "Walker County", "Shelby County", "Morgan County", "Marshall County", "Cullman County", "Madison County", "Limestone County", "Elmore County", "Wilcox County", "Perry County", "Dallas County", "Trussville", "Vestavia Hills", "Alabaster", "Hoover", "Homewood", "Athens", "Decatur", "Selma", "Prichard", "Bessemer",
"Tuscaloosa",
"University of Alabama", "RISE Center",
"Tuscaloosa", "Tuscaloosa County", "Cottondale",
"Tuscaloosa", "Northridge",
"West Side",
"Tuscaloosa",
"Northport",
"Tuscaloosa", "Saraland", "Mobile",
"Greensboro", "Hale County", "Bibb County", "Greene County", "Tuscaloosa County",
"Lake View", "Tuscaloosa County",
"Macon", "Russell", "Elmore", "Autauga", "Chilton", "Shelby", "Dallas", "Perry", "Bibb", "Fayette", "Greene", "Hale", "Pickens", "Lamar", "Sumter", "Tuscaloosa", "Cullman", "Lawrence", "Morgan", "Marion", "Walker", "Winston",
"Tuscaloosa County",
"Shelton",
"Tuscaloosa", "Tuscaloosa County",
"Pell City",
"Greensboro", "Tuscaloosa",
"Northport", "Parrish", "Eutaw", "Tuscaloosa", "Walker County",
"Montgomery",
"Montgomery",
"Tuscaloosa", "Cottondale",
"Bibb County", "West Blocton",
"Tuscaloosa",
"Louisville", "Birmingham",
"Tuscaloosa",
"University of Alabama",
"York", "Sumter County",
"Las Vegas", "Charlotte", "Brooklyn", "Sacramento", "Huntsville", "New Orleans", "Houston", "Tuscaloosa", "San Antonio", "Oklahoma City", "Portland",
"Tuscaloosa", "Northport", "Demopolis", "Fayette", "Carrollton", "Livingston",
"Tuscaloosa", "Tuscaloosa County",
"Tuscaloosa",
"Tuscaloosa",
"Dallas",
"Tuscaloosa",
"Tuscaloosa County", "Tuscaloosa",
"Bibb County", "Centreville", "West Blocton",
"Tuscaloosa",
"Norman", "Tuscaloosa",
"Tuscaloosa",
"Tuscaloosa",
"Northport", "Tuscaloosa County",
"Suwannee", "Mobile",
"Tuscaloosa", "Tuscaloosa County",
"University of Alabama",
"Walker County", "Greene County", "Auburn", "Brundidge", "Enterprise", "Fort Payne", "Coosa County",
"Magic Moments", "Sokol Park",
"University of Alabama",
"Tuscaloosa", "Tuscaloosa County",
"Birmingham", "Bessemer", "Cullman", "Jasper", "Oneonta", "Tuscaloosa", "Jefferson County",
"Fayette", "Fulton",
"Dora", "Walker County", "Bessemer", "Jasper",
"Tuscaloosa", "Chicago",
"Tuscaloosa", "Tuscaloosa County",
"Pickens County",
"Tuscaloosa",
"Tuscaloosa", "Northport", "Demopolis", "Fayette", "Carrollton", "Livingston",
"Pickens County", "Carrollton",
"Birmingham", "Hope Hull", "Dothan", "Tuscaloosa", "Montgomery",
"Tuscaloosa", "Tuscaloosa County",
"Mercer", "Norman",
"Tuscaloosa",
"Montgomery", "Greene County",
"Fayette",
"Hale County",
"Tuscaloosa",
"Tuscaloosa", "Haleyville",
"Bibb County", "West Blocton",
"Tuscaloosa", "Northport", "Tuscaloosa County",
"Tuscaloosa", "Atmore",
"Tuscaloosa", "Central High", "Oakdale Elementary",
"Tuscaloosa",
"Tuscaloosa",
"Birmingham",
"Parrish", "Walker County", "Jasper",
"Tuscaloosa County", "T-Town",
"Tuscaloosa",
"Moundville", "Hale County",
"Tuscaloosa",
"Fayette", "Fayette County",
"Perry County", "Dallas County",
"Tuscaloosa", "Tuscaloosa County",
"Northport",
"Tuscaloosa", "Kaulton Park",
"Tuscaloosa", "Sioux Falls", "Fresno",
"Aliceville", "Pickens County",
"University of Alabama", "Reese Phifer Hall", "Bryant-Denny Stadium", "Campus Drive",
"Dallas",
"University of Alabama", "Snow Hinton Park",
"Tuscaloosa",
"Tuscaloosa",
"Tuscaloosa",
"Cherokee County",
"Tuscaloosa", "Brookwood",
"Choctaw County", "Denton", "Dallas",
"Dallas", "Greene", "Hale", "Sumter", "Bibb", "Choctaw", "Fayette", "Lamar", "Perry", "Tuscaloosa",
"West Alabama",
"Tuscaloosa",
"Shelton",
"Moundville",
"Tuscaloosa",
"Tuscaloosa County",
"Tuscaloosa",
"Mobile",
"LSU", "Tuscaloosa", "Tiger Stadium", "Gainesville",
"Tuscaloosa",
"Milwaukee",
"Tuscaloosa",
"Northport",
"Perry County", "Dallas County", "Newbern",
"Northport",
"Tuscaloosa", "Meridian", "Vance", "Eutaw", "Jackson", "Brookhaven", "Tuscaloosa County",
"Northport",
"Houston",
"Tuscaloosa", "Philadelphia", "Detroit", "Diamondbacks", "Rangers", "Yankees", "White Sox", "Mets", "Rays", "Cubs", "Marlins",
"Tuscaloosa", "Tuscaloosa County",
"Tuscaloosa",
"Tuscaloosa",
"Tuscaloosa",
"Central Alabama",
"Tuscaloosa",
"Tuscaloosa",
"Tuscaloosa County", "Northport",
"Northport",
"Fosters",
"Talladega",
"Indian Hills",
"Butler",
"Tuscaloosa",
"Birmingham", "Tuscaloosa", "Pickens County", "Lamar County", "Fayette County", "Walker County",
"Tuscaloosa",
"Tuscaloosa",
"Tuscaloosa", "Northport", "Tuscaloosa County",
"Tuscaloosa", "Queen City",
"Tuscaloosa", "Fosters", "Cottondale",
"West Alabama", "Northport",
"Berry", "Tuscaloosa County",
"Tuscaloosa",
"Bibb County", "Brierfield",
"Selma",
"Trussville", "North Alabama",
"Tuscaloosa County",
"Tuscaloosa",
"Birmingham",
"Atlanta", "USC", "LSU",
"Birmingham", "University of Alabama",
"Tuscaloosa",
"Birmingham", "Jefferson County",
"Florence", "Grace Presbyterian Church",
"Tuscaloosa", "Tuscaloosa County",
"Coker",
"Holt", "Tuscaloosa County",
"Tuscaloosa",
"Birmingham", "Birmingport", "Demopolis", "Mobile",
"Tuscaloosa County", "Lake View",
"Augusta",
"Tuscaloosa",
"Mobile", "Tuscaloosa County",
"Tuscaloosa", "Northport", "Demopolis", "Fayette", "Carrollton", "Livingston",
"Columbia", "Tuscaloosa", "Baton Rouge",
"Moundville", "Birmingham",
"Calhoun", "Conecuh", "Crenshaw", "Cullman", "Escambia", "Jackson", "Marshall", "Tuscaloosa", "Shelby", "Morgan", "Baldwin", "Gulf Shores", "Orange Beach",
"Tuscaloosa",
"Tuscaloosa County", "Brookwood",
"Tuscaloosa", "Northridge",
"Tuscaloosa",
"Tuscaloosa", "Pickens County",
"West Alabama", "Midtown Village",
"Tuscaloosa", "Tuscaloosa County",
"Moundville", "Demopolis", "Providence", "Greensboro", "Thomasville", "Hale County",

    # Add more locations here
]

# Process missing locations
for location in missing_locations:
    print(f"Fetching coordinates for: {location}")
    lat, lng = fetch_coordinates(location)
    if lat and lng:
        print(f"Adding {location} with coordinates ({lat}, {lng}) to GeoJSON.")
        add_new_location(geojson_data, location, lat, lng)
    else:
        print(f"Location not found: {location}")

# Save updated GeoJSON file
with open('updated_geojson_file.geojson', 'w') as f:
    json.dump(geojson_data, f, indent=2)

print("GeoJSON update complete.")


```

    Fetching coordinates for: West Side
    Geocoding API error: ZERO_RESULTS for location: West Side
    Location not found: West Side
    Fetching coordinates for: Shelton
    Geocoding API error: ZERO_RESULTS for location: Shelton
    Location not found: Shelton
    Fetching coordinates for: Magic Moments, Sokol Park
    Geocoding API error: ZERO_RESULTS for location: Magic Moments, Sokol Park
    Location not found: Magic Moments, Sokol Park
    Fetching coordinates for: Mercer, Norman
    Geocoding API error: ZERO_RESULTS for location: Mercer, Norman
    Location not found: Mercer, Norman
    Fetching coordinates for: Montgomery, Greene County
    Geocoding API error: ZERO_RESULTS for location: Montgomery, Greene County
    Location not found: Montgomery, Greene County
    Fetching coordinates for: City1
    Geocoding API error: ZERO_RESULTS for location: City1
    Location not found: City1
    Fetching coordinates for: Mobile
    Geocoding API error: ZERO_RESULTS for location: Mobile
    Location not found: Mobile
    Fetching coordinates for: Fosters
    Geocoding API error: ZERO_RESULTS for location: Fosters
    Location not found: Fosters
    Fetching coordinates for: Indian Hills
    Geocoding API error: ZERO_RESULTS for location: Indian Hills
    Location not found: Indian Hills
    Fetching coordinates for: Nauvoo
    Adding Nauvoo with coordinates (40.550042, -91.3848749) to GeoJSON.
    Fetching coordinates for: Walker County
    Adding Walker County with coordinates (30.6815394, -95.6457951) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Tuscaloosa County
    Adding Tuscaloosa County with coordinates (33.3227653, -87.460397) to GeoJSON.
    Fetching coordinates for: Hale County
    Adding Hale County with coordinates (32.7859102, -87.6186379) to GeoJSON.
    Fetching coordinates for: Greensboro
    Adding Greensboro with coordinates (36.0725632, -79.791534) to GeoJSON.
    Fetching coordinates for: Sawyerville
    Adding Sawyerville with coordinates (32.7517973, -87.72945469999999) to GeoJSON.
    Fetching coordinates for: Akron
    Adding Akron with coordinates (41.081199, -81.51883769999999) to GeoJSON.
    Fetching coordinates for: Moundville
    Adding Moundville with coordinates (32.9976242, -87.6300075) to GeoJSON.
    Fetching coordinates for: Auburn
    Adding Auburn with coordinates (32.6098566, -85.48078249999999) to GeoJSON.
    Fetching coordinates for: Central-Phenix City
    Adding Central-Phenix City with coordinates (32.4709761, -85.0007653) to GeoJSON.
    Fetching coordinates for: Brookwood
    Geocoding API error: ZERO_RESULTS for location: Brookwood
    Location not found: Brookwood
    Fetching coordinates for: Hoover
    Geocoding API error: ZERO_RESULTS for location: Hoover
    Location not found: Hoover
    Fetching coordinates for: West Alabama
    Adding West Alabama with coordinates (33.2570618, -85.41661719999999) to GeoJSON.
    Fetching coordinates for: Nauvoo
    Adding Nauvoo with coordinates (40.550042, -91.3848749) to GeoJSON.
    Fetching coordinates for: Bibb County
    Adding Bibb County with coordinates (32.7865735, -83.7199136) to GeoJSON.
    Fetching coordinates for: Fayette County
    Adding Fayette County with coordinates (33.4502206, -84.4802606) to GeoJSON.
    Fetching coordinates for: Greene County
    Adding Greene County with coordinates (39.697399, -83.8897057) to GeoJSON.
    Fetching coordinates for: Hale County
    Adding Hale County with coordinates (32.7859102, -87.6186379) to GeoJSON.
    Fetching coordinates for: Pickens County
    Adding Pickens County with coordinates (34.9046217, -82.6483442) to GeoJSON.
    Fetching coordinates for: Tuscaloosa County
    Adding Tuscaloosa County with coordinates (33.3227653, -87.460397) to GeoJSON.
    Fetching coordinates for: Walker County
    Adding Walker County with coordinates (30.6815394, -95.6457951) to GeoJSON.
    Fetching coordinates for: Shelby County
    Adding Shelby County with coordinates (35.1268552, -89.9253233) to GeoJSON.
    Fetching coordinates for: Morgan County
    Adding Morgan County with coordinates (41.0576176, -111.6183755) to GeoJSON.
    Fetching coordinates for: Marshall County
    Adding Marshall County with coordinates (34.3652297, -86.3376761) to GeoJSON.
    Fetching coordinates for: Cullman County
    Adding Cullman County with coordinates (34.2011537, -86.8220341) to GeoJSON.
    Fetching coordinates for: Madison County
    Adding Madison County with coordinates (38.9041402, -89.9253233) to GeoJSON.
    Fetching coordinates for: Limestone County
    Adding Limestone County with coordinates (34.78000720000001, -86.9423801) to GeoJSON.
    Fetching coordinates for: Elmore County
    Adding Elmore County with coordinates (32.5647083, -86.0121573) to GeoJSON.
    Fetching coordinates for: Wilcox County
    Adding Wilcox County with coordinates (32.0105439, -87.3413599) to GeoJSON.
    Fetching coordinates for: Perry County
    Adding Perry County with coordinates (40.371376, -77.2405153) to GeoJSON.
    Fetching coordinates for: Dallas County
    Adding Dallas County with coordinates (32.8024682, -96.83509989999999) to GeoJSON.
    Fetching coordinates for: Trussville
    Adding Trussville with coordinates (33.6198251, -86.60887559999999) to GeoJSON.
    Fetching coordinates for: Vestavia Hills
    Adding Vestavia Hills with coordinates (33.4487183, -86.7877668) to GeoJSON.
    Fetching coordinates for: Alabaster
    Geocoding API error: ZERO_RESULTS for location: Alabaster
    Location not found: Alabaster
    Fetching coordinates for: Hoover
    Geocoding API error: ZERO_RESULTS for location: Hoover
    Location not found: Hoover
    Fetching coordinates for: Homewood
    Adding Homewood with coordinates (41.5676825, -87.6541852) to GeoJSON.
    Fetching coordinates for: Athens
    Adding Athens with coordinates (37.9838096, 23.7275388) to GeoJSON.
    Fetching coordinates for: Decatur
    Adding Decatur with coordinates (33.7748275, -84.2963123) to GeoJSON.
    Fetching coordinates for: Selma
    Adding Selma with coordinates (32.4073589, -87.02110069999999) to GeoJSON.
    Fetching coordinates for: Prichard
    Geocoding API error: ZERO_RESULTS for location: Prichard
    Location not found: Prichard
    Fetching coordinates for: Bessemer
    Geocoding API error: ZERO_RESULTS for location: Bessemer
    Location not found: Bessemer
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: University of Alabama
    Adding University of Alabama with coordinates (33.2114385, -87.5401002) to GeoJSON.
    Fetching coordinates for: RISE Center
    Geocoding API error: ZERO_RESULTS for location: RISE Center
    Location not found: RISE Center
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Tuscaloosa County
    Adding Tuscaloosa County with coordinates (33.3227653, -87.460397) to GeoJSON.
    Fetching coordinates for: Cottondale
    Adding Cottondale with coordinates (33.189202, -87.4565956) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Northridge
    Adding Northridge with coordinates (34.2354576, -118.5361381) to GeoJSON.
    Fetching coordinates for: West Side
    Geocoding API error: ZERO_RESULTS for location: West Side
    Location not found: West Side
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Northport
    Adding Northport with coordinates (40.9009313, -73.3431727) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Saraland
    Adding Saraland with coordinates (30.820742, -88.07055559999999) to GeoJSON.
    Fetching coordinates for: Mobile
    Geocoding API error: ZERO_RESULTS for location: Mobile
    Location not found: Mobile
    Fetching coordinates for: Greensboro
    Adding Greensboro with coordinates (36.0725632, -79.791534) to GeoJSON.
    Fetching coordinates for: Hale County
    Adding Hale County with coordinates (32.7859102, -87.6186379) to GeoJSON.
    Fetching coordinates for: Bibb County
    Adding Bibb County with coordinates (32.7865735, -83.7199136) to GeoJSON.
    Fetching coordinates for: Greene County
    Adding Greene County with coordinates (39.697399, -83.8897057) to GeoJSON.
    Fetching coordinates for: Tuscaloosa County
    Adding Tuscaloosa County with coordinates (33.3227653, -87.460397) to GeoJSON.
    Fetching coordinates for: Lake View
    Geocoding API error: ZERO_RESULTS for location: Lake View
    Location not found: Lake View
    Fetching coordinates for: Tuscaloosa County
    Adding Tuscaloosa County with coordinates (33.3227653, -87.460397) to GeoJSON.
    Fetching coordinates for: Macon
    Adding Macon with coordinates (32.8406946, -83.6324022) to GeoJSON.
    Fetching coordinates for: Russell
    Geocoding API error: ZERO_RESULTS for location: Russell
    Location not found: Russell
    Fetching coordinates for: Elmore
    Geocoding API error: ZERO_RESULTS for location: Elmore
    Location not found: Elmore
    Fetching coordinates for: Autauga
    Adding Autauga with coordinates (32.5791817, -86.49965460000001) to GeoJSON.
    Fetching coordinates for: Chilton
    Geocoding API error: ZERO_RESULTS for location: Chilton
    Location not found: Chilton
    Fetching coordinates for: Shelby
    Geocoding API error: ZERO_RESULTS for location: Shelby
    Location not found: Shelby
    Fetching coordinates for: Dallas
    Adding Dallas with coordinates (32.7766642, -96.79698789999999) to GeoJSON.
    Fetching coordinates for: Perry
    Adding Perry with coordinates (32.4582065, -83.7315723) to GeoJSON.
    Fetching coordinates for: Bibb
    Adding Bibb with coordinates (32.7865735, -83.7199136) to GeoJSON.
    Fetching coordinates for: Fayette
    Adding Fayette with coordinates (33.6845539, -87.8308522) to GeoJSON.
    Fetching coordinates for: Greene
    Adding Greene with coordinates (39.697399, -83.8897057) to GeoJSON.
    Fetching coordinates for: Hale
    Geocoding API error: ZERO_RESULTS for location: Hale
    Location not found: Hale
    Fetching coordinates for: Pickens
    Geocoding API error: ZERO_RESULTS for location: Pickens
    Location not found: Pickens
    Fetching coordinates for: Lamar
    Geocoding API error: ZERO_RESULTS for location: Lamar
    Location not found: Lamar
    Fetching coordinates for: Sumter
    Adding Sumter with coordinates (33.9204354, -80.3414693) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Cullman
    Adding Cullman with coordinates (34.1748208, -86.8436124) to GeoJSON.
    Fetching coordinates for: Lawrence
    Geocoding API error: ZERO_RESULTS for location: Lawrence
    Location not found: Lawrence
    Fetching coordinates for: Morgan
    Geocoding API error: ZERO_RESULTS for location: Morgan
    Location not found: Morgan
    Fetching coordinates for: Marion
    Geocoding API error: ZERO_RESULTS for location: Marion
    Location not found: Marion
    Fetching coordinates for: Walker
    Geocoding API error: ZERO_RESULTS for location: Walker
    Location not found: Walker
    Fetching coordinates for: Winston
    Geocoding API error: ZERO_RESULTS for location: Winston
    Location not found: Winston
    Fetching coordinates for: Tuscaloosa County
    Adding Tuscaloosa County with coordinates (33.3227653, -87.460397) to GeoJSON.
    Fetching coordinates for: Shelton
    Geocoding API error: ZERO_RESULTS for location: Shelton
    Location not found: Shelton
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Tuscaloosa County
    Adding Tuscaloosa County with coordinates (33.3227653, -87.460397) to GeoJSON.
    Fetching coordinates for: Pell City
    Adding Pell City with coordinates (33.5862149, -86.2860888) to GeoJSON.
    Fetching coordinates for: Greensboro
    Adding Greensboro with coordinates (36.0725632, -79.791534) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Northport
    Adding Northport with coordinates (40.9009313, -73.3431727) to GeoJSON.
    Fetching coordinates for: Parrish
    Geocoding API error: ZERO_RESULTS for location: Parrish
    Location not found: Parrish
    Fetching coordinates for: Eutaw
    Adding Eutaw with coordinates (32.8406848, -87.8875145) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Walker County
    Adding Walker County with coordinates (30.6815394, -95.6457951) to GeoJSON.
    Fetching coordinates for: Montgomery
    Adding Montgomery with coordinates (32.3792233, -86.3077368) to GeoJSON.
    Fetching coordinates for: Montgomery
    Adding Montgomery with coordinates (32.3792233, -86.3077368) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Cottondale
    Adding Cottondale with coordinates (33.189202, -87.4565956) to GeoJSON.
    Fetching coordinates for: Bibb County
    Adding Bibb County with coordinates (32.7865735, -83.7199136) to GeoJSON.
    Fetching coordinates for: West Blocton
    Adding West Blocton with coordinates (33.1181748, -87.1249954) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Louisville
    Adding Louisville with coordinates (38.2526647, -85.7584557) to GeoJSON.
    Fetching coordinates for: Birmingham
    Adding Birmingham with coordinates (52.4822694, -1.8900078) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: University of Alabama
    Adding University of Alabama with coordinates (33.2114385, -87.5401002) to GeoJSON.
    Fetching coordinates for: York
    Adding York with coordinates (53.9614205, -1.0739108) to GeoJSON.
    Fetching coordinates for: Sumter County
    Adding Sumter County with coordinates (28.6747526, -82.08429009999999) to GeoJSON.
    Fetching coordinates for: Las Vegas
    Adding Las Vegas with coordinates (36.171563, -115.1391009) to GeoJSON.
    Fetching coordinates for: Charlotte
    Adding Charlotte with coordinates (35.2270869, -80.8431267) to GeoJSON.
    Fetching coordinates for: Brooklyn
    Adding Brooklyn with coordinates (40.6781784, -73.9441579) to GeoJSON.
    Fetching coordinates for: Sacramento
    Adding Sacramento with coordinates (38.5815719, -121.4943996) to GeoJSON.
    Fetching coordinates for: Huntsville
    Adding Huntsville with coordinates (34.7303688, -86.5861037) to GeoJSON.
    Fetching coordinates for: New Orleans
    Adding New Orleans with coordinates (29.9508941, -90.07583559999999) to GeoJSON.
    Fetching coordinates for: Houston
    Adding Houston with coordinates (29.7600771, -95.37011079999999) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: San Antonio
    Adding San Antonio with coordinates (29.4251905, -98.4945922) to GeoJSON.
    Fetching coordinates for: Oklahoma City
    Adding Oklahoma City with coordinates (35.4675602, -97.5164276) to GeoJSON.
    Fetching coordinates for: Portland
    Adding Portland with coordinates (45.515232, -122.6783853) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Northport
    Adding Northport with coordinates (40.9009313, -73.3431727) to GeoJSON.
    Fetching coordinates for: Demopolis
    Adding Demopolis with coordinates (32.5176361, -87.83640199999999) to GeoJSON.
    Fetching coordinates for: Fayette
    Adding Fayette with coordinates (33.6845539, -87.8308522) to GeoJSON.
    Fetching coordinates for: Carrollton
    Adding Carrollton with coordinates (32.9756415, -96.8899636) to GeoJSON.
    Fetching coordinates for: Livingston
    Adding Livingston with coordinates (55.90070799999999, -3.518068) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Tuscaloosa County
    Adding Tuscaloosa County with coordinates (33.3227653, -87.460397) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Dallas
    Adding Dallas with coordinates (32.7766642, -96.79698789999999) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Tuscaloosa County
    Adding Tuscaloosa County with coordinates (33.3227653, -87.460397) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Bibb County
    Adding Bibb County with coordinates (32.7865735, -83.7199136) to GeoJSON.
    Fetching coordinates for: Centreville
    Adding Centreville with coordinates (38.8403909, -77.42887689999999) to GeoJSON.
    Fetching coordinates for: West Blocton
    Adding West Blocton with coordinates (33.1181748, -87.1249954) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Norman
    Adding Norman with coordinates (35.2225668, -97.4394777) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Northport
    Adding Northport with coordinates (40.9009313, -73.3431727) to GeoJSON.
    Fetching coordinates for: Tuscaloosa County
    Adding Tuscaloosa County with coordinates (33.3227653, -87.460397) to GeoJSON.
    Fetching coordinates for: Suwannee
    Adding Suwannee with coordinates (30.24850959999999, -82.99316069999999) to GeoJSON.
    Fetching coordinates for: Mobile
    Geocoding API error: ZERO_RESULTS for location: Mobile
    Location not found: Mobile
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Tuscaloosa County
    Adding Tuscaloosa County with coordinates (33.3227653, -87.460397) to GeoJSON.
    Fetching coordinates for: University of Alabama
    Adding University of Alabama with coordinates (33.2114385, -87.5401002) to GeoJSON.
    Fetching coordinates for: Walker County
    Adding Walker County with coordinates (30.6815394, -95.6457951) to GeoJSON.
    Fetching coordinates for: Greene County
    Adding Greene County with coordinates (39.697399, -83.8897057) to GeoJSON.
    Fetching coordinates for: Auburn
    Adding Auburn with coordinates (32.6098566, -85.48078249999999) to GeoJSON.
    Fetching coordinates for: Brundidge
    Adding Brundidge with coordinates (31.7201615, -85.81605669999999) to GeoJSON.
    Fetching coordinates for: Enterprise
    Geocoding API error: ZERO_RESULTS for location: Enterprise
    Location not found: Enterprise
    Fetching coordinates for: Fort Payne
    Adding Fort Payne with coordinates (34.4442547, -85.7196893) to GeoJSON.
    Fetching coordinates for: Coosa County
    Adding Coosa County with coordinates (32.9305115, -86.17517590000001) to GeoJSON.
    Fetching coordinates for: Magic Moments
    Geocoding API error: ZERO_RESULTS for location: Magic Moments
    Location not found: Magic Moments
    Fetching coordinates for: Sokol Park
    Adding Sokol Park with coordinates (33.2646868, -87.5381831) to GeoJSON.
    Fetching coordinates for: University of Alabama
    Adding University of Alabama with coordinates (33.2114385, -87.5401002) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Tuscaloosa County
    Adding Tuscaloosa County with coordinates (33.3227653, -87.460397) to GeoJSON.
    Fetching coordinates for: Birmingham
    Adding Birmingham with coordinates (52.4822694, -1.8900078) to GeoJSON.
    Fetching coordinates for: Bessemer
    Geocoding API error: ZERO_RESULTS for location: Bessemer
    Location not found: Bessemer
    Fetching coordinates for: Cullman
    Adding Cullman with coordinates (34.1748208, -86.8436124) to GeoJSON.
    Fetching coordinates for: Jasper
    Geocoding API error: ZERO_RESULTS for location: Jasper
    Location not found: Jasper
    Fetching coordinates for: Oneonta
    Adding Oneonta with coordinates (42.4528571, -75.0637746) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Jefferson County
    Adding Jefferson County with coordinates (39.5800298, -105.2662931) to GeoJSON.
    Fetching coordinates for: Fayette
    Adding Fayette with coordinates (33.6845539, -87.8308522) to GeoJSON.
    Fetching coordinates for: Fulton
    Geocoding API error: ZERO_RESULTS for location: Fulton
    Location not found: Fulton
    Fetching coordinates for: Dora
    Geocoding API error: ZERO_RESULTS for location: Dora
    Location not found: Dora
    Fetching coordinates for: Walker County
    Adding Walker County with coordinates (30.6815394, -95.6457951) to GeoJSON.
    Fetching coordinates for: Bessemer
    Geocoding API error: ZERO_RESULTS for location: Bessemer
    Location not found: Bessemer
    Fetching coordinates for: Jasper
    Geocoding API error: ZERO_RESULTS for location: Jasper
    Location not found: Jasper
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Chicago
    Adding Chicago with coordinates (41.8781136, -87.6297982) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Tuscaloosa County
    Adding Tuscaloosa County with coordinates (33.3227653, -87.460397) to GeoJSON.
    Fetching coordinates for: Pickens County
    Adding Pickens County with coordinates (34.9046217, -82.6483442) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Northport
    Adding Northport with coordinates (40.9009313, -73.3431727) to GeoJSON.
    Fetching coordinates for: Demopolis
    Adding Demopolis with coordinates (32.5176361, -87.83640199999999) to GeoJSON.
    Fetching coordinates for: Fayette
    Adding Fayette with coordinates (33.6845539, -87.8308522) to GeoJSON.
    Fetching coordinates for: Carrollton
    Adding Carrollton with coordinates (32.9756415, -96.8899636) to GeoJSON.
    Fetching coordinates for: Livingston
    Adding Livingston with coordinates (55.90070799999999, -3.518068) to GeoJSON.
    Fetching coordinates for: Pickens County
    Adding Pickens County with coordinates (34.9046217, -82.6483442) to GeoJSON.
    Fetching coordinates for: Carrollton
    Adding Carrollton with coordinates (32.9756415, -96.8899636) to GeoJSON.
    Fetching coordinates for: Birmingham
    Adding Birmingham with coordinates (52.4822694, -1.8900078) to GeoJSON.
    Fetching coordinates for: Hope Hull
    Adding Hope Hull with coordinates (32.2695189, -86.3567376) to GeoJSON.
    Fetching coordinates for: Dothan
    Adding Dothan with coordinates (31.2232313, -85.3904888) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Montgomery
    Adding Montgomery with coordinates (32.3792233, -86.3077368) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Tuscaloosa County
    Adding Tuscaloosa County with coordinates (33.3227653, -87.460397) to GeoJSON.
    Fetching coordinates for: Mercer
    Geocoding API error: ZERO_RESULTS for location: Mercer
    Location not found: Mercer
    Fetching coordinates for: Norman
    Adding Norman with coordinates (35.2225668, -97.4394777) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Montgomery
    Adding Montgomery with coordinates (32.3792233, -86.3077368) to GeoJSON.
    Fetching coordinates for: Greene County
    Adding Greene County with coordinates (39.697399, -83.8897057) to GeoJSON.
    Fetching coordinates for: Fayette
    Adding Fayette with coordinates (33.6845539, -87.8308522) to GeoJSON.
    Fetching coordinates for: Hale County
    Adding Hale County with coordinates (32.7859102, -87.6186379) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Haleyville
    Adding Haleyville with coordinates (34.226488, -87.6214133) to GeoJSON.
    Fetching coordinates for: Bibb County
    Adding Bibb County with coordinates (32.7865735, -83.7199136) to GeoJSON.
    Fetching coordinates for: West Blocton
    Adding West Blocton with coordinates (33.1181748, -87.1249954) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Northport
    Adding Northport with coordinates (40.9009313, -73.3431727) to GeoJSON.
    Fetching coordinates for: Tuscaloosa County
    Adding Tuscaloosa County with coordinates (33.3227653, -87.460397) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Atmore
    Adding Atmore with coordinates (31.0237921, -87.4938708) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Central High
    Geocoding API error: ZERO_RESULTS for location: Central High
    Location not found: Central High
    Fetching coordinates for: Oakdale Elementary
    Geocoding API error: ZERO_RESULTS for location: Oakdale Elementary
    Location not found: Oakdale Elementary
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Birmingham
    Adding Birmingham with coordinates (52.4822694, -1.8900078) to GeoJSON.
    Fetching coordinates for: Parrish
    Geocoding API error: ZERO_RESULTS for location: Parrish
    Location not found: Parrish
    Fetching coordinates for: Walker County
    Adding Walker County with coordinates (30.6815394, -95.6457951) to GeoJSON.
    Fetching coordinates for: Jasper
    Geocoding API error: ZERO_RESULTS for location: Jasper
    Location not found: Jasper
    Fetching coordinates for: Tuscaloosa County
    Adding Tuscaloosa County with coordinates (33.3227653, -87.460397) to GeoJSON.
    Fetching coordinates for: T-Town
    Adding T-Town with coordinates (22.4622473, 113.9978303) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Moundville
    Adding Moundville with coordinates (32.9976242, -87.6300075) to GeoJSON.
    Fetching coordinates for: Hale County
    Adding Hale County with coordinates (32.7859102, -87.6186379) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Fayette
    Adding Fayette with coordinates (33.6845539, -87.8308522) to GeoJSON.
    Fetching coordinates for: Fayette County
    Adding Fayette County with coordinates (33.4502206, -84.4802606) to GeoJSON.
    Fetching coordinates for: Perry County
    Adding Perry County with coordinates (40.371376, -77.2405153) to GeoJSON.
    Fetching coordinates for: Dallas County
    Adding Dallas County with coordinates (32.8024682, -96.83509989999999) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Tuscaloosa County
    Adding Tuscaloosa County with coordinates (33.3227653, -87.460397) to GeoJSON.
    Fetching coordinates for: Northport
    Adding Northport with coordinates (40.9009313, -73.3431727) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Kaulton Park
    Adding Kaulton Park with coordinates (33.1857445, -87.5738788) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Sioux Falls
    Adding Sioux Falls with coordinates (43.5460223, -96.731265) to GeoJSON.
    Fetching coordinates for: Fresno
    Adding Fresno with coordinates (36.7377981, -119.7871247) to GeoJSON.
    Fetching coordinates for: Aliceville
    Adding Aliceville with coordinates (33.1295681, -88.15141659999999) to GeoJSON.
    Fetching coordinates for: Pickens County
    Adding Pickens County with coordinates (34.9046217, -82.6483442) to GeoJSON.
    Fetching coordinates for: University of Alabama
    Adding University of Alabama with coordinates (33.2114385, -87.5401002) to GeoJSON.
    Fetching coordinates for: Reese Phifer Hall
    Adding Reese Phifer Hall with coordinates (33.209567, -87.54893369999999) to GeoJSON.
    Fetching coordinates for: Bryant-Denny Stadium
    Adding Bryant-Denny Stadium with coordinates (33.2082752, -87.55038359999999) to GeoJSON.
    Fetching coordinates for: Campus Drive
    Geocoding API error: ZERO_RESULTS for location: Campus Drive
    Location not found: Campus Drive
    Fetching coordinates for: Dallas
    Adding Dallas with coordinates (32.7766642, -96.79698789999999) to GeoJSON.
    Fetching coordinates for: University of Alabama
    Adding University of Alabama with coordinates (33.2114385, -87.5401002) to GeoJSON.
    Fetching coordinates for: Snow Hinton Park
    Adding Snow Hinton Park with coordinates (33.1886308, -87.5241296) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Cherokee County
    Adding Cherokee County with coordinates (34.2514526, -84.4802606) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Brookwood
    Geocoding API error: ZERO_RESULTS for location: Brookwood
    Location not found: Brookwood
    Fetching coordinates for: Choctaw County
    Adding Choctaw County with coordinates (32.0716631, -88.24611829999999) to GeoJSON.
    Fetching coordinates for: Denton
    Adding Denton with coordinates (33.2148412, -97.13306829999999) to GeoJSON.
    Fetching coordinates for: Dallas
    Adding Dallas with coordinates (32.7766642, -96.79698789999999) to GeoJSON.
    Fetching coordinates for: Dallas
    Adding Dallas with coordinates (32.7766642, -96.79698789999999) to GeoJSON.
    Fetching coordinates for: Greene
    Adding Greene with coordinates (39.697399, -83.8897057) to GeoJSON.
    Fetching coordinates for: Hale
    Geocoding API error: ZERO_RESULTS for location: Hale
    Location not found: Hale
    Fetching coordinates for: Sumter
    Adding Sumter with coordinates (33.9204354, -80.3414693) to GeoJSON.
    Fetching coordinates for: Bibb
    Adding Bibb with coordinates (32.7865735, -83.7199136) to GeoJSON.
    Fetching coordinates for: Choctaw
    Geocoding API error: ZERO_RESULTS for location: Choctaw
    Location not found: Choctaw
    Fetching coordinates for: Fayette
    Adding Fayette with coordinates (33.6845539, -87.8308522) to GeoJSON.
    Fetching coordinates for: Lamar
    Geocoding API error: ZERO_RESULTS for location: Lamar
    Location not found: Lamar
    Fetching coordinates for: Perry
    Adding Perry with coordinates (32.4582065, -83.7315723) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: West Alabama
    Adding West Alabama with coordinates (33.2570618, -85.41661719999999) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Shelton
    Geocoding API error: ZERO_RESULTS for location: Shelton
    Location not found: Shelton
    Fetching coordinates for: Moundville
    Adding Moundville with coordinates (32.9976242, -87.6300075) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Tuscaloosa County
    Adding Tuscaloosa County with coordinates (33.3227653, -87.460397) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Mobile
    Geocoding API error: ZERO_RESULTS for location: Mobile
    Location not found: Mobile
    Fetching coordinates for: LSU
    Adding LSU with coordinates (30.4132579, -91.1800023) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Tiger Stadium
    Adding Tiger Stadium with coordinates (30.412035, -91.18381629999999) to GeoJSON.
    Fetching coordinates for: Gainesville
    Adding Gainesville with coordinates (29.6519563, -82.324998) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Milwaukee
    Adding Milwaukee with coordinates (43.0389025, -87.9064736) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Northport
    Adding Northport with coordinates (40.9009313, -73.3431727) to GeoJSON.
    Fetching coordinates for: Perry County
    Adding Perry County with coordinates (40.371376, -77.2405153) to GeoJSON.
    Fetching coordinates for: Dallas County
    Adding Dallas County with coordinates (32.8024682, -96.83509989999999) to GeoJSON.
    Fetching coordinates for: Newbern
    Adding Newbern with coordinates (35.108493, -77.04411429999999) to GeoJSON.
    Fetching coordinates for: Northport
    Adding Northport with coordinates (40.9009313, -73.3431727) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Meridian
    Geocoding API error: ZERO_RESULTS for location: Meridian
    Location not found: Meridian
    Fetching coordinates for: Vance
    Geocoding API error: ZERO_RESULTS for location: Vance
    Location not found: Vance
    Fetching coordinates for: Eutaw
    Adding Eutaw with coordinates (32.8406848, -87.8875145) to GeoJSON.
    Fetching coordinates for: Jackson
    Geocoding API error: ZERO_RESULTS for location: Jackson
    Location not found: Jackson
    Fetching coordinates for: Brookhaven
    Adding Brookhaven with coordinates (33.8650186, -84.33712659999999) to GeoJSON.
    Fetching coordinates for: Tuscaloosa County
    Adding Tuscaloosa County with coordinates (33.3227653, -87.460397) to GeoJSON.
    Fetching coordinates for: Northport
    Adding Northport with coordinates (40.9009313, -73.3431727) to GeoJSON.
    Fetching coordinates for: Houston
    Adding Houston with coordinates (29.7600771, -95.37011079999999) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Philadelphia
    Adding Philadelphia with coordinates (39.9525839, -75.1652215) to GeoJSON.
    Fetching coordinates for: Detroit
    Adding Detroit with coordinates (42.331427, -83.0457538) to GeoJSON.
    Fetching coordinates for: Diamondbacks
    Geocoding API error: ZERO_RESULTS for location: Diamondbacks
    Location not found: Diamondbacks
    Fetching coordinates for: Rangers
    Geocoding API error: ZERO_RESULTS for location: Rangers
    Location not found: Rangers
    Fetching coordinates for: Yankees
    Geocoding API error: ZERO_RESULTS for location: Yankees
    Location not found: Yankees
    Fetching coordinates for: White Sox
    Geocoding API error: ZERO_RESULTS for location: White Sox
    Location not found: White Sox
    Fetching coordinates for: Mets
    Geocoding API error: ZERO_RESULTS for location: Mets
    Location not found: Mets
    Fetching coordinates for: Rays
    Geocoding API error: ZERO_RESULTS for location: Rays
    Location not found: Rays
    Fetching coordinates for: Cubs
    Geocoding API error: ZERO_RESULTS for location: Cubs
    Location not found: Cubs
    Fetching coordinates for: Marlins
    Geocoding API error: ZERO_RESULTS for location: Marlins
    Location not found: Marlins
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Tuscaloosa County
    Adding Tuscaloosa County with coordinates (33.3227653, -87.460397) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Central Alabama
    Adding Central Alabama with coordinates (34.2248222, -87.00917419999999) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Tuscaloosa County
    Adding Tuscaloosa County with coordinates (33.3227653, -87.460397) to GeoJSON.
    Fetching coordinates for: Northport
    Adding Northport with coordinates (40.9009313, -73.3431727) to GeoJSON.
    Fetching coordinates for: Northport
    Adding Northport with coordinates (40.9009313, -73.3431727) to GeoJSON.
    Fetching coordinates for: Fosters
    Geocoding API error: ZERO_RESULTS for location: Fosters
    Location not found: Fosters
    Fetching coordinates for: Talladega
    Adding Talladega with coordinates (33.4359416, -86.1058048) to GeoJSON.
    Fetching coordinates for: Indian Hills
    Geocoding API error: ZERO_RESULTS for location: Indian Hills
    Location not found: Indian Hills
    Fetching coordinates for: Butler
    Adding Butler with coordinates (39.8399145, -86.17260209999999) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Birmingham
    Adding Birmingham with coordinates (52.4822694, -1.8900078) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Pickens County
    Adding Pickens County with coordinates (34.9046217, -82.6483442) to GeoJSON.
    Fetching coordinates for: Lamar County
    Adding Lamar County with coordinates (33.75694, -95.6457951) to GeoJSON.
    Fetching coordinates for: Fayette County
    Adding Fayette County with coordinates (33.4502206, -84.4802606) to GeoJSON.
    Fetching coordinates for: Walker County
    Adding Walker County with coordinates (30.6815394, -95.6457951) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Northport
    Adding Northport with coordinates (40.9009313, -73.3431727) to GeoJSON.
    Fetching coordinates for: Tuscaloosa County
    Adding Tuscaloosa County with coordinates (33.3227653, -87.460397) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Queen City
    Adding Queen City with coordinates (39.1031182, -84.5120196) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Fosters
    Geocoding API error: ZERO_RESULTS for location: Fosters
    Location not found: Fosters
    Fetching coordinates for: Cottondale
    Adding Cottondale with coordinates (33.189202, -87.4565956) to GeoJSON.
    Fetching coordinates for: West Alabama
    Adding West Alabama with coordinates (33.2570618, -85.41661719999999) to GeoJSON.
    Fetching coordinates for: Northport
    Adding Northport with coordinates (40.9009313, -73.3431727) to GeoJSON.
    Fetching coordinates for: Berry
    Adding Berry with coordinates (-34.7757734, 150.6988896) to GeoJSON.
    Fetching coordinates for: Tuscaloosa County
    Adding Tuscaloosa County with coordinates (33.3227653, -87.460397) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Bibb County
    Adding Bibb County with coordinates (32.7865735, -83.7199136) to GeoJSON.
    Fetching coordinates for: Brierfield
    Adding Brierfield with coordinates (33.0390099, -86.908879) to GeoJSON.
    Fetching coordinates for: Selma
    Adding Selma with coordinates (32.4073589, -87.02110069999999) to GeoJSON.
    Fetching coordinates for: Trussville
    Adding Trussville with coordinates (33.6198251, -86.60887559999999) to GeoJSON.
    Fetching coordinates for: North Alabama
    Adding North Alabama with coordinates (34.807836, -87.6804676) to GeoJSON.
    Fetching coordinates for: Tuscaloosa County
    Adding Tuscaloosa County with coordinates (33.3227653, -87.460397) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Birmingham
    Adding Birmingham with coordinates (52.4822694, -1.8900078) to GeoJSON.
    Fetching coordinates for: Atlanta
    Adding Atlanta with coordinates (33.748752, -84.38768449999999) to GeoJSON.
    Fetching coordinates for: USC
    Adding USC with coordinates (34.0223519, -118.285117) to GeoJSON.
    Fetching coordinates for: LSU
    Adding LSU with coordinates (30.4132579, -91.1800023) to GeoJSON.
    Fetching coordinates for: Birmingham
    Adding Birmingham with coordinates (52.4822694, -1.8900078) to GeoJSON.
    Fetching coordinates for: University of Alabama
    Adding University of Alabama with coordinates (33.2114385, -87.5401002) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Birmingham
    Adding Birmingham with coordinates (52.4822694, -1.8900078) to GeoJSON.
    Fetching coordinates for: Jefferson County
    Adding Jefferson County with coordinates (39.5800298, -105.2662931) to GeoJSON.
    Fetching coordinates for: Florence
    Adding Florence with coordinates (43.7699685, 11.2576706) to GeoJSON.
    Fetching coordinates for: Grace Presbyterian Church
    Adding Grace Presbyterian Church with coordinates (40.7921349, -89.671759) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Tuscaloosa County
    Adding Tuscaloosa County with coordinates (33.3227653, -87.460397) to GeoJSON.
    Fetching coordinates for: Coker
    Geocoding API error: ZERO_RESULTS for location: Coker
    Location not found: Coker
    Fetching coordinates for: Holt
    Geocoding API error: ZERO_RESULTS for location: Holt
    Location not found: Holt
    Fetching coordinates for: Tuscaloosa County
    Adding Tuscaloosa County with coordinates (33.3227653, -87.460397) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Birmingham
    Adding Birmingham with coordinates (52.4822694, -1.8900078) to GeoJSON.
    Fetching coordinates for: Birmingport
    Geocoding API error: ZERO_RESULTS for location: Birmingport
    Location not found: Birmingport
    Fetching coordinates for: Demopolis
    Adding Demopolis with coordinates (32.5176361, -87.83640199999999) to GeoJSON.
    Fetching coordinates for: Mobile
    Geocoding API error: ZERO_RESULTS for location: Mobile
    Location not found: Mobile
    Fetching coordinates for: Tuscaloosa County
    Adding Tuscaloosa County with coordinates (33.3227653, -87.460397) to GeoJSON.
    Fetching coordinates for: Lake View
    Geocoding API error: ZERO_RESULTS for location: Lake View
    Location not found: Lake View
    Fetching coordinates for: Augusta
    Adding Augusta with coordinates (33.4687314, -82.0283188) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Mobile
    Geocoding API error: ZERO_RESULTS for location: Mobile
    Location not found: Mobile
    Fetching coordinates for: Tuscaloosa County
    Adding Tuscaloosa County with coordinates (33.3227653, -87.460397) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Northport
    Adding Northport with coordinates (40.9009313, -73.3431727) to GeoJSON.
    Fetching coordinates for: Demopolis
    Adding Demopolis with coordinates (32.5176361, -87.83640199999999) to GeoJSON.
    Fetching coordinates for: Fayette
    Adding Fayette with coordinates (33.6845539, -87.8308522) to GeoJSON.
    Fetching coordinates for: Carrollton
    Adding Carrollton with coordinates (32.9756415, -96.8899636) to GeoJSON.
    Fetching coordinates for: Livingston
    Adding Livingston with coordinates (55.90070799999999, -3.518068) to GeoJSON.
    Fetching coordinates for: Columbia
    Geocoding API error: ZERO_RESULTS for location: Columbia
    Location not found: Columbia
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Baton Rouge
    Adding Baton Rouge with coordinates (30.4514677, -91.18714659999999) to GeoJSON.
    Fetching coordinates for: Moundville
    Adding Moundville with coordinates (32.9976242, -87.6300075) to GeoJSON.
    Fetching coordinates for: Birmingham
    Adding Birmingham with coordinates (52.4822694, -1.8900078) to GeoJSON.
    Fetching coordinates for: Calhoun
    Geocoding API error: ZERO_RESULTS for location: Calhoun
    Location not found: Calhoun
    Fetching coordinates for: Conecuh
    Adding Conecuh with coordinates (31.501571, -86.9824288) to GeoJSON.
    Fetching coordinates for: Crenshaw
    Adding Crenshaw with coordinates (34.0181993, -118.3403506) to GeoJSON.
    Fetching coordinates for: Cullman
    Adding Cullman with coordinates (34.1748208, -86.8436124) to GeoJSON.
    Fetching coordinates for: Escambia
    Adding Escambia with coordinates (30.6389408, -87.3413599) to GeoJSON.
    Fetching coordinates for: Jackson
    Geocoding API error: ZERO_RESULTS for location: Jackson
    Location not found: Jackson
    Fetching coordinates for: Marshall
    Geocoding API error: ZERO_RESULTS for location: Marshall
    Location not found: Marshall
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Shelby
    Geocoding API error: ZERO_RESULTS for location: Shelby
    Location not found: Shelby
    Fetching coordinates for: Morgan
    Geocoding API error: ZERO_RESULTS for location: Morgan
    Location not found: Morgan
    Fetching coordinates for: Baldwin
    Geocoding API error: ZERO_RESULTS for location: Baldwin
    Location not found: Baldwin
    Fetching coordinates for: Gulf Shores
    Adding Gulf Shores with coordinates (30.2460361, -87.70081929999999) to GeoJSON.
    Fetching coordinates for: Orange Beach
    Adding Orange Beach with coordinates (30.2697033, -87.5867598) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Tuscaloosa County
    Adding Tuscaloosa County with coordinates (33.3227653, -87.460397) to GeoJSON.
    Fetching coordinates for: Brookwood
    Geocoding API error: ZERO_RESULTS for location: Brookwood
    Location not found: Brookwood
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Northridge
    Adding Northridge with coordinates (34.2354576, -118.5361381) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Pickens County
    Adding Pickens County with coordinates (34.9046217, -82.6483442) to GeoJSON.
    Fetching coordinates for: West Alabama
    Adding West Alabama with coordinates (33.2570618, -85.41661719999999) to GeoJSON.
    Fetching coordinates for: Midtown Village
    Adding Midtown Village with coordinates (39.9494949, -75.16110479999999) to GeoJSON.
    Fetching coordinates for: Tuscaloosa
    Adding Tuscaloosa with coordinates (33.2098407, -87.56917349999999) to GeoJSON.
    Fetching coordinates for: Tuscaloosa County
    Adding Tuscaloosa County with coordinates (33.3227653, -87.460397) to GeoJSON.
    Fetching coordinates for: Moundville
    Adding Moundville with coordinates (32.9976242, -87.6300075) to GeoJSON.
    Fetching coordinates for: Demopolis
    Adding Demopolis with coordinates (32.5176361, -87.83640199999999) to GeoJSON.
    Fetching coordinates for: Providence
    Adding Providence with coordinates (41.8239891, -71.4128343) to GeoJSON.
    Fetching coordinates for: Greensboro
    Adding Greensboro with coordinates (36.0725632, -79.791534) to GeoJSON.
    Fetching coordinates for: Thomasville
    Geocoding API error: ZERO_RESULTS for location: Thomasville
    Location not found: Thomasville
    Fetching coordinates for: Hale County
    Adding Hale County with coordinates (32.7859102, -87.6186379) to GeoJSON.
    GeoJSON update complete.
    


```python
from geopy.geocoders import GoogleV3
import json
import time

# Set up GoogleV3 geolocator with your API key
geolocator = GoogleV3(api_key='AIzaSyChg3ArAuJhYKEY2mv_CVOWHYYJ1tFHhvA')

# Define fallback coordinates for locations that cannot be found
fallback_location = (32.779, -96.8)  # Example: Dallas, TX coordinates

# List to store locations that could not be found
not_found_locations = []

# Function to get coordinates with retry logic
def get_coordinates(location_name, retries=3, delay=2):
    try:
        location = geolocator.geocode(location_name)
        if location:
            return location.latitude, location.longitude
        else:
            print(f"Location not found: {location_name}")
            not_found_locations.append(location_name)
            return fallback_location
    except Exception as e:
        if retries > 0:
            print(f"Error fetching coordinates for {location_name}: {e}. Retrying {retries} more times...")
            time.sleep(delay)  # Wait before retrying
            return get_coordinates(location_name, retries - 1, delay)
        else:
            print(f"Failed to fetch coordinates for {location_name} after retries. Error: {e}")
            not_found_locations.append(location_name)
            return fallback_location

# Example locations list
locations = [
    "West Side", "Shelton", "Magic Moments, Sokol Park", "Mercer, Norman",
    "Montgomery, Greene County", "City1", "Mobile", "Fosters", "Indian Hills","Nauvoo", "Walker County",
"Tuscaloosa", "Tuscaloosa County",
"Hale County", "Greensboro", "Sawyerville", "Akron", "Moundville",
"Auburn", "Central-Phenix City",
"Brookwood", "Hoover",
"West Alabama",
"Nauvoo",
"Bibb County", "Fayette County", "Greene County", "Hale County", "Pickens County", "Tuscaloosa County", "Walker County", "Shelby County", "Morgan County", "Marshall County", "Cullman County", "Madison County", "Limestone County", "Elmore County", "Wilcox County", "Perry County", "Dallas County", "Trussville", "Vestavia Hills", "Alabaster", "Hoover", "Homewood", "Athens", "Decatur", "Selma", "Prichard", "Bessemer",
"Tuscaloosa",
"University of Alabama", "RISE Center",
"Tuscaloosa", "Tuscaloosa County", "Cottondale",
"Tuscaloosa", "Northridge",
"West Side",
"Tuscaloosa",
"Northport",
"Tuscaloosa", "Saraland", "Mobile",
"Greensboro", "Hale County", "Bibb County", "Greene County", "Tuscaloosa County",
"Lake View", "Tuscaloosa County",
"Macon", "Russell", "Elmore", "Autauga", "Chilton", "Shelby", "Dallas", "Perry", "Bibb", "Fayette", "Greene", "Hale", "Pickens", "Lamar", "Sumter", "Tuscaloosa", "Cullman", "Lawrence", "Morgan", "Marion", "Walker", "Winston",
"Tuscaloosa County",
"Shelton",
"Tuscaloosa", "Tuscaloosa County",
"Pell City",
"Greensboro", "Tuscaloosa",
"Northport", "Parrish", "Eutaw", "Tuscaloosa", "Walker County",
"Montgomery",
"Montgomery",
"Tuscaloosa", "Cottondale",
"Bibb County", "West Blocton",
"Tuscaloosa",
"Louisville", "Birmingham",
"Tuscaloosa",
"University of Alabama",
"York", "Sumter County",
"Las Vegas", "Charlotte", "Brooklyn", "Sacramento", "Huntsville", "New Orleans", "Houston", "Tuscaloosa", "San Antonio", "Oklahoma City", "Portland",
"Tuscaloosa", "Northport", "Demopolis", "Fayette", "Carrollton", "Livingston",
"Tuscaloosa", "Tuscaloosa County",
"Tuscaloosa",
"Tuscaloosa",
"Dallas",
"Tuscaloosa",
"Tuscaloosa County", "Tuscaloosa",
"Bibb County", "Centreville", "West Blocton",
"Tuscaloosa",
"Norman", "Tuscaloosa",
"Tuscaloosa",
"Tuscaloosa",
"Northport", "Tuscaloosa County",
"Suwannee", "Mobile",
"Tuscaloosa", "Tuscaloosa County",
"University of Alabama",
"Walker County", "Greene County", "Auburn", "Brundidge", "Enterprise", "Fort Payne", "Coosa County",
"Magic Moments", "Sokol Park",
"University of Alabama",
"Tuscaloosa", "Tuscaloosa County",
"Birmingham", "Bessemer", "Cullman", "Jasper", "Oneonta", "Tuscaloosa", "Jefferson County",
"Fayette", "Fulton",
"Dora", "Walker County", "Bessemer", "Jasper",
"Tuscaloosa", "Chicago",
"Tuscaloosa", "Tuscaloosa County",
"Pickens County",
"Tuscaloosa",
"Tuscaloosa", "Northport", "Demopolis", "Fayette", "Carrollton", "Livingston",
"Pickens County", "Carrollton",
"Birmingham", "Hope Hull", "Dothan", "Tuscaloosa", "Montgomery",
"Tuscaloosa", "Tuscaloosa County",
"Mercer", "Norman",
"Tuscaloosa",
"Montgomery", "Greene County",
"Fayette",
"Hale County",
"Tuscaloosa",
"Tuscaloosa", "Haleyville",
"Bibb County", "West Blocton",
"Tuscaloosa", "Northport", "Tuscaloosa County",
"Tuscaloosa", "Atmore",
"Tuscaloosa", "Central High", "Oakdale Elementary",
"Tuscaloosa",
"Tuscaloosa",
"Birmingham",
"Parrish", "Walker County", "Jasper",
"Tuscaloosa County", "T-Town",
"Tuscaloosa",
"Moundville", "Hale County",
"Tuscaloosa",
"Fayette", "Fayette County",
"Perry County", "Dallas County",
"Tuscaloosa", "Tuscaloosa County",
"Northport",
"Tuscaloosa", "Kaulton Park",
"Tuscaloosa", "Sioux Falls", "Fresno",
"Aliceville", "Pickens County",
"University of Alabama", "Reese Phifer Hall", "Bryant-Denny Stadium", "Campus Drive",
"Dallas",
"University of Alabama", "Snow Hinton Park",
"Tuscaloosa",
"Tuscaloosa",
"Tuscaloosa",
"Cherokee County",
"Tuscaloosa", "Brookwood",
"Choctaw County", "Denton", "Dallas",
"Dallas", "Greene", "Hale", "Sumter", "Bibb", "Choctaw", "Fayette", "Lamar", "Perry", "Tuscaloosa",
"West Alabama",
"Tuscaloosa",
"Shelton",
"Moundville",
"Tuscaloosa",
"Tuscaloosa County",
"Tuscaloosa",
"Mobile",
"LSU", "Tuscaloosa", "Tiger Stadium", "Gainesville",
"Tuscaloosa",
"Milwaukee",
"Tuscaloosa",
"Northport",
"Perry County", "Dallas County", "Newbern",
"Northport",
"Tuscaloosa", "Meridian", "Vance", "Eutaw", "Jackson", "Brookhaven", "Tuscaloosa County",
"Northport",
"Houston",
"Tuscaloosa", "Philadelphia", "Detroit", "Diamondbacks", "Rangers", "Yankees", "White Sox", "Mets", "Rays", "Cubs", "Marlins",
"Tuscaloosa", "Tuscaloosa County",
"Tuscaloosa",
"Tuscaloosa",
"Tuscaloosa",
"Central Alabama",
"Tuscaloosa",
"Tuscaloosa",
"Tuscaloosa County", "Northport",
"Northport",
"Fosters",
"Talladega",
"Indian Hills",
"Butler",
"Tuscaloosa",
"Birmingham", "Tuscaloosa", "Pickens County", "Lamar County", "Fayette County", "Walker County",
"Tuscaloosa",
"Tuscaloosa",
"Tuscaloosa", "Northport", "Tuscaloosa County",
"Tuscaloosa", "Queen City",
"Tuscaloosa", "Fosters", "Cottondale",
"West Alabama", "Northport",
"Berry", "Tuscaloosa County",
"Tuscaloosa",
"Bibb County", "Brierfield",
"Selma",
"Trussville", "North Alabama",
"Tuscaloosa County",
"Tuscaloosa",
"Birmingham",
"Atlanta", "USC", "LSU",
"Birmingham", "University of Alabama",
"Tuscaloosa",
"Birmingham", "Jefferson County",
"Florence", "Grace Presbyterian Church",
"Tuscaloosa", "Tuscaloosa County",
"Coker",
"Holt", "Tuscaloosa County",
"Tuscaloosa",
"Birmingham", "Birmingport", "Demopolis", "Mobile",
"Tuscaloosa County", "Lake View",
"Augusta",
"Tuscaloosa",
"Mobile", "Tuscaloosa County",
"Tuscaloosa", "Northport", "Demopolis", "Fayette", "Carrollton", "Livingston",
"Columbia", "Tuscaloosa", "Baton Rouge",
"Moundville", "Birmingham",
"Calhoun", "Conecuh", "Crenshaw", "Cullman", "Escambia", "Jackson", "Marshall", "Tuscaloosa", "Shelby", "Morgan", "Baldwin", "Gulf Shores", "Orange Beach",
"Tuscaloosa",
"Tuscaloosa County", "Brookwood",
"Tuscaloosa", "Northridge",
"Tuscaloosa",
"Tuscaloosa", "Pickens County",
"West Alabama", "Midtown Village",
"Tuscaloosa", "Tuscaloosa County",
"Moundville", "Demopolis", "Providence", "Greensboro", "Thomasville", "Hale County",
]

# Dictionary to store location name and coordinates
geo_data = {}

# Fetch coordinates for each location
for loc in locations:
    coords = get_coordinates(loc)
    geo_data[loc] = coords

# Save the geo_data to a JSON file
with open('geo_data.json', 'w') as f:
    json.dump(geo_data, f, indent=4)

# Log locations that were not found
with open('not_found_locations.txt', 'w') as nf:
    for location in not_found_locations:
        nf.write(location + '\n')

print(f"Geocoding completed. {len(not_found_locations)} locations could not be found.")

```

    Location not found: West Side
    Location not found: Shelton
    Location not found: Magic Moments, Sokol Park
    Location not found: Mercer, Norman
    Location not found: Montgomery, Greene County
    Location not found: City1
    Location not found: Mobile
    Location not found: Fosters
    Location not found: Indian Hills
    Location not found: Brookwood
    Location not found: Hoover
    Location not found: Alabaster
    Location not found: Hoover
    Location not found: Prichard
    Location not found: Bessemer
    Location not found: RISE Center
    Location not found: West Side
    Location not found: Mobile
    Location not found: Lake View
    Location not found: Russell
    Location not found: Elmore
    Location not found: Chilton
    Location not found: Shelby
    Location not found: Hale
    Location not found: Pickens
    Location not found: Lamar
    Location not found: Lawrence
    Location not found: Morgan
    Location not found: Marion
    Location not found: Walker
    Location not found: Winston
    Location not found: Shelton
    Location not found: Parrish
    Location not found: Mobile
    Location not found: Enterprise
    Location not found: Magic Moments
    Location not found: Bessemer
    Location not found: Jasper
    Location not found: Fulton
    Location not found: Dora
    Location not found: Bessemer
    Location not found: Jasper
    Location not found: Mercer
    Location not found: Central High
    Location not found: Oakdale Elementary
    Location not found: Parrish
    Location not found: Jasper
    Location not found: Campus Drive
    Location not found: Brookwood
    Location not found: Hale
    Location not found: Choctaw
    Location not found: Lamar
    Location not found: Shelton
    Location not found: Mobile
    Location not found: Meridian
    Location not found: Vance
    Location not found: Jackson
    Location not found: Diamondbacks
    Location not found: Rangers
    Location not found: Yankees
    Location not found: White Sox
    Location not found: Mets
    Location not found: Rays
    Location not found: Cubs
    Location not found: Marlins
    Location not found: Fosters
    Location not found: Indian Hills
    Location not found: Fosters
    Location not found: Coker
    Location not found: Holt
    Location not found: Birmingport
    Location not found: Mobile
    Location not found: Lake View
    Location not found: Mobile
    Location not found: Columbia
    Location not found: Calhoun
    Location not found: Jackson
    Location not found: Marshall
    Location not found: Shelby
    Location not found: Morgan
    Location not found: Baldwin
    Location not found: Brookwood
    Location not found: Thomasville
    Geocoding completed. 83 locations could not be found.
    


```python
import requests
import folium
import pandas as pd
from geopy.geocoders import GoogleV3
import geopandas as gpd
from shapely.geometry import Point

# File path to your CSV file
csv_file = "D:\\News Project\\all the data sets\\gpt\\wvua_news_gpt_trial_28.csv"

# Insert your Google Maps API Key here
API_KEY = 'AIzaSyChg3ArAuJhYKEY2mv_CVOWHYYJ1tFHhvA'  # Replace with your actual Google API key

# Initialize the geocoder
geolocator = GoogleV3(api_key=API_KEY)

# Function to safely read a CSV file
def read_csv_file(file_path):
    try:
        # Use on_bad_lines='skip' to ignore problematic lines
        df = pd.read_csv(file_path, encoding='ISO-8859-1', on_bad_lines='skip')
        return df
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None

# Read the CSV file
df = read_csv_file(csv_file)

# Check if the dataframe was loaded successfully
if df is not None:
    locations = df['Locations'].dropna().tolist()  # Extract location list from 'Locations' column
else:
    print("Error: Dataframe could not be loaded.")
    locations = []

# Function to geocode a location using Google Maps API
def geocode_location(location):
    try:
        location_data = geolocator.geocode(location)
        if location_data:
            return (location_data.latitude, location_data.longitude)  # Return latitude and longitude
        else:
            print(f"Location not found: {location}")
            return None
    except Exception as e:
        print(f"Error geocoding {location}: {e}")
        return None

# Create a Folium map centered around Alabama
alabama_coords = [33.5186, -86.8104]
map = folium.Map(location=alabama_coords, zoom_start=6)

# Path to the GeoJSON file containing county boundaries
geojson_file = "C:\\Users\\ADARSH G\\Downloads\\updated_geojson_file.geojson"

# Load GeoJSON data
try:
    gdf = gpd.read_file(geojson_file)
except Exception as e:
    print(f"Error loading GeoJSON file: {e}")
    gdf = None

# Function to check if a point lies within a GeoJSON region
def is_point_in_region(lat_lon, region):
    point = Point(lat_lon[1], lat_lon[0])  # Longitude first for Shapely
    return region.geometry.contains(point)

# Plot the locations on the map if the GeoJSON file is loaded
if gdf is not None and locations:
    for location in locations:
        lat_lon = geocode_location(location)
        if lat_lon:
            for _, region in gdf.iterrows():
                # Check if the location is within the region's geometry
                if is_point_in_region(lat_lon, region):
                    # Add the region as a blue polygon to the map
                    folium.GeoJson(
                        region.geometry,
                        style_function=lambda x: {'fillColor': 'blue', 'color': 'blue', 'weight': 2, 'fillOpacity': 0.5},
                        tooltip=location
                    ).add_to(map)
                    break  # Stop checking once the correct region is found
        else:
            print(f"Skipping location: {location}, coordinates not found.")

else:
    print("Error: No locations to plot or GeoJSON data not available.")

# Save the map to an HTML file
map_file = 'news_locations_map_2.html'
try:
    map.save(map_file)
    print(f"Map has been saved as '{map_file}'")
except Exception as e:
    print(f"Error saving the map: {e}")

```

    Map has been saved as 'news_locations_map_2.html'
    


```python
##code for map with the locations in point manner
import folium
import pandas as pd
from geopy.geocoders import GoogleV3
import random

# Insert your Google Maps API Key here
API_KEY = 'AIzaSyChg3ArAuJhYKEY2mv_CVOWHYYJ1tFHhvA'  # Add your Google API Key

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
csv_file = "D:\\News Project\\all the data sets\\gpt\\wvua_news_gpt_trial_29.csv"
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

# Function to assign a random color for county polygons
def get_random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

# Create a Folium map centered around Alabama
alabama_coords = [33.5186, -86.8104]
map = folium.Map(location=alabama_coords, zoom_start=6)

# Process and plot locations
if locations:
    for loc_group in locations:
        loc_list = loc_group.split('/')
        
        for loc in loc_list:
            parts = loc.strip().rsplit(',', 1)  # Split by the last comma
            if len(parts) == 2:
                city = parts[0].strip()
                state = parts[1].strip()
                lat_lon = geocode_location(city, state)  # Geocode the city/state
                if lat_lon:
                    folium.Marker(
                        location=lat_lon,
                        tooltip=f"{city}, {state}",
                        icon=folium.Icon(color='blue', icon='info-sign')
                    ).add_to(map)

# Save the map to an HTML file
map_file = 'news_locations_map.html'
try:
    map.save(map_file)
    print(f"Map has been saved as '{map_file}'")
except Exception as e:
    print(f"Error saving the map: {e}")

```

    Map has been saved as 'news_locations_map.html'
    


```python
pip install --upgrade stack_data ipython

```

    Requirement already satisfied: stack_data in c:\users\adarsh g\appdata\roaming\python\python312\site-packages (0.6.3)
    Requirement already satisfied: ipython in c:\users\adarsh g\anaconda3\envs\adarsh_trial\lib\site-packages (8.27.0)
    Collecting ipython
      Downloading ipython-8.28.0-py3-none-any.whl.metadata (5.0 kB)
    Collecting executing>=1.2.0 (from stack_data)
      Using cached executing-2.1.0-py2.py3-none-any.whl.metadata (8.9 kB)
    Requirement already satisfied: asttokens>=2.1.0 in c:\users\adarsh g\appdata\roaming\python\python312\site-packages (from stack_data) (2.4.1)
    Requirement already satisfied: pure-eval in c:\users\adarsh g\appdata\roaming\python\python312\site-packages (from stack_data) (0.2.3)
    Requirement already satisfied: decorator in c:\users\adarsh g\appdata\roaming\python\python312\site-packages (from ipython) (5.1.1)
    Requirement already satisfied: jedi>=0.16 in c:\users\adarsh g\appdata\roaming\python\python312\site-packages (from ipython) (0.19.1)
    Requirement already satisfied: matplotlib-inline in c:\users\adarsh g\appdata\roaming\python\python312\site-packages (from ipython) (0.1.7)
    Requirement already satisfied: prompt-toolkit<3.1.0,>=3.0.41 in c:\users\adarsh g\appdata\roaming\python\python312\site-packages (from ipython) (3.0.47)
    Requirement already satisfied: pygments>=2.4.0 in c:\users\adarsh g\appdata\roaming\python\python312\site-packages (from ipython) (2.18.0)
    Requirement already satisfied: traitlets>=5.13.0 in c:\users\adarsh g\appdata\roaming\python\python312\site-packages (from ipython) (5.14.3)
    Requirement already satisfied: colorama in c:\users\adarsh g\anaconda3\envs\adarsh_trial\lib\site-packages (from ipython) (0.4.6)
    Requirement already satisfied: six>=1.12.0 in c:\users\adarsh g\anaconda3\envs\adarsh_trial\lib\site-packages (from asttokens>=2.1.0->stack_data) (1.16.0)
    Requirement already satisfied: parso<0.9.0,>=0.8.3 in c:\users\adarsh g\appdata\roaming\python\python312\site-packages (from jedi>=0.16->ipython) (0.8.4)
    Requirement already satisfied: wcwidth in c:\users\adarsh g\appdata\roaming\python\python312\site-packages (from prompt-toolkit<3.1.0,>=3.0.41->ipython) (0.2.13)
    Downloading ipython-8.28.0-py3-none-any.whl (819 kB)
       ---------------------------------------- 0.0/819.5 kB ? eta -:--:--
       ---------------------------------------- 819.5/819.5 kB 8.8 MB/s eta 0:00:00
    Using cached executing-2.1.0-py2.py3-none-any.whl (25 kB)
    Installing collected packages: executing, ipython
      Attempting uninstall: executing
        Found existing installation: executing 0.8.3
        Uninstalling executing-0.8.3:
          Successfully uninstalled executing-0.8.3
      Attempting uninstall: ipython
        Found existing installation: ipython 8.27.0
        Uninstalling ipython-8.27.0:
          Successfully uninstalled ipython-8.27.0
    Successfully installed executing-2.1.0 ipython-8.28.0
    Note: you may need to restart the kernel to use updated packages.
    


```python
conda activate adarsh_trial
pip install folium

```


      Cell In[6], line 1
        conda activate adarsh_trial
              ^
    SyntaxError: invalid syntax
    



```python
### checking map locations are correct or wrong 
import folium
import pandas as pd
from geopy.geocoders import GoogleV3
import random

# Insert your Google Maps API Key here
API_KEY = 'AIzaSyChg3ArAuJhYKEY2mv_CVOWHYYJ1tFHhvA'  # Add your Google API Key

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
csv_file = "D:\\News Project\\all the data sets\\gpt\\wvua_news_gpt_trial_28.csv"
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

# Create a Folium map centered around Alabama
alabama_coords = [33.5186, -86.8104]
map = folium.Map(location=alabama_coords, zoom_start=6)

# Lists to track geocoding results
successful_geocodes = []
failed_geocodes = []

# Process and plot locations
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
                    folium.Marker(
                        location=lat_lon,
                        tooltip=f"{city}, {state}",
                        icon=folium.Icon(color='blue', icon='info-sign')
                    ).add_to(map)
                else:
                    failed_geocodes.append((city, state))

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

```

    Map has been saved as 'news_locations_map.html'
    Geocoding Results:
    
    Successfully geocoded locations (7):
    - Nauvoo, Alabama: (33.9895503, -87.4889033)
    - Walker County, Alabama: (33.8563605, -87.30161319999999)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Greensboro, Alabama: (32.7045753, -87.59583959999999)
    - Sawyerville, Alabama: (32.7517973, -87.72945469999999)
    - Akron, Alabama: (32.8765165, -87.7425105)
    - Moundville, Alabama: (32.9976242, -87.6300075)
    
    Failed to geocode locations (0):
    Failed geocodes saved to 'failed_geocodes.txt'
    


```python
import folium
from folium import plugins
import pandas as pd
from geopy.geocoders import GoogleV3
import geopandas as gpd
import random

# Insert your Google Maps API Key here
API_KEY = 'AIzaSyChg3ArAuJhYKEY2mv_CVOWHYYJ1tFHhvA'  # Add your Google API Key

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
csv_file = "D:\\News Project\\all the data sets\\gpt\\wvua_news_gpt_trial_28.csv"
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

# Create a Folium map centered around Alabama
alabama_coords = [33.5186, -86.8104]
map = folium.Map(location=alabama_coords, zoom_start=6)

# Add plugins for water features, national parks, and landmark fill
folium.TileLayer('Stamen Terrain').add_to(map)  # Water features and terrain
folium.TileLayer('Stamen Toner').add_to(map)  # City borders and landmarks
folium.TileLayer('Stamen Watercolor').add_to(map)  # Artistic view
folium.LayerControl().add_to(map)

# Add shapefile for county and city boundaries
county_gdf = gpd.read_file("D:\\News Project\\all the data sets\\map_county_data\\cb_2018_us_county_500k")  # Load the shapefile for counties
city_gdf = gpd.read_file("D:\\News Project\\all the data sets\\map_county_data\\cb_2018_01_cousub_500k")  # Load the shapefile for cities

# Add the county boundaries to the map
folium.GeoJson(
    county_gdf,
    style_function=lambda feature: {
        'color': 'green',
        'weight': 2,
        'fillColor': 'green',
        'fillOpacity': 0.1,
    },
    name='County Borders'
).add_to(map)

# Add the city boundaries to the map
folium.GeoJson(
    city_gdf,
    style_function=lambda feature: {
        'color': 'blue',
        'weight': 2,
        'fillColor': 'blue',
        'fillOpacity': 0.1,
    },
    name='City Borders'
).add_to(map)

# Lists to track geocoding results
successful_geocodes = []
failed_geocodes = []

# Process and plot locations
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
                    
                    # Generate random color for each location marker
                    color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
                    
                    folium.Marker(
                        location=lat_lon,
                        tooltip=f"{city}, {state}",
                        icon=folium.Icon(color=color, icon='info-sign')
                    ).add_to(map)
                else:
                    failed_geocodes.append((city, state))

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

```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    Cell In[16], line 52
         49 map = folium.Map(location=alabama_coords, zoom_start=6)
         51 # Add plugins for water features, national parks, and landmark fill
    ---> 52 folium.TileLayer('Stamen Terrain').add_to(map)  # Water features and terrain
         53 folium.TileLayer('Stamen Toner').add_to(map)  # City borders and landmarks
         54 folium.TileLayer('Stamen Watercolor').add_to(map)  # Artistic view
    

    File ~\anaconda3\envs\adarsh_trial\Lib\site-packages\folium\raster_layers.py:140, in TileLayer.__init__(self, tiles, min_zoom, max_zoom, max_native_zoom, attr, detect_retina, name, overlay, control, show, no_wrap, subdomains, tms, opacity, **kwargs)
        138 self.tiles = tiles
        139 if not attr:
    --> 140     raise ValueError("Custom tiles must have an attribution.")
        142 self.options = parse_options(
        143     min_zoom=min_zoom or 0,
        144     max_zoom=max_zoom or 18,
       (...)
        152     **kwargs,
        153 )
    

    ValueError: Custom tiles must have an attribution.



```python
pip install folium geopandas geopy pandas

```

    Requirement already satisfied: folium in c:\users\adarsh g\anaconda3\envs\adarsh_trial\lib\site-packages (0.17.0)Note: you may need to restart the kernel to use updated packages.
    
    Requirement already satisfied: geopandas in c:\users\adarsh g\anaconda3\envs\adarsh_trial\lib\site-packages (1.0.1)
    Requirement already satisfied: geopy in c:\users\adarsh g\anaconda3\envs\adarsh_trial\lib\site-packages (2.4.1)
    Requirement already satisfied: pandas in c:\users\adarsh g\anaconda3\envs\adarsh_trial\lib\site-packages (2.2.2)
    Requirement already satisfied: branca>=0.6.0 in c:\users\adarsh g\anaconda3\envs\adarsh_trial\lib\site-packages (from folium) (0.8.0)
    Requirement already satisfied: jinja2>=2.9 in c:\users\adarsh g\anaconda3\envs\adarsh_trial\lib\site-packages (from folium) (3.1.4)
    Requirement already satisfied: numpy in c:\users\adarsh g\anaconda3\envs\adarsh_trial\lib\site-packages (from folium) (1.26.4)
    Requirement already satisfied: requests in c:\users\adarsh g\anaconda3\envs\adarsh_trial\lib\site-packages (from folium) (2.32.3)
    Requirement already satisfied: xyzservices in c:\users\adarsh g\anaconda3\envs\adarsh_trial\lib\site-packages (from folium) (2024.9.0)
    Requirement already satisfied: pyogrio>=0.7.2 in c:\users\adarsh g\anaconda3\envs\adarsh_trial\lib\site-packages (from geopandas) (0.10.0)
    Requirement already satisfied: packaging in c:\users\adarsh g\appdata\roaming\python\python312\site-packages (from geopandas) (24.1)
    Requirement already satisfied: pyproj>=3.3.0 in c:\users\adarsh g\anaconda3\envs\adarsh_trial\lib\site-packages (from geopandas) (3.7.0)
    Requirement already satisfied: shapely>=2.0.0 in c:\users\adarsh g\anaconda3\envs\adarsh_trial\lib\site-packages (from geopandas) (2.0.6)
    Requirement already satisfied: geographiclib<3,>=1.52 in c:\users\adarsh g\anaconda3\envs\adarsh_trial\lib\site-packages (from geopy) (2.0)
    Requirement already satisfied: python-dateutil>=2.8.2 in c:\users\adarsh g\anaconda3\envs\adarsh_trial\lib\site-packages (from pandas) (2.9.0.post0)
    Requirement already satisfied: pytz>=2020.1 in c:\users\adarsh g\anaconda3\envs\adarsh_trial\lib\site-packages (from pandas) (2024.1)
    Requirement already satisfied: tzdata>=2022.7 in c:\users\adarsh g\anaconda3\envs\adarsh_trial\lib\site-packages (from pandas) (2023.3)
    Requirement already satisfied: MarkupSafe>=2.0 in c:\users\adarsh g\anaconda3\envs\adarsh_trial\lib\site-packages (from jinja2>=2.9->folium) (2.1.3)
    Requirement already satisfied: certifi in c:\users\adarsh g\anaconda3\envs\adarsh_trial\lib\site-packages (from pyogrio>=0.7.2->geopandas) (2024.8.30)
    Requirement already satisfied: six>=1.5 in c:\users\adarsh g\anaconda3\envs\adarsh_trial\lib\site-packages (from python-dateutil>=2.8.2->pandas) (1.16.0)
    Requirement already satisfied: charset-normalizer<4,>=2 in c:\users\adarsh g\anaconda3\envs\adarsh_trial\lib\site-packages (from requests->folium) (3.3.2)
    Requirement already satisfied: idna<4,>=2.5 in c:\users\adarsh g\anaconda3\envs\adarsh_trial\lib\site-packages (from requests->folium) (3.7)
    Requirement already satisfied: urllib3<3,>=1.21.1 in c:\users\adarsh g\anaconda3\envs\adarsh_trial\lib\site-packages (from requests->folium) (2.2.2)
    


```python
import folium
import geopandas as gpd
from geopy.geocoders import GoogleV3
import pandas as pd

# Insert your Google Maps API Key here
API_KEY = 'AIzaSyChg3ArAuJhYKEY2mv_CVOWHYYJ1tFHhvA'  # Add your Google API Key

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
csv_file = "D:\\News Project\\all the data sets\\gpt\\wvua_news_gpt_trial_29_.csv"
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
map = folium.Map(location=alabama_coords, zoom_start=6)

# Add county boundaries to the map
folium.GeoJson(
    county_gdf,
    name='County Boundaries',
    style_function=lambda x: {
        'fillColor': 'blue',
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
        'fillColor': 'green',
        'color': 'black',
        'weight': 1,
        'fillOpacity': 0.5,
    }
).add_to(map)

# Add a custom tile layer with attribution
folium.TileLayer(
    tiles='https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
    attr='Map data © OpenStreetMap contributors',
    name='OpenStreetMap'
).add_to(map)

# Add a layer control to toggle the layers
folium.LayerControl().add_to(map)

# Lists to track geocoding results
successful_geocodes = []
failed_geocodes = []

# Process and plot locations
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
                    folium.Marker(
                        location=lat_lon,
                        tooltip=f"{city}, {state}",
                        icon=folium.Icon(color='blue', icon='info-sign')
                    ).add_to(map)
                else:
                    failed_geocodes.append((city, state))

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

```

    Map has been saved as 'news_locations_map.html'
    Geocoding Results:
    
    Successfully geocoded locations (305):
    - Nauvoo, Alabama: (33.9895503, -87.4889033)
    - Walker County, Alabama: (33.8563605, -87.30161319999999)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Tuscaloosa County, Alabama: (33.3227653, -87.460397)
    - Greensboro, Alabama: (32.7045753, -87.59583959999999)
    - Sawyerville, Alabama: (32.7517973, -87.72945469999999)
    - Akron, Alabama: (32.8765165, -87.7425105)
    - Moundville, Alabama: (32.9976242, -87.6300075)
    - Auburn, Alabama: (32.6098566, -85.48078249999999)
    - Central-Phenix City, Alabama: (32.4853154, -85.03919119999999)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Oklahoma City, Oklahoma: (35.4675602, -97.5164276)
    - Brookwood, Alabama: (33.2556719, -87.3208336)
    - Hoover, Alabama: (33.4053867, -86.8113781)
    - West Alabama, AL: (33.2570618, -85.41661719999999)
    - Nauvoo, Alabama: (33.9895503, -87.4889033)
    - Tuscaloosa County, Alabama: (33.3227653, -87.460397)
    - Bibb County, Alabama: (32.9562798, -87.14228949999999)
    - Fayette County, Alabama: (33.6871392, -87.77633329999999)
    - Greene County, Alabama: (32.9718107, -87.9334803)
    - Hale County, Alabama: (32.7859102, -87.6186379)
    - Pickens County, Alabama: (33.3339954, -88.0900762)
    - Walker County, Alabama: (33.8563605, -87.30161319999999)
    - Shelby County, Alabama: (33.3039292, -86.6611083)
    - Morgan County, Alabama: (34.4240875, -86.86218269999999)
    - Madison County, Alabama: (34.72397309999999, -86.49965460000001)
    - Limestone County, Alabama: (34.78000720000001, -86.9423801)
    - Elmore County, Alabama: (32.5647083, -86.0121573)
    - Wilcox County, Alabama: (32.0105439, -87.3413599)
    - Perry County, Alabama: (32.598888, -87.30161319999999)
    - Dallas County, Alabama: (32.2332138, -87.14228949999999)
    - Trussville, Alabama: (33.6198251, -86.60887559999999)
    - Vestavia Hills, Alabama: (33.4487183, -86.7877668)
    - Alabaster, Alabama: (33.2442813, -86.8163773)
    - Hoover, Alabama: (33.4053867, -86.8113781)
    - Homewood, Alabama: (33.4717732, -86.80082279999999)
    - Madison, Alabama: (34.6992579, -86.74833180000002)
    - Athens, Alabama: (34.8028661, -86.9716741)
    - Decatur, Alabama: (34.6059253, -86.9833417)
    - Selma, Alabama: (32.4073589, -87.02110069999999)
    - Prichard, Alabama: (30.74515449999999, -88.0896618)
    - Bessemer, Alabama: (33.4017766, -86.954437)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Cottondale, Alabama: (33.189202, -87.4565956)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Northport, Alabama: (33.229007, -87.5772293)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Saraland, Alabama: (30.820742, -88.07055559999999)
    - Mobile, Alabama: (30.6953657, -88.0398912)
    - Greensboro, Alabama: (32.7045753, -87.59583959999999)
    - Hale County, Alabama: (32.7859102, -87.6186379)
    - Lake View, Alabama: (33.2806703, -87.13749589999999)
    - Tuscaloosa County, Alabama: (33.3227653, -87.460397)
    - Macon, Alabama: (32.3731182, -85.684578)
    - Russell, Alabama: (32.3552497, -85.1894045)
    - Elmore, Alabama: (32.5387448, -86.3149712)
    - Autauga, Alabama: (32.4340249, -86.65470189999999)
    - Chilton, Alabama: (32.944392, -86.6611083)
    - Shelby, Alabama: (33.1086539, -86.5835907)
    - Dallas, Alabama: (32.2332138, -87.14228949999999)
    - Perry, Alabama: (32.598888, -87.30161319999999)
    - Bibb, Alabama: (32.9562798, -87.14228949999999)
    - Fayette, Alabama: (33.6845539, -87.8308522)
    - Greene, Alabama: (32.9718107, -87.9334803)
    - Hale, Alabama: (32.7859102, -87.6186379)
    - Pickens, Alabama: (33.3339954, -88.0900762)
    - Lamar, Alabama: (33.6923649, -88.0900762)
    - Sumter, Alabama: (32.6155551, -88.24611829999999)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Cullman, Alabama: (34.1748208, -86.8436124)
    - Lawrence, Alabama: (34.567428, -87.30161319999999)
    - Morgan, Alabama: (34.4240875, -86.86218269999999)
    - Marion, Alabama: (32.6323536, -87.3191655)
    - Walker, Alabama: (33.8563605, -87.30161319999999)
    - Winston, Alabama: (34.1690087, -87.3413599)
    - Tuscaloosa County, Alabama: (33.3227653, -87.460397)
    - Shelton, Alabama: (32.3182314, -86.902298)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Tuscaloosa County, Alabama: (33.3227653, -87.460397)
    - Pell City, Alabama: (33.5862149, -86.2860888)
    - Greensboro, Alabama: (32.7045753, -87.59583959999999)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Northport, Alabama: (33.229007, -87.5772293)
    - Parrish, Alabama: (33.7306642, -87.2844473)
    - Eutaw, Alabama: (32.8406848, -87.8875145)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Montgomery, Alabama: (32.3792233, -86.3077368)
    - Montgomery, Alabama: (32.3792233, -86.3077368)
    - Atlanta, Georgia: (33.7501275, -84.3885209)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Cottondale, Alabama: (33.189202, -87.4565956)
    - West Blocton, Alabama: (33.1181748, -87.1249954)
    - Bibb County, Alabama: (32.9562798, -87.14228949999999)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Louisville, Kentucky: (38.2468618, -85.7663724)
    - Birmingham, Alabama: (33.5185892, -86.8103567)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - York, Alabama: (32.4862491, -88.29641830000001)
    - Sumter County, Alabama: (32.6155551, -88.24611829999999)
    - Huntsville, Alabama: (34.7303688, -86.5861037)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - San Antonio, Texas: (29.4251905, -98.4945922)
    - Oklahoma City, Oklahoma: (35.4675602, -97.5164276)
    - Portland, Oregon: (45.515232, -122.6783853)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Northport, Alabama: (33.229007, -87.5772293)
    - Demopolis, Alabama: (32.5176361, -87.83640199999999)
    - Fayette, Alabama: (33.6845539, -87.8308522)
    - Carrollton, Alabama: (33.2617871, -88.0950263)
    - Livingston, Alabama: (32.5843025, -88.1872475)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Tuscaloosa County, Alabama: (33.3227653, -87.460397)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Dallas, Texas: (32.7766642, -96.79698789999999)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Tuscaloosa County, Alabama: (33.3227653, -87.460397)
    - Centreville, Alabama: (32.9445682, -87.1386067)
    - West Blocton, Alabama: (33.1181748, -87.1249954)
    - Bibb County, Alabama: (32.9562798, -87.14228949999999)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Norman, Oklahoma: (35.2225668, -97.4394777)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Northport, Alabama: (33.229007, -87.5772293)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Mobile, Alabama: (30.6953657, -88.0398912)
    - Mississippi, Alabama: (32.3182314, -86.902298)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Auburn, Alabama: (32.6098566, -85.48078249999999)
    - Brundidge, Alabama: (31.7201615, -85.81605669999999)
    - Enterprise, Alabama: (31.3151708, -85.85521609999999)
    - Fort Payne, Alabama: (34.4442547, -85.7196893)
    - Coosa County, Alabama: (32.9305115, -86.17517590000001)
    - Walker County, Alabama: (33.8563605, -87.30161319999999)
    - Greene County, Alabama: (32.9718107, -87.9334803)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Alabama, AL: (32.3182314, -86.902298)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Tuscaloosa County, Alabama: (33.3227653, -87.460397)
    - Birmingham, Alabama: (33.5185892, -86.8103567)
    - Bessemer, Alabama: (33.4017766, -86.954437)
    - Cullman, Alabama: (34.1748208, -86.8436124)
    - Jasper, Alabama: (33.8312185, -87.2775053)
    - Oneonta, Alabama: (33.9481537, -86.472764)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Fayette, Alabama: (33.6845539, -87.8308522)
    - Fulton, Mississippi: (34.2739933, -88.40921329999999)
    - Dora, Alabama: (33.728717, -87.0902772)
    - Bessemer, Alabama: (33.4017766, -86.954437)
    - Jasper, Alabama: (33.8312185, -87.2775053)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Tuscaloosa County, Alabama: (33.3227653, -87.460397)
    - Pickens County, Alabama: (33.3339954, -88.0900762)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Northport, Alabama: (33.229007, -87.5772293)
    - Demopolis, Alabama: (32.5176361, -87.83640199999999)
    - Fayette, Alabama: (33.6845539, -87.8308522)
    - Carrollton, Alabama: (33.2617871, -88.0950263)
    - Livingston, Alabama: (32.5843025, -88.1872475)
    - Carrollton, Alabama: (33.2617871, -88.0950263)
    - Pickens County, Alabama: (33.3339954, -88.0900762)
    - Birmingham, Alabama: (33.5185892, -86.8103567)
    - Hope Hull, Alabama: (32.2695189, -86.3567376)
    - Dothan, Alabama: (31.2233594, -85.389326)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Montgomery, Alabama: (32.3792233, -86.3077368)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Norman, Oklahoma: (35.2225668, -97.4394777)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Montgomery, Alabama: (32.3792233, -86.3077368)
    - Greene County, Alabama: (32.9718107, -87.9334803)
    - Fayette, Alabama: (33.6845539, -87.8308522)
    - Hale County, Alabama: (32.7859102, -87.6186379)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Haleyville, Alabama: (34.226488, -87.6214133)
    - West Blocton, Alabama: (33.1181748, -87.1249954)
    - Bibb County, Alabama: (32.9562798, -87.14228949999999)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Northport, Alabama: (33.229007, -87.5772293)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Atmore, Alabama: (31.0237921, -87.4938708)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Birmingham, Alabama: (33.5185892, -86.8103567)
    - Parrish, Alabama: (33.7306642, -87.2844473)
    - Walker County, Alabama: (33.8563605, -87.30161319999999)
    - Jasper, Alabama: (33.8312185, -87.2775053)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Moundville, Alabama: (32.9976242, -87.6300075)
    - Hale County, Alabama: (32.7859102, -87.6186379)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Fayette, AL: (33.6845539, -87.8308522)
    - Perry County, Alabama: (32.598888, -87.30161319999999)
    - Dallas County, Alabama: (32.2332138, -87.14228949999999)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Tuscaloosa County, Alabama: (33.3227653, -87.460397)
    - Northport, Alabama: (33.229007, -87.5772293)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Sioux Falls, South Dakota: (43.5460223, -96.731265)
    - Fresno, California: (36.7377981, -119.7871247)
    - Aliceville, Alabama: (33.1295681, -88.15141659999999)
    - Pickens County, Alabama: (33.3339954, -88.0900762)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Dallas, Texas: (32.7766642, -96.79698789999999)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Cherokee County, Alabama: (34.1665322, -85.684578)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Brookwood, Alabama: (33.2556719, -87.3208336)
    - Choctaw County, Mississippi: (33.3914427, -89.28472510000002)
    - Denton, Texas: (33.2148412, -97.13306829999999)
    - Dallas, Texas: (32.7766642, -96.79698789999999)
    - Dallas, AL: (32.2332138, -87.14228949999999)
    - Greene, AL: (32.9718107, -87.9334803)
    - Hale, AL: (32.7859102, -87.6186379)
    - Sumter, AL: (32.6155551, -88.24611829999999)
    - Bibb, AL: (32.9562798, -87.14228949999999)
    - Choctaw, AL: (32.0716631, -88.24611829999999)
    - Fayette, AL: (33.6845539, -87.8308522)
    - Lamar, AL: (33.6923649, -88.0900762)
    - Perry, AL: (32.598888, -87.30161319999999)
    - Tuscaloosa, AL: (33.2098407, -87.56917349999999)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Shelton, Alabama: (32.3182314, -86.902298)
    - Moundville, Alabama: (32.9976242, -87.6300075)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Tuscaloosa County, Alabama: (33.3227653, -87.460397)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Mobile, Alabama: (30.6953657, -88.0398912)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Baton Rouge, Louisiana: (30.4514677, -91.18714659999999)
    - Gainesville, Florida: (29.6519563, -82.324998)
    - College Station, Texas: (30.627977, -96.3344068)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Milwaukee, Wisconsin: (43.0389025, -87.9064736)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Northport, Alabama: (33.229007, -87.5772293)
    - Newbern, Alabama: (32.5931884, -87.5327815)
    - Perry County, Alabama: (32.598888, -87.30161319999999)
    - Dallas County, Alabama: (32.2332138, -87.14228949999999)
    - Northport, Alabama: (33.229007, -87.5772293)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Meridian, Mississippi: (32.3643098, -88.703656)
    - Vance, Alabama: (33.1742847, -87.23360919999999)
    - Eutaw, Alabama: (32.8406848, -87.8875145)
    - Jackson, Alabama: (31.5090521, -87.8944435)
    - Brookhaven, Mississippi: (31.5790588, -90.4406506)
    - Northport, Alabama: (33.229007, -87.5772293)
    - Houston, Texas: (29.7600771, -95.37011079999999)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Central, Alabama: (34.2248222, -87.00917419999999)
    - South, Alabama: (30.6959406, -88.184236)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Northport, Alabama: (33.229007, -87.5772293)
    - Northport, Alabama: (33.229007, -87.5772293)
    - Fosters, AL: (33.0948441, -87.68584279999999)
    - Talladega, Alabama: (33.4359416, -86.1058048)
    - Indian Hills, AL: (32.9759556, -85.94496439999999)
    - Butler, Pennsylvania: (40.8611755, -79.89533279999999)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Birmingham, Alabama: (33.5185892, -86.8103567)
    - Montgomery, Alabama: (32.3792233, -86.3077368)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Pickens County, Alabama: (33.3339954, -88.0900762)
    - Lamar County, Alabama: (33.6923649, -88.0900762)
    - Fayette County, Alabama: (33.6871392, -87.77633329999999)
    - Walker County, Alabama: (33.8563605, -87.30161319999999)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Northport, Alabama: (33.229007, -87.5772293)
    - Tuscaloosa County, Alabama: (33.3227653, -87.460397)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Tuscaloosa, Alabama: (33.2098407, -87.56917349999999)
    - Fosters, Alabama: (33.0948441, -87.68584279999999)
    - Cottondale, Alabama: (33.189202, -87.4565956)
    
    Failed to geocode locations (0):
    Failed geocodes saved to 'failed_geocodes.txt'
    


```python
#trial1
import folium
import geopandas as gpd
import pandas as pd
import branca.colormap as cm

# Load the dataset and shapefiles
csv_file = "D:\\News Project\\all the data sets\\gpt\\wvua_news_gpt_trial_29_.csv"  # Adjust the path as needed
city_shapefile = "D:\\News Project\\all the data sets\\map_county_data\\cb_2018_01_cousub_500k"  # City/town shapefile

# Read the CSV file
df = pd.read_csv(csv_file, encoding='ISO-8859-1', on_bad_lines='skip')

# Check if the dataframe was loaded successfully
if df is not None:
    locations = df['Locations'].dropna().tolist()
else:
    print("Error: Dataframe could not be loaded.")
    locations = []

# Read the city shapefile into a GeoDataFrame
city_gdf = gpd.read_file(city_shapefile)

# Count the frequency of cities in your dataset
# Assuming 'Locations' in the CSV file contains the city names
location_counts = df['Locations'].value_counts().reset_index()
location_counts.columns = ['City', 'Frequency']

# Clean and normalize the city names in both datasets for matching
city_gdf['City'] = city_gdf['NAME'].str.lower()  # Column name from shapefile for city names
location_counts['City'] = location_counts['City'].str.strip().str.lower()

# Merge the city frequency data with the GeoDataFrame based on the city name
city_gdf = city_gdf.merge(location_counts, how='left', on='City')
city_gdf['Frequency'] = city_gdf['Frequency'].fillna(0)  # Fill missing frequencies with 0

# Create a folium map centered around a general location, e.g., Alabama
alabama_coords = [33.5186, -86.8104]  # Coordinates for centering the map
map = folium.Map(location=alabama_coords, zoom_start=6)

# Define a color map (gradient) based on frequency
colormap = cm.LinearColormap(
    colors=['green', 'yellow', 'red'],  # Gradient from low (green) to high (red)
    vmin=0,
    vmax=location_counts['Frequency'].max(),
    caption="Location Frequency"
)

# Add the city polygons to the map and color them based on the frequency
folium.GeoJson(
    city_gdf,
    name='City Boundaries',
    style_function=lambda feature: {
        'fillColor': colormap(feature['properties']['Frequency']),  # Color by frequency
        'color': 'black',
        'weight': 0.5,
        'fillOpacity': 0.6,
    }
).add_to(map)

# Add the color map to the map as a legend
colormap.add_to(map)

# Add a layer control to allow toggling between layers
folium.LayerControl().add_to(map)

# Save the map to an HTML file
map_file = 'city_polygon_frequency_map_1.html'
try:
    map.save(map_file)
    print(f"Map has been saved as '{map_file}'")
except Exception as e:
    print(f"Error saving the map: {e}")
# Output geocoding results

```

    Map has been saved as 'city_polygon_frequency_map_1.html'
    


```python
#trial2
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
csv_file =  "D:\\News Project\\all the data sets\\gpt\\wvua_news_gpt_trial_29_.csv"  # Update to your file path
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

```

    Map saved as us_city_frequency_map_gradient.html
    City Frequencies:
    Nauvoo: 2
     Walker County: 5
    Tuscaloosa: 78
     Tuscaloosa County: 10
    Greensboro: 3
     Sawyerville: 1
     Akron: 1
     Moundville: 1
    Auburn: 2
    Phenix City: 1
     Tuscaloosa: 11
     Oklahoma City: 2
    Brookwood: 1
     Hoover: 2
    West Alabama: 1
    Tuscaloosa County: 2
     Bibb County: 4
     Fayette County: 2
     Greene County: 3
     Hale County: 3
     Pickens County: 4
     Shelby County: 1
     Morgan County: 1
     Madison County: 1
     Limestone County: 1
     Elmore County: 1
     Wilcox County: 1
     Perry County: 2
     Dallas County: 3
     Trussville: 1
     Vestavia Hills: 1
     Alabaster: 1
     Homewood: 1
     Madison: 1
     Athens: 1
     Decatur: 1
     Selma: 1
     Prichard: 1
     Bessemer: 3
     Cottondale: 3
    Northport: 8
     Saraland: 1
     Mobile: 1
    Lake View: 1
    Macon: 1
     Russell: 1
     Elmore: 1
     Autauga: 1
     Chilton: 1
     Shelby: 1
     Dallas: 3
     Perry: 2
     Bibb: 2
     Fayette: 4
     Greene: 2
     Hale: 2
     Pickens: 1
     Lamar: 2
     Sumter: 2
     Cullman: 2
     Lawrence: 1
     Morgan: 1
     Marion: 1
     Walker: 1
     Winston: 1
    Shelton: 2
    Pell City: 1
     Parrish: 1
     Eutaw: 2
    Montgomery: 3
     Atlanta: 1
    West Blocton: 2
    Louisville: 1
     Birmingham: 1
    York: 1
     Sumter County: 1
    Huntsville: 1
     San Antonio: 1
     Portland: 1
     Northport: 5
     Demopolis: 2
     Carrollton: 2
     Livingston: 2
    Centreville: 1
     West Blocton: 1
     Norman: 2
    Mobile: 2
     Mississippi: 1
     Brundidge: 1
     Enterprise: 1
     Fort Payne: 1
     Coosa County: 1
    Alabama: 1
    Birmingham: 4
     Jasper: 3
     Oneonta: 1
    Fayette: 3
     Fulton: 1
    Dora: 1
    Pickens County: 1
    Carrollton: 1
     Hope Hull: 1
     Dothan: 1
     Montgomery: 2
    Hale County: 1
     Haleyville: 1
     Atmore: 1
    Parrish: 1
    Moundville: 2
    Perry County: 1
     Sioux Falls: 1
     Fresno: 1
    Aliceville: 1
    Dallas: 2
    Cherokee County: 1
     Brookwood: 1
    Choctaw County: 1
     Denton: 1
     Choctaw: 1
     Baton Rouge: 1
     Gainesville: 1
     College Station: 1
    Milwaukee: 1
    Newbern: 1
     Meridian: 1
     Vance: 1
     Jackson: 1
     Brookhaven: 1
    Houston: 1
    Central: 1
     South: 1
    Fosters: 1
    Talladega: 1
    Indian Hills: 1
    Butler: 1
     Lamar County: 1
     Fosters: 1
    


```python
#trial3
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
csv_file = "D:\\News Project\\all the data sets\\gpt\\wvua_news_gpt_trial_29_.csv"  # Update to your file path
df = pd.read_csv(csv_file)

# Drop any rows with missing location data
df = df.dropna(subset=['Locations'])

# Extract cities from the 'Locations' column
df['Cities'] = df['Locations'].apply(extract_cities)

# Flatten the list of cities and calculate their frequency
cities_list = [city for sublist in df['Cities'].tolist() for city in sublist]
city_counter = Counter(cities_list)

# Load the comprehensive city shapefile (for the entire US or relevant region)
city_gdf = gpd.read_file("D:\\News Project\\all the data sets\\map_county_data\\cb_2018_us_county_500k")  # Adjust to your shapefile

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

```

    Map saved as us_city_frequency_map_gradient.html
    City Frequencies:
    Nauvoo: 2
     Walker County: 5
    Tuscaloosa: 78
     Tuscaloosa County: 10
    Greensboro: 3
     Sawyerville: 1
     Akron: 1
     Moundville: 1
    Auburn: 2
    Phenix City: 1
     Tuscaloosa: 11
     Oklahoma City: 2
    Brookwood: 1
     Hoover: 2
    West Alabama: 1
    Tuscaloosa County: 2
     Bibb County: 4
     Fayette County: 2
     Greene County: 3
     Hale County: 3
     Pickens County: 4
     Shelby County: 1
     Morgan County: 1
     Madison County: 1
     Limestone County: 1
     Elmore County: 1
     Wilcox County: 1
     Perry County: 2
     Dallas County: 3
     Trussville: 1
     Vestavia Hills: 1
     Alabaster: 1
     Homewood: 1
     Madison: 1
     Athens: 1
     Decatur: 1
     Selma: 1
     Prichard: 1
     Bessemer: 3
     Cottondale: 3
    Northport: 8
     Saraland: 1
     Mobile: 1
    Lake View: 1
    Macon: 1
     Russell: 1
     Elmore: 1
     Autauga: 1
     Chilton: 1
     Shelby: 1
     Dallas: 3
     Perry: 2
     Bibb: 2
     Fayette: 4
     Greene: 2
     Hale: 2
     Pickens: 1
     Lamar: 2
     Sumter: 2
     Cullman: 2
     Lawrence: 1
     Morgan: 1
     Marion: 1
     Walker: 1
     Winston: 1
    Shelton: 2
    Pell City: 1
     Parrish: 1
     Eutaw: 2
    Montgomery: 3
     Atlanta: 1
    West Blocton: 2
    Louisville: 1
     Birmingham: 1
    York: 1
     Sumter County: 1
    Huntsville: 1
     San Antonio: 1
     Portland: 1
     Northport: 5
     Demopolis: 2
     Carrollton: 2
     Livingston: 2
    Centreville: 1
     West Blocton: 1
     Norman: 2
    Mobile: 2
     Mississippi: 1
     Brundidge: 1
     Enterprise: 1
     Fort Payne: 1
     Coosa County: 1
    Alabama: 1
    Birmingham: 4
     Jasper: 3
     Oneonta: 1
    Fayette: 3
     Fulton: 1
    Dora: 1
    Pickens County: 1
    Carrollton: 1
     Hope Hull: 1
     Dothan: 1
     Montgomery: 2
    Hale County: 1
     Haleyville: 1
     Atmore: 1
    Parrish: 1
    Moundville: 2
    Perry County: 1
     Sioux Falls: 1
     Fresno: 1
    Aliceville: 1
    Dallas: 2
    Cherokee County: 1
     Brookwood: 1
    Choctaw County: 1
     Denton: 1
     Choctaw: 1
     Baton Rouge: 1
     Gainesville: 1
     College Station: 1
    Milwaukee: 1
    Newbern: 1
     Meridian: 1
     Vance: 1
     Jackson: 1
     Brookhaven: 1
    Houston: 1
    Central: 1
     South: 1
    Fosters: 1
    Talladega: 1
    Indian Hills: 1
    Butler: 1
     Lamar County: 1
     Fosters: 1
    Unmapped locations saved to 'unmapped_locations.txt'
    Mapped locations saved to 'mapped_locations.csv'
    Total mapped locations saved to 'total_mapped_locations.txt'
    


```python

```
