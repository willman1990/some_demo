# coding=utf-8
import re
def judge_mac(list_mac, Len):
    if Len != 6:
        return -1
    for Str in list_mac:
        str_len = len(Str)
        if str_len != 2:
            return -1
        if re.match(r'[0-9a-fA-F]{2}', Str):
            pass
        else:
            return -1
    return 0
if __name__ == '__main__':
    yes = 'y'
    while yes == 'y':
        strmac = raw_input("input a mac address > ")
        str_list = strmac.split(':')
        mac_len = len(str_list)

        result = judge_mac(str_list, mac_len)
        print result
        yes = raw_input("carry on or not [y][n] > ")
