# Restaurant Vibes

This app uses Yelp API and Instagram API to display photos and reviews for a restaurant to get a feeling of what the place is like.

TO RUN:
Currently, the project is still fragmented and will not be fully combined until the final submission.

To run the Yelp API, run Connection.py and specify which location and search terms you would like to use.
For now this returns a Json response which is not very user friendly. For the final submission, this will return readable text.

To run the Instagram API, run ConnectionInstagramScript.py. The error that appears in command line is just a warning the pictures should download in a folder called "restaurantvibess" in your computer. The warning about using --login can be ignored as it is only neccessary to download HD photos, which we do not need.

The UI is built using [Bottle](https://bottlepy.org/). To run, first download bottle using `pip install bottle` or another method mentioned in the Bottle website. Then run main.py and navigate to http://localhost:8080 in your browser.
