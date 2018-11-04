import nessie
import requests
import json
import random
from random import randint
import time

fifty_above_block = ["Express","Lucky Brand","OMEGA Boutique","Louis Vuitton","Williams-Sonoma"]
thirty_below_block = ["Cookout","Exxon","The Row","Cookout","Burger King","Urgent Care","Desano Pizza Bakery"]
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
        self.spent = spent
        self.time = str(hourGenerator())
        self.day = dayGenerator()
class Store:
    def __init__(self,name,keywords,address,latitude,longitude):
        self.name = name
        self.keywords = keywords
        self.address = address
        self.latitude = latitude
        self.longitude = longitude

# post method for customer
def customerPost(customers):
    url="http://172.20.10.13:5000/adduser"
    customer = {
        "first_name": customers.firstName,
        "last_name": customers.lastName,
        "age": customers.age,
        "income_level": customers.incomeLevel
    }

    response = requests.post(
	       url,
	       data=customer,
	       )
    print(response.status_code)
    print(response.text)
    if response.status_code == 201:
	       print('customer created')


# post method for stores
def storePost(stores):
    url ="http://172.20.10.13:5000/addstore"
    store = {
        "name":stores.name,
        "keywords":stores.keywords,
        "address":stores.address,
        "lat":stores.latitude,
        "long":stores.longitude,
    }
    print("HELLO",json.dumps(store))
    response = requests.post(
        url,
        data=store
    )
    print(response)
    print(response.text)
    time.sleep(0.001)

# post method for transactions
def transactionPost(transactions):
    url = "http://172.20.10.13:5000/transaction"
    customer = transactions.customer

    transaction = {
        "storename":transactions.name,
        "first_name":customer.firstName,
        "last_name":customer.lastName,
        "lat":transactions.latitude,
        "long":transactions.longitude,
        "spent":transactions.spent,
        "time":transactions.time,
        "day":transactions.day
    }
    response = requests.post(
            url,
            data=transaction
        )
    print(response.text)
    time.sleep(0.001)

#method for creating store array
def setStores(storeName,storeDict,address,latitude,longitude):
    storeArr = []
    for i in range(0, len(storeName)):
        store = Store(storeName[i],str(storeDict[i]),address[i],latitude[i],longitude[i])
        storeArr.append(store)
        print('store true')
    return storeArr

#method for creating customer array
def setCustomers(firstName,lastName):
    customerArr = []
    for i in range(0, 20):
        index = randint(0,len(firstName))
        customer = Customer(firstName[index],lastName[index])
        customerArr.append(customer)
        print('cust true')
    return customerArr

#method for creating transaction array
def setTransactions(storenames,customers,latitude,longitude, weightDict):
    transactionsArr = []
    for i in range(0, len(customers)):
        for x in range(0,1 ):
            storename = random.choice(storenames)
            index = storenames.index(storename)
            # if(int(customers[i].age) > 50):
            #     while(storename in fifty_above_block):
            #         storename = random.choice(storenames)
            #         index = storenames.index(storename)
            if(int(customers[i].age) > 50):
                print("old")
                storename = random.choice(fifty_above_block)
                index = storenames.index(storename)
                transaction = Transaction(storename,customers[i],latitude[index],longitude[index], str(float(weightDict[index])*randint(10,100)))
                transactionsArr.append(transaction)
            else:
                print("young")
                storename = random.choice(thirty_below_block)
                index = storenames.index(storename)
                transaction = Transaction(storename,customers[i],latitude[index],longitude[index], str(float(weightDict[index])*randint(10,100)))
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
    probability = random.random()
    if probability < 0.8:
        return randint(9,13)
    else:
        return randint(9,21)

#day generator
def dayGenerator():
    day = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    probability = random.random()
    if probability < 0.8:
        return day[randint(3,6)]
    else:
        return day[randint(0,6)]

def postData(storeArr, customerArr, transactionArr):
    for i in range(0,len(storeArr)):
        storePost(storeArr[i])
    for j in range(0, len(customerArr)):
        customerPost(customerArr[j])
    for k in range(0, len(transactionArr)):
        transactionPost(transactionArr[k])
    print('true')


def main():
    # import hella data
    firstnames = fileReader("firstnames.txt")
    lastnames = fileReader("lastnames.txt")
    storename=fileReader("storenames.txt")
    address = fileReader("streetnames.txt")
    lat = fileReader("latitude.txt")
    long = fileReader("longitude.txt")
    storeDict = fileReader("keywords.txt")
    weightDict = fileReader("weights.txt")

    storeArr = setStores(storename,storeDict,address,lat,long)
    customerArr = setCustomers(firstnames,lastnames)
    transactionArr = setTransactions(storename,customerArr,lat,long,weightDict)

    postData(storeArr, customerArr, transactionArr)


if __name__ == "__main__":
    main()
