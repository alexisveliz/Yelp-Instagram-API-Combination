# Implementation by Haley Anderson and Elise May

import YelpAPI as YelpAPI
import argparse

location = input("Where are you looking to eat?\nCurrently Supported Locations: Los Angeles, San Francisco, Seattle\nLocation: ")
term = input("What kind of food are you looking for?\nExamples: bars, dinner, Thai, etc\nResponse: ")

parser = argparse.ArgumentParser()

parser.add_argument('-q', '--term', dest='term', default=term,
                    type=str, help='Search term (default: %(default)s)')
parser.add_argument('-l', '--location', dest='location',
                    default=location, type=str,
                    help='Search location (default: %(default)s)')

input_values = parser.parse_args()

try:
    YelpAPI.query_api(input_values.term, input_values.location)
except HTTPError as error:
    sys.exit(
        'Encountered HTTP error {0} on {1}:\n {2}\nAbort program.'.format(
            error.code,
            error.url,
            error.read(),
        )
    )
