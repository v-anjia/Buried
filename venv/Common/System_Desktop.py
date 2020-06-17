'''
Buried Point for System Desktop
author: antony weijiang
date: 2020/4/7
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

Default = {"Default":[{"startMap":"Click"},\
                    {"startEnergy":"Click"},\
                    {"startMusic":"Click"},\
                    {"startBtPhone":"Click"},\
                    {"startDVR":"Click"},\
                    {"startFM":"Click"},\
                    {"startSetting":"Click"},\
                    {"startWeChat":"Click"},\
                    {"startMiant":"Click"},\
                    {"startVideo":"Click"},\
                    {"startCarControl":"Click"},\
                    {"startAQY":"Click"},\
                    {"startAVM":"Click"},\
                    {"startAudioBook":"Click"},\
                    {"startSkinStore":"Click"},\
                    {"startMiJia":"Click"},\
                    {"startWeMeet":"Click"},\
                    {"EnterWidgetPage":"Click"},\
                    {"incomingCalling":"Set"},\
                ]}

Widget = {"Widget":[{"EnterDefaultPage":"Click"},\
                    {"showDefaultPage":"Click"},\
                    {"editingWidget":"Start"},\
                    {"editingWidget":"End"},\
                    {"EditApp":"Click"},\
                    {"EnterApp":"Click"},\
                    {"defaultWidget":"Click"},\
                ]}

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
    def enter_system_desktop(cls, sn):
        logger.log_debug("enter pay page", \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                         sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d.press("home")
        logger.log_debug("enter system desktop",\
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(3, 5))


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

class Check_System_Desktop_Actions(object):
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

class Default_(object):
    def __init__(self):
        pass

    @classmethod
    @Check_System_Desktop_Actions.check_log(Action=list(Default["Default"][0].keys())[0],
                                     Event=list(Default["Default"][0].values())[0])
    def startMap(cls, sn):
        logger.log_info("Enter map app through System Desktop UI ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[2]').click()
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[2]').click()
        time.sleep(random.randint(3,5))


    @classmethod
    @Check_System_Desktop_Actions.check_log(Action=list(Default["Default"][1].keys())[0],
                                     Event=list(Default["Default"][1].values())[0])
    def startEnergy(cls, sn):
        logger.log_info("Enter Energy app through System Desktop UI ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[2]').click()
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[4]').click()
        time.sleep(random.randint(3,5))

    @classmethod
    @Check_System_Desktop_Actions.check_log(Action=list(Default["Default"][2].keys())[0],
                                            Event=list(Default["Default"][2].values())[0])
    def startMusic(cls, sn):
        logger.log_info("Enter Music app through System Desktop UI ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[2]').click()
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[3]').click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_System_Desktop_Actions.check_log(Action=list(Default["Default"][3].keys())[0],
                                            Event=list(Default["Default"][3].values())[0])
    def startBtPhone(cls, sn):
        logger.log_info("Enter BtPhone app through System Desktop UI ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[2]').click()
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[5]').click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_System_Desktop_Actions.check_log(Action=list(Default["Default"][4].keys())[0],
                                            Event=list(Default["Default"][4].values())[0])
    def startDVR(cls, sn):
        logger.log_info("Enter DVR app through System Desktop UI ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[2]').click()
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[5]').click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_System_Desktop_Actions.check_log(Action=list(Default["Default"][5].keys())[0],
                                            Event=list(Default["Default"][5].values())[0])
    def startFM(cls, sn):
        logger.log_info("Enter FM app through System Desktop UI ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[2]').click()
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[10]').click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_System_Desktop_Actions.check_log(Action=list(Default["Default"][6].keys())[0],
                                            Event=list(Default["Default"][6].values())[0])
    def startSetting(cls, sn):
        logger.log_info("Enter Settings app through System Desktop UI ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[2]').click()
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[12]').click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_System_Desktop_Actions.check_log(Action=list(Default["Default"][7].keys())[0],
                                            Event=list(Default["Default"][7].values())[0])
    def startWeChat(cls, sn):
        logger.log_info("Enter WeChat app through System Desktop UI ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[2]').click()
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[14]').click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_System_Desktop_Actions.check_log(Action=list(Default["Default"][8].keys())[0],
                                            Event=list(Default["Default"][8].values())[0])
    def startMiant(cls, sn):
        logger.log_info("Enter Miant app through System Desktop UI ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[2]').click()
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[9]').click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_System_Desktop_Actions.check_log(Action=list(Default["Default"][9].keys())[0],
                                            Event=list(Default["Default"][9].values())[0])
    def startVideo(cls, sn):
        logger.log_info("Enter Video app through System Desktop UI ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[2]').click()
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[6]').click()
        time.sleep(random.randint(3, 5))


    @classmethod
    @Check_System_Desktop_Actions.check_log(Action=list(Default["Default"][10].keys())[0],
                                            Event=list(Default["Default"][10].values())[0])
    def startCarControl(cls, sn):
        logger.log_info("Enter Car Control app through System Desktop UI ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[2]').click()
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[18]').click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_System_Desktop_Actions.check_log(Action=list(Default["Default"][11].keys())[0],
                                            Event=list(Default["Default"][11].values())[0])
    def startAQY(cls, sn):
        logger.log_info("Enter AQY app through System Desktop UI ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[2]').click()
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[11]').click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_System_Desktop_Actions.check_log(Action=list(Default["Default"][12].keys())[0],
                                            Event=list(Default["Default"][12].values())[0])
    def startAVM(cls, sn):
        logger.log_info("Enter AVM app through System Desktop UI ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[2]').click()
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[16]').click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_System_Desktop_Actions.check_log(Action=list(Default["Default"][13].keys())[0],
                                            Event=list(Default["Default"][13].values())[0])
    def startAudioBook(cls, sn):
        logger.log_info("Enter Audio book app through System Desktop UI ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[2]').click()
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[13]').click()
        time.sleep(random.randint(3, 5))


    @classmethod
    @Check_System_Desktop_Actions.check_log(Action=list(Default["Default"][14].keys())[0],
                                            Event=list(Default["Default"][14].values())[0])
    def startSkinStore(cls, sn):
        logger.log_info("Enter skin store app through System Desktop UI ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[2]').click()
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[17]').click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_System_Desktop_Actions.check_log(Action=list(Default["Default"][15].keys())[0],
                                            Event=list(Default["Default"][15].values())[0])
    def startMiJia(cls, sn):
        logger.log_info("Enter mi jia app through System Desktop UI ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[2]').click()
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[15]').click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_System_Desktop_Actions.check_log(Action=list(Default["Default"][16].keys())[0],
                                            Event=list(Default["Default"][16].values())[0])
    def startWeMeet(cls, sn):
        logger.log_info("Enter we meet app through System Desktop UI ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[2]').click()
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[8]').click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_System_Desktop_Actions.check_log(Action=list(Default["Default"][17].keys())[0],
                                            Event=list(Default["Default"][17].values())[0])
    def EnterWidgetPage(cls, sn):
        logger.log_info("Enter widget page app through System Desktop UI ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[2]').click()
        time.sleep(random.randint(3, 5))
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(3, 5))

class Widget_(object):
    def __init__(self):
        pass

    @classmethod
    @Check_System_Desktop_Actions.check_log(Action=list(Widget["Widget"][0].keys())[0],
                                            Event=list(Widget["Widget"][0].values())[0])
    def EnterDefaultPage(cls, sn):
        logger.log_info("Enter Default page  through System Desktop UI ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(3, 5))
        d.swipe(85, 440, 355, 180, 0.5)
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_System_Desktop_Actions.check_log(Action=list(Widget["Widget"][1].keys())[0],
                                            Event=list(Widget["Widget"][1].values())[0])
    def showDefaultPage(cls, sn):
        logger.log_info("Show Default page  through System Desktop UI ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[2]').click()
        time.sleep(random.randint(3, 5))


    @classmethod
    @Check_System_Desktop_Actions.check_log(Action=list(Widget["Widget"][2].keys())[0],
                                            Event=list(Widget["Widget"][2].values())[0])
    def editingWidget_Start(cls, sn):
        logger.log_info("Show Default page  through System Desktop UI ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(3, 5))
        d.long_click(210, 130, 2)
        time.sleep(random.randint(3, 5))
        d(resourceId="com.wm.launcher:id/edit_confirm").click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_System_Desktop_Actions.check_log(Action=list(Widget["Widget"][2].keys())[0],
                                            Event=list(Widget["Widget"][2].values())[0])
    def editingWidget_End(cls, sn):
        logger.log_info("Show Default page  through System Desktop UI ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(3, 5))
        d.long_click(210, 130, 2)
        time.sleep(random.randint(3, 5))
        d.drag(645, 1542, 625, 483, 1)
        time.sleep(random.randint(3, 5))
        d.drag(645, 1542, 625, 483, 1)
        time.sleep(random.randint(3, 5))
        d(resourceId="com.wm.launcher:id/edit_confirm").click()
        time.sleep(random.randint(3, 5))


    @classmethod
    @Check_System_Desktop_Actions.check_log(Action=list(Widget["Widget"][3].keys())[0],
                                            Event=list(Widget["Widget"][3].values())[0])
    def EditApp(cls, sn):
        logger.log_info("Show Default page  through System Desktop UI ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(3, 5))
        d.long_click(210, 130, 2)
        time.sleep(random.randint(3, 5))
        d.drag(645, 1542, 625, 483, 1)
        time.sleep(random.randint(3, 5))
        d.drag(645, 1542, 625, 483, 1)
        time.sleep(random.randint(3, 5))
        d(resourceId="com.wm.launcher:id/edit_confirm").click()
        time.sleep(random.randint(3, 5))
































