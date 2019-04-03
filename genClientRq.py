import os
import subprocess
import argparse
from termcolor import colored

def initArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('-name', dest='name', type=str, help='client name')
    parser.add_argument('-config', dest='config', type=str, help='config file path')
    return parser.parse_args()

def printTitle(strings):
    print('\r\n' + colored(strings, 'yellow'))

def checkCode(code):
    if code is not 0:
        print(colored('\tFail', 'red'))
    else:
        print(colored('\tOk', 'green'))

def createPrivateKey(name):
    printTitle('Creating client private key')
    returnCode = subprocess.call('openssl genrsa -aes256 -out '+name+' 2048', shell=True)
    checkCode(returnCode)

def createRq(inName, outName, config):
    printTitle('Creating client certificate file')
    returnCode = subprocess.call('openssl req -config '+config+' -key '+inName+' -new -sha256 -out '+outName, shell=True)
    checkCode(returnCode)

if __name__ == '__main__':
    args = initArgs()
    createPrivateKey(args.name + '.key.pem')
    createRq(args.name+'.key.pem', args.name+'.csr.pem', args.config)
