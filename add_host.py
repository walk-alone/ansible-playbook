#coding:utf-8
#
import json

a = ["172.17.2.220", "172.17.2.219", "172.17.2.218", ]
b = ["172.17.1.255", "172.17.1.254", "172.17.1.253", ]
c = ["172.17.1.150", "172.17.1.149", "172.17.1.148", ]
d = ["172.17.0.255", "172.17.0.254", "172.17.0.253", ]




data = {
    "databases"   : {
        "hosts"   : a,
    },
    "webservers"  : b,
    "cdog-hosts"     : {
        "hosts"   : c,
    },
    "scalio-hosts": {
        "hosts": d,
    },
}

def main():
    from optparse import OptionParser
    parse = OptionParser()
    parse.add_option("-l", "--list", action="store_true", dest="list", default=False)
    (option, arges) = parse.parse_args()
    if option.list:
        print(json.dumps(data))
    else:
        print({})


if __name__ == '__main__':
    main()
