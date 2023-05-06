import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    octets = ip.split('.')
    if len(octets) != 4:
        return False

    for octet in octets:
        if not octet.isdigit():
            return False

        num = int(octet)
        if num < 0 or num > 255:
            return False

    return True


if __name__ == "__main__":
    main()
