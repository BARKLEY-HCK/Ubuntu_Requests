# Ubuntu_Requests

> "I am because we are" – Ubuntu Philosophy 🌍

This project is a Python script that mindfully fetches images from the internet, following Ubuntu principles of **community, respect, sharing, and practicality**.

## Features
- Fetch images from user-provided URLs
- Supports **multiple URLs at once**
- Handles errors gracefully (network, HTTP, invalid file types)
- Prevents duplicate downloads
- Saves images neatly in a `Fetched_Images` folder
- Checks HTTP headers before saving (only stores images)

## Requirements
- Python 3.x
- `requests` library

Install dependencies:
```bash
pip install requests

How to Run
python ubuntu_image_fetcher.py
