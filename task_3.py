class NumError(Exception):
    def __init__(self, param):
        self.param = param

    def check(self):
        try:
            self.param = int(self.param)
        except ValueError:
            print("That is not an integer")
            self.param = None
        return self.param


if __name__ == '__main__':
    res_list = []
    print('To exit type "stop" ')
    while True:
        el = input('Enter anything ')
        if el == 'stop':
            break
        if_num = NumError(el)
        if if_num.check():
            res_list.append(if_num.check())
    print(res_list)
