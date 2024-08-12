import openai
from instagrapi import Client
from respondtextGen import generate_text

# Replace these with your Instagram account credentials
USERNAME = 'USERNAME'
PASSWORD = 'PASSWORD'

# Initialize the Instagram client
client = Client()

# Login to Instagram
try:
    client.login(USERNAME, PASSWORD)
    print("Logged in successfully.")
except Exception as e:
    print(f"Failed to log in: {e}")
    exit()  # Exit if login fails

def get_media_id_from_url(media_url):
    """Extracts media ID from the URL."""
    try:
        media_id = client.media_pk_from_url(media_url)
        print(f"Media ID: {media_id}")
        return media_id
    except Exception as e:
        print(f"An error occurred while fetching media ID: {e}")
        return None

def respond_to_comments(media_id):
    """Responds to comments on the specified media."""
    try:
        comments = client.media_comments(media_id)
        commented_users = set()  # Track users we've already commented on

        for comment in comments:
            if comment.user.username not in commented_users:
                prompt = f"Write a friendly response to the comment: {comment.text}"
                response_text = generate_text(prompt)
                client.comment(media_id, response_text)
                print(f"Commented on media with ID {media_id}: {response_text}")
                commented_users.add(comment.user.username)  # Add user to the set
    except Exception as e:
        print(f"An error occurred while responding to comments: {e}")


# URL of the Instagram post to monitor
media_url = 'https://www.instagram.com/reel/xxxx/'  # Replace with the actual post URL

# Get media ID from the URL
media_id = get_media_id_from_url(media_url)

if media_id:
    # Call the function to respond to comments
    respond_to_comments(media_id)
