#"News"

import requests # to make requests for https package - need to install request package in virtual environme
from dotenv import load_dotenv
from pprint import pprint
#####
##
#
#


import json #use to convert json string to dictionary #module don't need to install in virtual part of python
import csv # module
import os # module



load_dotenv() #> loads contents of the .env file into the script's environment


api_key = os.environ.get("NEWS_API_KEY")

url = f"https://newsapi.org/v2/everything?q=Apple&from=2019-06-27&language=en&sortBy=popularity&apiKey={api_key}"

response = requests.get(url)

#print(type(response)) #<class 'requests.models.Response'>
#print(response.status_code) #200
#print(type(response.text))
#print(response.text)
#print(response.json())

parsed_response =json.loads(response.text) # variable, parse str to dict

print(type(parsed_response))

print(parsed_response.keys()) #= top keys
print(parsed_response["articles"][1])



#print(parsed_reponse.keys()) #= top keys
#parsed_response["Meta Data"].keys()


#create a dictionary for each term and source

#My search terms
#my sources for each search terms
#send an e-mail



#print("-------------------------")
#print("SELECTED GOOGLE SEARCH: ")
#print("-------------------------")
#print("REQUESTING GOOGLE SEARCH TRENDS...")
#print("REQUEST AT: 2018-02-20 02:00pm")
#print("-------------------------")
#print("LATEST DAY: 2018-02-20")
#print("LATEST CLOSE: $100,000.00")
#print("RECENT HIGH: $101,000.00")
#print("RECENT LOW: $99,000.00")
#print("-------------------------")
#print("RECOMMENDATION: BUY!")
#print("RECOMMENDATION REASON: ")
#print("-------------------------")
#print("HAPPY INVESTING!")
#print("-------------------------")