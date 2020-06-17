'''
Buried Point for System Setting
author: antony weijiang
date: 2020/1/7
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



Setting_Actions = {"settings":[{"Back":"Click"},\
                               {"PageDisplay":"Start"},\
                               {"PageDisplay":"End"},\
                               {"Open_WIFI":"Set"},\
                               {"OpenBluetooth":"Set"},\
                               {"WirelessCharging":"Set"},\
                               {"PrivacyMode":"Set"},\
                               {"ClickUser":"Click"},\
                               {"ClickBluetooth":"Click"},\
                               {"ClickWIFI":"Click"},\
                               {"ClickPrivacy":"Click"},\
                               {"ClickVoice":"Click"},\
                               {"ClickVolume":"Click"},\
                               {"ClickCurrency":"Click"},\
                               {"ClickSystem":"Click"},
                               {"Open_App":"Click"},\
                               {"Foreground":"Start"},\
                               {"Foreground":"End"},\
                               ]
                    }

WMBluetoothSettings = {"WMBluetoothSettings":[{"PageDisplay":"Start"},\
                                              {"OpenBluetoothSwitch":"set"},\
                                              {"VehicleName":"Click"},\
                                              {"ConnectBluetooth":"Click"},\
                                              {"BreakBluetooth":"Click"},\
                                              {"ClickdeleteBluetooth":"Click"},\
                                              {"Back":"Click"},\
                                              {"PageDisplay":"End"}]
                       }

WMDeleteBluetoothDialog = {"WMDeleteBluetoothDialog":[{"PageDisplay":"Start"},\
                                                      {"ClickDelete":"Click"},\
                                                      {"ClickCancel":"Click"},
                                                      {"PageDisplay":"End"}]
                           }

WMEditBluetoothNameActivity ={"WMEditBluetoothNameActivity":[{"PageDisplay":"Start"},\
                                                             {"ConfirmRevision":"Click"},\
                                                             {"ClickEliminate":"Click"},\
                                                             {"Back":"Click"},\
                                                             {"PageDisplay":"End"}
                                                             ]
                              }

WifiSettings ={"WifiSettings":[{"PageDisplay":"Start"},\
                               {"Back":"Click"},\
                               {"PageDisplay":"End"},\
                               {"ClickIgnoreWIFI":"Click"},\
                               {"OpenWIFISwitch":"Set"},\
                               {"ConnectWIFI":"Click"}]
               }

WMRemoveWIFIDialog = {"WMRemoveWIFIDialog":[{"PageDisplay":"Start"},\
                                            {"RemoveWIFI":"Click"},\
                                            {"CancelDialog":"Click"},\
                                            {"Back":"Click"},\
                                            {"PageDisplay":"End"}]
                      }

WMEditTextActivity = {"WMEditTextActivity":[{"PageDisplay":"Start"},\
                                            {"ClickConnectWIFI":"Click"},\
                                            {"ClickEliminate":"Click"},\
                                            {"Back":"Click"},\
                                            {"PageDisplay":"End"}]
                      }

WMPrivacySettings ={"WMPrivacySettings":[{"PageDisplay":"Start"},\
                                         {"PrivacModeSwitch":"Set"},\
                                         {"MapSwitch":"Set"},\
                                         {"CallSwitch":"Set"},\
                                         {"DVRSwitch":"Set"},\
                                         {"VideoSwitch":"Set"},\
                                         {"WeChat":"Set"},\
                                         {"CarHomeSwitch":"Set"},\
                                         {"VehicleSettingSwitch":"Set"},\
                                         {"SetClick":"Set"},\
                                         {"Back":"Click"},\
                                         {"PageDisplay":"End"}]
                    }

WMSpeechSettings ={"WMSpeechSettings":[{"PageDisplay":"Start"},\
                                       {"ClickVoiceSwitch":"Click"},\
                                       {"HelpDocument":"Click"},\
                                       {"Back":"Click"},\
                                       {"PageDisplay":"End"}]
                   }

VoiceHelpManualFragment = {"VoiceHelpManualFragment" : [{"PageDisplay":"Start"},\
                                                        {"Back":"Click"},\
                                                        {"PageDisplay":"End"}]
                           }

WMSwitchVoiceDialog = {"WMSwitchVoiceDialog":[{"PageDisplay":"Start"},\
                                              {"VoiceSwitch":"Set"},\
                                              {"Back":"Click"},\
                                              {"ClickClose":"Click"},\
                                              {"PageDisplay":"End"}]
                       }

WMSoundSettings = {"WMSoundSettings": [{"PageDisplay":"Start"},\
                                       {"ClickSwitch":"Set"},\
                                       {"MediaVolume":"Set"},\
                                       {"ConversationVolume":"Set"},\
                                       {"NavigationVolume":"Set"},\
                                       {"VoiceVolume":"Set"},\
                                       {"ClickEqualizer":"Click"},\
                                       {"ClickSoundField":"Click"},\
                                       {"Back":"Click"},\
                                       {"PageDisplay":"End"},\
                                       ]
                   }

WMVolumeEquilizerSettings = {"WMVolumeEquilizerSettings":[{"PageDisplay":"Start"},\
                                                          {"EqualizerSwitch":"Click"},\
                                                          {"Back":"Click"},\
                                                          {"AdjustEQ60HZ":"Set"},\
                                                          {"AdjustEQ125HZ":"Set"},\
                                                          {"AdjustEQ315HZ":"Set"},\
                                                          {"AdjustEQ800HZ":"Set"},\
                                                          {"AdjustEQ2KHZ":"Set"},\
                                                          {"AdjustEQ5KHZ":"Set"},\
                                                          {"AdjustEQ12.5KHZ":"Set"},\
                                                          {"SwitchEqualizer":"Set"},\
                                                          {"PageDisplay":"End"},\
                                                        ]
                             }

WMVolumeBalanceSettingsActivity = {"WMVolumeBalanceSettingsActivity":[{"PageDisplay":"Start"},\
                                                                      {"DragSundField":"Set"},\
                                                                      {"Back":"Click"},\
                                                                      {"PageDisplay":"End"},\
                                                                        ]
                                   }

WMGeneralSettings = {"WMGeneralSettings":[{"PageDisplay":"Start"},\
                                          {"TimeFormat":"Click"},\
                                          {"Back":"Click"},\
                                          {"PageDisplay":"End"},\
                                          ]}

WMTimeFormatDialog = {"WMTimeFormatDialog":[{"PageDisplay":"Start"},\
                                            {"SwitchTimeFormat":"Set"},\
                                            {"ClickClose":"Click"},\
                                            {"Back":"Click"},\
                                            {"PageDisplay":"End"},\
                                            ]
                      }

WMSystemSettings = {"WMSystemSettings":[{"PageDisplay":"Start"},\
                                        {"FunctionDemo":"Click"},\
                                        {"ClickStorage":"Click"},\
                                        {"ClickTBox":"Click"},\
                                        {"ClickInformation":"Click"},\
                                        {"ClickRecoverySystem":"Click"},\
                                        {"Back":"Click"},\
                                        {"PageDisplay":"End"},\
                                        ]
                    }

PrivateVolumeSettings ={"PrivateVolumeSettings":[{"PageDisplay":"Start"},\
                                                 {"Back":"Click"},\
                                                 {"PageDisplay":"End"},\
                                                 ]
                        }

WMTBoxSettings = {"WMTBoxSettings":[{"PageDisplay":"Start"},\
                                    {"UpdateNetwork":"Click"},\
                                    {"Back":"Click"},\
                                    {"PageDisplay":"End"},\
                                    ]
                  }

WMLawInfoSettingsActivity = {"WMLawInfoSettingsActivity":[{"PageDisplay":"Start"},\
                                                          {"Back":"Click"},\
                                                          {"PageDisplay":"End"},\
                                                          ]
                             }

WMRestoreDefaultDialog = {"WMRestoreDefaultDialog":[{"PageDisplay":"Start"},\
                                                    {"SecoverySystem":"Click"},\
                                                    {"ClickCancel":"Click"},\
                                                    {"Back":"Click"},\
                                                    {"PageDisplay":"End"},\
                                                    ]
                          }

setting_log = "/sdcard/lvlog/com.android.settings/normal/*"
buried_point = "/sdcard/Android/data/com.wm.tracker/files/temp/*"
busybox = "/yf/bin/busybox"
app_id = "app_id=SystemSetting"
buried_point_field = "AidlConnectManager"

adb_object = co.ADB_SN()
sn = adb_object.check_adb_device_isalive()

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
        return  self.count_fail
    
    @classmethod
    def delete_lvlog(cls, sn):
        try:
            cmd = 'adb -s %s shell "rm -rf %s;echo $?"' %(sn, setting_log)
            Result = subprocess.check_output(cmd, shell = True)
            Result = co.removal(Result)
            logger.log_debug("Result value is :%s" %(Result),\
                             sys._getframe().f_code.co_filename,sys._getframe().f_code.co_name,sys._getframe().f_lineno)
            if Result == '0':
                logger.log_info("delete lvlog successfully",\
                                sys._getframe().f_code.co_filename,sys._getframe().f_code.co_name,sys._getframe().f_lineno)
                return  0
            else:
                logger.log_error("delete lvlog failed",\
                                 sys._getframe().f_code.co_filename,sys._getframe().f_code.co_name,sys._getframe().f_lineno)
                return  1
        except Exception as e:
            logger.log_error("%s" %(e),\
                                sys._getframe().f_code.co_filename,sys._getframe().f_code.co_name,sys._getframe().f_lineno)
            return 1
        
    @classmethod
    def delete_tracker_log(cls, sn):
        try:
            cmd = 'adb -s %s shell "rm -rf %s;echo $?' % (sn, buried_point)
            Result = subprocess.check_output(cmd, shell = True)
            Result = co.removal(Result)
            logger.log_debug("Result value is : %s" % (Result), \
                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,sys._getframe().f_lineno)

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
    def check_android_tracker_log(cls, sn, action= None, event= None, page=None):
        try:
            time.sleep(2)
            str_expr = ".*action.{3}.?%s.*event.{3}%s.*page_name.{3}%s" %(action,event,page)
            logger.log_info("%s" %(str_expr),\
                            sys._getframe().f_code.co_filename,sys._getframe().f_code.co_name,sys._getframe().f_lineno)
            print(str_expr)
            time.sleep(random.randint(5,10))
            cmd = 'adb -s %s shell "cat %s |grep -iE %s |%s wc -l"' % (sn, buried_point, str_expr, busybox)
            # cmd = 'adb -s %s shell "cat %s |grep %s |grep %s|grep -v grep | %s wc -l"' %(sn, buried_point, action, event, busybox)
            Result = subprocess.check_output(cmd, shell= True)
            Result = int(co.removal(Result))
            logger.log_info("antony @@@debug %s" % (Result),\
                            sys._getframe().f_code.co_filename,sys._getframe().f_code.co_name,sys._getframe().f_lineno)
            print("antony @@@debug %s" % (Result))
            logger.log_debug("tracker directory log collect result is : %s" %(Result),\
                             sys._getframe().f_code.co_filename,sys._getframe().f_code.co_name,sys._getframe().f_lineno)
            return Result
        except Exception as e:
            logger.log_error("%s" %(e),\
                             sys._getframe().f_code.co_filename,sys._getframe().f_code.co_name,sys._getframe().f_lineno)
            return False

    def check_android_tracker_log_exist(self,sn):
        try:
            cmd = 'adb -s %s shell "cat %s |grep %s |grep %s | %s wc -l   "' %(sn, buried_point, app_id, module_id, busybox)
            Result = subprocess.check_call(cmd, stdout= subprocess.PIPE, shell= True)
            if Result == '0':
                logger.log_info("tracker log exist",\
                                sys._getframe().f_code.co_filename,sys._getframe().f_code.co_name,sys._getframe().f_lineno)
                return False
            else:
                logger.log_info("tracker log not exist",\
                                sys._getframe().f_code.co_filename,sys._getframe().f_code.co_name,sys._getframe().f_lineno)
                return True
        except Exception as e:
            logger.log_error("%s" %(e),\
                             sys._getframe().f_code.co_filename,sys._getframe().f_code.co_name,sys._getframe().f_lineno)
            return False

    def check_reboot_log_exist(self,sn):
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
                                    sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,sys._getframe().f_lineno)
                    return 0
                else :
                    logger.log_error("file not  transfer to platform",\
                                     sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,sys._getframe().f_lineno)
                    return 1
            else:
                serial.open_adb_through_serial(self.count)
                if loop_count <= 0:
                    logger.log_error("adb devices init failed", \
                                     sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                                     sys._getframe().f_lineno)
                    return 1
            loop_count = loop_count - 1

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
    def set_ui_object(cls,sn):
        cls.set_sn(sn)
        cls.d = u2.connect(cls.get_sn())

    @classmethod
    def get_ui_object(cls):
        return cls.d

    @classmethod
    def enter_settings_ui(cls):
        try:
            logger.log_info("enter setting ui",\
                            sys._getframe().f_code.co_filename,sys._getframe().f_code.co_name,sys._getframe().f_lineno)

            # subprocess.Popen('adb -s %s shell "am start -a home -n com.android.settings/com.android.settings.livingui.LVSettingHomePageActivity"' %(cls.get_sn()),stdout=subprocess.PIPE,shell=True)
            subprocess.Popen('adb -s %s shell "am start -a home -n com.android.settings/.Settings"' % (cls.get_sn()), stdout=subprocess.PIPE, shell=True)
            return 0
        except Exception as e:
            logger.log_error("%s" %(e),\
                             sys._getframe().f_code.co_filename,sys._getframe().f_code.co_name,sys._getframe().f_lineno)
            return 1

    @classmethod
    def kill_setting(cls):
        try:
            logger.log_info("kill setting progress",\
                            sys._getframe().f_code.co_filename,sys._getframe().f_code.co_name,sys._getframe().f_lineno)
            subprocess.Popen('adb -s %s shell "ps |grep -i "com.android.settings"|grep -v grep | %s awk \'{print $2}\' | xargs kill -9 "' %(cls.get_sn(),busybox),stdout=subprocess.PIPE,shell= True)
            return 0
        except Exception as e:
            logger.log_error("%s" %(e),\
                             sys._getframe().f_code.co_filename,sys._getframe().f_code.co_name,sys._getframe().f_lineno)
            return 1

    @classmethod
    def enter_bluetooth(cls, sn):
        try:
            d = u2.connect(sn)
            logger.log_debug(d.info, \
                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                             sys._getframe().f_lineno)
            time.sleep(random.randint(1, 3))
            d.xpath('//*[@resource-id="com.android.settings:id/dashboard_container"]/android.widget.FrameLayout[1]').click()
            time.sleep(random.randint(1, 3))
        except Exception as e:
            logger.log_error("%s" %(e), \
                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                             sys._getframe().f_lineno)

    @classmethod
    def enter_wifi(cls,sn):
        try:
            d = u2.connect(sn)
            logger.log_debug(d.info, \
                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                             sys._getframe().f_lineno)
            time.sleep(random.randint(1, 3))
            d.xpath('//*[@resource-id="com.android.settings:id/dashboard_container"]/android.widget.FrameLayout[2]').click()
            time.sleep(random.randint(1, 3))
        except Exception as e:
            logger.log_error("%s" % (e), \
                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                             sys._getframe().f_lineno)

    @classmethod
    def enter_privacy(cls,sn):
        try:
            d = u2.connect(sn)
            logger.log_debug(d.info, \
                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                             sys._getframe().f_lineno)
            time.sleep(random.randint(1, 3))
            d.xpath('//*[@resource-id="com.android.settings:id/dashboard_container"]/android.widget.FrameLayout[3]').click()
            time.sleep(random.randint(1, 3))
        except Exception as e:
            logger.log_error("%s" % (e), \
                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                             sys._getframe().f_lineno)

    @classmethod
    def enter_voice(cls,sn):
        try:
            d = u2.connect(sn)
            logger.log_debug(d.info, \
                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                             sys._getframe().f_lineno)
            time.sleep(random.randint(1, 3))
            d.xpath('//*[@resource-id="com.android.settings:id/dashboard_container"]/android.widget.FrameLayout[4]').click()
            time.sleep(random.randint(1, 3))
        except Exception as e:
            logger.log_error("%s" % (e), \
                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                             sys._getframe().f_lineno)

    @classmethod
    def enter_sound(cls,sn):
        try:
            d = u2.connect(sn)
            logger.log_debug(d.info, \
                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                             sys._getframe().f_lineno)
            time.sleep(random.randint(1, 3))
            d.xpath('//*[@resource-id="com.android.settings:id/dashboard_container"]/android.widget.FrameLayout[5]').click()
            time.sleep(random.randint(1, 3))
        except Exception as e:
            logger.log_error("%s" % (e), \
                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                             sys._getframe().f_lineno)


    @classmethod
    def enter_general(cls,sn):
        try:
            d = u2.connect(sn)
            logger.log_debug(d.info, \
                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                             sys._getframe().f_lineno)
            time.sleep(random.randint(1, 3))
            os.system('adb -s %s shell "input swipe 400 1400 400 400"' %(sn))
            time.sleep(random.randint(1,3))
            os.system('adb -s %s shell "input swipe 400 1400 400 400"' %(sn))
            time.sleep(random.randint(1, 3))
            d.xpath('//*[@resource-id="com.android.settings:id/dashboard_container"]/android.widget.FrameLayout[6]').click()
            time.sleep(random.randint(1, 3))
        except Exception as e:
            logger.log_error("%s" % (e), \
                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                             sys._getframe().f_lineno)
    @classmethod
    def enter_system(cls,sn):
        try:
            d = u2.connect(sn)
            logger.log_debug(d.info, \
                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                             sys._getframe().f_lineno)
            time.sleep(random.randint(1, 3))
            os.system('adb -s %s shell "input swipe 400 1400 400 400"' %(sn))
            time.sleep(random.randint(1,3))
            os.system('adb -s %s shell "input swipe 400 1400 400 400"' %(sn))
            time.sleep(random.randint(1, 3))
            d.xpath('//*[@resource-id="com.android.settings:id/dashboard_container"]/android.widget.FrameLayout[7]').click()
            time.sleep(random.randint(1, 3))
        except Exception as e:
            logger.log_error("%s" % (e), \
                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                             sys._getframe().f_lineno)

    @classmethod
    def enter_timeformate(cls,sn):
        try:
            d = u2.connect(sn)
            logger.log_debug(d.info, \
                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                             sys._getframe().f_lineno)
            time.sleep(random.randint(1, 3))
            d.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[1]').click()
            time.sleep(random.randint(1, 3))
        except Exception as e:
            logger.log_error("%s" % (e), \
                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                             sys._getframe().f_lineno)


    @classmethod
    def enter_volumeequilizer(cls, sn):
        try:
            d = u2.connect(sn)
            logger.log_debug(d.info, \
                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                             sys._getframe().f_lineno)
            time.sleep(random.randint(1, 3))
            os.system('adb -s %s shell "input swipe 400 1600 400 400"' %(sn))
            time.sleep(random.randint(1, 3))
            os.system('adb -s %s shell "input swipe 400 1600 400 400"' % (sn))
            time.sleep(random.randint(1, 3))
            d.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[5]').click()
            time.sleep(random.randint(1, 3))
        except Exception as e:
            logger.log_error("%s" % (e), \
                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                             sys._getframe().f_lineno)

    @classmethod
    def enter_volumebalance(cls, sn):
        try:
            d = u2.connect(sn)
            logger.log_debug(d.info, \
                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                             sys._getframe().f_lineno)
            time.sleep(random.randint(1, 3))
            os.system('adb -s %s shell "input swipe 400 1600 400 400"' %(sn))
            time.sleep(random.randint(1, 3))
            os.system('adb -s %s shell "input swipe 400 1600 400 400"' % (sn))
            time.sleep(random.randint(1, 3))
            d.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[6]').click()
            time.sleep(random.randint(1, 3))
        except Exception as e:
            logger.log_error("%s" % (e), \
                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                             sys._getframe().f_lineno)

    @classmethod
    def enter_voice_person_page(cls, sn):
        try:
            d = u2.connect(sn)
            logger.log_debug(d.info, \
                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                             sys._getframe().f_lineno)
            time.sleep(random.randint(1, 3))
            d.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[1]').click()
            time.sleep(random.randint(1, 3))
        except Exception as e:
            logger.log_error("%s" % (e), \
                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                             sys._getframe().f_lineno)


    @classmethod
    def enter_blue_dialog(cls, sn):
        try:
            d = u2.connect(sn)
            logger.log_debug(d.info, \
                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                             sys._getframe().f_lineno)
            time.sleep(random.randint(1, 3))
            if d(text="删除").exists():
                d(resourceId="com.android.settings:id/delete").click()
                time.sleep(random.randint(3, 5))
            elif d(text="断开").exists():
                d(resourceId="com.android.settings:id/disconnect").click()
                time.sleep(random.randint(3, 5))
                d(resourceId="com.android.settings:id/delete").click()
            else:
                time.sleep(random.randint(5, 10))
                d(resourceId="com.android.settings:id/connect").click()
                time.sleep(random.randint(5, 10))
                d(resourceId="com.android.settings:id/disconnect").click()
                time.sleep(random.randint(3, 5))
                d(resourceId="com.android.settings:id/delete").click()
        except Exception as e:
            logger.log_error("%s" %(e), \
                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                             sys._getframe().f_lineno)

    @classmethod
    def enter_wifi_dialog(cls,sn):
        try:
            d = u2.connect(sn)
            logger.log_debug(d.info, \
                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                             sys._getframe().f_lineno)
            time.sleep(random.randint(1, 3))
            if d(text="忽略").exists():
                d(text="忽略").click()
            time.sleep(random.randint(1, 3))
        except Exception as e:
            logger.log_error("%s" % (e), \
                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                             sys._getframe().f_lineno)

    @classmethod
    def enter_wifi_weditor_page(cls,sn):
        try:
            d = u2.connect(sn)
            logger.log_debug(d.info, \
                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                             sys._getframe().f_lineno)
            time.sleep(random.randint(1, 3))
            if d(text="忽略").exists():
                d(text="忽略").click()
                time.sleep(random.randint(3, 5))
                d(text="移除").click()
                time.sleep(random.randint(1, 3))
            if d(text="TP-LINK_F143").exists():
                d(text="TP-LINK_F143").right(text="连接").click()
            time.sleep(random.randint(1, 3))
        except Exception as e:
            logger.log_error("%s" % (e), \
                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                             sys._getframe().f_lineno)

    @classmethod
    def delay_time(cls):
        time.sleep(random.randint(1,4))

class Check_Setting_Actions(object):
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

class Setting_Actions_(object):
    def __init__(self):
        pass

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(Setting_Actions["settings"][15].keys())[0],
                                     Event=list(Setting_Actions["settings"][15].values())[0])
    def OpenApp(cls, sn):
        logger.log_info("Enter settings page ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[12]').click()
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[12]').click()
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(Setting_Actions["settings"][16].keys())[0],
                                     Event=list(Setting_Actions["settings"][16].values())[0])
    def Foreground_Start(cls, sn):
        logger.log_info("Enter settings page ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[12]').click()
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[12]').click()
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(Setting_Actions["settings"][17].keys())[0],
                                     Event=list(Setting_Actions["settings"][17].values())[0])
    def Foreground_End(cls, sn):
        logger.log_info("Enter settings page ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d.press("home")
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(Setting_Actions["settings"][0].keys())[0],
                                     Event=list(Setting_Actions["settings"][0].values())[0])
    def Back(cls, sn):
        logger.log_info("Enter settings page ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[12]').click()
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[12]').click()
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(Setting_Actions["settings"][1].keys())[0], Event=list(Setting_Actions["settings"][1].values())[0])
    def PageDisplay_Start(cls,sn):
        logger.log_info("Enter settings page ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[12]').click()
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[12]').click()
        time.sleep(random.randint(1, 3))


    @classmethod
    @Check_Setting_Actions.check_log(Action=list(Setting_Actions["settings"][2].keys())[0], Event=list(Setting_Actions["settings"][2].values())[0])
    def PageDisplay_End(cls,sn):
        logger.log_info("Enter settings page ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[12]').click()
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[12]').click()
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(Setting_Actions["settings"][3].keys())[0], Event=list(Setting_Actions["settings"][3].values())[0])
    def Open_WIFI(cls,sn):
        logger.log_info("settings click wifi shortcut ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.settings:id/wireless_switch").click()
        time.sleep(random.randint(1, 3))


    @classmethod
    @Check_Setting_Actions.check_log(Action=list(Setting_Actions["settings"][4].keys())[0], Event=list(Setting_Actions["settings"][4].values())[0])
    def OpenBluetooth(cls,sn):
        logger.log_info("settings click open blue tooth shortcut ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.settings:id/bluetooth_switch").click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(Setting_Actions["settings"][5].keys())[0], Event=list(Setting_Actions["settings"][5].values())[0])
    def WirelessCharging(cls,sn):
        logger.log_info("settings click wireless charging shortcut ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                        sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                         sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.settings:id/wireless_charge_switch").click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(Setting_Actions["settings"][6].keys())[0], Event=list(Setting_Actions["settings"][6].values())[0])
    def PrivacyMode(cls,sn):
        logger.log_info("settings click privacy mode shortcut ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                        sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                         sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.settings:id/privacy_switch").click()
        time.sleep(random.randint(3, 5))


    @classmethod
    @Check_Setting_Actions.check_log(Action=list(Setting_Actions["settings"][7].keys())[0], Event=list(Setting_Actions["settings"][7].values())[0])
    def ClickUser(cls,sn):
        logger.log_info("settings click user shortcut ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                        sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                         sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.android.settings:id/dashboard_container"]/android.widget.LinearLayout[2]').click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(3, 5))


    @classmethod
    @Check_Setting_Actions.check_log(Action=list(Setting_Actions["settings"][8].keys())[0], Event=list(Setting_Actions["settings"][8].values())[0])
    def ClickBluetooth(cls,sn):
        logger.log_info("settings click blue tooth  ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                        sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                         sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.android.settings:id/dashboard_container"]/android.widget.FrameLayout[1]').click()
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1,3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(Setting_Actions["settings"][9].keys())[0], Event=list(Setting_Actions["settings"][9].values())[0])
    def ClickWIFI(cls,sn):
        logger.log_info("settings click wifi ui", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                        sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                         sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.android.settings:id/dashboard_container"]/android.widget.FrameLayout[2]').click()
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1,3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(Setting_Actions["settings"][10].keys())[0], Event=list(Setting_Actions["settings"][10].values())[0])
    def ClickPrivacy(cls,sn):
        logger.log_info("settings click privacy ui ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                        sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                         sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.android.settings:id/dashboard_container"]/android.widget.FrameLayout[3]').click()
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1,3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(Setting_Actions["settings"][11].keys())[0],Event=list(Setting_Actions["settings"][11].values())[0])
    def ClickVoice(cls,sn):
        logger.log_info("settings click voice ui ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                        sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                         sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.android.settings:id/dashboard_container"]/android.widget.FrameLayout[4]').click()
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1,3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(Setting_Actions["settings"][12].keys())[0],Event=list(Setting_Actions["settings"][12].values())[0])
    def ClickVolume(cls,sn):
        logger.log_info("settings click volume ui ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                        sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                         sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.android.settings:id/dashboard_container"]/android.widget.FrameLayout[5]').click()
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1,3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(Setting_Actions["settings"][13].keys())[0],Event=list(Setting_Actions["settings"][13].values())[0])
    def ClickCurrency(cls,sn):
        logger.log_info("settings click currency ui ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                        sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                         sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.android.settings:id/dashboard_container"]/android.widget.FrameLayout[6]').click()
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(Setting_Actions["settings"][14].keys())[0],Event=list(Setting_Actions["settings"][14].values())[0])
    def ClickSystem(cls,sn):
        logger.log_info("settings click system ui ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                        sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                         sys._getframe().f_lineno)
        os.system('adb -s %s shell "input swipe 400 1400 400 400"' %(sn))
        time.sleep(random.randint(1, 3))
        os.system('adb -s %s shell "input swipe 400 1400 400 400"' %(sn))
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.android.settings:id/dashboard_container"]/android.widget.FrameLayout[7]').click()
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(3, 5))

class WMBluetoothSettings_(object):
    def __init__(self):
        pass
    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMBluetoothSettings["WMBluetoothSettings"][0].keys())[0], Event=list(WMBluetoothSettings["WMBluetoothSettings"][0].values())[0])
    def PageDisplay_Start(cls,sn):
        logger.log_info("settings enter blue tooth ui or exit blue tooth ui ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        # print("delay 40 sed")
        # time.sleep(40)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.android.settings:id/dashboard_container"]/android.widget.FrameLayout[1]').click()
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMBluetoothSettings["WMBluetoothSettings"][1].keys())[0], Event=list(WMBluetoothSettings["WMBluetoothSettings"][1].values())[0])
    def OpenBluetoothSwitch(cls,sn):
        logger.log_info("settings click openbluetoothswitch ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                        sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                         sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        if d(text="开启").exists() or d(text = "关闭").exists():
            d(resourceId="android:id/switchWidget").click()
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMBluetoothSettings["WMBluetoothSettings"][2].keys())[0], Event=list(WMBluetoothSettings["WMBluetoothSettings"][2].values())[0])
    def VehicleName(cls,sn):
        logger.log_info("settings click vehicle name ui ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                        sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                         sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[2]').click()
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMBluetoothSettings["WMBluetoothSettings"][3].keys())[0], Event=list(WMBluetoothSettings["WMBluetoothSettings"][3].values())[0])
    def ConnectBluetooth(cls,sn):
        logger.log_info("settings click blue tooth ui ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                        sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                         sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        if d(text="关闭").exists():
            d(resourceId="android:id/switchWidget").click()
            random.randint(random.randint(5,10))
        if d(text= "断开").exists():
            d.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[3]').click()
        time.sleep(random.randint(5, 10))
        if d(text= "连接").exists():
            d.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[3]/android.widget.LinearLayout[2]\
                            /android.widget.LinearLayout[1]/android.widget.TextView[1]').click()
        time.sleep(random.randint(2, 4))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMBluetoothSettings["WMBluetoothSettings"][4].keys())[0], Event=list(WMBluetoothSettings["WMBluetoothSettings"][4].values())[0])
    def BreakBluetooth(cls,sn):
        logger.log_info("settings click blue tooth ui ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                        sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                         sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        if d(text="关闭").exists():
            d(resourceId="android:id/switchWidget").click()
            random.randint(random.randint(5,10))
        if d(text="断开").exists():
            d(resourceId="com.android.settings:id/disconnect").click()
        else:
            d(resourceId="com.android.settings:id/connect").click()
            time.sleep(random.randint(5, 10))
            d(resourceId="com.android.settings:id/disconnect").click()
        time.sleep(random.randint(5, 10))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMBluetoothSettings["WMBluetoothSettings"][5].keys())[0], Event=list(WMBluetoothSettings["WMBluetoothSettings"][5].values())[0])
    def ClickdeleteBluetooth(cls,sn):
        logger.log_info("settings click blue tooth ui ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                        sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                         sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        if d(text="关闭").exists():
            d(resourceId="android:id/switchWidget").click()
            random.randint(random.randint(5,10))
        if d(text="删除").exists():
            d(resourceId="com.android.settings:id/delete").click()
            time.sleep(random.randint(3, 5))
        elif d(text="断开").exists():
            d(resourceId="com.android.settings:id/disconnect").click()
            time.sleep(random.randint(3, 5))
            d(resourceId="com.android.settings:id/delete").click()
        else:
            time.sleep(random.randint(5, 10))
            d(resourceId="com.android.settings:id/connect").click()
            time.sleep(random.randint(5, 10))
            d(resourceId="com.android.settings:id/disconnect").click()
            time.sleep(random.randint(3, 5))
            d(resourceId="com.android.settings:id/delete").click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMBluetoothSettings["WMBluetoothSettings"][6].keys())[0], Event=list(WMBluetoothSettings["WMBluetoothSettings"][6].values())[0])
    def Back(cls,sn):
        logger.log_info("settings click back ui ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMBluetoothSettings["WMBluetoothSettings"][7].keys())[0], Event=list(WMBluetoothSettings["WMBluetoothSettings"][7].values())[0])
    def PageDisplay_End(cls,sn):
        logger.log_info("settings click back ui ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        print("delay 10 sec")
        time.sleep(10)
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))

class WMDeleteBluetoothDialog_(object):
    def __init__(self):
        pass

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMDeleteBluetoothDialog["WMDeleteBluetoothDialog"][0].keys())[0],Event=list(WMDeleteBluetoothDialog["WMDeleteBluetoothDialog"][0].values())[0])
    def PageDisplay_Start(cls,sn):
        logger.log_info("settings click delete blue tooth dialog ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                        sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,sys._getframe().f_lineno)
        time.sleep(random.randint(1,3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1,3))
        d(resourceId="com.android.settings:id/delete").click()


    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMDeleteBluetoothDialog["WMDeleteBluetoothDialog"][1].keys())[0],Event=list(WMDeleteBluetoothDialog["WMDeleteBluetoothDialog"][1].values())[0])
    def ClickDelete(cls,sn):
        logger.log_info("settings click delete button ui ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                        sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(text="删除").click()
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMDeleteBluetoothDialog["WMDeleteBluetoothDialog"][2].keys())[0],Event=list(WMDeleteBluetoothDialog["WMDeleteBluetoothDialog"][2].values())[0])
    def ClickCancel(cls, sn):
        logger.log_info("settings click cancle button ui ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                        sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(text="取消").click()
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMDeleteBluetoothDialog["WMDeleteBluetoothDialog"][3].keys())[0],Event=list(WMDeleteBluetoothDialog["WMDeleteBluetoothDialog"][3].values())[0])
    def PageDisplay_End(cls, sn):
        logger.log_info("settings click page display end button ui ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                        sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))

class WMEditBluetoothNameActivity_(object):
    def __init__(self):
        print("to be defined")
        pass

class WifiSettings_(object):
    def __init__(self):
        pass

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WifiSettings["WifiSettings"][0].keys())[0],Event=list(WifiSettings["WifiSettings"][0].values())[0])
    def PageDisplay_Start(cls, sn):
        logger.log_info("settings click WiFi page display  button ui ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                        sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.android.settings:id/dashboard_container"]/android.widget.FrameLayout[2]').click()
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WifiSettings["WifiSettings"][1].keys())[0],Event=list(WifiSettings["WifiSettings"][1].values())[0])
    def Back(cls,sn):
        logger.log_info("settings click WiFi back button ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WifiSettings["WifiSettings"][2].keys())[0],Event=list(WifiSettings["WifiSettings"][2].values())[0])
    def PageDisplay_End(cls,sn):
        logger.log_info("settings click WiFi back button ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WifiSettings["WifiSettings"][3].keys())[0],Event=list(WifiSettings["WifiSettings"][3].values())[0])
    def ClickIgnoreWIFI(cls,sn):
        logger.log_info("settings click WiFi ignore  button ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        if d(text = "忽略").exists():
            d(resourceId="com.android.settings:id/delete").click()
        time.sleep(random.randint(1, 3))


    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WifiSettings["WifiSettings"][4].keys())[0],Event=list(WifiSettings["WifiSettings"][4].values())[0])
    def OpenWIFISwitch(cls,sn):
        logger.log_info("settings click Open WiFi Switch   button ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        if d(text="开启").exists() or d(text="关闭").exists():
            d(resourceId="android:id/switchWidget").click()
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WifiSettings["WifiSettings"][5].keys())[0],Event=list(WifiSettings["WifiSettings"][5].values())[0])
    def ConnectWIFI(cls,sn):
        logger.log_info("settings click Connect WiFi  button ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        if d(text= "关闭").exists():
            d(resourceId="android:id/switchWidget").click()
        time.sleep(random.randint(3, 5))
        d(text="选择网络...").down(className="android.widget.LinearLayout").click()
        time.sleep(random.randint(3, 5))

class WMRemoveWIFIDialog_(object):
    def __init__(self):
        pass

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMRemoveWIFIDialog["WMRemoveWIFIDialog"][0].keys())[0],Event=list(WMRemoveWIFIDialog["WMRemoveWIFIDialog"][0].values())[0])
    def PageDisplay_Start(cls, sn):
        logger.log_info("settings click Move WiFi Dialog", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(3, 5))
        if d(text = "忽略").exists():
            d(resourceId="com.android.settings:id/delete").click()
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMRemoveWIFIDialog["WMRemoveWIFIDialog"][1].keys())[0],Event=list(WMRemoveWIFIDialog["WMRemoveWIFIDialog"][1].values())[0])
    def RemoveWIFI(cls,sn):
        logger.log_info("settings click remove WiFi Dialog", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(text="移除").click()
        time.sleep(random.randint(3,5))
        if d(text="TP-LINK_F143").exists():
            d(text="TP-LINK_F143").right(text="连接").click()
            time.sleep(random.randint(3,5))
            d.send_keys("wm123456", clear=True)
            time.sleep(random.randint(3,5))
            d(resourceId="com.android.settings:id/btn_submit").click()
            time.sleep(random.randint(5,10))
        time.sleep(random.randint(1, 3))


    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMRemoveWIFIDialog["WMRemoveWIFIDialog"][2].keys())[0],Event=list(WMRemoveWIFIDialog["WMRemoveWIFIDialog"][2].values())[0])
    def CancelDialog(cls,sn):
        logger.log_info("settings click Cancel WiFi Dialog", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(text="取消").click()
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMRemoveWIFIDialog["WMRemoveWIFIDialog"][3].keys())[0],Event=list(WMRemoveWIFIDialog["WMRemoveWIFIDialog"][3].values())[0])
    def Back(cls,sn):
        logger.log_info("settings click back WiFi master ui", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1,3))
        if d(text="忽略").exists():
            d(text="忽略").click()
        time.sleep(random.randint(1, 3))


    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMRemoveWIFIDialog["WMRemoveWIFIDialog"][4].keys())[0],Event=list(WMRemoveWIFIDialog["WMRemoveWIFIDialog"][4].values())[0])
    def PageDisplay_End(cls, sn):
        logger.log_info("settings click back WiFi master ui", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))

class WMEditTextActivity_(object):
    def __init__(self):
        pass

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMEditTextActivity["WMEditTextActivity"][0].keys())[0],\
                                     Event=list(WMEditTextActivity["WMEditTextActivity"][0].values())[0])
    def PageDisplay_Start(cls,sn):
        logger.log_info("settings click back WiFi master ui", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1,3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1,3))
        if d(text="TP-LINK_F143").exists():
            d(text="TP-LINK_F143").right(text="连接").click()
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMEditTextActivity["WMEditTextActivity"][1].keys())[0],\
                                     Event=list(WMEditTextActivity["WMEditTextActivity"][1].values())[0])
    def ClickConnectWIFI(cls,sn):
        logger.log_info("settings click back WiFi master ui", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d.send_keys("wm123456", clear=True)
        time.sleep(random.randint(3, 5))
        d(resourceId="com.android.settings:id/btn_submit").click()
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMEditTextActivity["WMEditTextActivity"][2].keys())[0],\
                                     Event=list(WMEditTextActivity["WMEditTextActivity"][2].values())[0])
    def ClickEliminate(cls,sn):
        logger.log_info("settings click back WiFi master ui", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d.send_keys("wm123456", clear=True)
        time.sleep(random.randint(3, 5))
        d.set_fastinput_ime(False)
        time.sleep(random.randint(1,3))
        d(resourceId="com.android.settings:id/clear").click()
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMEditTextActivity["WMEditTextActivity"][3].keys())[0],\
                                     Event=list(WMEditTextActivity["WMEditTextActivity"][3].values())[0])
    def Back(cls,sn):
        logger.log_info("settings click back WiFi master ui", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))
        if d(text="TP-LINK_F143").exists():
            d(text="TP-LINK_F143").right(text="连接").click()
        time.sleep(random.randint(1, 3))
    
    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMEditTextActivity["WMEditTextActivity"][4].keys())[0],\
                                     Event=list(WMEditTextActivity["WMEditTextActivity"][4].values())[0])
    def PageDisplay_End(cls,sn):
        logger.log_info("settings click back WiFi master ui", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))
        if d(text="TP-LINK_F143").exists():
            d(text="TP-LINK_F143").right(text="连接").click()
        time.sleep(random.randint(1, 3))

class WMPrivacySettings_(object):
    def __init__(self):
        pass

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMPrivacySettings["WMPrivacySettings"][0].keys())[0],\
                                     Event=list(WMPrivacySettings["WMPrivacySettings"][0].values())[0])
    def PageDisplay_Start(cls,sn):
        logger.log_info("settings click wm privacy setting ui", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1,3))
        d.xpath('//*[@resource-id="com.android.settings:id/dashboard_container"]/android.widget.FrameLayout[3]').click()
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMPrivacySettings["WMPrivacySettings"][1].keys())[0],\
                                     Event=list(WMPrivacySettings["WMPrivacySettings"][1].values())[0])
    def PrivacModeSwitch(cls,sn):
        logger.log_info("settings click privacy mode switch ui", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(text="隐私模式").right(className="android.widget.LinearLayout").click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMPrivacySettings["WMPrivacySettings"][2].keys())[0],\
                                     Event=list(WMPrivacySettings["WMPrivacySettings"][2].values())[0])
    def MapSwitch(cls,sn):
        logger.log_info("settings click map switch ui", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        if d(text="隐私保护内容包括").exists():
            d(text="地图").right(resourceId="android:id/widget_frame").click()
        else:
            d(text="隐私模式").right(className="android.widget.LinearLayout").click()
            time.sleep(random.randint(3,5))
            if d(text="隐私保护内容包括").exists():
                d(text="地图").right(resourceId="android:id/widget_frame").click()
                time.sleep(random.randint(3,5))
        time.sleep(random.randint(1, 3))


    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMPrivacySettings["WMPrivacySettings"][3].keys())[0],\
                                     Event=list(WMPrivacySettings["WMPrivacySettings"][3].values())[0])
    def CallSwitch(cls,sn):
        logger.log_info("settings click call switch ui", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        if d(text="隐私保护内容包括").exists():
            d(text="通讯").right(resourceId="android:id/widget_frame").click()
        else:
            d(text="隐私模式").right(className="android.widget.LinearLayout").click()
            time.sleep(random.randint(3,5))
            if d(text="隐私保护内容包括").exists():
                d(text="通讯").right(resourceId="android:id/widget_frame").click()
                time.sleep(random.randint(3,5))
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMPrivacySettings["WMPrivacySettings"][4].keys())[0],Event=list(WMPrivacySettings["WMPrivacySettings"][4].values())[0])
    def DVRSwitch(cls,sn):
        logger.log_info("settings click DVR switch ui", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        if d(text="隐私保护内容包括").exists():
            d(text="行车记录仪").right(resourceId="android:id/widget_frame").click()
        else:
            d(text="隐私模式").right(className="android.widget.LinearLayout").click()
            time.sleep(random.randint(3, 5))
            if d(text="隐私保护内容包括").exists():
                d(text="行车记录仪").right(resourceId="android:id/widget_frame").click()
                time.sleep(random.randint(3, 5))
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMPrivacySettings["WMPrivacySettings"][5].keys())[0],Event=list(WMPrivacySettings["WMPrivacySettings"][5].values())[0])
    def VideoSwitch(cls,sn):
        logger.log_info("settings click video switch ui", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        if d(text="隐私保护内容包括").exists():
            d(text="在线视频").right(resourceId="android:id/widget_frame").click()
        else:
            d(text="隐私模式").right(className="android.widget.LinearLayout").click()
            time.sleep(random.randint(3, 5))
            if d(text="隐私保护内容包括").exists():
                d(text="在线视频").right(resourceId="android:id/widget_frame").click()
                time.sleep(random.randint(3, 5))
        time.sleep(random.randint(1, 3))
        
    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMPrivacySettings["WMPrivacySettings"][6].keys())[0],Event=list(WMPrivacySettings["WMPrivacySettings"][6].values())[0])
    def WeChat(cls,sn):
        logger.log_info("settings click wechat switch ui", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        if d(text="隐私保护内容包括").exists():
            d(text="微信").right(resourceId="android:id/widget_frame").click()
        else:
            d(text="隐私模式").right(className="android.widget.LinearLayout").click()
            time.sleep(random.randint(3, 5))
            if d(text="隐私保护内容包括").exists():
                d(text="微信").right(resourceId="android:id/widget_frame").click()
                time.sleep(random.randint(3, 5))
        time.sleep(random.randint(1, 3))
        
    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMPrivacySettings["WMPrivacySettings"][7].keys())[0],Event=list(WMPrivacySettings["WMPrivacySettings"][7].values())[0])
    def CarHomeSwitch(cls,sn):
        logger.log_info("settings click car home switch ui", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d(text="车家互联").drag_to(text="微信", duration=0.25)
        time.sleep(random.randint(1, 3))
        if d(text="隐私保护内容包括").exists():
            d(text="车家互联").right(resourceId="android:id/widget_frame").click()
        else:
            d(text="隐私模式").right(className="android.widget.LinearLayout").click()
            time.sleep(random.randint(3, 5))
            if d(text="隐私保护内容包括").exists():
                d(text="车家互联").right(resourceId="android:id/widget_frame").click()
                time.sleep(random.randint(3, 5))
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMPrivacySettings["WMPrivacySettings"][8].keys())[0],Event=list(WMPrivacySettings["WMPrivacySettings"][8].values())[0])
    def VehicleSettingSwitch(cls,sn):
        logger.log_info("settings click car home switch ui", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        if d(text="隐私保护内容包括").exists():
            os.system('adb -s %s shell "input swipe 400 1400 400 400"' % (sn))
            time.sleep(random.randint(1, 3))
            os.system('adb -s %s shell "input swipe 400 1400 400 400"' % (sn))
            d(text="车辆设置").right(resourceId="android:id/widget_frame").click()
        else:
            d(text="隐私模式").right(className="android.widget.LinearLayout").click()
            time.sleep(random.randint(3, 5))
            if d(text="隐私保护内容包括").exists():
                os.system('adb -s %s shell "input swipe 400 1400 400 400"' % (sn))
                time.sleep(random.randint(1, 3))
                os.system('adb -s %s shell "input swipe 400 1400 400 400"' % (sn))
                d(text="车辆设置").right(resourceId="android:id/widget_frame").click()
                time.sleep(random.randint(3, 5))
        time.sleep(random.randint(1, 3))


    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMPrivacySettings["WMPrivacySettings"][9].keys())[0],Event=list(WMPrivacySettings["WMPrivacySettings"][9].values())[0])
    def SetClick(cls,sn):
        logger.log_info("settings click system settings switch ui", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        if d(text="隐私保护内容包括").exists():
            os.system('adb -s %s shell "input swipe 400 1400 400 400"' % (sn))
            time.sleep(random.randint(1, 3))
            os.system('adb -s %s shell "input swipe 400 1400 400 400"' % (sn))
            d(text="系统设置").right(resourceId="android:id/widget_frame").click()
        else:
            d(text="隐私模式").right(className="android.widget.LinearLayout").click()
            time.sleep(random.randint(3, 5))
            if d(text="隐私保护内容包括").exists():
                os.system('adb -s %s shell "input swipe 400 1400 400 400"' % (sn))
                time.sleep(random.randint(1, 3))
                os.system('adb -s %s shell "input swipe 400 1400 400 400"' % (sn))
                d(text="系统设置").right(resourceId="android:id/widget_frame").click()
                time.sleep(random.randint(3, 5))
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMPrivacySettings["WMPrivacySettings"][10].keys())[0],Event=list(WMPrivacySettings["WMPrivacySettings"][10].values())[0])
    def Back(cls,sn):
        logger.log_info("settings click system settings switch ui", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.android.settings:id/dashboard_container"]/android.widget.FrameLayout[3]').click()
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMPrivacySettings["WMPrivacySettings"][11].keys())[0],\
                                     Event=list(WMPrivacySettings["WMPrivacySettings"][11].values())[0])
    def PageDisplay_End(cls,sn):
        logger.log_info("settings click system settings switch ui", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.android.settings:id/dashboard_container"]/android.widget.FrameLayout[3]').click()
        time.sleep(random.randint(1, 3))

class WMSpeechSettings_(object):
    def __init__(self):
        pass

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMSpeechSettings["WMSpeechSettings"][0].keys())[0],Event=list(WMSpeechSettings["WMSpeechSettings"][0].values())[0])
    def PageDisplay_Start(cls,sn):
        logger.log_info("settings click WM speech settings switch ui", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1,3))
        d.xpath('//*[@resource-id="com.android.settings:id/dashboard_container"]/android.widget.FrameLayout[4]').click()
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMSpeechSettings["WMSpeechSettings"][1].keys())[0],Event=list(WMSpeechSettings["WMSpeechSettings"][1].values())[0])
    def ClickVoiceSwitch(cls,sn):
        logger.log_info("settings click voice switch ui", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[1]').click()
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMSpeechSettings["WMSpeechSettings"][2].keys())[0],Event=list(WMSpeechSettings["WMSpeechSettings"][2].values())[0])
    def HelpDocument(cls,sn):
        logger.log_info("setting click voice, then click help document ui", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        logger.log_info("start click voice help document ",\
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[2]').click()
        time.sleep(random.randint(1, 3))
        logger.log_info("start click back button ",\
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d(resourceId="com.android.systemui:id/status_bar_back").click()

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMSpeechSettings["WMSpeechSettings"][3].keys())[0],Event=list(WMSpeechSettings["WMSpeechSettings"][3].values())[0])
    def Back(cls,sn):
        logger.log_info("settings click help document ui", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))
    
    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMSpeechSettings["WMSpeechSettings"][3].keys())[0],Event=list(WMSpeechSettings["WMSpeechSettings"][3].values())[0])
    def PageDisplay_End(cls,sn):
        logger.log_info("settings click help document ui", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))

class WMSwitchVoiceDialog_(object):
    def __init__(self):
        pass

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMSwitchVoiceDialog["WMSwitchVoiceDialog"][0].keys())[0],Event=list(WMSwitchVoiceDialog["WMSwitchVoiceDialog"][0].values())[0])
    def PageDisplay_Start(cls,sn):
        logger.log_info("settings click voiceswitch", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[1]').click()
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMSwitchVoiceDialog["WMSwitchVoiceDialog"][1].keys())[0],Event=list(WMSwitchVoiceDialog["WMSwitchVoiceDialog"][1].values())[0])
    def VoiceSwitch(cls,sn):
        logger.log_info("settings click voiceswitch", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d.xpath('//android.widget.ListView/android.widget.RelativeLayout[3]').click()
        time.sleep(random.randint(1, 3))
        d.xpath('//android.widget.ListView/android.widget.RelativeLayout[1]').click()
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMSwitchVoiceDialog["WMSwitchVoiceDialog"][2].keys())[0],Event=list(WMSwitchVoiceDialog["WMSwitchVoiceDialog"][2].values())[0])
    def Back(cls,sn):
        logger.log_info("settings click voiceswitch", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[1]').click()
        time.sleep(random.randint(1, 3))


    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMSwitchVoiceDialog["WMSwitchVoiceDialog"][3].keys())[0],Event=list(WMSwitchVoiceDialog["WMSwitchVoiceDialog"][3].values())[0])
    def ClickClose(cls,sn):
        logger.log_info("settings click voiceswitch", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(text="关闭").click()
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[1]').click()
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMSwitchVoiceDialog["WMSwitchVoiceDialog"][4].keys())[0],Event=list(WMSwitchVoiceDialog["WMSwitchVoiceDialog"][4].values())[0])
    def PageDisplay_End(cls,sn):
        logger.log_info("settings click voiceswitch", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[1]').click()
        time.sleep(random.randint(1, 3))

class WMSoundSettings_(object):
    def __init__(self):
        pass

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMSoundSettings["WMSoundSettings"][0].keys())[0],Event=list(WMSoundSettings["WMSoundSettings"][0].values())[0])
    def PageDisplay_Start(cls,sn):
        logger.log_info("settings click sound page", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.android.settings:id/dashboard_container"]/android.widget.FrameLayout[5]').click()
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMSoundSettings["WMSoundSettings"][1].keys())[0],Event=list(WMSoundSettings["WMSoundSettings"][1].values())[0])
    def ClickSwitch(cls,sn):
        logger.log_info("settings click sound switch", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        if d(text="开启").exists() or d(text = "关闭").exists():
            d(resourceId="android:id/switchWidget").click()
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMSoundSettings["WMSoundSettings"][2].keys())[0],Event=list(WMSoundSettings["WMSoundSettings"][2].values())[0])
    def MediaVolume(cls,sn):
        logger.log_info("settings click sound MediaVolume", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(text="多媒体音量").down(className="android.widget.LinearLayout").child(
            resourceId="android:id/seekbar").swipe("left", steps=1)
        time.sleep(random.randint(1, 3))
        d(text="多媒体音量").down(className="android.widget.LinearLayout").child(
            resourceId="android:id/seekbar").swipe("right", steps=1)
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMSoundSettings["WMSoundSettings"][3].keys())[0],Event=list(WMSoundSettings["WMSoundSettings"][3].values())[0])
    def ConversationVolume(cls,sn):
        logger.log_info("settings click sound MediaVolume", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(text="通话音量").down(className="android.widget.LinearLayout").child(
            resourceId="android:id/seekbar").swipe("left", steps=1)
        time.sleep(random.randint(1, 3))
        d(text="通话音量").down(className="android.widget.LinearLayout").child(
            resourceId="android:id/seekbar").swipe("right", steps=1)
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMSoundSettings["WMSoundSettings"][4].keys())[0],Event=list(WMSoundSettings["WMSoundSettings"][4].values())[0])
    def NavigationVolume(cls,sn):
        logger.log_info("settings click sound NavigationVolume", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(text="导航音量").down(className="android.widget.LinearLayout").child(
            resourceId="android:id/seekbar").swipe("left", steps=1)
        time.sleep(random.randint(1, 3))
        d(text="导航音量").down(className="android.widget.LinearLayout").child(
            resourceId="android:id/seekbar").swipe("right", steps=1)
        time.sleep(random.randint(1, 3))


    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMSoundSettings["WMSoundSettings"][5].keys())[0],Event=list(WMSoundSettings["WMSoundSettings"][5].values())[0])
    def VoiceVolume(cls,sn):
        logger.log_info("settings click sound VoiceVolume", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(text="语音音量").down(className="android.widget.LinearLayout").child(
            resourceId="android:id/seekbar").swipe("left", steps=1)
        time.sleep(random.randint(1, 3))
        d(text="语音音量").down(className="android.widget.LinearLayout").child(
            resourceId="android:id/seekbar").swipe("right", steps=1)
        time.sleep(random.randint(1, 3))


    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMSoundSettings["WMSoundSettings"][6].keys())[0],Event=list(WMSoundSettings["WMSoundSettings"][6].values())[0])
    def ClickEqualizer(cls,sn):
        logger.log_info("settings click sound VoiceVolume", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        os.system('adb -s %s shell "input swipe 400 1400 400 400"' %(sn))
        time.sleep(random.randint(1, 3))
        os.system('adb -s %s shell "input swipe 400 1400 400 400"' % (sn))
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[5]').click()
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMSoundSettings["WMSoundSettings"][7].keys())[0],Event=list(WMSoundSettings["WMSoundSettings"][7].values())[0])
    def ClickSoundField(cls,sn):
        logger.log_info("settings click sound VoiceVolume", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(text="语音音量").swipe("up", steps=1000)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[6]').click()
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))


    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMSoundSettings["WMSoundSettings"][8].keys())[0],Event=list(WMSoundSettings["WMSoundSettings"][8].values())[0])
    def Back(cls,sn):
        logger.log_info("settings click sound Back Button", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1,3))
        d.xpath('//*[@resource-id="com.android.settings:id/dashboard_container"]/android.widget.FrameLayout[5]').click()
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMSoundSettings["WMSoundSettings"][9].keys())[0],Event=list(WMSoundSettings["WMSoundSettings"][9].values())[0])
    def PageDisplay_End(cls,sn):
        logger.log_info("settings click sound page", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                        sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                         sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.android.settings:id/dashboard_container"]/android.widget.FrameLayout[5]').click()
        time.sleep(random.randint(1, 3))

class WMVolumeEquilizerSettings_(object):
    def __init__(self):
        pass

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMVolumeEquilizerSettings["WMVolumeEquilizerSettings"][0].keys())[0],\
                           Event=list(WMVolumeEquilizerSettings["WMVolumeEquilizerSettings"][0].values())[0])
    def PageDisplay_Start(cls, sn):
        logger.log_info("click volume equilizer page", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[5]').click()
        time.sleep(random.randint(1, 3))


    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMVolumeEquilizerSettings["WMVolumeEquilizerSettings"][1].keys())[0],\
                           Event=list(WMVolumeEquilizerSettings["WMVolumeEquilizerSettings"][1].values())[0])
    def EqualizerSwitch(cls, sn):
        logger.log_info("click volume equilizer page", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[1]').click()
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="android:id/content"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]').click()
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMVolumeEquilizerSettings["WMVolumeEquilizerSettings"][10].keys())[0],\
                           Event=list(WMVolumeEquilizerSettings["WMVolumeEquilizerSettings"][10].values())[0])
    def SwitchEqualizer(cls, sn):
        logger.log_info("click volume equilizer page", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[1]').click()
        time.sleep(random.randint(1, 3))
        d.xpath('//android.widget.ListView/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]').click()
        time.sleep(random.randint(1, 3))
        d.xpath('//android.widget.ListView/android.widget.RelativeLayout[3]/android.widget.FrameLayout[1]').click()
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMVolumeEquilizerSettings["WMVolumeEquilizerSettings"][2].keys())[0],\
                           Event=list(WMVolumeEquilizerSettings["WMVolumeEquilizerSettings"][2].values())[0])
    def Back(cls, sn):
        logger.log_info("click volume equilizer page", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[5]').click()
        time.sleep(random.randint(1, 3))


    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMVolumeEquilizerSettings["WMVolumeEquilizerSettings"][2].keys())[0],\
                           Event=list(WMVolumeEquilizerSettings["WMVolumeEquilizerSettings"][2].values())[0])
    def Back(cls, sn):
        logger.log_info("click volume equilizer page", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[5]').click()
        time.sleep(random.randint(1, 3))



    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMVolumeEquilizerSettings["WMVolumeEquilizerSettings"][3].keys())[0],\
                           Event=list(WMVolumeEquilizerSettings["WMVolumeEquilizerSettings"][3].values())[0])
    def AdjustEQ60HZ(cls, sn):
        logger.log_info("click volume equilizer page", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[1]').click()
        time.sleep(random.randint(3, 5))
        d.xpath('//android.widget.ListView/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]').click()
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="android:id/content"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]').click()
        time.sleep(random.randint(3, 5))
        d(text="60Hz").up(className="android.widget.SeekBar").swipe("down", steps=1)
        time.sleep(random.randint(1, 3))
        d(text="60Hz").up(className="android.widget.SeekBar").swipe("up", steps=1)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))


    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMVolumeEquilizerSettings["WMVolumeEquilizerSettings"][4].keys())[0],\
                           Event=list(WMVolumeEquilizerSettings["WMVolumeEquilizerSettings"][4].values())[0])
    def AdjustEQ125HZ(cls, sn):
        logger.log_info("click volume equilizer page", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[1]').click()
        time.sleep(random.randint(3, 5))
        d.xpath('//android.widget.ListView/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]').click()
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="android:id/content"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]').click()
        time.sleep(random.randint(3, 5))
        d(text="125Hz").up(className="android.widget.SeekBar").swipe("down", steps=1)
        time.sleep(random.randint(1, 3))
        d(text="125Hz").up(className="android.widget.SeekBar").swipe("up", steps=1)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMVolumeEquilizerSettings["WMVolumeEquilizerSettings"][5].keys())[0],\
                           Event=list(WMVolumeEquilizerSettings["WMVolumeEquilizerSettings"][5].values())[0])
    def AdjustEQ315HZ(cls, sn):
        logger.log_info("click volume equilizer page", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[1]').click()
        time.sleep(random.randint(3, 5))
        d.xpath('//android.widget.ListView/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]').click()
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="android:id/content"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]').click()
        time.sleep(random.randint(3, 5))
        d(text="315Hz").up(className="android.widget.SeekBar").swipe("down", steps=1)
        time.sleep(random.randint(1, 3))
        d(text="315Hz").up(className="android.widget.SeekBar").swipe("up", steps=1)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMVolumeEquilizerSettings["WMVolumeEquilizerSettings"][6].keys())[0],\
                           Event=list(WMVolumeEquilizerSettings["WMVolumeEquilizerSettings"][6].values())[0])
    def AdjustEQ800HZ(cls, sn):
        logger.log_info("click volume equilizer page", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[1]').click()
        time.sleep(random.randint(3, 5))
        d.xpath('//android.widget.ListView/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]').click()
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="android:id/content"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]').click()
        time.sleep(random.randint(3, 5))
        d(text="800Hz").up(className="android.widget.SeekBar").swipe("down", steps=1)
        time.sleep(random.randint(1, 3))
        d(text="800Hz").up(className="android.widget.SeekBar").swipe("up", steps=1)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMVolumeEquilizerSettings["WMVolumeEquilizerSettings"][7].keys())[0],\
                           Event=list(WMVolumeEquilizerSettings["WMVolumeEquilizerSettings"][7].values())[0])
    def AdjustEQ2KHZ(cls, sn):
        logger.log_info("click volume equilizer page", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[1]').click()
        time.sleep(random.randint(3, 5))
        d.xpath('//android.widget.ListView/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]').click()
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="android:id/content"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]').click()
        time.sleep(random.randint(3, 5))
        d(text="2KHz").up(className="android.widget.SeekBar").swipe("down", steps=1)
        time.sleep(random.randint(1, 3))
        d(text="2KHz").up(className="android.widget.SeekBar").swipe("up", steps=1)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMVolumeEquilizerSettings["WMVolumeEquilizerSettings"][8].keys())[0],\
                           Event=list(WMVolumeEquilizerSettings["WMVolumeEquilizerSettings"][8].values())[0])
    def AdjustEQ5KHZ(cls, sn):
        logger.log_info("click volume equilizer page", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[1]').click()
        time.sleep(random.randint(3, 5))
        d.xpath('//android.widget.ListView/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]').click()
        time.sleep(random.randint(3, 5))
        d.xpath(
            '//*[@resource-id="android:id/content"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]').click()
        time.sleep(random.randint(3, 5))
        d(text="5KHz").up(className="android.widget.SeekBar").swipe("down", steps=1)
        time.sleep(random.randint(1, 3))
        d(text="5KHz").up(className="android.widget.SeekBar").swipe("up", steps=1)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMVolumeEquilizerSettings["WMVolumeEquilizerSettings"][9].keys())[0],\
                           Event=list(WMVolumeEquilizerSettings["WMVolumeEquilizerSettings"][9].values())[0])
    def AdjustEQ12_5KHZ(cls, sn):
        logger.log_info("click volume equilizer page", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[1]').click()
        time.sleep(random.randint(3, 5))
        d.xpath('//android.widget.ListView/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]').click()
        time.sleep(random.randint(3, 5))
        d.xpath(
            '//*[@resource-id="android:id/content"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]').click()
        time.sleep(random.randint(3, 5))
        d(text="12.5KHz").up(className="android.widget.SeekBar").swipe("down", steps=1)
        time.sleep(random.randint(1, 3))
        d(text="12.5KHz").up(className="android.widget.SeekBar").swipe("up", steps=1)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMVolumeEquilizerSettings["WMVolumeEquilizerSettings"][10].keys())[0],\
                           Event=list(WMVolumeEquilizerSettings["WMVolumeEquilizerSettings"][10].values())[0])
    def PageDisplay_End(cls, sn):
        logger.log_info("click volume equilizer page", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[5]').click()
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))

class WMVolumeBalanceSettingsActivity_(object):
    def __init__(self):
        pass

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMVolumeBalanceSettingsActivity["WMVolumeBalanceSettingsActivity"][0].keys())[0],\
                           Event=list(WMVolumeBalanceSettingsActivity["WMVolumeBalanceSettingsActivity"][0].values())[0])
    def PageDisplay_Start(cls, sn):
        logger.log_info("click Volume Balance Settings page", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[6]').click()
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=
    list(WMVolumeBalanceSettingsActivity["WMVolumeBalanceSettingsActivity"][2].keys())[0], \
                                     Event=list(WMVolumeBalanceSettingsActivity["WMVolumeBalanceSettingsActivity"][2].values())[0])
    def Back(cls, sn):
        logger.log_info("click Volume Balance Settings page", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[6]').click()
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=
    list(WMVolumeBalanceSettingsActivity["WMVolumeBalanceSettingsActivity"][3].keys())[0], \
                                     Event=list(WMVolumeBalanceSettingsActivity["WMVolumeBalanceSettingsActivity"][3].values())[0])
    def PageDisplay_End(cls, sn):
        logger.log_info("click Volume Balance Settings page", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[6]').click()
        time.sleep(random.randint(1, 3))

class WMGeneralSettings_(object):
    def __init__(self):
        pass

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMGeneralSettings["WMGeneralSettings"][0].keys())[0],\
                           Event=list(WMGeneralSettings["WMGeneralSettings"][0].values())[0])
    def PageDisplay_Start(cls, sn):
        logger.log_info("click Volume Balance Settings page", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.android.settings:id/dashboard_container"]/android.widget.FrameLayout[6]').click()
        time.sleep(random.randint(1, 3))


    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMGeneralSettings["WMGeneralSettings"][1].keys())[0],\
                           Event=list(WMGeneralSettings["WMGeneralSettings"][1].values())[0])
    def TimeFormat(cls, sn):
        logger.log_info("click Volume Balance Settings page", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[1]').click()
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMGeneralSettings["WMGeneralSettings"][2].keys())[0],\
                           Event=list(WMGeneralSettings["WMGeneralSettings"][2].values())[0])
    def Back(cls, sn):
        logger.log_info("click Volume Balance Settings page", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.android.settings:id/dashboard_container"]/android.widget.FrameLayout[6]').click()
        time.sleep(random.randint(1, 3))


    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMGeneralSettings["WMGeneralSettings"][3].keys())[0],\
                           Event=list(WMGeneralSettings["WMGeneralSettings"][3].values())[0])
    def PageDisplay_End(cls, sn):
        logger.log_info("click Volume Balance Settings page", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.android.settings:id/dashboard_container"]/android.widget.FrameLayout[6]').click()
        time.sleep(random.randint(1, 3))

class WMTimeFormatDialog_(object):
    def __init__(self):
        pass

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMTimeFormatDialog["WMTimeFormatDialog"][0].keys())[0],\
                           Event=list(WMTimeFormatDialog["WMTimeFormatDialog"][0].values())[0])
    def PageDisplay_Start(cls, sn):
        logger.log_info("click Volume Balance Settings page", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[1]').click()
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMTimeFormatDialog["WMTimeFormatDialog"][1].keys())[0],\
                           Event=list(WMTimeFormatDialog["WMTimeFormatDialog"][1].values())[0])
    def SwitchTimeFormat(cls, sn):
        logger.log_info("click Volume Balance Settings page", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d.xpath('//android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.FrameLayout[1]').click()
        time.sleep(random.randint(1, 3))
        d.xpath('//android.widget.ListView/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]').click()
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMTimeFormatDialog["WMTimeFormatDialog"][2].keys())[0],\
                           Event=list(WMTimeFormatDialog["WMTimeFormatDialog"][2].values())[0])
    def ClickClose(cls, sn):
        logger.log_info("click Volume Balance Settings page", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(text="关闭").click()
        time.sleep(random.randint(1, 3))
        # d.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[1]').click()
        # time.sleep(random.randint(1, 3))


    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMTimeFormatDialog["WMTimeFormatDialog"][3].keys())[0],\
                           Event=list(WMTimeFormatDialog["WMTimeFormatDialog"][3].values())[0])
    def Back(cls, sn):
        logger.log_info("click Volume Balance Settings page", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[1]').click()


    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMTimeFormatDialog["WMTimeFormatDialog"][4].keys())[0],\
                           Event=list(WMTimeFormatDialog["WMTimeFormatDialog"][4].values())[0])
    def PageDisplay_End(cls, sn):
        logger.log_info("click Volume Balance Settings page", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[1]').click()

class WMSystemSettings_(object):
    def __init__(self):
        pass

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMSystemSettings["WMSystemSettings"][0].keys())[0], \
                           Event=list(WMSystemSettings["WMSystemSettings"][0].values())[0])
    def PageDisplay_Start(cls, sn):
        logger.log_info("click System Settings page", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.android.settings:id/dashboard_container"]/android.widget.FrameLayout[7]').click()
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMSystemSettings["WMSystemSettings"][1].keys())[0], \
                           Event=list(WMSystemSettings["WMSystemSettings"][1].values())[0])
    def FunctionDemo(cls, sn):
        logger.log_info("click Function Demo page", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[1]').click()
        if d(text="下次不再提醒").exists():
            d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMSystemSettings["WMSystemSettings"][2].keys())[0], \
                           Event=list(WMSystemSettings["WMSystemSettings"][2].values())[0])
    def ClickStorage(cls, sn):
        logger.log_info("click Storage page", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[2]').click()
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))



    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMSystemSettings["WMSystemSettings"][3].keys())[0], \
                           Event=list(WMSystemSettings["WMSystemSettings"][3].values())[0])
    def ClickTBox(cls, sn):
        logger.log_info("click TBox page", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        os.system('adb -s %s shell "input swipe 400 1200 400 400"' %(sn))
        time.sleep(random.randint(1, 3))
        os.system('adb -s %s shell "input swipe 400 1200 400 400"' %(sn))
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[7]').click()
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))


    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMSystemSettings["WMSystemSettings"][4].keys())[0], \
                           Event=list(WMSystemSettings["WMSystemSettings"][4].values())[0])
    def ClickInformation(cls, sn):
        logger.log_info("click Information page", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        os.system('adb -s %s shell "input swipe 400 1200 400 400"' %(sn))
        time.sleep(random.randint(1, 3))
        os.system('adb -s %s shell "input swipe 400 1200 400 400"' %(sn))
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[8]').click()
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))


    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMSystemSettings["WMSystemSettings"][5].keys())[0], \
                           Event=list(WMSystemSettings["WMSystemSettings"][5].values())[0])
    def CilckRecoverySystem(cls, sn):
        logger.log_info("click Recovery page", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        os.system('adb -s %s shell "input swipe 400 1200 400 400"' %(sn))
        time.sleep(random.randint(1, 3))
        os.system('adb -s %s shell "input swipe 400 1200 400 400"' %(sn))
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="android:id/list"]/android.widget.LinearLayout[9]').click()
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMSystemSettings["WMSystemSettings"][6].keys())[0], \
                           Event=list(WMSystemSettings["WMSystemSettings"][6].values())[0])
    def Back(cls, sn):
        logger.log_info("click Back button", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.android.settings:id/dashboard_container"]/android.widget.FrameLayout[7]').click()
        time.sleep(random.randint(1, 3))

    @classmethod
    @Check_Setting_Actions.check_log(Action=list(WMSystemSettings["WMSystemSettings"][7].keys())[0], \
                           Event=list(WMSystemSettings["WMSystemSettings"][7].values())[0])
    def PageDisplay_End(cls, sn):
        logger.log_info("Page Display End", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.android.settings:id/dashboard_container"]/android.widget.FrameLayout[7]').click()
        time.sleep(random.randint(1, 3))

































































































