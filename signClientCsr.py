import subprocess
import argparse
from termcolor import colored

def initArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('-name', dest='name', type=str, help='client csr file path, like: ./name.csr.pem')
    return parser.parse_args()

def printTitle(strings):
    print('\r\n' + colored(strings, 'yellow'))

def checkCode(code):
    if code is not 0:
        print(colored('\tFail', 'red'))
    else:
        print(colored('\tOk', 'green'))

if __name__=='__main__':
    args = initArgs()

    printTitle('Try to sign certificate request')
    certFileName = './certs/' + args.name.replace('csr', 'cert')
    cmd = 'openssl ca -config ./openssl.cnf -days 365 -notext -md sha256 -in ./'+args.name+' -out '+certFileName
    returnCode = subprocess.call(cmd, shell=True)
    checkCode(returnCode)

    printTitle('Verify certificate...')
    cmd = 'openssl x509 -noout -text -in '+certFileName
    returnCode = subprocess.call(cmd, shell=True)
    checkCode(returnCode)

