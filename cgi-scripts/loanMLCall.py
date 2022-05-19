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

gender = form.getvalue("gender")
mrd = form.getvalue("mrd")
depend = form.getvalue("depend")
edu = form.getvalue("edu")
emp = form.getvalue("emp")
income = form.getvalue("income")
coincome = form.getvalue("coincome")
loanamt = form.getvalue("loanamt")
loanterm = form.getvalue("loanterm")
hist = form.getvalue("hist")
area = form.getvalue("area")

# Request data goes here
data = {
    "data":
    [
        {
            'Loan_ID': "example_value",
            'Gender': gender,
            'Married': mrd,
            'Dependents': depend,
            'Education': edu,
            'Self_Employed': emp,
            'ApplicantIncome': income,
            'CoapplicantIncome': coincome,
            'LoanAmount': loanamt,
            'Loan_Amount_Term': loanterm,
            'Credit_History': hist,
            'Property_Area': area,
        },
    ],
}

url = 'http://26df597f-7a79-406a-839e-69b3a8e65470.southcentralus.azurecontainer.io/score'

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
