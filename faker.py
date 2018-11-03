import nessie
import requests
import json
from random import randint
import time

# object definitions
class Customer:
    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.age = str(randint(14,70))
        self.incomeLevel = str(randint(1,3))
class Transaction:
    def __init__(self,name,customer,latitude,longitude,spent):
        self.name = name
        self.customer = customer
        self.latitude = latitude
        self.longitude = longitude
        self.spent = randint()
        self.time = str(hourGenerator())
        self.day = dayGenerator()
class Store:
    def __init__(self,name,keywords,latitude,longitude):
        self.name = name
        self.keywords = keywords
        self.latitude = latitude
        self.longitude = longitude

# post method for customer
def customerPost(customer):
    url="http://127.20.10.5:5000/"
    customer = {
        "first_name": customer.firstName,
        "last_name": customer.lastName,
        "age": customer.age,
        "income_level": customer.incomeLevel
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
def storePost(store):
    url ="http://172.20.10.4:5000/addstore"
    index = 0;
    for key, values in storeDict.items():
        store = {
            "name":store.name,
            "keywords":store.keywords,
            "lat":store.latitude,
            "long":store.longitude,
        }
        print("HELLO",json.dumps(store))
        response = requests.post(
            url,
            data=store
        )
        print(response)
        print(response.text)
        time.sleep(0.001)
        index+=1

# post method for transactions
def transactionPost(transaction):
    url = "http://172.20.10.4:5000/transaction"
    for x in range(300):
        index = randint(0,len(storename)-2)
        transaction = {
            "storename":transaction.name,
            "customer":transaction.customer,
            "lat":transaction.latitude,
            "long":transaction.longitude,
            "spent":transaction.spent
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
    for i in range(0, len(storeName) - 1):
        store = Store(storeName[i],str(storeDict[i]),latitude[i],longitude[i])
        storeArr.append(store)
        print('store true')
    return storeArr

#method for creating customer array
def setCustomers(firstName,lastName):
    customerArr = []
    for i in range(0, 20):
        index = randint(0,len(firstName-1))
        customer = Customer(firstName[index],lastName[index])
        customerArr.append(customer)
        print('cust true')
    return customerArr

#method for creating transaction array
def setTransactions(storenames,customers,latitude,longitude, weightDict):
    transactionsArr = []
    for i in range(0, len(customers) - 1):
        for x in range(0,100):
            index = randint(0,len(storenames-1))
            transaction = Transaction(storenames[index],customers[i],latitude[i],longitude[i], str(weightDict[index]*randint(10,100)))
            transactionsArr.append(transaction)
            print('trans true')
    return transactionsArr


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

#time generator
def hourGenerator():
    probability = random()
    if probability < 0.8:
        return randint(9,13)
    else:
        return randint(9,21)

#day generator
def dayGenerator():
    day = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    probability = random()
    if probability < 0.8:
        return day[randint(4,7)]
    else:
        return day[randint(0,7)]

def postData(storeArr, customerArr, transactionArr):
    storePost(storeArr)
    customerPost(customerArr)
    transactionPost(transactionArr)
    print('true')


def main():
    # import hella data
    firstnames = fileReader("firstnames.txt")
    lastnames = fileReader("lastnames.txt")
    storename=fileReader("storenames.txt")
    lat = fileReader("latitude.txt")
    long = fileReader("longitude.txt")
    storeDict = fileReader("keywords.txt")
    weightDict = fileReader("weights.txt")


    storeArr = setStores(storeName,storeDict,lat,long)
    customerArr = setCustomers(firstnames,lastnames)
    transactionArr = setTransactions(storename,customerArr,latitude,longitude,weightDict)

    postData(storeArr, customerArr, transactionArr)


if __name__ == "__main__":
    main()
