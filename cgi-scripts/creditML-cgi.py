#! /usr/bin/python3

print("Content-type: text/html")
print()

import cgi
import subprocess
import urllib.request
import json
import os
import ssl
# from bs4 import BeautifulSoup

form = cgi.FieldStorage()

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

// Request data goes here
data = {
    "data":
    [
        {
            'V1': "0",
            'V2': "0",
            'V3': "0",
            'V4': "0",
            'V5': "0",
            'V6': "0",
            'V7': "0",
            'V8': "0",
            'V9': "0",
            'V10': "0",
            'V11': "0",
            'V12': "0",
            'V13': "0",
            'V14': "0",
            'V15': "0",
            'V16': "0",
            'V17': "0",
            'V18': "0",
            'V19': "0",
            'V20': "0",
            'V21': "0",
            'V22': "0",
            'V23': "0",
            'V24': "0",
            'V25': "0",
            'V26': "0",
            'V27': "0",
            'V28': "0",
        },
    ],
}


url = 'http://fb59789a-91bf-4210-9df0-23e943399ae9.eastus.azurecontainer.io/score'


req = urllib.request.Request(url)
req.add_header('Content-Type', 'application/json; charset=utf-8')
jsondata = json.dumps(data)

jsondataasbytes = jsondata.encode('utf-8')
req.add_header('Content-Length', len(jsondataasbytes))

response = urllib.request.urlopen(req, jsondataasbytes)

result = response.read()

# soup = BeautifulSoup(result, 'html-parser')
result = result.decode('utf-8')
print("<p>Result is: ", result[15:28])

result_new = float(result)
if(result_new <= 0.96):
    print("<p>Person is not eligible for loan</p>")
else:
    print("<p>Person is eligible for loan</p>")