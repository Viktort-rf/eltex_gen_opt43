# Script for generate option 43 (with vendor specific suboptions  10 and 13) for Eltex access point

import ipaddress


def ascii_to_hex(input_str):
    """
    Converts a string to a HEX value based on the length of the string

    Args:
        input_str (str): String. In this case, a string with an ip address or domain

    Return:
        HEX: String
    """
    hex_result = ''
    hex_result += hex(len(input_str))[2:].zfill(2)  # [2:] del prefix 0x. zfill(2) add '0' if string < 2
    for char in input_str:
        hex_result += hex(ord(char))[2:]
    return hex_result


def is_valid_ip(ip_str):
    """
    Checking the IP address for validity

    Args:
        ip_str (str): String

    Return:
        bool: True of False
    """
    try:
        ip_address = ipaddress.ip_address(ip_str)
        return True
    except ValueError:
        return False


while True:
    swlc_addr = input('Enter the IP address of the controller: ')
    if is_valid_ip(swlc_addr) is True:
        break
    else:
        print('The IP address is invalid. Check and try again')

swlc_domain = input('Enter the domain: ').lower()  # For standardization, converts the domain to lowercase
if '.root' not in swlc_domain:
    swlc_domain = swlc_domain + '.root'

result = '0a' + ascii_to_hex(swlc_addr) + '0d' + ascii_to_hex(swlc_domain)
print(result)
