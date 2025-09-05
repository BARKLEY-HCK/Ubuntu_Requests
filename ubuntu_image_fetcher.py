import requests
import os
from urllib.parse import urlparse

def fetch_image(url):
    try:
        # Create directory if it doesn't exist
        os.makedirs("Fetched_Images", exist_ok=True)

        # Fetch the image
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise exception for HTTP errors

        # Check HTTP headers before saving
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"Skipping {url} (not an image, content-type={content_type})")
            return

        # Extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        if not filename:  # If filename not in URL
            filename = "downloaded_image.jpg"

        filepath = os.path.join("Fetched_Images", filename)

        # Prevent duplicate downloads
        if os.path.exists(filepath):
            print(f"Duplicate found, skipping: {filename}")
            return

        # Save the image
        with open(filepath, 'wb') as f:
            f.write(response.content)

        print(f"Successfully fetched: {filename}")
        print(f"Image saved to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"Connection error while fetching {url}: {e}")
    except Exception as e:
        print(f"An error occurred while fetching {url}: {e}")


def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Ask for multiple URLs (comma-separated)
    urls = input("Please enter one or more image URLs (comma-separated): ")

    # Split into a list and strip whitespace
    url_list = [u.strip() for u in urls.split(",") if u.strip()]

    if not url_list:
        print("No valid URLs provided.")
        return

    # Process each URL
    for url in url_list:
        fetch_image(url)

    print("\nCommunity enriched.")


if __name__ == "__main__":
    main()
