'''
deposit public class or function
data:2020-3-20
@author antony weijiang
'''
import can
import time
import sys
import os
from log import logger as loger

logger = loger.Current_Module()
# from Common import Signal_List as SL


class PCAN(object):
    def __enter__(self):
        return self

    def __init__(self):
        self.bus = can.interface.Bus(bustype='pcan', channel='PCAN_USBBUS1', bitrate=500000)

    def send(self, id, data):
        id = int(id, 16)
        data = list(map(lambda i: int(i), data))
        # print(id, list(data))
        msg = can.Message(arbitration_id=id, dlc=8, data=data, extended_id=False)
        try:
            self.bus.send(msg)
            logger.log_debug("Message sent on {0},id:{1},data:{2}".format(self.bus.channel_info,id,data), \
                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                             sys._getframe().f_lineno)
            # print("Message sent on {0},id:{1},data:{2}".format(self.bus.channel_info,id,data))
        except can.CanError as e:
            logger.log_error("%s" %(e), \
                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                             sys._getframe().f_lineno)

    def send_arry(self, arry_list=[]):
        for i in arry_list:
            self.send(i['id'], i['data'])
        time.sleep(0.2)

    def clean(self):
        self.bus.shutdown()





