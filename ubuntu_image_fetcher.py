import requests
import os
from urllib.parse import urlparse

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")
    
    # Get URL from user
    url = input("Please enter the image URL: ")
    
    try:
        # 1. Create directory if it doesn't exist
        os.makedirs("Fetched_Images", exist_ok=True)
        
        # 2. Fetch the image
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise exception for HTTP errors
        
        # 3. Extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        
        if not filename:
            filename = "downloaded_image.jpg"
        
        # 4. Save image
        filepath = os.path.join("Fetched_Images", filename)
        with open(filepath, 'wb') as f:
            f.write(response.content)
        
        # 5. Success messages
        print(f"Successfully fetched: {filename}")
        print(f"Image saved to {filepath}")
        print("\nCommunity enriched.")
    
    except requests.exceptions.RequestException as e:
        print(f"Connection error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
