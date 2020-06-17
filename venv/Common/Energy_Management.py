'''
Buried Point for Energy Management
author: antony weijiang
date: 2020/3/19
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
from Common import Signal_Common as SC
from Common import Signal_List as SL

logger = loger.Current_Module()

Energy_Management = {"Energy_Management":[{"Foreground":"Start"},\
                               {"Foreground":"End"},\
                               {"OpenApp":"Click"},\
                                          ]
                    }

BatteryInfo = {"BatteryInfo":[{"MileageSwitch_10KM":"Click"},\
                               {"MileageSwitch_25KM":"Click"},\
                               {"MileageSwitch_50KM":"Click"},\
                                {"MileageSwitch_100KM":"Click"},\
                                {"EnergyEfficiency":"Click"},\
                                {"PowerConsumeSwitch":"Click"},\
                                {"SpeedSwitch":"Click"},\
                                {"VoiceReport":"Set"},\
                                {"BatteryInfoForeground":"Start"},\
                                {"BatteryInfoForeground":"End"}, \
                                {"IntoBatteryInfo": "Click"}, \
                              ]
                    }

PowerConsume = {"PowerConsume":[{"PeriodSwitch_Week":"Click"},\
                               {"PeriodSwitch_Month":"Click"},\
                               {"PeriodSwitch_Year":"Click"},\
                                {"PowerConsumeForeground":"Start"},\
                                {"PowerConsumeForeground":"End"},\
                                {"IntoPowerConsume":"Click"},\
                              ]
                    }

HistoricalJourney = {"HistoricalJourney":[{"HistoricalJourneyForeground":"Start"},\
                               {"HistoricalJourneyForeground":"End"},\
                               {"IntoHistoricalJourney":"Click"},\
                                {"HistoricalJourneyList":"Click"},\
                              ]
                    }

EnergyBall = {"EnergyBall":[{"EconomyModeAdviseAppare":"Click"},\
                               {"EconomyModeAdvise":"Click"},\
                               {"EnergyRecoveryAppare":"Click"},\
                                {"EnergyRecovery":"Click"},\
                                {"ACOffAdviseAppare":"Click"},\
                                {"ACOffAdvise":"Click"},\
                                {"SpeedAdviceAppare":"Click"},\
                                {"SpeedAdvice":"Click"},\
                              ]
                }

setting_log = "/sdcard/lvlog/com.android.settings/normal/*"
buried_point = "/sdcard/Android/data/com.wm.tracker/files/temp/*"
busybox = "/yf/bin/busybox"
app_id = "app_id=SystemSetting"
buried_point_field = "AidlConnectManager"
enery_management_pid = "ps |grep com.yftech.vehiclecenter | %s awk \'{print $2}\' |xargs kill -9 " %(busybox)
enery_management_pid_exist = "ps |grep com.yftech.vehiclecenter | %s awk \'{print $2}\' |%s wc -l" %(busybox,busybox)
start_enery_management = "am start com.yftech.vehiclecenter/.ui.activites.EnergyActivity"

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
    def kill_energy_management_progress(cls,sn):
        logger.log_debug("kill energy management", \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                         sys._getframe().f_lineno)
        Result = subprocess.check_output('adb -s %s shell "%s"' %(sn,enery_management_pid_exist),shell=True)
        Result = co.removal(Result)
        # print("antony@@@debug %s" %(Result))
        if int(Result) == 1:
            subprocess.Popen('adb -s %s shell "%s"' %(sn,enery_management_pid),shell=True)

    @classmethod
    def start_energy_management(cls,sn):
        logger.log_debug("start energy management", \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                         sys._getframe().f_lineno)
        subprocess.Popen('adb -s %s shell "%s"' %(sn,start_enery_management),shell=True)
        time.sleep(random.randint(1,3))
        

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
    def check_android_tracker_log(cls, sn, action=None, event=None, page = None):
        try:
            time.sleep(2)
            str_expr = ".*action.{3}%s.*event.{3}%s.*page_name.{3}%s.*" % (action, event, page)
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

class Check_Energy_Management_Actions(object):
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

class Energy_Management_(object):
    def __init__(self):
        pass

    @classmethod
    @Check_Energy_Management_Actions.check_log(Action=list(Energy_Management["Energy_Management"][0].keys())[0],
                                               Event=list(Energy_Management["Energy_Management"][0].values())[0])
    def PageDisplay_Start(cls, sn):
        logger.log_info("System Activation has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)

        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1,3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[2]').click()
        time.sleep(random.randint(1,3))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3,5))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[4]').click()
        time.sleep(random.randint(1, 3))
    
    @classmethod
    @Check_Energy_Management_Actions.check_log(Action=list(Energy_Management["Energy_Management"][1].keys())[0],
                                               Event=list(Energy_Management["Energy_Management"][1].values())[0])
    def PageDisplay_End(cls, sn):
        logger.log_info("System Activation has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1,3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[2]').click()
        time.sleep(random.randint(1,3))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3,5))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[4]').click()
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Energy_Management_Actions.check_log(Action=list(Energy_Management["Energy_Management"][2].keys())[0],
                                               Event=list(Energy_Management["Energy_Management"][2].values())[0])
    def OpenApp(cls, sn):
        logger.log_info("System Activation has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1,3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[2]').click()
        time.sleep(random.randint(1,3))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3,5))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[4]').click()
        time.sleep(random.randint(1, 3))


class BatteryInfo_(object):
    def __init__(self):
        pass

    @classmethod
    @Check_Energy_Management_Actions.check_log(Action=list(BatteryInfo["BatteryInfo"][0].keys())[0],
                                               Event=list(BatteryInfo["BatteryInfo"][0].values())[0])
    def MileageSwitch_10KM(cls, sn):
        logger.log_info("Energy Management page has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.yftech.vehiclecenter:id/txt_10km").click()
        time.sleep(random.randint(1,3))

    @classmethod
    @Check_Energy_Management_Actions.check_log(Action=list(BatteryInfo["BatteryInfo"][1].keys())[0],
                                               Event=list(BatteryInfo["BatteryInfo"][1].values())[0])
    def MileageSwitch_25KM(cls, sn):
        logger.log_info("Energy Management page has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.yftech.vehiclecenter:id/txt_25km").click()
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Energy_Management_Actions.check_log(Action=list(BatteryInfo["BatteryInfo"][2].keys())[0],
                                               Event=list(BatteryInfo["BatteryInfo"][2].values())[0])
    def MileageSwitch_50KM(cls, sn):
        logger.log_info("Energy Management page has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.yftech.vehiclecenter:id/txt_50km").click()
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Energy_Management_Actions.check_log(Action=list(BatteryInfo["BatteryInfo"][3].keys())[0],
                                               Event=list(BatteryInfo["BatteryInfo"][3].values())[0])
    def MileageSwitch_100KM(cls, sn):
        logger.log_info("Energy Management page has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.yftech.vehiclecenter:id/txt_100km").click()
        time.sleep(random.randint(1, 3))


    @classmethod
    @Check_Energy_Management_Actions.check_log(Action=list(BatteryInfo["BatteryInfo"][4].keys())[0],
                                               Event=list(BatteryInfo["BatteryInfo"][4].values())[0])
    def EnergyEfficiency(cls, sn):
        logger.log_info("Energy Management page has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        Action.kill_energy_management_progress(sn)
        time.sleep(random.randint(3,5))
        Action.start_energy_management(sn)


    @classmethod
    @Check_Energy_Management_Actions.check_log(Action=list(BatteryInfo["BatteryInfo"][5].keys())[0],
                                               Event=list(BatteryInfo["BatteryInfo"][5].values())[0])
    def PowerConsumeSwitch(cls, sn):
        logger.log_info("Energy Management page has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1,3))
        d(resourceId="com.yftech.vehiclecenter:id/txt_power").click()

    @classmethod
    @Check_Energy_Management_Actions.check_log(Action=list(BatteryInfo["BatteryInfo"][6].keys())[0],
                                               Event=list(BatteryInfo["BatteryInfo"][6].values())[0])
    def SpeedSwitch(cls, sn):
        logger.log_info("Energy Management page has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.yftech.vehiclecenter:id/txt_speed").click()

    @classmethod
    @Check_Energy_Management_Actions.check_log(Action=list(BatteryInfo["BatteryInfo"][7].keys())[0],
                                               Event=list(BatteryInfo["BatteryInfo"][7].values())[0])
    def VoiceReport(cls, sn):
        logger.log_info("Energy Management page has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        os.system('adb -s %s shell "input swipe 400 1400 400 400"' %(sn))
        time.sleep(random.randint(3,5))
        d(resourceId="com.yftech.vehiclecenter:id/power_manager_tts_switch").click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Energy_Management_Actions.check_log(Action=list(BatteryInfo["BatteryInfo"][8].keys())[0],
                                               Event=list(BatteryInfo["BatteryInfo"][8].values())[0])
    def BatteryInfoForeground_Start(cls, sn):
        logger.log_info("Energy Management page has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        Action.kill_energy_management_progress(sn)
        time.sleep(random.randint(3, 5))
        Action.start_energy_management(sn)
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Energy_Management_Actions.check_log(Action=list(BatteryInfo["BatteryInfo"][9].keys())[0],
                                               Event=list(BatteryInfo["BatteryInfo"][9].values())[0])
    def BatteryInfoForeground_End(cls, sn):
        logger.log_info("Energy Management page has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(3, 5))
    
    
    @classmethod
    @Check_Energy_Management_Actions.check_log(Action=list(BatteryInfo["BatteryInfo"][10].keys())[0],
                                               Event=list(BatteryInfo["BatteryInfo"][10].values())[0])
    def IntoBatteryInfo(cls, sn):
        logger.log_info("Energy Management page has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        Action.kill_energy_management_progress(sn)
        time.sleep(random.randint(3, 5))
        Action.start_energy_management(sn)
        time.sleep(random.randint(1, 3))

class PowerConsume_(object):
    def __init__(self):
        pass

    @classmethod
    @Check_Energy_Management_Actions.check_log(Action=list(PowerConsume["PowerConsume"][0].keys())[0],
                                               Event=list(PowerConsume["PowerConsume"][0].values())[0])
    def PeriodSwitch_Week(cls, sn):
        logger.log_info("Energy Management page has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.yftech.vehiclecenter:id/power_consume_layout").click()
        time.sleep(random.randint(1, 3))
        d(resourceId="com.yftech.vehiclecenter:id/txt_week").click()
        time.sleep(random.randint(1, 3))
        d(resourceId="com.yftech.vehiclecenter:id/txt_month").click()
        time.sleep(random.randint(1, 3))
        d(resourceId="com.yftech.vehiclecenter:id/txt_week").click()
        time.sleep(random.randint(1, 3))
    
    @classmethod
    @Check_Energy_Management_Actions.check_log(Action=list(PowerConsume["PowerConsume"][1].keys())[0],
                                               Event=list(PowerConsume["PowerConsume"][1].values())[0])
    def PeriodSwitch_Month(cls, sn):
        logger.log_info("Energy Management page has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.yftech.vehiclecenter:id/power_consume_layout").click()
        time.sleep(random.randint(1, 3))
        d(resourceId="com.yftech.vehiclecenter:id/txt_month").click()
        time.sleep(random.randint(1, 3))


    @classmethod
    @Check_Energy_Management_Actions.check_log(Action=list(PowerConsume["PowerConsume"][2].keys())[0],
                                               Event=list(PowerConsume["PowerConsume"][2].values())[0])
    def PeriodSwitch_Year(cls, sn):
        logger.log_info("Energy Management page has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.yftech.vehiclecenter:id/power_consume_layout").click()
        time.sleep(random.randint(1, 3))
        d(resourceId="com.yftech.vehiclecenter:id/txt_year").click()
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Energy_Management_Actions.check_log(Action=list(PowerConsume["PowerConsume"][3].keys())[0],
                                               Event=list(PowerConsume["PowerConsume"][3].values())[0])
    def PowerConsumeForeground_Start(cls, sn):
        logger.log_info("Energy Management page has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.yftech.vehiclecenter:id/power_consume_layout").click()
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Energy_Management_Actions.check_log(Action=list(PowerConsume["PowerConsume"][4].keys())[0],
                                               Event=list(PowerConsume["PowerConsume"][4].values())[0])
    def PowerConsumeForeground_End(cls, sn):
        logger.log_info("Energy Management page has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.yftech.vehiclecenter:id/power_consume_layout").click()
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
    
    
    @classmethod
    @Check_Energy_Management_Actions.check_log(Action=list(PowerConsume["PowerConsume"][5].keys())[0],
                                               Event=list(PowerConsume["PowerConsume"][5].values())[0])
    def IntoPowerConsume(cls, sn):
        logger.log_info("Energy Management page has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.yftech.vehiclecenter:id/power_consume_layout").click()
        time.sleep(random.randint(1, 3))


class HistoricalJourney_(object):
    def __init__(self):
        pass

    @classmethod
    @Check_Energy_Management_Actions.check_log(Action=list(HistoricalJourney["HistoricalJourney"][0].keys())[0],
                                               Event=list(HistoricalJourney["HistoricalJourney"][0].values())[0])
    def HistoricalJourneyForeground_Start(cls, sn):
        logger.log_info("Energy Management page has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.yftech.vehiclecenter:id/historical_journey_layout").click()
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Energy_Management_Actions.check_log(Action=list(HistoricalJourney["HistoricalJourney"][1].keys())[0],
                                               Event=list(HistoricalJourney["HistoricalJourney"][1].values())[0])
    def HistoricalJourneyForeground_End(cls, sn):
        logger.log_info("Energy Management page has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.yftech.vehiclecenter:id/historical_journey_layout").click()
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()


    @classmethod
    @Check_Energy_Management_Actions.check_log(Action=list(HistoricalJourney["HistoricalJourney"][2].keys())[0],
                                               Event=list(HistoricalJourney["HistoricalJourney"][2].values())[0])
    def IntoHistoricalJourney(cls, sn):
        logger.log_info("Energy Management page has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.yftech.vehiclecenter:id/historical_journey_layout").click()
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Energy_Management_Actions.check_log(Action=list(HistoricalJourney["HistoricalJourney"][3].keys())[0],
                                               Event=list(HistoricalJourney["HistoricalJourney"][3].values())[0])
    def HistoricalJourneyList(cls, sn):
        logger.log_info("Energy Management page has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.yftech.vehiclecenter:id/historical_journey_layout").click()
        time.sleep(random.randint(5, 10))
        d.xpath('//*[@resource-id="com.yftech.vehiclecenter:id/rlCenter"]/android.widget.FrameLayout[1]').click()
        time.sleep(random.randint(5, 10))

class EnergyBall_(object):
    def __init__(self):
        pass

    @classmethod
    @Check_Energy_Management_Actions.check_log(Action=list(EnergyBall["EnergyBall"][0].keys())[0],
                                               Event=list(EnergyBall["EnergyBall"][0].values())[0])
    def EconomyModeAdviseAppare(cls, sn):
        logger.log_info("Energy Management page has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        pcan_object = SC.PCAN()
        logger.log_debug("send hideball signal",\
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        for i in range(50):
            pcan_object.send_arry(SL.HideBall)
            time.sleep(0.2)
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3,5))
        logger.log_debug("send showball signal",\
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        for i in range(50):
            pcan_object.send_arry(SL.ShowBall)
            time.sleep(0.2)

    @classmethod
    @Check_Energy_Management_Actions.check_log(Action=list(EnergyBall["EnergyBall"][2].keys())[0],
                                               Event=list(EnergyBall["EnergyBall"][2].values())[0])
    def EnergyRecoveryAppare(cls, sn):
        logger.log_info("Energy Management page has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        pcan_object = SC.PCAN()
        logger.log_debug("send hideball signal", \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        for i in range(50):
            pcan_object.send_arry(SL.HideBall)
            time.sleep(0.2)
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        logger.log_debug("send showball signal", \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        for i in range(50):
            pcan_object.send_arry(SL.ShowBall)
            time.sleep(0.2)

    @classmethod
    @Check_Energy_Management_Actions.check_log(Action=list(EnergyBall["EnergyBall"][4].keys())[0],
                                               Event=list(EnergyBall["EnergyBall"][4].values())[0])
    def ACOffAdviseAppare(cls, sn):
        logger.log_info("Energy Management page has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        pcan_object = SC.PCAN()
        logger.log_debug("send hideball signal", \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        for i in range(50):
            pcan_object.send_arry(SL.HideBall)
            time.sleep(0.2)
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        logger.log_debug("send showball signal", \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        for i in range(50):
            pcan_object.send_arry(SL.ShowBall)
            time.sleep(0.2)

    @classmethod
    @Check_Energy_Management_Actions.check_log(Action=list(EnergyBall["EnergyBall"][1].keys())[0],
                                               Event=list(EnergyBall["EnergyBall"][1].values())[0])
    def EconomyModeAdvise(cls, sn):
        logger.log_info("Energy Management page has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        pcan_object = SC.PCAN()
        logger.log_debug("send showball signal", \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        for i in range(50):
            pcan_object.send_arry(SL.ShowBall)
            time.sleep(0.2)
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d.xpath(
            '//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.FrameLayout[3]').click()
        time.sleep(random.randint(3, 5))
        logger.log_debug("send hideball signal", \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        for i in range(50):
            pcan_object.send_arry(SL.HideBall)
            time.sleep(0.2)
        

    @classmethod
    @Check_Energy_Management_Actions.check_log(Action=list(EnergyBall["EnergyBall"][3].keys())[0],
                                               Event=list(EnergyBall["EnergyBall"][3].values())[0])
    def EnergyRecovery(cls, sn):
        logger.log_info("Energy Management page has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        pcan_object = SC.PCAN()
        logger.log_debug("send showball signal", \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        for i in range(50):
            pcan_object.send_arry(SL.ShowBall)
            time.sleep(0.2)
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]').click()
        time.sleep(random.randint(3, 5))
        logger.log_debug("send hideball signal", \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        for i in range(50):
            pcan_object.send_arry(SL.HideBall)
            time.sleep(0.2)
            
        
    @classmethod
    @Check_Energy_Management_Actions.check_log(Action=list(EnergyBall["EnergyBall"][5].keys())[0],
                                               Event=list(EnergyBall["EnergyBall"][5].values())[0])
    def ACOffAdvise(cls, sn):
        logger.log_info("Energy Management page has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        pcan_object = SC.PCAN()
        logger.log_debug("send showball signal", \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        for i in range(50):
            pcan_object.send_arry(SL.ShowBall)
            time.sleep(0.2)
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d.xpath(
            '//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]').click()
        time.sleep(random.randint(3, 5))
        logger.log_debug("send hideball signal", \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        for i in range(50):
            pcan_object.send_arry(SL.HideBall)
            time.sleep(0.2)





    



