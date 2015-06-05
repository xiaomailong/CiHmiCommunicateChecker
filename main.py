#
from ping import *
from termcolor import *
import colorama

hmi_com_boards = [
        {"NAME":"厂内站I系","A":"192.168.1.2","B":"192.168.2.2"},
        {"NAME":"厂内站II系","A":"192.168.1.4","B":"192.168.2.4"},
        ]

colorama.init()

C = colored

#ping = verbose_ping
ping = quiet_ping

def check_result(res):
    if res != 1.0:
        return C("√","green")
    else:
        return C("×","red",attrs=["bold"])

for hmi_com_board in hmi_com_boards:
    print(C("正在检查{0}控显机通信板状态...".format(hmi_com_board["NAME"]),"yellow"))
    # check A
    res = ping(hmi_com_board['A'])
    print(C("   正在检查A口通信状态，ip:{0}         [{1}]"
        .format(hmi_com_board['A'],check_result(res[3])),"yellow"))

    # check B
    res = ping(hmi_com_board['B'])
    print(C("   正在检查B口通信状态，ip:{0}         [{1}]"
        .format(hmi_com_board['B'],check_result(res[3])),"yellow"))

    print()


