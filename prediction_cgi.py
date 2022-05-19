#! /usr/bin/python3

print("Content-type: text/html")
print()

import cgi
import subprocess
import urllib.request
import json
import os
import ssl

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

# Request data goes here
data = {
    "data":
    [
        {
            'year': "0",
            'systemic_crisis': "0",
            'exch_usd': "0",
            'domestic_debt_in_default': "0",
            'sovereign_external_debt_default': "0",
            'gdp_weighted_default': "0",
            'inflation_annual_cpi': "0",
            'independence': "0",
            'currency_crises': "0",
            'inflation_crises': "0",
        },
    ],
}


url = 'http://5b78955d-9a62-4ea2-a6e9-fadfd93db1b7.eastus.azurecontainer.io/score'
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

