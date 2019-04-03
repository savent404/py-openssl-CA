import os
import subprocess

def genConfigFile():
    print('Going to gen openssl.cnf')
    f = open('config.tmp', 'r')
    contents = f.read()
    f.close()

    f = open('openssl.cnf', 'w+')
    contents = contents.replace("pydir", os.getcwd())
    f.write(contents)
    f.close()
    print('\tOK')

def genBasicConstructure():
    print('Going to gen basic constructure')
    returnCode = subprocess.call('mkdir certs crl newcerts private && touch index.txt && echo 1000 > serial', shell=True)
    if returnCode is not 0:
        print('\tFail')
    else:
        print('\tOk')
def createRootKey():
    print('Going to create Root Key')
    returnCode = subprocess.call('openssl genrsa -aes256 -out private/ca.key.pem 4096', shell=True)
    if returnCode is not 0:
        print('\tFail')
    else:
        print('\tOk')

if __name__=='__main__':
    genBasicConstructure()
    genConfigFile()
    createRootKey()

