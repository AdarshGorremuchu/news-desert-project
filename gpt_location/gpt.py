import pandas as pd
from openai import OpenAI
import os
from dotenv import load_dotenv
from tqdm import tqdm
import time

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI client with your API key from environment variables
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Start timing the entire script
script_start_time = time.time()

# Read the CSV file
csv_file_path = "D:\\News Project\\all the data sets\\gpt\\wvua_news_combined_file.csv"
df = pd.read_csv(csv_file_path)

# Select only the first 150 rows for testing
#df = df.head(150)

# Count the total number of rows
total_rows = len(df)
print(f"Processing the first {total_rows} articles from the dataset")

# Variables to track API call times
total_api_time = 0
api_call_count = 0

def call_openai_api(prompt):
    global total_api_time
    global api_call_count
    
    max_retries = 3
    for attempt in range(max_retries):
        try:
            api_start_time = time.time()
            response = client.chat.completions.create(
                model="gpt-4o-mini-2024-07-18",
                messages=[
                    {"role": "system", "content": "You are an assistant that extracts location information from news articles."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=150,
                n=1,
                stop=None,
                temperature=0.3
            )
            api_end_time = time.time()
            api_duration = api_end_time - api_start_time
            total_api_time += api_duration
            api_call_count += 1

            return response.choices[0].message.content.strip()
        except Exception as e:
            if attempt < max_retries - 1:
                print(f"Error occurred: {str(e)}. Retrying in 5 seconds...")
                time.sleep(5)
            else:
                return f"Error: {str(e)}"

def extract_location(description):
    # Update the prompt to ensure city and state names are both included, exclude state-only results
    prompt = f"""
    Analyze the following news article description and extract any city, county, or town names along with their corresponding state names. 
    Only include locations that have both a city/county and state. Do not include standalone state names or ambiguous locations. 
    Pay special attention to names that might have common variations or abbreviations.
    Format the output as city1, state1 / city2, state2 / city3, state3 for multiple locations. 
    If no city or county is found, leave it blank.

    Description: 
    {description}
    """
    
    location_data = call_openai_api(prompt)

    # Process the response to filter out any "state only" locations
    if "No specific city, county, or town names are mentioned" in location_data or "state only" in location_data:
        return ""  # Return a blank value
    
    # Split the locations based on '/' and filter to ensure no state-only results like "Alabama, Alabama"
    locations = [loc.strip() for loc in location_data.split('/') if ',' in loc]
    
    # Further filter to remove entries where the same state appears twice, e.g., "Alabama, Alabama"
    valid_locations = []
    for loc in locations:
        city, state = loc.split(',')[0].strip(), loc.split(',')[1].strip()
        if city.lower() != state.lower():  # Ensure city and state aren't the same
            valid_locations.append(f"{city}, {state}")

    # Return valid locations joined by ' / ', or blank if no valid locations
    return ' / '.join(valid_locations) if valid_locations else ""

# Process the dataset
print("Starting to process the articles...")
tqdm.pandas(desc="Processing articles", total=total_rows)
df['Locations'] = df['Description'].progress_apply(lambda x: extract_location(str(x)))

# Save the results to a new CSV file
output_file = "D:\\News Project\\all the data sets\\gpt\\wvua_news_gpt_trial_29.csv"
df.to_csv(output_file, index=False)

# Calculate and print timing information
script_end_time = time.time()
total_script_time = script_end_time - script_start_time
average_api_time = total_api_time / api_call_count if api_call_count > 0 else 0

print(f"\nTiming Information:")
print(f"Total script execution time: {total_script_time:.2f} seconds")
print(f"Total API call time: {total_api_time:.2f} seconds")
print(f"Number of API calls: {api_call_count}")
print(f"Average time per API call: {average_api_time:.2f} seconds")

print(f"\nResults have been saved to: {output_file}")

# Print summary statistics
df['Locations'] = df['Locations'].astype(str)
location_counts = df['Locations'].value_counts()

print("\nLocation extraction summary:")
print(f"Total articles processed: {total_rows}")
print(f"Articles with 'No location information': {location_counts.get('', 0)}")

single_location_count = location_counts[location_counts.index.str.startswith('Single location')].sum()
multiple_locations_count = location_counts[location_counts.index.str.startswith('Multiple locations')].sum()
errors_count = location_counts[location_counts.index.str.startswith('Error')].sum()

print(f"Articles with 'Single location': {single_location_count}")
print(f"Articles with 'Multiple locations': {multiple_locations_count}")
print(f"Articles with errors: {errors_count}")

# Print the first few rows of results for quick review
print(df[['Description', 'Locations']].head().to_string())
