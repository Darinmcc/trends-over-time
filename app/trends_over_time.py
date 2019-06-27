"News"

import requests # to make requests for https package - need to install request package in virtual environme
from dotenv import load_dotenv

import json #use to convert json string to dictionary #module don't need to install in virtual part of python
import datetime #module
import calendar # module
import csv # module
import os # module
import statistics # statistic module
import pandas

load_dotenv() #> loads contents of the .env file into the script's environment


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
#print("RECOMMENDATION REASON: TODO")
#print("-------------------------")
#print("HAPPY INVESTING!")
#print("-------------------------")