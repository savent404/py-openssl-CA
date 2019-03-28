import argparse
import subprocess

def argsInit():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', dest='filename', default='CA', type=str, help='输出文件名')
    return parser.parse_args();

def mkdirs():
    subprocess.run(["mkdir", "-p", "./private"])
    subprocess.run(["mkdir", "-p", "./crt"])

def generateRootKey(filename):
    subprocess.run(["openssl", "genrsa", "-out", "private/" + filename + "_key.pem", "2048"])

def generateRootCertification(filename):
    subprocess.run(["openssl", "req", "-new", "-x509", "-key", "private/" + filename + "_key.pem", "-out", "crt/" + filename + "_cert.pem"])

if __name__ == '__main__':
    args = argsInit()

    mkdirs()
    generateRootKey(args.filename)
    generateRootCertification(args.filename)

