import base64
import json
from pprint import pprint


def createJSON():
    return "hell0:"

"""
Takes in a converted base64 string and returns:
signed int, unsigned int, short, float, double, and another double in big endian. 
In that order. Separated by a '_'. Uses 4 bytes ints in 32 bits
"""
def manipulate(data):
    print("inside manipulate function")
    print(data)

def main():
    print("importing data....")
    try:     
        data = json.load(open('data.json'))
        pprint(data) #printing the data
        bytesInformation = data["bytes"] #reading out the values
        print("\nBefore Conversion: ${}".format(bytesInformation))#printing out the bytes info
        
        #now we need to convert from base64 to human readable language
        convertedBase64 = base64.b64decode(bytesInformation)
        print("After Conversion: ${}".format(convertedBase64))
        
        #calling manipulate, which will convert into the following way
        manipulate(bytesInformation)
    except:
        print("Error, data not loaded properly")


if __name__ == "__main__": main()