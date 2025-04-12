#!/usr/bin/env python

"""
This script provides a function to interact with the URLhaus API.
It can be imported and used directly in other Python projects.
"""

import json
import requests
import re

__author__ = "Corsin Camichel"
__copyright__ = "Copyright 2018, Corsin Camichel"
__license__ = "Creative Commons Attribution-ShareAlike 4.0 International License."
__version__ = "1.0-20180326"
__email__ = "cocaman@gmail.com"

API_URL = 'https://urlhaus.abuse.ch/api/'

def check_tag_regex(tag):
    """
    Validates that a tag has the correct format.
    """
    if not tag:
        return None
    pattern = re.compile(r'([a-zA-Z\.-]+)')
    match = pattern.match(tag)
    if match is None or not match.group() == tag:
        raise ValueError(f"Invalid tag used '{tag}'")
    return str(tag)

def submit_url(api_key, url, tags=None, anon=0, threat="malware_download"):
    """
    Submits a new malicious URL to URLhaus.

    Parameters:
        api_key (str): API key for authentication.
        url (str): URL to submit.
        tags (list[str]): Optional tags for the URL.
        anon (int): Whether the submission should be anonymous (0 or 1).
        threat (str): The threat type (default: "malware_download").

    Returns:
        dict: JSON response from the URLhaus API.
    """
    if tags:
        tags = [check_tag_regex(tag) for tag in tags]
    json_data = {
        'token': api_key,
        'anonymous': str(anon),
        'submission': [
            {
                'url': url,
                'threat': threat,
                'tags': tags or []
            }
        ]
    }
    headers = {
        'Content-Type': 'application/json',
        'user-agent': 'URLhaus Python Submission Script'
    }

    try:
        response = requests.post(API_URL, json=json_data, timeout=15, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Failed to submit URL: {str(e)}"}

# Example usage as a script (optional)
'''
    tags like -> ["malware", "phishing"]
    result = submit_url(api_key, url, tags)
'''