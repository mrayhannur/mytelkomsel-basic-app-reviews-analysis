from google_play_scraper import Sort, reviews
import pandas as pd
from datetime import datetime
from tqdm import tqdm
import time

# Define the app ID for the Google Play Store app you want to scrape
app_id = 'com.tsel.telkomselku'

# Initialize an empty list to store the fetched reviews
result = []
continuation_token = None  # This will be used to fetch more reviews if available
reviews_count = 50000  # Set the desired total number of reviews to fetch

# Use tqdm to create a progress bar for tracking the fetching process
with tqdm(total=reviews_count, position=0, leave=True) as pbar:
    while len(result) < reviews_count:  # Continue fetching until the desired count is reached
        # Fetch reviews from the Google Play Store
        new_result, continuation_token = reviews(
            app_id,
            continuation_token=continuation_token,  # Use the continuation token to fetch more reviews
            lang='id',  # Set the language to Indonesian
            country='id',  # Set the country to Indonesia
            sort=Sort.NEWEST,  # Sort reviews by the newest first
            filter_score_with=None,  # Fetch all reviews regardless of score
            count=150  # Number of reviews to fetch in each request
        )
        
        # Check if any new reviews were fetched
        if not new_result:
            break  # Exit the loop if no more reviews are available
        
        # Extend the result list with the newly fetched reviews
        result.extend(new_result)
        
        # Update the progress bar with the number of new reviews fetched
        pbar.update(len(new_result))

# Create a DataFrame from the list of reviews
df = pd.DataFrame(result)

# Generate a timestamp for the filename to avoid overwriting files
today = str(datetime.now().astimezone().strftime("%m-%d-%Y_%H%M%S"))

# Save the DataFrame to a CSV file with a timestamped filename
filename = f'reviews-{app_id}_{today}.csv'
df.to_csv(f'./data/{filename}', index=False)

# Print the total number of reviews fetched
print(len(df))