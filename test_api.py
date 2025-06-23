import requests
import time

url = 'http://ec2-18-223-99-99.us-east-2.compute.amazonaws.com/'
claim = "Facebook post says that PepsiCo announced Mountain Dew will be discontinued over health concerns."
headers = {'content-type': 'application/json'}
start_time = time.time()
response = requests.post(url, json={"claim": claim})
print("--- %s seconds ---" % (time.time() - start_time))
print(response.text)
