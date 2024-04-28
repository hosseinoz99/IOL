import os
import requests

def download_file(url, filename):
    """Download file from given URL and save it with given filename."""
    try:
        with open(filename, 'wb') as file:
            response = requests.get(url)
            file.write(response.content)
        print(f"Downloaded {filename}")
    except Exception as e:
        print(f"Failed to download {filename}: {e}")

def main():
    # Check if links.txt exists
    if not os.path.exists("links.txt"):
        print("Error: links.txt not found.")
        return

    # Read links from links.txt and download files
    with open("links.txt", "r") as file:
        for line in file:
            url = line.strip()
            filename = url.split('/')[-1]  # Extract filename from URL
            download_file(url, filename)

if __name__ == "__main__":
    main()
