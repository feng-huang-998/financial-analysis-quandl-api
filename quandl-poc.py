import quandl as quandl
import numpy as np 
import pandas as pd 

# quandl.ApiConfig.verify_ssl = False
quandl.read_key()

mydata = quandl.get("EIA/PET_RWTC_D")
print (mydata)