#!/usr/bin/env python

"""
Main script to aggregate results from multiple API calls, including URLhaus.
This script imports functions from `urlhaus.py` and other modules for use in a Django project or standalone application.
"""

import json
import os
from urlhaus import submit_url

def call_urlhaus(api_key, url, tags=None, anon=0, threat="malware_download"):
    """
    Calls the URLhaus API and formats the response for aggregation.

    Parameters:
        api_key (str): API key for authentication.
        url (str): The URL to submit.
        tags (list[str]): Optional tags for the URL.
        anon (int): Whether the submission should be anonymous (0 or 1).
        threat (str): The threat type (default: "malware_download").

    Returns:
        dict: A dictionary with the key 'urlhaus' containing the API response.
    """
    response = submit_url(api_key, url, tags, anon, threat)
    return {"urlhaus": response}

def web_sec_check(api_key, url, tags=None):
    """
    Aggregates results from multiple security APIs.

    Parameters:
        api_key (str): API key for authentication (shared by all APIs).
        url (str): The URL to analyze.
        tags (list[str]): Optional tags for API calls.

    Returns:
        dict: A dictionary of API results.
    """

    with open("API_JUNK/api_file.txt", "r") as API_file:
        my_api = {}
        counter = 0
        while next(API_file):
            my_api[counter] = API_file.read()
            counter = counter + 1

    results = {}
    # URLhaus
    results.update(call_urlhaus(my_api[0], url, tags))
    # Add other API calls here
    return results