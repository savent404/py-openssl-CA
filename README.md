# py-openssl-CA
use python to use openssl CA function


## CAgenrate.py
生成CA的私钥与证书, 输出后的文件结构如下。
``` shell
.
├── crt
│   └── [name]_cert.pem
└── private
    └── [name]_key.pem
```
其中private文件下为CA的私钥，而crt文件夹下为用私钥加密的证书
