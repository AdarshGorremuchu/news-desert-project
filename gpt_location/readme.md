Location Extraction from News Articles
This project extracts city, county, and town names along with their corresponding state names from news article descriptions using OpenAI's GPT model. The extracted locations are then saved in a CSV file. The script processes a CSV dataset containing article descriptions, interacts with OpenAI's API for location extraction, and outputs the results in a new CSV file. Below are the steps to set up and run the script.
-------------------
Add your OpenAI API key to the .env file like so:

OPENAI_API_KEY=your_openai_api_key
----------
Input Data:

The script expects a CSV file with a column named Description containing news article descriptions.
Update the path to your input CSV file in the code:
python
-----------
Run the script:

The script processes each article in the dataset, sending the Description field to OpenAI's API to extract the locations.
The extracted locations are formatted and filtered to ensure valid results (e.g., no "state-only" entries).
The script handles API call retries in case of failures and tracks the total API call time.
-------------
Processing the Dataset:

The script processes each article, calling the OpenAI API to extract location data, which is then saved in a new column called Locations.
A progress bar (tqdm) shows the progress of the extraction.
Saving the Results:

The extracted locations are saved in a new CSV file along with the original article descriptions.
Timing Information:

Once processing is complete, the script prints the total execution time, number of API calls made, and average API call duration.
--------------
Summary Statistics:

The script prints summary statistics, such as the number of articles with extracted locations and errors.
Output Example
The output CSV will contain two main columns:
--------
Description: The original article description.
Locations: Extracted city, county, or town names and their corresponding state names, formatted as city, state / city, state for multiple locations.
Error Handling
The script handles up to 3 retries in case of API call failures.
If no valid location information is found, the Locations field will be left blank.
Customization
You can adjust the number of rows to process by modifying the dataset slicing logic in the script (currently, the script processes the entire dataset).
You can switch to other models if necessary.