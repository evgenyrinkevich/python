from utils import currency_rates


if __name__ == '__main__':
    import sys

    _, val = sys.argv

    exit(currency_rates(val))
