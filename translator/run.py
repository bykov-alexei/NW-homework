#!/bin/python3
from config import *
import urllib.parse as urlparse
from urllib.parse import urlencode
import requests
import json
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--lang', dest='lang', required=True)
parser.add_argument('--file', dest='file', required=True)
parser.add_argument('--output', dest='output', default=None)
args = parser.parse_args()

headers = {
    'Ocp-Apim-Subscription-Key': api_key,
    'Ocp-Apim-Subscription-Region': api_region,
    'Content-Type': 'application/json',   
}

try:
    with open(args.file, 'r') as f:
        text = f.read()
except FileNotFoundError:
    sys.stderr.write('File not found exception\n')
    exit(-1)

lang = args.lang
params = {'api-version': api_version, 'to': lang}

url_parts = list(urlparse.urlparse(api_url))
query = dict(urlparse.parse_qsl(url_parts[4]))
query.update(params)
url_parts[4] = urlencode(query)
url = urlparse.urlunparse(url_parts)

data = json.dumps([{'Text': text}])

response = requests.post(url, headers=headers, data=data)
result = json.loads(response.text)
if "error" not in result:
    answer = result[0]["translations"][0]["text"]
    output = sys.stdout if args.output is None else open(args.output, 'w')
    output.write(answer + "\n")
    output.close()
else:
    sys.stderr.write(result['error']['message'] + "\n")
