import requests
import os
from Packages.Connection import send_message

def download_file(url, destination_folder="."):
    """
    Download a file from the given URL and save it to the destination folder.
    
    Parameters:
        url (str): The URL of the file to download.
        destination_folder (str): The folder where the downloaded file will be saved. Default is the current directory.
        
    Returns:
        str: The path to the downloaded file.
    """
    # Create the destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    # Extract filename from the URL
    filename = os.path.join(destination_folder, url.split('/')[-1])
    
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Save the content to a file
        with open(filename, 'wb') as f:
            f.write(response.content)
        #print("File downloaded successfully:", filename)
        return filename[2:]
    else:
        #print("Failed to download file:", url)
        return None

# Example usage:
# url = "https://example.com/file_to_download.zip"
# download_file(url, "downloads")
