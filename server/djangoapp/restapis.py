import requests
import os
from dotenv import load_dotenv


load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")


# Get request method
def get_request(endpoint, **kwargs):
    params = ""
    if (kwargs):
        for key, value in kwargs.items():
            params = params+key+"="+value+"&"

    request_url = backend_url+endpoint+"?"+params

    print("GET from {} ".format(request_url))
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)

        # Check if the response was successful (status code 200)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Request failed with status code: {response.status_code}")
            # Raise an exception or handle non-200 status codes based on your requirements
            response.raise_for_status()
    except requests.exceptions.RequestException as e:
        # Handle network-related errors or HTTP request failures
        print(f"Error during request: {e}")
    except ValueError as e:
        # Handle JSON decoding errors if response is not valid JSON
        print(f"Error decoding JSON response: {e}")
    except Exception as e:
        # Handle any other unexpected exceptions
        print(f"An unexpected error occurred: {e}")


# The analyze_review_sentiment method calls the sentiment analyzer
# microservice to analyze the review and returns the sentiment
def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url+"analyze/"+text
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")


# The post_review method takes a customers review and returns a json object
def post_review(data_dict):
    request_url = backend_url+"/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            return response.json()
        else:
            # If the request was not successful, handle the error
            print(f"Request failed with status code: {response.status_code}")
            # Optionally raise an exception or handle the error based on your requirements
            response.raise_for_status()
    except requests.exceptions.RequestException as e:
        # Handle network-related errors or HTTP request failures
        print(f"Error during request: {e}")
    except ValueError as e:
        # Handle JSON decoding errors if response is not valid JSON
        print(f"Error decoding JSON response: {e}")
    except Exception as e:
        # Handle any other unexpected exceptions
        print(f"An unexpected error occurred: {e}")
