#!/usr/bin/env python3

# Using the GATE Cloud on-line API:
# An example using ANNIE.
#
# This is a command line tool, example use:
#   python annie.py Greta Thunberg spoke yesterday at the UN

# REFERENCES
#
# GATE Cloud on-line API
#   https://cloud.gate.ac.uk/info/help/online-api.html
#
# ANNIE, English Named Entity Recognizer
#   https://cloud.gate.ac.uk/shopfront/displayItem/annie-named-entity-recognizer

# Python standard library https://docs.python.org/3.6/library/index.html
import json
import sys
import urllib

# pip install requests
# https://pypi.org/project/requests/
import requests

# The base URL for all GATE Cloud API services
prefix = "https://cloud-api.gate.ac.uk/"
# The service point for ANNIE
service = "process-document/annie-named-entity-recognizer"
url = urllib.parse.urljoin(prefix, service)

def main():
    # Create the text from the arguments
    text = " ".join(sys.argv[1:])
    headers = {'Content-Type': 'text/plain'}

    # Make the API request and raise error if status >= 4xx
    response = requests.post(url, data=text, headers=headers)
    response.raise_for_status()

    # The requests library has a method for returning parsed JSON
    gate_json = response.json()

    # Pretty print the response, mostly for debugging
    print(json.dumps(gate_json, indent=2))

    # Find each annotation and print its type and the text it is annotating
    response_text = gate_json["text"]
    for annotation_type, annotations in gate_json['entities'].items():
        for annotation in annotations:
            i, j = annotation["indices"]
            print(annotation_type, ":", response_text[i:j])

if __name__ == "__main__":
    main()
