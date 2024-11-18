import requests

# Replace these with your Page Access Token and Page ID
ACCESS_TOKEN = "EAApWu02srqIBOwDaGgYYvoOxq99voCc54MsZCWbvZCxDhZCAG0lfimWTacxNkQlduXUncT7xRRiZARKvVWFLr1Mc27bdM0XXTW4XLqjYPwde10fMXedeCBFXvtHGvQ9ZAkbHlnwsfZAc2pggfzQ9RpPOlRQAScLz6Sm7O8sGePP4GVwyhcTDw2uc6aKBSXazjcqjZBFatxvmF7E5lN4JglyEOYZD"
PAGE_ID = "108897431499092"

# Define the post message and the link to an image (optional)
message = "How to Fix the WordPress HTTP Error When Uploading Images: A Complete Guide"
image_url = "https://i.pinimg.com/736x/19/d2/2e/19d22e466f90e7c03cea056060608c54.jpg"  # Optional: Use a valid image URL if you want to include an image

def post_to_facebook(message, image_url="https://cdn.ostad.app/user/avatar/2024-07-03T14-58-00.113Z-Screenshot_15.png"):
    """
    Posts a message to a Facebook Page using Graph API.
    
    Args:
        message (str): The text content of the post.
        image_url (str, optional): A URL to an image to include in the post.
    """
    # Facebook Graph API endpoint for posting
    post_url = f"https://graph.facebook.com/v17.0/{PAGE_ID}/feed"

    # Payload for a text post
    payload = {
        "message": message,
        "access_token": ACCESS_TOKEN,
    }

    # If you want to include an image, change the endpoint and payload accordingly
    if image_url:
        post_url = f"https://graph.facebook.com/v17.0/{PAGE_ID}/photos"
        payload["url"] = image_url  # This is for posting a photo with a URL

    # Send the POST request to the Facebook Graph API
    response = requests.post(post_url, data=payload)

    # Check for a successful response
    if response.status_code == 200:
        print("Post successfully published!")
        print(response.json())  # Print the response for details about the post
    else:
        print(f"Failed to post: {response.json()}")  # Properly display the error message

# Call the function to post
post_to_facebook(message, image_url)
