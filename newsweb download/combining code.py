# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 11:29:27 2024

@author: ADARSH G
"""
import pandas as pd
import os

# List of file paths
file_paths = [
    r"D:\690\t-100\T_T100_SEGMENT_US_CARRIER_ONLY_2022.csv",
    r"D:\690\t-100\T_T100_SEGMENT_US_CARRIER_ONLY_2023.csv",
    r"D:\690\t-100\T_T100_SEGMENT_US_CARRIER_ONLY_2024.csv",
    

    
    # Add more file paths here
]

# Initialize an empty list to hold DataFrames
dfs = []

# Iterate through the file paths
for file in file_paths:
    if os.path.exists(file):
        # Read each CSV file and append to the list
        df = pd.read_csv(file, encoding='ISO-8859-1')  # or 'windows-1252'
        dfs.append(df)
    else:
        print(f"File not found: {file}")

# Concatenate all DataFrames in the list
combined_df = pd.concat(dfs, ignore_index=True)

# Save the combined DataFrame to a new CSV file
combined_df.to_csv(r"D:\690\t-100\T_T100_SEGMENT__2022_2024.csv", index=False)

print("All files have been combined successfully!")
