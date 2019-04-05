import os
import subprocess
from termcolor import colored

def printTitle(strings):
    print('\r\n' + colored(strings, 'yellow'))

def checkCode(code):
    if code is not 0:
        print(colored('\tFail', 'red'))
    else:
        print(colored('\tOk', 'green'))

def genConfigFile():
    printTitle('Going to gen openssl.cnf')
    f = open('config.tmp', 'r')
    contents = f.read()
    f.close()

    f = open('openssl.cnf', 'w+')
    contents = contents.replace("pydir", os.getcwd())
    f.write(contents)
    f.close()
    checkCode(0)


def genBasicConstructure():
    printTitle('Going to gen basic constructure')
    cmd = 'mkdir certs crl newcerts private && touch index.txt && echo 1000 > serial'
    returnCode = subprocess.call(cmd, shell=True)
    checkCode(returnCode)

def createRootKey():
    printTitle('Going to create Root Key')
    returnCode = subprocess.call('openssl genrsa -aes256 -out private/ca.key.pem 4096', shell=True)
    checkCode(returnCode)

def createRootCert():
    printTitle('Going to create Root Certificate')
    nowDir = os.getcwd()
    cmdLine = 'openssl req -config ' + os.getcwd() + '/openssl.cnf'  + ' -key private/ca.key.pem -new -x509 -days 7300 -sha256 -extensions v3_ca -out certs/ca.cert.pem'
    printTitle(cmdLine)
    returnCode = subprocess.call(cmdLine, shell=True)
    checkCode(returnCode)

def verifyRootCertificate():
    printTitle('Going to verify the root certificate')
    returnCode = subprocess.call('openssl x509 -noout -text -in certs/ca.cert.pem', shell=True)
    checkCode(returnCode)

if __name__=='__main__':
    genBasicConstructure()
    genConfigFile()
    createRootKey()
    createRootCert()
    verifyRootCertificate()

