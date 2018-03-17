import json
from pprint import pprint

def manipulate(data):
    print("inside manipulate function")
    print(data)

def main():
    print("importing data....")
    try:     
        data = json.load(open('data.json'))
        pprint(data) #printing the data
        #reading out the values
        bytesInformation = data["bytes"] 
        print(bytesInformation)#printing out the bytes info
        manipulate(bytesInformation)
    except:
        print("Error, data not loaded properly")


if __name__ == "__main__": main()