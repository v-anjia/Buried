'''
Buried Point for Living Flow
author: antony weijiang
date: 2020/3/16
'''
import  os
import time
import sys
import subprocess
import random
import uiautomator2 as u2
from functools import  wraps
from Common import Common as co
from log import logger as loger

logger = loger.Current_Module()


Living_Flow = {"default":[{"REFRESH_ONLINE_RADIO":"Click"},\
                               {"REFRESH_PERSONAL_RADIO":"Click"},\
                               {"REFRESH_ABOOK":"Click"},\
                               {"SHOW_ECONOMIC_SPEED":"Click"},\
                               {"HIDE_ECONOMIC_SPEED":"Click"},\
                               {"SHOW_AC_CONTROL":"Click"},\
                               {"HIDE_AC_CONTROL":"Click"},\
                               {"SHOW_REGENERATION_LEVEL":"Click"},\
                               {"HIDE_REGENERATION_LEVEL":"Click"},\
                               {"REFRESH_ONLINE_MUSIC":"Click"},\
                               {"HIDE_ENVIRONMENT_SONGLIST":"Click"},\
                               {"SHOW_PERSONAL_SONGLIST":"Click"},\
                               {"SHOW_POI":"Click"},\
                               {"HIDE_POI":"Click"},\
                               ]
                    }
REFRESH_ONLINE_MUSIC ='am broadcast -a "wm.livingengine.action.REFRESH_ONLINE_MUSIC" -c "wm.livingengine.category.REFRESH_WIDGET"'
REFRESH_ONLINE_RADIO ='am broadcast -a "wm.livingengine.action.REFRESH_ONLINE_RADIO" -c "wm.livingengine.category.REFRESH_WIDGET"'
REFRESH_PERSONAL_RADIO ='am broadcast -a "wm.livingengine.action.REFRESH_PERSONAL_RADIO" -c "wm.livingengine.category.REFRESH_WIDGET"'
REFRESH_ABOOK ='am broadcast -a "wm.livingengine.action.REFRESH_ABOOK" -c "wm.livingengine.category.REFRESH_WIDGET"'

SHOW_ECONOMIC_SPEED = 'am broadcast -a wm.livingengine.action.SHOW_ECONOMIC_SPEED --es poi ECONOMIC SPEED'
SHOW_AC_CONTROL = 'am broadcast -a wm.livingengine.action.SHOW_AC_CONTROL --es poi AC CONTROL'
SHOW_REGENERATION_LEVEL = 'am broadcast -a wm.livingengine.action.SHOW_REGENERATION_LEVEL --es poi REGENERATION LEVEL'
SHOW_PERSONAL_SONGLIST ='am broadcast -a wm.livingengine.action.SHOW_PERSONAL_SONGLIST --es poi REGENERATION LEVEL'
SHOW_POI = 'am broadcast -a wm.livingengine.action.SHOW_POI --es poi home'

HIDE_ECONOMIC_SPEED = 'am broadcast -a wm.livingengine.action.SHOW_ECONOMIC_SPEED --es poi ECONOMIC SPEED'
HIDE_AC_CONTROL = 'am broadcast -a wm.livingengine.action.SHOW_AC_CONTROL --es poi AC CONTROL'
HIDE_REGENERATION_LEVEL = 'am broadcast -a wm.livingengine.action.SHOW_REGENERATION_LEVEL --es poi REGENERATION LEVEL'
HIDE_PERSONAL_SONGLIST ='am broadcast -a wm.livingengine.action.SHOW_PERSONAL_SONGLIST --es poi REGENERATION LEVEL'
HIDE_POI = 'am broadcast -a wm.livingengine.action.HIDE_POI --es --es speed 95'



setting_log = "/sdcard/lvlog/com.android.settings/normal/*"
buried_point = "/sdcard/Android/data/com.wm.tracker/files/temp/*"
busybox = "/yf/bin/busybox"
app_id = "app_id=SystemSetting"
buried_point_field = "AidlConnectManager"

adb_object = co.ADB_SN()
sn = adb_object.check_adb_device_isalive()

class Check_Living_Flow_Actions(object):
    def __init__(self):
        pass

    @classmethod
    def check_log(cls, Action=None, Event=None):
        def Common(func):
            @wraps(func)
            def warpper(*args, **kwargs):
                try:
                    logger.log_info("check if Action:%s" %(Action), \
                                    sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                                    sys._getframe().f_lineno)
                    func(*args)
                    # result = subprocess.check_output(
                    #     'adb -s %s shell "cat %s |grep %s |grep %s |grep %s |grep -v grep | %s wc -l"' % (
                    #     sn, setting_log, buried_point_field, Action, Event, busybox))

                    result = subprocess.check_output(
                        'adb -s %s shell "cat %s |grep %s |grep %s |grep %s |grep -v grep | %s wc -l"' % (
                        sn, buried_point, buried_point_field, Action, Event, busybox))
                    result = co.removal(result)
                    logger.log_debug("lvlog collect result value is : %s " % (result), \
                                     sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                                     sys._getframe().f_lineno)
                    return result
                except Exception as e:
                    logger.log_error("%s" % (e), \
                                     sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                                     sys._getframe().f_lineno)
                    return False

            return warpper
        return Common


class Check_Living_Flow(object):
    def __init__(self):
        pass

    @classmethod
    @Check_Living_Flow_Actions.check_log(Action=list(Living_Flow["default"][0].keys())[0],
                                     Event=list(Living_Flow["default"][0].values())[0])
    def REFRESH_ONLINE_RADIO(cls, sn):
        logger.log_info("Test Living Flow Page", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        os.system('adb -s %s shell "%s"' %(sn,REFRESH_ONLINE_RADIO))