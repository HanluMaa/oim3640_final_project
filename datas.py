import urllib.request
import json
from pprint import pprint

def get_data(email):
    """
    Get data using the News API.
    """
    api_url = f"https://emailvalidation.abstractapi.com/v1/?api_key=78b71126da324a9e944fbaaed58bc67b&email={email}"


    with urllib.request.urlopen(api_url) as response:
        response_text = response.read().decode("utf-8")
        email_data = json.loads(response_text)
    # pprint(email_data)
    
    return email_data

def main():
    email = "hma3@babson.edu" #strip spaces
    email = email.strip()
    get_data(email)


main()