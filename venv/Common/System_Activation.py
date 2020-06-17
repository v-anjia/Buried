'''
Buried Point for System Activation
author: antony weijiang
date: 2020/3/17
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
Activate_Page = {"Activate_Page":[{"PageDisplay":"Start"},\
                               {"PageDisplay":"End"},\
                               {"Get_Download_QR_Code_Click":"Click"},\
                               {"Activate_Click":"Click"},\
                               {"Close_QR_Code_Click":"Click"},\
                                  ]
                    }

print(list(Activate_Page.keys())[0])

Welcome_Page = {"Welcome_Page":[{"PageDisplay":"Start"},\
                               {"PageDisplay":"End"},\
                               {"Disclaimer_Page_Click":"Click"},\
                               {"Disclaimer_Agree_Select":"Set"},\
                               {"Confirm_Click":"Click"},\
                                  ]
                    }

Disclaimer_Page = {"Disclaimer_Page":[{"PageDisplay":"Start"},\
                               {"PageDisplay":"End"},\
                               {"Back_Click":"Click"},\
                                  ]
                    }

setting_log = "/sdcard/lvlog/com.android.settings/normal/*"
buried_point = "/sdcard/Android/data/com.wm.tracker/files/temp/*"
busybox = "/yf/bin/busybox"
app_id = "app_id=SystemSetting"
buried_point_field = "AidlConnectManager"
json_str = "\{hu_disclatmer_flag:flase,hu_activate_flag:flase\}"
json_path = "/crypto/flag/flag.json"
system_activation_pid = "ps |grep com.wm.activate"

adb_object = co.ADB_SN()
sn = adb_object.check_adb_device_isalive()

class Action(object):
    def __init__(self):
        pass

    @classmethod
    def set_sn(cls,sn):
        cls.sn = sn

    @classmethod
    def get_sn(cls):
        return  cls.sn

    @classmethod
    def modify_json_file(cls,sn):
        logger.log_debug("echo json str %s to %s" %(json_str,json_path), \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                         sys._getframe().f_lineno)
        os.system('adb -s %s shell "echo %s >%s"' %(sn,json_str,json_path))
        time.sleep(random.randint(3,5))

    @classmethod
    def wait_system_activation_page(cls,sn):
        try:
            co.reboot_device(sn)
            time.sleep(random.randint(30,40))
            logger.log_info("wait adb alive", \
                            sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                            sys._getframe().f_lineno)
            adb_object.check_adb_device_isalive()
            os.system('adb root')
            time.sleep(random.randint(3,6))
            while True:
                Result  = subprocess.check_output('adb -s %s shell "%s|%s wc -l"' %(sn,system_activation_pid,busybox),shell=True)
                print("antony@@debug")
                Result = co.removal(Result)
                print("antony@@@debug %s" %(Result))
                if int(Result) == 1:
                    logger.log_info("system activation has showed", \
                                    sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                                    sys._getframe().f_lineno)
                    return 0
                time.sleep(random.randint(5,10))
        except Exception as e:
            logger.log_error("%s" %(e), \
                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                             sys._getframe().f_lineno)

class Check_Result(object):
    def __init__(self):
        self.total = 0
        self.count_pass = 0
        self.count_fail = 0

    def set_total(self, total):
        self.total = total

    def get_total(self):
        return self.total

    def set_count_pass(self, count_pass):
        self.count_pass = count_pass

    def get_count_pass(self):
        return self.count_pass

    def set_count_fail(self, count_fail):
        self.count_fail = count_fail

    def get_count_fail(self):
        return self.count_fail

    @classmethod
    def delete_lvlog(cls, sn):
        try:
            cmd = 'adb -s %s shell "rm -rf %s;echo $?"' % (sn, setting_log)
            Result = subprocess.check_output(cmd, shell=True)
            Result = co.removal(Result)
            logger.log_debug("Result value is :%s" % (Result), \
                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                             sys._getframe().f_lineno)
            if Result == '0':
                logger.log_info("delete lvlog successfully", \
                                sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                                sys._getframe().f_lineno)
                return 0
            else:
                logger.log_error("delete lvlog failed", \
                                 sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                                 sys._getframe().f_lineno)
                return 1
        except Exception as e:
            logger.log_error("%s" % (e), \
                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                             sys._getframe().f_lineno)
            return 1

    @classmethod
    def delete_tracker_log(cls, sn):
        try:
            cmd = 'adb -s %s shell "rm -rf %s;echo $?' % (sn, buried_point)
            Result = subprocess.check_output(cmd, shell=True)
            Result = co.removal(Result)
            logger.log_debug("Result value is : %s" % (Result), \
                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                             sys._getframe().f_lineno)

            if int(Result) == 0:
                logger.log_info("delete tracker log successfully", \
                                sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                                sys._getframe().f_lineno)
                return 1
            else:
                logger.log_error("delete tracker log failed", \
                                 sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                                 sys._getframe().f_lineno)
                return 0
        except Exception as e:
            logger.log_error("%s" % (e), \
                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                             sys._getframe().f_lineno)
            return 1

    @classmethod
    def check_android_tracker_log(cls, sn, action=None, event=None, page=None):
        try:
            time.sleep(2)
            str_expr = ".*action.{3}%s.*event.{3}%s.*page_name.{3}%s.*" % (action, event,page)
            logger.log_info("%s" % (str_expr), \
                            sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                            sys._getframe().f_lineno)
            print(str_expr)
            time.sleep(random.randint(5,10))
            cmd = 'adb -s %s shell "cat %s |grep -iE %s |%s wc -l"' % (sn, buried_point, str_expr, busybox)
            # cmd = 'adb -s %s shell "cat %s |grep %s |grep %s|grep -v grep | %s wc -l"' %(sn, buried_point, action, event, busybox)
            Result = subprocess.check_output(cmd, shell=True)
            Result = int(co.removal(Result))
            logger.log_info("antony @@@debug %s" % (Result), \
                            sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                            sys._getframe().f_lineno)
            print("antony @@@debug %s" % (Result))
            logger.log_debug("tracker directory log collect result is : %s" % (Result), \
                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                             sys._getframe().f_lineno)
            return Result
        except Exception as e:
            logger.log_error("%s" % (e), \
                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                             sys._getframe().f_lineno)
            return False

    def check_android_tracker_log_exist(self, sn):
        try:
            cmd = 'adb -s %s shell "cat %s |grep %s |grep %s | %s wc -l   "' % (
            sn, buried_point, app_id, module_id, busybox)
            Result = subprocess.check_call(cmd, stdout=subprocess.PIPE, shell=True)
            if Result == '0':
                logger.log_info("tracker log exist", \
                                sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                                sys._getframe().f_lineno)
                return False
            else:
                logger.log_info("tracker log not exist", \
                                sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                                sys._getframe().f_lineno)
                return True
        except Exception as e:
            logger.log_error("%s" % (e), \
                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                             sys._getframe().f_lineno)
            return False

    def check_reboot_log_exist(self, sn):
        loop_count = 3
        logger.log_info("reboot system", sys._getframe().f_code.co_filename, \
                        sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        os.system('adb -s %s reboot' % (sn))
        logger.log_info("wait for adb device", sys._getframe().f_code.co_filename, \
                        sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        p = subprocess.Popen('adb -s %s wait-for-device' % (sn), stderr=subprocess.PIPE, stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE, shell=False)
        while True:
            time.sleep(random.randint(20, 30))
            print(p.poll())
            if p.poll() is not None:
                logger.log_info("adb devices init successfully", \
                                sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                                sys._getframe().f_lineno)
                if self.check_android_tracker_log_exist():
                    logger.log_info("file transfer to platform", \
                                    sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                                    sys._getframe().f_lineno)
                    return 0
                else:
                    logger.log_error("file not  transfer to platform", \
                                     sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                                     sys._getframe().f_lineno)
                    return 1
            else:
                serial.open_adb_through_serial(self.count)
                if loop_count <= 0:
                    logger.log_error("adb devices init failed", \
                                     sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                                     sys._getframe().f_lineno)
                    return 1
            loop_count = loop_count - 1

class Check_System_Activation_Actions(object):
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

class Activate_Page_(object):
    def __init__(self):
        pass

    @classmethod
    @Check_System_Activation_Actions.check_log(Action=list(Activate_Page["Activate_Page"][0].keys())[0],
                                     Event=list(Activate_Page["Activate_Page"][0].values())[0])
    def PageDisplay_Start(cls, sn):
        logger.log_info("System Activation has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        pass

    @classmethod
    @Check_System_Activation_Actions.check_log(Action=list(Activate_Page["Activate_Page"][1].keys())[0],
                                     Event=list(Activate_Page["Activate_Page"][1].values())[0])
    def PageDisplay_End(cls, sn):
        logger.log_info("Enter settings page ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        Check_Result.delete_tracker_log(sn)
        # time.sleep(random.randint(3, 5))
        time.sleep(random.randint(5, 10))
        os.system('adb -s %s shell "input swipe 310 1540 750 1540"' % (sn))
        # d(text="激活网络服务").click()
        time.sleep(random.randint(3, 5))


    @classmethod
    @Check_System_Activation_Actions.check_log(Action=list(Activate_Page["Activate_Page"][2].keys())[0],
                                     Event=list(Activate_Page["Activate_Page"][2].values())[0])
    def Get_Download_QR_Code_Click(cls, sn):
        logger.log_info("Enter settings page ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(3, 5))
        os.system('adb -s %s shell "input swipe 370 568 640 568"' %(sn))
        time.sleep(random.randint(3, 5))
        os.system('adb -s %s shell "input swipe 310 1560 750 1560"' %(sn))
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_System_Activation_Actions.check_log(Action=list(Activate_Page["Activate_Page"][3].keys())[0],
                                     Event=list(Activate_Page["Activate_Page"][3].values())[0])
    def Activate_Click(cls, sn):
        logger.log_info("Enter settings page ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(5, 10))
        os.system('adb -s %s shell "input swipe 310 1540 750 1540"' % (sn))
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_System_Activation_Actions.check_log(Action=list(Activate_Page["Activate_Page"][4].keys())[0],
                                     Event=list(Activate_Page["Activate_Page"][4].values())[0])
    def Close_QR_Code_Click(cls, sn):
        logger.log_info("Enter settings page ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(3, 5))
        os.system('adb -s %s shell "input swipe 370 568 640 568"' %(sn))
        time.sleep(random.randint(3, 5))
        os.system('adb -s %s shell "input swipe 310 1560 750 1560"' %(sn))
        time.sleep(random.randint(3, 5))


class Welcome_Page_(object):
    def __init__(self):
        pass

    @classmethod
    @Check_System_Activation_Actions.check_log(Action=list(Welcome_Page["Welcome_Page"][0].keys())[0],
                                     Event=list(Welcome_Page["Welcome_Page"][0].values())[0])
    def PageDisplay_Start(cls, sn):
        logger.log_info("Disclaimer page show", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(5, 10))
        os.system('adb -s %s shell "input swipe 310 1540 750 1540"' % (sn))
        time.sleep(random.randint(3, 5))


    @classmethod
    @Check_System_Activation_Actions.check_log(Action=list(Welcome_Page["Welcome_Page"][1].keys())[0],
                                     Event=list(Welcome_Page["Welcome_Page"][1].values())[0])
    def PageDisplay_End(cls, sn):
        logger.log_info("Disclaimer page show", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(5, 10))
        os.system('adb -s %s shell "input swipe 310 1540 750 1540"' % (sn))
        time.sleep(random.randint(5, 10))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d(resourceId="com.wm.activate:id/ok_bt").click()
        time.sleep(random.randint(3, 5))


    @classmethod
    @Check_System_Activation_Actions.check_log(Action=list(Welcome_Page["Welcome_Page"][2].keys())[0],
                                     Event=list(Welcome_Page["Welcome_Page"][2].values())[0])
    def Disclaimer_Page_Click(cls, sn):
        logger.log_info("Disclaimer page show", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(5, 10))
        os.system('adb -s %s shell "input swipe 310 1540 750 1540"' % (sn))
        time.sleep(random.randint(5, 10))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d(resourceId="com.wm.activate:id/disclaimerMoreInfo").click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_System_Activation_Actions.check_log(Action=list(Welcome_Page["Welcome_Page"][3].keys())[0],
                                     Event=list(Welcome_Page["Welcome_Page"][3].values())[0])
    def Disclaimer_Agree_Select(cls, sn):
        logger.log_info("Disclaimer page show", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(5, 10))
        os.system('adb -s %s shell "input swipe 310 1540 750 1540"' % (sn))
        time.sleep(random.randint(5, 10))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d(resourceId="com.wm.activate:id/pact_cb").click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_System_Activation_Actions.check_log(Action=list(Welcome_Page["Welcome_Page"][4].keys())[0],
                                               Event=list(Welcome_Page["Welcome_Page"][4].values())[0])
    def Confirm_Click(cls, sn):
        logger.log_info("Disclaimer page show", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(5, 10))
        os.system('adb -s %s shell "input swipe 310 1540 750 1540"' % (sn))
        time.sleep(random.randint(5, 10))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d(resourceId="com.wm.activate:id/ok_bt").click()
        time.sleep(random.randint(3, 5))



class Disclaimer_Page_(object):
    def __init__(self):
        pass

    @classmethod
    @Check_System_Activation_Actions.check_log(Action=list(Disclaimer_Page["Disclaimer_Page"][0].keys())[0],
                                     Event=list(Disclaimer_Page["Disclaimer_Page"][0].values())[0])
    def PageDisplay_Start(cls, sn):
        logger.log_info("Disclaimer page show", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(5, 10))
        os.system('adb -s %s shell "input swipe 310 1540 750 1540"' % (sn))
        time.sleep(random.randint(8, 10))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d(resourceId="com.wm.activate:id/disclaimerMoreInfo").click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_System_Activation_Actions.check_log(Action=list(Disclaimer_Page["Disclaimer_Page"][1].keys())[0],
                                               Event=list(Disclaimer_Page["Disclaimer_Page"][1].values())[0])
    def PageDisplay_End(cls, sn):
        logger.log_info("Disclaimer page show", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(5, 10))
        os.system('adb -s %s shell "input swipe 310 1540 750 1540"' % (sn))
        time.sleep(random.randint(5, 10))
        d(resourceId="com.wm.activate:id/disclaimerMoreInfo").click()
        time.sleep(random.randint(3, 5))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d(resourceId="com.wm.activate:id/disclaimerBack").click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_System_Activation_Actions.check_log(Action=list(Disclaimer_Page["Disclaimer_Page"][2].keys())[0],
                                               Event=list(Disclaimer_Page["Disclaimer_Page"][2].values())[0])
    def Back_Click(cls, sn):
        logger.log_info("Disclaimer page show", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(5, 10))
        os.system('adb -s %s shell "input swipe 310 1540 750 1540"' % (sn))
        time.sleep(random.randint(5, 10))
        d(resourceId="com.wm.activate:id/disclaimerMoreInfo").click()
        time.sleep(random.randint(3, 5))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d(resourceId="com.wm.activate:id/disclaimerBack").click()
        time.sleep(random.randint(3, 5))















