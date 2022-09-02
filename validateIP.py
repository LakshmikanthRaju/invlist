
import re


REGEX_IP4_OCTET="^(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]?[0-9]|[0]{1,2}[0-7])$"
REGEX_IP4='''^(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]?[0-9]|[0]{1,3}[0-7])\.
            (25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]?[0-9]|[0]{1,3}[0-7])\.
            (25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]?[0-9]|[0]{1,3}[0-7])\.
            (25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]?[0-9]|[0]{1,3}[0-7])$'''

CHARS_IP6='1234567890abcdef:'

def isValidIPv4(addr):
    octets = addr.split('.')
    #return re.search(REGEX_IP4, addr)
    if (len(octets) != 4):
        return False
    for octect in octets:
        if not re.search(REGEX_IP4_OCTET, octect):
            return False
    return True

def isValidIPv6(addr):
    if not all(digit in CHARS_IP6 for digit in addr):
        return False

    octets = addr.split(':')
    length = len(octets)

    if length > 8:
        return False

    if length == 8:
        return all(0 < len(octect) <= 4 for octect in octets)

    if '::' in addr and addr.count('::') == 1:
        return True

    return False

def validateAddresses(addresses):
    # Write your code here
    for addr in addresses:
        if isValidIPv4(addr):
            print("IPv4")
        elif isValidIPv6(addr):
            print("IPv6")
        else:
            print("Neither")


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    addresses_count = 1#int(input().strip())

    #addresses = ["10.196.179.009"]
    addresses = ["2001:0db8:85a3:0000:0000:8a2e:0370:7334",
                 "2001:0db8:0000:0000:0000:ff00:0042:8329",
                 "2001:db8:0:0:0:ff00:0:8329",
                 "2001:db8::ff00:0:8329",
                 '2001:0db8:0000:0000:0000:ff00:0042:8329',
                 '2001:db8:0:0:0:ff00:42:8329',
                 '2001:db8:0:0:0:ff00:42:8329',
                 '2001:db8::ff00:42:8329',
                 '0000:0000:0000:0000:0000:0000:0000:0001',
                 '::1']

    #for _ in range(addresses_count):
    #    addresses_item = input()
    #    addresses.append(addresses_item)

    #result = \
    validateAddresses(addresses)

    #fptr.write('\n'.join(result))
    #fptr.write('\n')

    #fptr.close()