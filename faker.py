import nessie
import requests
import json
from random import randint
import time

#file reader for randomized names
def fileReader(name):
    array = []
    file = open(name,'r')
    f1 = file.readlines()
    for x in f1:
        name = x[:-1]
        array.append(name)
    file.close()
    return array


# object definitions
class Customer:
    def __init__(self,firstName,lastName,age,incomeLevel):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.incomeLevel = incomeLevel
class Transaction:
    def __init__(self,name,customer,latitude,longitude,spent):
        self.name = name
        self.customer = customer
        self.latitude = latitude
        self.longitude = longitude
        self.spent = spent
class Store:
    def __init__(self,name,keywords,latitude,longitude):
        self.name = name
        self.keywords = keywords
        self.latitude = latitude
        self.longitude = longitude

# post method for customer
def customerPost(firstnames, lastnames, streetname):
    apiKey='80951ee1fca397896a359f0acadad71f'
    url="http://127.20.10.5:5000/"

    customer = {
        "first_name": firstnames[randint(0,len(firstnames)-1)],
        "last_name": lastnames[randint(0,len(lastnames)-1)],
        }


    }
    response = requests.post(
	       url,
	       data=json.dumps(customer),
	       headers={'content-type':'application/json'},
	       )

    print(response.status_code)
    print(response.text)

    if response.status_code == 201:
	       print('customer created')

# post method for stores
def storePost(storename, lat, longi, storeDict):
    url ="http://172.20.10.4:5000/addstore"

    index = 0;
    for key, values in storeDict.items():
        store = {
            "name":storename[index],
            "keywords":str(values),
            "lat":lat[index],
            "long":longi[index],
        }
        print("HELLo",json.dumps(store))
        response = requests.post(
            url,
            data=store
        )
        print(response)
        print(response.text)
        time.sleep(3)
        index+=1

# post method for transactions
def transactionPost(storename,lat,longi,weightDict):
    url = "http://172.20.10.4:5000/transaction"

    for x in range(300):
        index = randint(0,len(storename)-2)


        transaction = {
            "storename":storename[index],
            "lat":lat[index],
            "long":longi[index],
            "spent":str(weightDict[index]*randint(10,100))
        }
        response = requests.post(
            url,
            data=transaction,
        )
        print(response.text)
        time.sleep(0.001)

#method for creating store array
def setStores(storeName,storeDict,latitude,longitude):
    storeArr = []
    for i in range(0, storeName.length - 1):
        store = Store(storeName[i],str(storeDict[i]),latitude[i],longitude[i])
        storeArr.append(store)
    return storeArr




def main():
    firstnames = fileReader("firstnames.txt")
    lastnames = fileReader("lastnames.txt")
    storename=fileReader("storenames.txt")
    lat = fileReader("latitude.txt")
    long = fileReader("longitude.txt")


    storeDict = dict(
        Dillards = ['retail','department'],
        Express = ['clothing','high-end','formal'],
        Petsmart = ['pet','retail'],
        OMEGA = ['jewelry','accessories','high-end'],
        Lucky = ['clothing','jeans'],
        Nordstrom = ['retail','department','high-end','clothing'],
        Williams = ['retail','home-goods','high-end'],
        Brooks = ['clothing','high-end','formal'],
        Louis = ['clothing','fashion','high-end','jewelry'],
        Wendys = ['fast-food','restaurant'],
        Cookout = ['fast-food','restaurant'],
        Krystal = ['fast-food','restaurant'],
        Ruths = ['high-end','steakhouse','restaurant'],
        Melting = ['high-end','fondue','restuarant'],
        Miel = ['high-end','restaurant']

    )
    weightDict = fileReader("weights.txt")

    storeArr = setStores(storeName,storeDict,lat,long)

    #customerPost(firstnames, lastnames, streetname, storeDict)
    #storePost(storename,lat,long,storeDict)
    transactionPost(storename,lat,long,weightDict)



if __name__ == "__main__":
    main()
