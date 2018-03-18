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

"""
An encoded set of bytes are stored in a JSON file.
the main method decodes the base64,
unpacks the values from it, and then sends them back.
We're using 4 byte ints int the context of a 32-bit
platform. The next step is extracting those numbers
from the byte string. And them sending them
back to the solution endpoint.
"""
def main():
    print("importing data....")
    try:     
        data = json.load(open('data.json'))
        pprint(data) #printing the data
        bytesInformation = data["bytes"] #reading out the values
        print("\nBefore Conversion: {}".format(bytesInformation))#printing out the bytes info
        #now we need to convert from base64 to human readable language
        #convertedBase64 = base64.b64decode(bytesInformation)
        convertedBase64 = base64.b64decode(bytesInformation)
        print("After Conversion: {}".format(convertedBase64))
        print("Secondary Conversion Test: {}".format(convertedBase64.decode("utf-8")))
        #calling manipulate, which will convert into the following way
        manipulate(bytesInformation)
    except:
        print("Error, data not loaded properly")

    #this is an experiment, to make sure the conversion is working properly
    print("\nExperiment: {} ".format(base64.b64decode("TWFuIGlzIGRpc3Rpbmd1aXNoZWQsIG5vdCBvbmx5IGJ5IGhpcyByZWFzb24sIGJ1dCAuLi4=")))
    print("ExperimentV2: {}".format(base64.b85decode("uz6hiDLQ0eCLKwAA9C5uQiUVvDscizBAQDCLHDu8FSU=")))
if __name__ == "__main__": main()