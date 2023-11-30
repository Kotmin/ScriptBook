import requests

# URL of the website you want to access
url = 'https://kotmin.onrender.com/'

try:
    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        print(f"Successfully opened {url}")
    else:
        print(f"Failed to open {url}. Status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Failed to open {url}. Error: {e}")
