import argparse
import subprocess

def argsInit():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', dest='filename', default='default', type=str, help='输出证书请求的文件名')
    parser.add_argument('-n', dest='webname', default='www.example.com', type=str, help='授予证书的域名')
    return parser.parse_args();

def generatePrivateKey(filename):
    subprocess.run(['openssl', 'genrsa', '-out', filename+'.key', '2048'])
def generateCertRQ(filename, webaddr):
    subprocess.run(['openssl', 'req', '-new', '-key', args.filename+'.key', '-subj', "/CN="+webaddr, '-out', args.filename+'.csr'])
if __name__ == '__main__':
    args = argsInit()
    generatePrivateKey(args.filename)
    generateCertRQ(args.filename, args.webname)

