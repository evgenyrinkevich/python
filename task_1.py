import re
import sys


def email_parse(address):
    pattern = r"^((\w|\.|_|-)+)@((\w|_|-|\.)+\.\w+)$"
    # тут понаставил скобок, чтобы парсилось то что нужно
    # читать невозможно, но работает))
    validate = re.search(pattern, address)
    parsed_email = dict()
    if validate:
        parsed_email['username'] = validate.group(1)
        parsed_email['domain'] = validate.group(3)
        print(parsed_email)
    else:
        raise ValueError


if __name__ == '__main__':
    email = sys.argv[1]
    email_parse(email)
