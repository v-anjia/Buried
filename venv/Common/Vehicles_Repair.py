'''
Buried Point for Vehicles Repair
author: antony weijiang
date: 2020/3/23
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

Home = {"Home":[{"Foreground":"Start"},\
                {"Foreground":"End"},\
                {"Home":"Start"},\
                {"Home":"End"},\
                {"Home_startResult":"Click"},\
                {"Home_Result":"Click"},\
                {"Check":"Click"},\
                {"Check":"Start"},\
                {"Check":"End"},\
                {"Check_Result":"Click"},\
                {"Check_Report":"Click"},\
                {"Check_Report":"Start"},\
                {"Check_Report_Hide":"Click"},\
                {"Check_Report":"End"},\
                {"History":"Click"},\
                {"Remind":"Click"}
                ]
        }

History = {"History":[{"History":"Start"},\
                {"History":"End"},\
                {"History_Result":"Click"},\
                ]
        }

Remind = {"Remind":[{"Remind":"Start"},\
                {"Remind":"End"},\
                {"Remind_Result":"Click"},\
                ]
        }

Account_login = {"Account_login":[{"Account_login":"Start"},\
                                    {"Account_login":"End"},\
                                    {"Account_login":"Click"},\
                                ]
                }

Widget_maintain = {"Widget_maintain":[{"Widget_maintain":"Click"},\
                                    {"Widget_maintain":"Start"},\
                                    {"Widget_maintain":"End"},\
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

vehicles_repair = "ps |grep com.ivi.maint | %s awk \'{print $2}\' |xargs kill -9 " %(busybox)
vehicles_repair_pid_exist = "ps |grep com.ivi.maint | %s awk \'{print $2}\' |%s wc -l" %(busybox,busybox)

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
    def kill_vehicles_repair_progress(cls, sn):
        logger.log_debug("kill vehicles repair", \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                         sys._getframe().f_lineno)
        Result = subprocess.check_output('adb -s %s shell "%s"' % (sn, vehicles_repair_pid_exist), shell=True)
        Result = co.removal(Result)
        # print("antony@@@debug %s" %(Result))
        if int(Result) == 1:
            subprocess.Popen('adb -s %s shell "%s"' % (sn, vehicles_repair), shell=True)


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
            str_expr = ".*action.{3}%s.{3}app_id.*event.{3}%s.*page_name.{3}%s.*" % (action, event,page)
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


class Check_Vehicles_Repair_Actions(object):
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


class Home_(object):
    def __init__(self):
        pass

    @classmethod
    @Check_Vehicles_Repair_Actions.check_log(Action=list(Home["Home"][0].keys())[0],
                                     Event=list(Home["Home"][0].values())[0])
    def Foreground_Start(cls, sn):
        logger.log_info("System Activation has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[2]').click()
        time.sleep(random.randint(1, 3))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[9]').click()
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Vehicles_Repair_Actions.check_log(Action=list(Home["Home"][1].keys())[0],
                                             Event=list(Home["Home"][1].values())[0])
    def Foreground_End(cls, sn):
        logger.log_info("System Activation has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1,3))
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[2]').click()
        time.sleep(random.randint(1, 3))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[9]').click()
        time.sleep(random.randint(1, 3))
        time.sleep(random.randint(5,10))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))
    
    @classmethod
    @Check_Vehicles_Repair_Actions.check_log(Action=list(Home["Home"][2].keys())[0],
                                             Event=list(Home["Home"][2].values())[0])
    def Home_Start(cls, sn):
        logger.log_info("System Activation has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1,3))
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[2]').click()
        time.sleep(random.randint(1, 3))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[9]').click()
        time.sleep(random.randint(5,10))


    @classmethod
    @Check_Vehicles_Repair_Actions.check_log(Action=list(Home["Home"][3].keys())[0],
                                             Event=list(Home["Home"][3].values())[0])
    def Home_End(cls, sn):
        logger.log_info("System Activation has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[2]').click()
        time.sleep(random.randint(1, 3))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[9]').click()
        time.sleep(random.randint(5, 10))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))


    @classmethod
    @Check_Vehicles_Repair_Actions.check_log(Action=list(Home["Home"][4].keys())[0],
                                             Event=list(Home["Home"][4].values())[0])
    def Home_startResult(cls, sn):
        logger.log_info("System Activation has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[2]').click()
        time.sleep(random.randint(1, 3))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[9]').click()
        time.sleep(random.randint(5, 10))

    @classmethod
    @Check_Vehicles_Repair_Actions.check_log(Action=list(Home["Home"][5].keys())[0],
                                             Event=list(Home["Home"][5].values())[0])
    def Home_Result(cls, sn):
        logger.log_info("vehicles Repair has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[2]').click()
        time.sleep(random.randint(1, 3))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[9]').click()
        time.sleep(random.randint(5, 10))


    @classmethod
    @Check_Vehicles_Repair_Actions.check_log(Action=list(Home["Home"][6].keys())[0],
                                             Event=list(Home["Home"][6].values())[0])
    def Check_Click(cls, sn):
        logger.log_info("System Activation has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[2]').click()
        time.sleep(random.randint(1, 3))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[9]').click()
        time.sleep(random.randint(5, 10))
        d(resourceId="com.ivi.maint:id/home_checkBt").click()
        time.sleep(random.randint(15,20))

    @classmethod
    @Check_Vehicles_Repair_Actions.check_log(Action=list(Home["Home"][7].keys())[0],
                                             Event=list(Home["Home"][7].values())[0])
    def Check_Start(cls, sn):
        logger.log_info("System Activation has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[2]').click()
        time.sleep(random.randint(1, 3))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[9]').click()
        time.sleep(random.randint(5, 10))
        d(resourceId="com.ivi.maint:id/home_checkBt").click()
        time.sleep(random.randint(15, 20))
    
    
    @classmethod
    @Check_Vehicles_Repair_Actions.check_log(Action=list(Home["Home"][8].keys())[0],
                                             Event=list(Home["Home"][8].values())[0])
    def Check_End(cls, sn):
        logger.log_info("System Activation has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[2]').click()
        time.sleep(random.randint(1, 3))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[9]').click()
        time.sleep(random.randint(5, 10))
        d(resourceId="com.ivi.maint:id/home_checkBt").click()
        time.sleep(random.randint(15, 20))


    @classmethod
    @Check_Vehicles_Repair_Actions.check_log(Action=list(Home["Home"][9].keys())[0],
                                             Event=list(Home["Home"][9].values())[0])
    def Check_Result(cls, sn):
        logger.log_info("System Activation has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[2]').click()
        time.sleep(random.randint(1, 3))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[9]').click()
        time.sleep(random.randint(5, 10))
        d(resourceId="com.ivi.maint:id/home_checkBt").click()
        time.sleep(random.randint(15, 20))


    @classmethod
    @Check_Vehicles_Repair_Actions.check_log(Action=list(Home["Home"][10].keys())[0],
                                             Event=list(Home["Home"][10].values())[0])
    def Check_Report_Click(cls, sn):
        logger.log_info("System Activation has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[2]').click()
        time.sleep(random.randint(1, 3))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[9]').click()
        time.sleep(random.randint(5, 10))
        d(resourceId="com.ivi.maint:id/home_direction").click()
        time.sleep(random.randint(5, 10))
    
    
    @classmethod
    @Check_Vehicles_Repair_Actions.check_log(Action=list(Home["Home"][11].keys())[0],
                                             Event=list(Home["Home"][11].values())[0])
    def Check_Report_Start(cls, sn):
        logger.log_info("System Activation has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[2]').click()
        time.sleep(random.randint(1, 3))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[9]').click()
        time.sleep(random.randint(5, 10))
        d(resourceId="com.ivi.maint:id/home_direction").click()
        time.sleep(random.randint(5, 10))


    @classmethod
    @Check_Vehicles_Repair_Actions.check_log(Action=list(Home["Home"][12].keys())[0],
                                             Event=list(Home["Home"][12].values())[0])
    def Check_Report_Hide(cls, sn):
        logger.log_info("System Activation has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[2]').click()
        time.sleep(random.randint(1, 3))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[9]').click()
        time.sleep(random.randint(5, 10))
        d(resourceId="com.ivi.maint:id/home_direction").click()
        time.sleep(random.randint(5, 10))
        d(resourceId="com.ivi.maint:id/home_down").click()
        time.sleep(random.randint(5, 10))


    @classmethod
    @Check_Vehicles_Repair_Actions.check_log(Action=list(Home["Home"][13].keys())[0],
                                             Event=list(Home["Home"][13].values())[0])
    def Check_Report_End(cls, sn):
        logger.log_info("System Activation has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[2]').click()
        time.sleep(random.randint(1, 3))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[9]').click()
        time.sleep(random.randint(5, 10))
        d(resourceId="com.ivi.maint:id/home_direction").click()
        time.sleep(random.randint(5, 10))
        d(resourceId="com.ivi.maint:id/home_down").click()
        time.sleep(random.randint(5, 10))

    @classmethod
    @Check_Vehicles_Repair_Actions.check_log(Action=list(Home["Home"][14].keys())[0],
                                             Event=list(Home["Home"][14].values())[0])
    def History(cls, sn):
        logger.log_info("System Activation has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[2]').click()
        time.sleep(random.randint(1, 3))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[9]').click()
        time.sleep(random.randint(5, 10))
        d(resourceId="com.ivi.maint:id/home_history_layout").click()
        time.sleep(random.randint(5, 10))

    @classmethod
    @Check_Vehicles_Repair_Actions.check_log(Action=list(Home["Home"][15].keys())[0],
                                             Event=list(Home["Home"][15].values())[0])
    def Remind(cls, sn):
        logger.log_info("System Activation has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[2]').click()
        time.sleep(random.randint(1, 3))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[9]').click()
        time.sleep(random.randint(5, 10))
        d(resourceId="com.ivi.maint:id/home_details_layout").click()
        time.sleep(random.randint(5, 10))

class History_(object):
    def __init__(self):
        pass

    @classmethod
    @Check_Vehicles_Repair_Actions.check_log(Action=list(History["History"][0].keys())[0],
                                     Event=list(History["History"][0].values())[0])
    def History_Start(cls, sn):
        logger.log_info("Vehicles Repair has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[2]').click()
        time.sleep(random.randint(1, 3))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[9]').click()
        time.sleep(random.randint(5, 10))
        d(resourceId="com.ivi.maint:id/home_history_layout").click()
        time.sleep(random.randint(5, 10))

    @classmethod
    @Check_Vehicles_Repair_Actions.check_log(Action=list(History["History"][1].keys())[0],
                                     Event=list(History["History"][1].values())[0])
    def History_End(cls, sn):
        logger.log_info("Vehicles Repair has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[2]').click()
        time.sleep(random.randint(1, 3))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[9]').click()
        time.sleep(random.randint(5, 10))
        d(resourceId="com.ivi.maint:id/home_history_layout").click()
        time.sleep(random.randint(5, 10))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(5, 10))
    
    @classmethod
    @Check_Vehicles_Repair_Actions.check_log(Action=list(History["History"][2].keys())[0],
                                     Event=list(History["History"][2].values())[0])
    def History_Result(cls, sn):
        logger.log_info("Vehicles Repair has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[2]').click()
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[9]').click()
        time.sleep(random.randint(5, 10))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d(resourceId="com.ivi.maint:id/home_history_layout").click()
        time.sleep(random.randint(5, 10))


class Remind_(object):
    def __init__(self):
        pass

    @classmethod
    @Check_Vehicles_Repair_Actions.check_log(Action=list(Remind["Remind"][0].keys())[0],
                                     Event=list(Remind["Remind"][0].values())[0])
    def Remind_Start(cls, sn):
        logger.log_info("Vehicles Repair has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[2]').click()
        time.sleep(random.randint(1, 3))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[9]').click()
        time.sleep(random.randint(5, 10))
        d(resourceId="com.ivi.maint:id/home_details_value").click()
        time.sleep(random.randint(5, 10))

    @classmethod
    @Check_Vehicles_Repair_Actions.check_log(Action=list(Remind["Remind"][1].keys())[0],
                                             Event=list(Remind["Remind"][1].values())[0])
    def Remind_End(cls, sn):
        logger.log_info("Vehicles Repair has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[2]').click()
        time.sleep(random.randint(1, 3))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[9]').click()
        time.sleep(random.randint(5, 10))
        d(resourceId="com.ivi.maint:id/home_details_value").click()
        time.sleep(random.randint(5, 10))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(5, 10))


    @classmethod
    @Check_Vehicles_Repair_Actions.check_log(Action=list(Remind["Remind"][2].keys())[0],
                                             Event=list(Remind["Remind"][2].values())[0])
    def Remind_Result(cls, sn):
        logger.log_info("Vehicles Repair has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[2]').click()
        time.sleep(random.randint(1, 3))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[9]').click()
        time.sleep(random.randint(5, 10))
        d(resourceId="com.ivi.maint:id/home_details_value").click()
        # time.sleep(random.randint(5, 10))
        # d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(5, 10))


class Widget_maintain_(object):
    def __init__(self):
        pass

    @classmethod
    @Check_Vehicles_Repair_Actions.check_log(Action=list(Widget_maintain["Widget_maintain"][0].keys())[0],
                                     Event=list(Widget_maintain["Widget_maintain"][0].values())[0])
    def Widget_maintain_Click(cls, sn):
        logger.log_info("Vehicles Repair has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.ivi.maint:id/root").click()
        time.sleep(random.randint(5,10))

    @classmethod
    @Check_Vehicles_Repair_Actions.check_log(Action=list(Widget_maintain["Widget_maintain"][1].keys())[0],
                                     Event=list(Widget_maintain["Widget_maintain"][1].values())[0])
    def Widget_maintain_Start(cls, sn):
        logger.log_info("Vehicles Repair has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1, 3))
        d.long_click(125, 200, 2)
        time.sleep(random.randint(1, 3))
        d.drag(175, 1540, 600, 450, 0.5)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.wm.launcher:id/edit_confirm").click()
        time.sleep(random.randint(5, 10))
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1, 3))
        d.long_click(125, 200, 2)
        time.sleep(random.randint(1, 3))
        d.drag(175, 1540, 600, 450, 0.5)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.wm.launcher:id/edit_confirm").click()
        time.sleep(random.randint(5, 10))

    @classmethod
    @Check_Vehicles_Repair_Actions.check_log(Action=list(Widget_maintain["Widget_maintain"][2].keys())[0],
                                     Event=list(Widget_maintain["Widget_maintain"][2].values())[0])
    def Widget_maintain_End(cls, sn):
        logger.log_info("Vehicles Repair has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1, 3))
        d.long_click(125, 200, 2)
        time.sleep(random.randint(1, 3))
        d.drag(175, 1540, 600, 450, 0.5)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.wm.launcher:id/edit_confirm").click()
        time.sleep(random.randint(5, 10))
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1, 3))
        d.long_click(125, 200, 2)
        time.sleep(random.randint(1, 3))
        d.drag(175, 1540, 600, 450, 0.5)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.wm.launcher:id/edit_confirm").click()
        time.sleep(random.randint(5, 10))


    
    