# Implementation by Haley Anderson

import YelpAPI as YelpAPI
import argparse
import requests

# location = input("Where are you looking to eat?\nCurrently Supported Locations: Los Angeles, San Francisco, Seattle\nLocation: ")
# term = input("What kind of food are you looking for?\nExamples: bars, dinner, Thai, etc\nResponse: ")
# Sample inputs for testing only

# Function to call Yelp API that is used in the UI. This brings up the top result for each search term and
# location pair.
# If first translates the input into the correct form for the API and then queries the Yelp API, methods of
# which are located in the YelpAPI.py file.
# It throws an error if the Yelp API cannot be accessed

# Yelp API information can be found at: http://www.yelp.com/developers/v3/documentation

def YelpSearch(location, term):
    SEARCH_LIMIT = 5

    parser = argparse.ArgumentParser()

    parser.add_argument('-q', '--term', dest='term', default=term,
                        type=str, help='Search term (default: %(default)s)')
    parser.add_argument('-l', '--location', dest='location',
                        default=location, type=str,
                        help='Search location (default: %(default)s)')

    input_values = parser.parse_args()

    try:
        return YelpAPI.query_api(input_values.term, input_values.location)
    except:
        sys.exit(
            'Encountered HTTP error {0} on {1}:\n {2}\nAbort program.'.format(
                error.code,
                error.url,
                error.read(),
            )
        )
