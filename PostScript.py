import pandas as pd
import requests
from datetime import datetime, timedelta
import time

# Replace with your actual Page Access Token and Page ID
PAGE_ACCESS_TOKEN = 'Replace with your actual Page Access Token'
PAGE_ID = 'Replace with your actual Page ID'

# Read the Excel file
posts_df = pd.read_excel('file path .xlsx')

# Convert 'Scheduled Time' column to datetime
posts_df['Scheduled Time'] = pd.to_datetime(posts_df['Scheduled Time'])

print(posts_df.columns)

# Function to post on Facebook
def post_to_facebook(message, image_url=None):
    url = f"https://graph.facebook.com/{PAGE_ID}/feed"
    payload = {
        'message': message,
        'access_token': PAGE_ACCESS_TOKEN
    }
    if image_url:
        payload['url'] = image_url
        url = f"https://graph.facebook.com/{PAGE_ID}/photos"  # Use this URL for photo posts

    response = requests.post(url, data=payload)
    return response.json()

# Schedule and post
for index, row in posts_df.iterrows():
    post_content = row['Post Content']
    image_url = row.get('Image URL', None)
    scheduled_time = row['Scheduled Time']

    # Calculate time to wait before posting
    time_to_wait = (scheduled_time - datetime.now()).total_seconds()

    if time_to_wait > 0:
        print(f"Waiting for {time_to_wait} seconds to post...")
        time.sleep(time_to_wait)

    # Post to Facebook
    response = post_to_facebook(post_content, image_url)
    print(f"Post Response: {response}")

print("All posts have been scheduled and posted.")

