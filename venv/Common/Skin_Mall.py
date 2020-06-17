'''
Buried Point for Skin Mall
author: antony weijiang
date: 2020/3/25
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

Index = {"Index":[{"LifeCycle":"Start"},\
                {"Back":"Click"},\
                {"Review":"Start"},\
                {"Review":"End"},\
                {"Recommend":"Click"},\
                {"Manager":"Click"},\
                {"Order":"Click"},\
                {"LifeCycle":"End"},\
                {"Open_App":"Click"},\
                ]
        }

Recommend = {"Recommend":[{"Review":"Start"},\
                {"Review":"End"},\
                {"SkinItem":"Click"},\
                {"Refresh":"Click"},\
                {"LoadMore":"Click"},\
                ]}

SkinManager = {"SkinManager":[
                {"Review":"Start"},\
                {"Review":"End"},\
                {"SkinItem":"Click"},\
                {"Remove":"Click"},\
                {"RemoveDialog":"Start"},\
                {"RemoveDialog": "Click"},\
                {"RemoveDialog":"Click"},\
                {"RemoveDialog":"End"},\
                {"Download":"Click"},\
                {"Download":"Start"},\
                {"Cancel":"Click"},\
                {"Use":"Click"},\
                {"UseDialog":"Start"},\
                {"UseDialog":"Click"},\
                {"UseDialog":"Click"},\
                {"UseDialog":"End"},\
                {"GetDownloadUrl":"Click"},\
                {"Update":"Click"},\
                {"VersionError":"Click"},\
    ]}


Detail = {"Detail":[{"LifeCycle":"Start"},\
                    {"Back":"Click"},\
                    {"Review":"Start"},\
                    {"Review":"End"},\
                    {"Buy":"Click"},\
                    {"BuyBack":"Click"},\
                    {"LimitDialog":"Start"},\
                    {"LimitDialog":"Click"},\
                    {"LimitDialog":"End"},\
                    {"author":"Click"},\
                    {"Download":"Click"},\
                    {"Download":"Start"},\
                    {"Download":"End"},\
                    {"Cancel":"Click"},\
                    {"Use":"Click"},\
                    {"UseDialog":"Start"},\
                    {"UseDialog":"Click"},\
                    {"UseDialog":"Click"},\
                    {"UseDialog":"End"},\
                    {"VersionError":"Click"},\
                    {"LifeCycle":"End"},\
    ]}

ConfirmOrder ={"ConfirmOrder":[{"LifeCycle":"Start"},\
                               {"Back":"Click"},\
                               {"Review":"Start"},\
                               {"Review":"End"},\
                               {"AliPay":"Click"},\
                               {"WxPay":"Click"},\
                               {"SubmitOrder":"Click"},\
                               {"SubmitOrderBack":"Click"},\
                               {"LifeCycle":"End"},\
                               ]}

QrCode = {"QrCode":[{"LifeCycle":"Start"},\
                    {"Back":"Click"},\
                    {"Review":"Start"},\
                    {"Review":"End"},\
                    {"TimeOutDialog":"Start"},\
                    {"TimeOutDialog":"Click"},\
                    {"TimeOutDialog":"Click"},\
                    {"TimeOutDialog":"End"},\
                    {"PaySucc":"Click"},\
                    {"PayTimeOut":"Click"},\
                    {"PayClose":"Click"},\
                    {"LifeCycle":"End"},\
                    ]}

Feedback = {"Feedback":[{"LifeCycle":"Start"},\
                        {"Back":"Click"},\
                        {"Review":"Start"},\
                        {"Review":"End"},\
                        {"LifeCycle":"End"},\
                        ]}

Author = {"Author":[{"LifeCycle":"Start"},\
                    {"Back":"Click"},\
                    {"AuthorBack":"Click"},\
                    {"Review":"Start"},\
                    {"Review":"End"},\
                    {"SkinItem":"Click"},\
                    {"LifeCycle":"End"},\
                    ]}

Order = {"Order":[{"LifeCycle":"Start"},\
                  {"Back":"Click"},\
                  {"Review":"Start"},\
                  {"Review":"End"},\
                  {"TabAll":"Click"},\
                  {"TabPayment":"Click"},\
                  {"TabPaymented":"Click"},\
                  {"OrderItem":"Click"},\
                  {"Refresh":"Click"},\
                  {"LoadMore":"Click"},\
                  {"LifeCycle":"End"},\
                    ]}

OrderDetail = {"OrderDetail":[{"LifeCycle":"Start"},\
                              {"Back":"Click"},\
                              {"Review":"Start"},\
                              {"Review":"End"},\
                              {"SkinClick":"Click"},\
                              {"Pay":"Click"},\
                              {"PayBack":"Click"},\
                              {"CancelOrder":"Click"},\
                              {"CancelDialog":"Start"},\
                              {"CancelDialog":"Click"},\
                              {"CancelDialog":"Click"},\
                              {"CancelDialog":"End"},\
                              {"CancelOrderBack":"Click"},\
                              {"DeleteOrder":"Click"},\
                              {"DeleteDialog":"Start"},\
                              {"DeleteDialog":"Click"},\
                              {"DeleteDialog":"Click"},\
                              {"DeleteDialog":"End"},\
                              {"DeleteOrderBack":"Click"},\
                              {"LifeCycle":"End"},\
                              {"LimitDialog":"Start"},\
                              {"LimitDialog":"Click"},\
                              {"LimitDialog":"Click"},\
                              {"LimitDialog":"End"},\
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
skill_mall = "ps |grep com.living.store | %s awk \'{print $2}\' |xargs kill -9 " %(busybox)
skill_mall_pid_exist = "ps |grep com.living.store | %s awk \'{print $2}\' |%s wc -l" %(busybox,busybox)

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
    def kill_skill_mall_progress(cls, sn):
        logger.log_debug("kill skin mall progress", \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                         sys._getframe().f_lineno)
        Result = subprocess.check_output('adb -s %s shell "%s"' % (sn, skill_mall_pid_exist), shell=True)
        Result = co.removal(Result)
        # print("antony@@@debug %s" %(Result))
        if int(Result) == 1:
            subprocess.Popen('adb -s %s shell "%s"' % (sn, skill_mall), shell=True)

    @classmethod
    def enter_pay_page(cls,sn):
        logger.log_debug("enter pay page", \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                         sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[2]').click()
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[17]').click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/tv_name", text="Freeman0330版本").click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/rl_bottom").click()
        time.sleep(random.randint(3, 5))

    @classmethod
    def click_submit_button(cls,sn):
        logger.log_debug("enter submit page", \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                         sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d(resourceId="com.living.store:id/btn_next").click()
        time.sleep(random.randint(3,5))

    @classmethod
    def skin_author(cls,sn):
        logger.log_debug("enter author page", \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                         sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[2]').click()
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[17]').click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/tv_name", text="Freeman0330版本").click()

    @classmethod
    def enter_skin_main_page(cls,sn):
        logger.log_debug("enter pay page", \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                         sys._getframe().f_lineno)
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
    def enter_skin_list_details(cls, sn):
        logger.log_debug("enter pay page", \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                         sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[2]').click()
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[17]').click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/btn_order").click()
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

class Check_Skin_Mall_Actions(object):
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

class Index_(object):
    def __init__(self):
        pass

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(Index["Index"][0].keys())[0],
                                       Event=list(Index["Index"][0].values())[0])
    def LifeCycle_Start(cls, sn):
        logger.log_info("Skin Mall has showed ", \
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
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[17]').click()
        time.sleep(random.randint(20, 30))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(Index["Index"][8].keys())[0],
                                       Event=list(Index["Index"][8].values())[0])
    def Open_App(cls, sn):
        logger.log_info("Skin Mall has showed ", \
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
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[17]').click()
        time.sleep(random.randint(20, 30))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(Index["Index"][1].keys())[0],
                                       Event=list(Index["Index"][1].values())[0])
    def Back(cls, sn):
        logger.log_info("Skin Mall has showed ", \
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
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[17]').click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(Index["Index"][2].keys())[0],
                                       Event=list(Index["Index"][2].values())[0])
    def Review_Start(cls, sn):
        logger.log_info("Skin Mall has showed ", \
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
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[17]').click()
        time.sleep(random.randint(10, 15))
        d.press("home")
        time.sleep(random.randint(3, 5))
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[2]').click()
        time.sleep(random.randint(1, 3))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[17]').click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(Index["Index"][3].keys())[0],
                                       Event=list(Index["Index"][3].values())[0])
    def Review_End(cls, sn):
        logger.log_info("Skin Mall has showed ", \
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
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[17]').click()
        time.sleep(random.randint(10, 15))
        d.press("home")
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(Index["Index"][4].keys())[0],
                                       Event=list(Index["Index"][4].values())[0])
    def Recommend(cls, sn):
        logger.log_info("Skin Mall has showed ", \
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
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[17]').click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/tv_nav_skin_manager").click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/tv_nav_recommend").click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(Index["Index"][5].keys())[0],
                                       Event=list(Index["Index"][5].values())[0])
    def Manager(cls, sn):
        logger.log_info("Skin Mall has showed ", \
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
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[17]').click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/tv_nav_skin_manager").click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/tv_nav_recommend").click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(Index["Index"][6].keys())[0],
                                       Event=list(Index["Index"][6].values())[0])
    def Order(cls, sn):
        logger.log_info("Skin Mall has showed ", \
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
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[17]').click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/tv_nav_skin_manager").click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/tv_nav_recommend").click()
        time.sleep(random.randint(3, 5))

class Recommend_(object):
    def __init__(self):
        pass

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(Recommend["Recommend"][0].keys())[0],
                                       Event=list(Recommend["Recommend"][0].values())[0])
    def Review_Start(cls, sn):
        logger.log_info("Skin Mall has showed ", \
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
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[17]').click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/tv_nav_recommend").click()
        time.sleep(random.randint(3, 5))
        d.press("home")
        time.sleep(random.randint(3, 5))
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[2]').click()
        time.sleep(random.randint(1, 3))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[17]').click()
        time.sleep(random.randint(5, 10))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(Recommend["Recommend"][1].keys())[0],
                                       Event=list(Recommend["Recommend"][1].values())[0])
    def Review_End(cls, sn):
        logger.log_info("Skin Mall has showed ", \
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
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[17]').click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/tv_nav_recommend").click()
        time.sleep(random.randint(3, 5))
        d.press("home")
        time.sleep(random.randint(5, 10))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(Recommend["Recommend"][2].keys())[0],
                                       Event=list(Recommend["Recommend"][2].values())[0])
    def SkinItem(cls, sn):
        logger.log_info("Skin Mall has showed ", \
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
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[17]').click()
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.living.store:id/frame_layout"]/android.view.ViewGroup[1]/android.widget.RelativeLayout[1]/android.support.v7.widget.RecyclerView[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]').click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(5, 10))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(Recommend["Recommend"][3].keys())[0],
                                       Event=list(Recommend["Recommend"][3].values())[0])
    def Refresh(cls, sn):
        logger.log_info("Skin Mall has showed ", \
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
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[17]').click()
        time.sleep(random.randint(20,25))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(Recommend["Recommend"][4].keys())[0],
                                       Event=list(Recommend["Recommend"][4].values())[0])
    def LoadMore(cls, sn):
        logger.log_info("Skin Mall has showed ", \
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
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[17]').click()
        time.sleep(random.randint(3, 5))
        os.system('adb -s %s shell "input swipe 400 1400 400 500"' % (sn))
        time.sleep(random.randint(10, 15))

class SkinManager_(object):
    def __init__(self):
        pass

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(SkinManager["SkinManager"][0].keys())[0],
                                       Event=list(SkinManager["SkinManager"][0].values())[0])
    def Review_Start(cls, sn):
        logger.log_info("Skin Mall has showed ", \
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
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[17]').click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/tv_nav_skin_manager").click()
        time.sleep(random.randint(10, 15))
        d.press("home")
        time.sleep(random.randint(3, 5))
        d.swipe(355, 180, 85, 440, 0.5)
        time.sleep(random.randint(1, 3))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[2]').click()
        time.sleep(random.randint(1, 3))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[17]').click()
        time.sleep(random.randint(3, 5))


    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(SkinManager["SkinManager"][1].keys())[0],
                                       Event=list(SkinManager["SkinManager"][1].values())[0])
    def Review_End(cls, sn):
        logger.log_info("Skin Mall has showed ", \
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
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[17]').click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/tv_nav_skin_manager").click()
        time.sleep(random.randint(10, 15))
        d.press("home")
        time.sleep(random.randint(3, 5))


    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(SkinManager["SkinManager"][2].keys())[0],
                                       Event=list(SkinManager["SkinManager"][2].values())[0])
    def SkinItem(cls, sn):
        logger.log_info("Skin Mall has showed ", \
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
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[17]').click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/tv_nav_skin_manager").click()
        time.sleep(random.randint(10, 15))
        d.xpath('//*[@resource-id="com.living.store:id/rv_list"]/android.widget.RelativeLayout[1]').click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(SkinManager["SkinManager"][3].keys())[0],
                                       Event=list(SkinManager["SkinManager"][3].values())[0])
    def Remove(cls, sn):
        logger.log_info("Skin Mall has showed ", \
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
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[17]').click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/tv_nav_skin_manager").click()
        time.sleep(random.randint(10, 15))
        d.xpath('//*[@resource-id="com.living.store:id/frame_layout"]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.view.ViewGroup[1]/android.widget.RelativeLayout[1]/android.support.v7.widget.RecyclerView[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView[1]').click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(SkinManager["SkinManager"][4].keys())[0],
                                       Event=list(SkinManager["SkinManager"][4].values())[0])
    def RemoveDialog_Start(cls, sn):
        logger.log_info("Skin Mall has showed ", \
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
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[17]').click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/tv_nav_skin_manager").click()
        time.sleep(random.randint(10, 15))
        d.xpath('//*[@resource-id="com.living.store:id/frame_layout"]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.view.ViewGroup[1]/android.widget.RelativeLayout[1]/android.support.v7.widget.RecyclerView[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView[1]').click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(SkinManager["SkinManager"][5].keys())[0],
                                       Event=list(SkinManager["SkinManager"][5].values())[0])
    def RemoveDialog_Click_Remove(cls, sn):
        logger.log_info("Skin Mall has showed ", \
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
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[17]').click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/tv_nav_skin_manager").click()
        time.sleep(random.randint(10, 15))
        d.xpath('//*[@resource-id="com.living.store:id/frame_layout"]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.view.ViewGroup[1]/android.widget.RelativeLayout[1]/android.support.v7.widget.RecyclerView[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView[1]').click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/btn_negative").click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(SkinManager["SkinManager"][6].keys())[0],
                                       Event=list(SkinManager["SkinManager"][6].values())[0])
    def RemoveDialog_Click_Cancel(cls, sn):
        logger.log_info("Skin Mall has showed ", \
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
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[17]').click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/tv_nav_skin_manager").click()
        time.sleep(random.randint(10, 15))
        d.xpath('//*[@resource-id="com.living.store:id/frame_layout"]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.view.ViewGroup[1]/android.widget.RelativeLayout[1]/android.support.v7.widget.RecyclerView[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView[1]').click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/btn_negative").click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(SkinManager["SkinManager"][7].keys())[0],
                                       Event=list(SkinManager["SkinManager"][7].values())[0])
    def RemoveDialog_End(cls, sn):
        logger.log_info("Skin Mall has showed ", \
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
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[17]').click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/tv_nav_skin_manager").click()
        time.sleep(random.randint(10, 15))
        d.xpath('//*[@resource-id="com.living.store:id/frame_layout"]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.view.ViewGroup[1]/android.widget.RelativeLayout[1]/android.support.v7.widget.RecyclerView[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView[1]').click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/btn_negative").click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(SkinManager["SkinManager"][8].keys())[0],
                                       Event=list(SkinManager["SkinManager"][8].values())[0])
    def Download_Click(cls, sn):
        logger.log_info("Skin Mall has showed ", \
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
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[17]').click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/tv_nav_skin_manager").click()
        time.sleep(random.randint(10, 15))
        d(resourceId="com.living.store:id/btn_download", text="下载").click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/btn_download", text="取消下载").click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(SkinManager["SkinManager"][9].keys())[0],
                                       Event=list(SkinManager["SkinManager"][9].values())[0])
    def Download_Start(cls, sn):
        logger.log_info("Skin Mall has showed ", \
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
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[17]').click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/tv_nav_skin_manager").click()
        time.sleep(random.randint(10, 15))
        d(resourceId="com.living.store:id/btn_download", text="下载").click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/btn_download", text="取消下载").click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(SkinManager["SkinManager"][10].keys())[0],
                                       Event=list(SkinManager["SkinManager"][10].values())[0])
    def Cancel(cls, sn):
        logger.log_info("Skin Mall has showed ", \
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
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[17]').click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/tv_nav_skin_manager").click()
        time.sleep(random.randint(10, 15))
        d(resourceId="com.living.store:id/btn_download", text="下载").click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/btn_download", text="取消下载").click()
        time.sleep(random.randint(3, 5))


    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(SkinManager["SkinManager"][11].keys())[0],
                                       Event=list(SkinManager["SkinManager"][11].values())[0])
    def Use(cls, sn):
        logger.log_info("Skin Mall has showed ", \
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
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[17]').click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/tv_nav_skin_manager").click()
        time.sleep(random.randint(10, 15))
        d.xpath('//*[@resource-id="com.living.store:id/rv_list"]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView[2]').click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(SkinManager["SkinManager"][12].keys())[0],
                                       Event=list(SkinManager["SkinManager"][12].values())[0])
    def UseDialog_Start(cls, sn):
        logger.log_info("Skin Mall has showed ", \
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
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[17]').click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/tv_nav_skin_manager").click()
        time.sleep(random.randint(10, 15))
        d.xpath('//*[@resource-id="com.living.store:id/rv_list"]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView[2]').click()
        time.sleep(random.randint(3, 5))


    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(SkinManager["SkinManager"][13].keys())[0],
                                       Event=list(SkinManager["SkinManager"][13].values())[0])
    def UseDialog_Use(cls, sn):
        logger.log_info("Skin Mall has showed ", \
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
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[17]').click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/tv_nav_skin_manager").click()
        time.sleep(random.randint(10, 15))
        d.xpath('//*[@resource-id="com.living.store:id/rv_list"]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView[2]').click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/btn_cancel").click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(SkinManager["SkinManager"][14].keys())[0],
                                       Event=list(SkinManager["SkinManager"][14].values())[0])
    def UseDialog_Cancel(cls, sn):
        logger.log_info("Skin Mall has showed ", \
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
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[17]').click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/tv_nav_skin_manager").click()
        time.sleep(random.randint(10, 15))
        d.xpath('//*[@resource-id="com.living.store:id/rv_list"]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView[2]').click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/btn_cancel").click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(SkinManager["SkinManager"][15].keys())[0],
                                       Event=list(SkinManager["SkinManager"][15].values())[0])
    def UseDialog_End(cls, sn):
        logger.log_info("Skin Mall has showed ", \
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
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[17]').click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/tv_nav_skin_manager").click()
        time.sleep(random.randint(10, 15))
        d.xpath('//*[@resource-id="com.living.store:id/rv_list"]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView[2]').click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/btn_cancel").click()
        time.sleep(random.randint(3, 5))

class Detail_(object):
    def __init__(self):
        pass

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(Detail["Detail"][0].keys())[0],
                                       Event=list(Detail["Detail"][0].values())[0])
    def LifeCycle(cls, sn):
        logger.log_info("Skin Mall has showed ", \
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
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[17]').click()
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.living.store:id/rv_list"]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]').click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(Detail["Detail"][1].keys())[0],
                                       Event=list(Detail["Detail"][1].values())[0])
    def Back(cls, sn):
        logger.log_info("Skin Mall has showed ", \
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
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[17]').click()
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.living.store:id/rv_list"]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]').click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(Detail["Detail"][2].keys())[0],
                                       Event=list(Detail["Detail"][2].values())[0])
    def Review_Start(cls, sn):
        logger.log_info("Skin Mall has showed ", \
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
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[17]').click()
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.living.store:id/rv_list"]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]').click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(Detail["Detail"][3].keys())[0],
                                       Event=list(Detail["Detail"][3].values())[0])
    def Review_End(cls, sn):
        logger.log_info("Skin Mall has showed ", \
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
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[17]').click()
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.living.store:id/rv_list"]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]').click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(3, 5))


    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(Detail["Detail"][4].keys())[0],
                                       Event=list(Detail["Detail"][4].values())[0])
    def Buy_Click(cls, sn):
        logger.log_info("Skin Mall has showed ", \
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
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[17]').click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/tv_name", text="freeman0316").click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/rl_bottom").click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(Detail["Detail"][5].keys())[0],
                                       Event=list(Detail["Detail"][5].values())[0])
    def BuyBack_Click(cls, sn):
        logger.log_info("Skin Mall has showed ", \
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
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[17]').click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/tv_name", text="freeman0316").click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/rl_bottom").click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(Detail["Detail"][9].keys())[0],
                                       Event=list(Detail["Detail"][9].values())[0])
    def author(cls, sn):
        logger.log_info("Skin Mall has showed ", \
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
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[17]').click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/tv_name", text="freeman0316").click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/iv_avatar").click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(Detail["Detail"][14].keys())[0],
                                       Event=list(Detail["Detail"][14].values())[0])
    def Use_Click(cls, sn):
        logger.log_info("Skin Mall has showed ", \
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
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[17]').click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/tv_name", text="星空0316").click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/rl_bottom").click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(Detail["Detail"][15].keys())[0],
                                       Event=list(Detail["Detail"][15].values())[0])
    def UseDialog_Start(cls, sn):
        logger.log_info("Skin Mall has showed ", \
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
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[17]').click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/tv_name", text="星空0316").click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/rl_bottom").click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(Detail["Detail"][16].keys())[0],
                                       Event=list(Detail["Detail"][16].values())[0])
    def UseDialog_Click_Use(cls, sn):
        logger.log_info("Skin Mall has showed ", \
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
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[17]').click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/tv_name", text="星空0316").click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/rl_bottom").click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/btn_cancel").click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(Detail["Detail"][17].keys())[0],
                                       Event=list(Detail["Detail"][17].values())[0])
    def UseDialog_Click_Cancel(cls, sn):
        logger.log_info("Skin Mall has showed ", \
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
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[17]').click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/tv_name", text="星空0316").click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/rl_bottom").click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/btn_cancel").click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(Detail["Detail"][18].keys())[0],
                                       Event=list(Detail["Detail"][18].values())[0])
    def UseDialog_End(cls, sn):
        logger.log_info("Skin Mall has showed ", \
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
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[17]').click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/tv_name", text="星空0316").click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/rl_bottom").click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/btn_cancel").click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(Detail["Detail"][20].keys())[0],
                                       Event=list(Detail["Detail"][20].values())[0])
    def LifeCycle_End(cls, sn):
        logger.log_info("Skin Mall has showed ", \
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
        d.xpath('//*[@resource-id="com.wm.launcher:id/view_root"]/android.widget.ImageView[17]').click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/tv_name", text="星空0316").click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(3, 5))

class ConfirmOrder_(object):
    def __init__(self):
        pass

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(ConfirmOrder["ConfirmOrder"][0].keys())[0],
                                       Event=list(ConfirmOrder["ConfirmOrder"][0].values())[0])
    def LifeCycle_Start(cls, sn):
        logger.log_info("Skin Mall has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1,3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(3,5))
        d(resourceId="com.living.store:id/rl_bottom").click()
        time.sleep(random.randint(3,5))


    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(ConfirmOrder["ConfirmOrder"][1].keys())[0],
                                       Event=list(ConfirmOrder["ConfirmOrder"][1].values())[0])
    def Back(cls, sn):
        logger.log_info("Skin Mall has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1,3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(3,5))
        d(resourceId="com.living.store:id/rl_bottom").click()
        time.sleep(random.randint(3,5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(ConfirmOrder["ConfirmOrder"][2].keys())[0],
                                       Event=list(ConfirmOrder["ConfirmOrder"][2].values())[0])
    def Review_Start(cls, sn):
        logger.log_info("Skin Mall has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1,3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(3,5))
        d(resourceId="com.living.store:id/rl_bottom").click()
        time.sleep(random.randint(3,5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(ConfirmOrder["ConfirmOrder"][3].keys())[0],
                                       Event=list(ConfirmOrder["ConfirmOrder"][3].values())[0])
    def Review_End(cls, sn):
        logger.log_info("Skin Mall has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1,3))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(3,5))
        d(resourceId="com.living.store:id/rl_bottom").click()
        time.sleep(random.randint(3,5))


    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(ConfirmOrder["ConfirmOrder"][4].keys())[0],
                                       Event=list(ConfirmOrder["ConfirmOrder"][4].values())[0])
    def AliPay(cls, sn):
        logger.log_info("Skin Mall has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1,3))
        d(resourceId="com.living.store:id/rb_wxpay").click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/rb_alipay").click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(ConfirmOrder["ConfirmOrder"][5].keys())[0],
                                       Event=list(ConfirmOrder["ConfirmOrder"][5].values())[0])
    def WxPay(cls, sn):
        logger.log_info("Skin Mall has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.living.store:id/rb_wxpay").click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/rb_alipay").click()
        time.sleep(random.randint(3, 5))


    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(ConfirmOrder["ConfirmOrder"][6].keys())[0],
                                       Event=list(ConfirmOrder["ConfirmOrder"][6].values())[0])
    def SubmitOrder(cls, sn):
        logger.log_info("Skin Mall has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.living.store:id/btn_next").click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(ConfirmOrder["ConfirmOrder"][8].keys())[0],
                                       Event=list(ConfirmOrder["ConfirmOrder"][8].values())[0])
    def LifeCycle_End(cls, sn):
        logger.log_info("Skin Mall has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(3, 5))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/rl_bottom").click()
        time.sleep(random.randint(3, 5))

class QrCode_(object):
    def __init__(self):
        pass

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(QrCode["QrCode"][0].keys())[0],
                                       Event=list(QrCode["QrCode"][0].values())[0])
    def LifeCycle_Start(cls, sn):
        logger.log_info("Skin Mall has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1,3))
        d(resourceId="com.living.store:id/btn_next").click()
        time.sleep(random.randint(3,5))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(3,5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(QrCode["QrCode"][1].keys())[0],
                                       Event=list(QrCode["QrCode"][1].values())[0])
    def Back(cls, sn):
        logger.log_info("Skin Mall has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.living.store:id/btn_next").click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(QrCode["QrCode"][2].keys())[0],
                                       Event=list(QrCode["QrCode"][2].values())[0])
    def Review_Start(cls, sn):
        logger.log_info("Skin Mall has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.living.store:id/btn_next").click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(QrCode["QrCode"][3].keys())[0],
                                       Event=list(QrCode["QrCode"][3].values())[0])
    def Review_End(cls, sn):
        logger.log_info("Skin Mall has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1, 3))
        d(resourceId="com.living.store:id/btn_next").click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(QrCode["QrCode"][4].keys())[0],
                                       Event=list(QrCode["QrCode"][4].values())[0])
    def TimeOutDialog_Start(cls, sn):
        logger.log_info("Skin Mall has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1,3))
        d(resourceId="com.living.store:id/btn_next").click()
        time.sleep(random.randint(1,3))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(60,80))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(QrCode["QrCode"][5].keys())[0],
                                       Event=list(QrCode["QrCode"][5].values())[0])
    def TimeOutDialog_Click(cls, sn):
        logger.log_info("Skin Mall has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1,3))
        d(resourceId="com.living.store:id/btn_next").click()
        time.sleep(random.randint(1,3))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(60,80))
        d(resourceId="com.living.store:id/btn_positive").click()
        time.sleep(random.randint(5, 10))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(3, 5))


    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(QrCode["QrCode"][7].keys())[0],
                                       Event=list(QrCode["QrCode"][7].values())[0])
    def TimeOutDialog_End(cls, sn):
        logger.log_info("Skin Mall has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1,3))
        d(resourceId="com.living.store:id/btn_next").click()
        time.sleep(random.randint(1,3))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(60,80))
        d(resourceId="com.living.store:id/btn_positive").click()
        time.sleep(random.randint(5, 10))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(3, 5))


    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(QrCode["QrCode"][7].keys())[0],
                                       Event=list(QrCode["QrCode"][7].values())[0])
    def PayClose(cls, sn):
        logger.log_info("Skin Mall has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1,3))
        d(resourceId="com.living.store:id/btn_next").click()
        time.sleep(random.randint(1,3))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(60,80))
        d(resourceId="com.living.store:id/btn_positive").click()
        time.sleep(random.randint(5, 10))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(QrCode["QrCode"][11].keys())[0],
                                       Event=list(QrCode["QrCode"][11].values())[0])
    def LifeCycle_End(cls, sn):
        logger.log_info("Skin Mall has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(1,3))
        d(resourceId="com.living.store:id/btn_next").click()
        time.sleep(random.randint(3,5))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(3,5))

class Feedback_(object):
    def __init__(self):
        pass

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(Feedback["Feedback"][0].keys())[0],
                                       Event=list(Feedback["Feedback"][0].values())[0])
    def LifeCycle_Start(cls, sn):
        logger.log_info("Skin Mall has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(60, 80))
        Check_Result.delete_tracker_log(sn)
        d(resourceId="com.living.store:id/btn_negative").click()
        time.sleep(random.randint(3,5))


    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(Feedback["Feedback"][1].keys())[0],
                                       Event=list(Feedback["Feedback"][1].values())[0])
    def Back(cls, sn):
        logger.log_info("Skin Mall has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(60, 80))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3,5))
        d(resourceId="com.living.store:id/btn_negative").click()
        time.sleep(random.randint(3,5))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(Feedback["Feedback"][2].keys())[0],
                                       Event=list(Feedback["Feedback"][2].values())[0])
    def Review_Start(cls, sn):
        logger.log_info("Skin Mall has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(60, 80))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/btn_negative").click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(Feedback["Feedback"][3].keys())[0],
                                       Event=list(Feedback["Feedback"][3].values())[0])
    def Review_End(cls, sn):
        logger.log_info("Skin Mall has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(60, 80))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/btn_negative").click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(Feedback["Feedback"][4].keys())[0],
                                       Event=list(Feedback["Feedback"][4].values())[0])
    def LifeCycle_End(cls, sn):
        logger.log_info("Skin Mall has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(60, 80))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/btn_negative").click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(3, 5))

class Author_(object):
    def __init__(self):
        pass

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(Author["Author"][0].keys())[0],
                                       Event=list(Author["Author"][0].values())[0])
    def LifeCycle_Start(cls, sn):
        logger.log_info("Skin Mall has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(3,5))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3,5))
        d(resourceId="com.living.store:id/tv_author").click()
        time.sleep(random.randint(5,7))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(Author["Author"][1].keys())[0],
                                       Event=list(Author["Author"][1].values())[0])
    def Back(cls, sn):
        logger.log_info("Skin Mall has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(3, 5))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/tv_author").click()
        time.sleep(random.randint(5, 7))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(5, 7))


    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(Author["Author"][2].keys())[0],
                                       Event=list(Author["Author"][2].values())[0])
    def AuthorBack(cls, sn):
        logger.log_info("Skin Mall has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(3, 5))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/tv_author").click()
        time.sleep(random.randint(5, 7))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(5, 7))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(Author["Author"][3].keys())[0],
                                       Event=list(Author["Author"][3].values())[0])
    def Review_Start(cls, sn):
        logger.log_info("Skin Mall has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(3, 5))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/tv_author").click()
        time.sleep(random.randint(5, 7))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(5, 7))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(Author["Author"][4].keys())[0],
                                       Event=list(Author["Author"][4].values())[0])
    def Review_End(cls, sn):
        logger.log_info("Skin Mall has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(3, 5))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/tv_author").click()
        time.sleep(random.randint(5, 7))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(5, 7))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(Author["Author"][5].keys())[0],
                                       Event=list(Author["Author"][5].values())[0])
    def SkinItem(cls, sn):
        logger.log_info("Skin Mall has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(3, 5))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/tv_author").click()
        time.sleep(random.randint(5, 7))
        d.xpath('//*[@resource-id="com.living.store:id/rv_list"]/android.widget.RelativeLayout[1]').click()
        time.sleep(random.randint(5, 7))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(5, 7))


    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(Author["Author"][6].keys())[0],
                                       Event=list(Author["Author"][6].values())[0])
    def LifeCycle_End(cls, sn):
        logger.log_info("Skin Mall has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(3, 5))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/tv_author").click()
        time.sleep(random.randint(5, 7))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(5, 7))

class Order_(object):
    def __init__(self):
        pass

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(Order["Order"][0].keys())[0],
                                       Event=list(Order["Order"][0].values())[0])
    def LifeCycle_Start(cls, sn):
        logger.log_info("Skin Mall has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(3, 5))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/btn_order").click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(Order["Order"][1].keys())[0],
                                       Event=list(Order["Order"][1].values())[0])
    def Back(cls, sn):
        logger.log_info("Skin Mall has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(3, 5))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/btn_order").click()
        time.sleep(random.randint(5, 7))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(3, 5))


    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(Order["Order"][2].keys())[0],
                                       Event=list(Order["Order"][2].values())[0])
    def Review_Start(cls, sn):
        logger.log_info("Skin Mall has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(3, 5))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/btn_order").click()
        time.sleep(random.randint(5, 7))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(Order["Order"][3].keys())[0],
                                       Event=list(Order["Order"][3].values())[0])
    def Review_End(cls, sn):
        logger.log_info("Skin Mall has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(3, 5))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/btn_order").click()
        time.sleep(random.randint(5, 7))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(Order["Order"][4].keys())[0],
                                       Event=list(Order["Order"][4].values())[0])
    def TabAll(cls, sn):
        logger.log_info("Skin Mall has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(3, 5))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/btn_order").click()
        time.sleep(random.randint(5, 7))
        d(resourceId="com.living.store:id/rb_payment").click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/rb_all").click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(Order["Order"][5].keys())[0],
                                       Event=list(Order["Order"][5].values())[0])
    def TabPayment(cls, sn):
        logger.log_info("Skin Mall has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(3, 5))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/btn_order").click()
        time.sleep(random.randint(5, 7))
        d(resourceId="com.living.store:id/rb_payment").click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/rb_all").click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(Order["Order"][6].keys())[0],
                                       Event=list(Order["Order"][6].values())[0])
    def TabPaymented(cls, sn):
        logger.log_info("Skin Mall has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(3, 5))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/btn_order").click()
        time.sleep(random.randint(5, 7))
        d(resourceId="com.living.store:id/rb_paymented").click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(Order["Order"][7].keys())[0],
                                       Event=list(Order["Order"][7].values())[0])
    def OrderItem(cls, sn):
        logger.log_info("Skin Mall has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(3, 5))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/btn_order").click()
        time.sleep(random.randint(5, 7))
        d.xpath('//*[@resource-id="com.living.store:id/rv_list"]/android.widget.LinearLayout[1]').click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(Order["Order"][8].keys())[0],
                                       Event=list(Order["Order"][8].values())[0])
    def Refresh(cls, sn):
        logger.log_info("Skin Mall has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(3, 5))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/btn_order").click()
        time.sleep(random.randint(5, 7))
        os.system('adb -s %s shell "input swipe 400 400 400 1400"' %(sn))
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(Order["Order"][9].keys())[0],
                                       Event=list(Order["Order"][9].values())[0])
    def LoadMore(cls, sn):
        logger.log_info("Skin Mall has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(3, 5))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/btn_order").click()
        time.sleep(random.randint(5, 7))
        os.system('adb -s %s shell "input swipe 400 1400 400 400"' %(sn))
        time.sleep(random.randint(3, 5))
        os.system('adb -s %s shell "input swipe 400 1400 400 400"' % (sn))
        time.sleep(random.randint(3, 5))
        os.system('adb -s %s shell "input swipe 400 1400 400 400"' % (sn))
        time.sleep(random.randint(3, 5))
        os.system('adb -s %s shell "input swipe 400 1400 400 400"' % (sn))
        time.sleep(random.randint(3, 5))


    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(Order["Order"][10].keys())[0],
                                       Event=list(Order["Order"][10].values())[0])
    def LifeCycle_End(cls, sn):
        logger.log_info("Skin Mall has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(3, 5))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/btn_order").click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(3, 5))

class OrderDetail_(object):
    def __init__(self):
        pass

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(OrderDetail["OrderDetail"][0].keys())[0],
                                       Event=list(OrderDetail["OrderDetail"][0].values())[0])
    def LifeCycle_Start(cls, sn):
        logger.log_info("Skin Mall has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(3, 5))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.living.store:id/rv_list"]/android.widget.LinearLayout[1]').click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(OrderDetail["OrderDetail"][1].keys())[0],
                                       Event=list(OrderDetail["OrderDetail"][1].values())[0])
    def Back(cls, sn):
        logger.log_info("Skin Mall has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(3, 5))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.living.store:id/rv_list"]/android.widget.LinearLayout[1]').click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(OrderDetail["OrderDetail"][2].keys())[0],
                                       Event=list(OrderDetail["OrderDetail"][2].values())[0])
    def Review_Start(cls, sn):
        logger.log_info("Skin Mall has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(3, 5))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.living.store:id/rv_list"]/android.widget.LinearLayout[1]').click()
        time.sleep(random.randint(3, 5))


    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(OrderDetail["OrderDetail"][3].keys())[0],
                                       Event=list(OrderDetail["OrderDetail"][3].values())[0])
    def Review_End(cls, sn):
        logger.log_info("Skin Mall has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(3, 5))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.living.store:id/rv_list"]/android.widget.LinearLayout[1]').click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(OrderDetail["OrderDetail"][4].keys())[0],
                                       Event=list(OrderDetail["OrderDetail"][4].values())[0])
    def SkinClick(cls, sn):
        logger.log_info("Skin Mall has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(3, 5))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.living.store:id/rv_list"]/android.widget.LinearLayout[1]').click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/iv_thumbnail").click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(OrderDetail["OrderDetail"][5].keys())[0],
                                       Event=list(OrderDetail["OrderDetail"][5].values())[0])
    def Pay(cls, sn):
        logger.log_info("Skin Mall has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(3, 5))
        Check_Result.delete_tracker_log(sn)
        d(resourceId="com.living.store:id/rb_payment").click()
        time.sleep(random.randint(3,5))
        d.xpath('//*[@resource-id="com.living.store:id/rv_list"]/android.widget.LinearLayout[1]').click()
        time.sleep(random.randint(3,5))
        d(resourceId="com.living.store:id/btn_buy").click()
        time.sleep(random.randint(3,5))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(3,5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(OrderDetail["OrderDetail"][6].keys())[0],
                                       Event=list(OrderDetail["OrderDetail"][6].values())[0])
    def PayBack(cls, sn):
        logger.log_info("Skin Mall has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(3, 5))
        Check_Result.delete_tracker_log(sn)
        d(resourceId="com.living.store:id/rb_payment").click()
        time.sleep(random.randint(3,5))
        d.xpath('//*[@resource-id="com.living.store:id/rv_list"]/android.widget.LinearLayout[1]').click()
        time.sleep(random.randint(3,5))
        d(resourceId="com.living.store:id/btn_buy").click()
        time.sleep(random.randint(3,5))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(3,5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(OrderDetail["OrderDetail"][7].keys())[0],
                                       Event=list(OrderDetail["OrderDetail"][7].values())[0])
    def CancelOrder(cls, sn):
        logger.log_info("Skin Mall has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(3, 5))
        Check_Result.delete_tracker_log(sn)
        d(resourceId="com.living.store:id/rb_payment").click()
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.living.store:id/rv_list"]/android.widget.LinearLayout[1]').click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/btn_cancel").click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/btn_negative").click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(OrderDetail["OrderDetail"][9].keys())[0],
                                       Event=list(OrderDetail["OrderDetail"][9].values())[0])
    def CancelDialog(cls, sn):
        logger.log_info("Skin Mall has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(3, 5))
        Check_Result.delete_tracker_log(sn)
        d(resourceId="com.living.store:id/rb_payment").click()
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.living.store:id/rv_list"]/android.widget.LinearLayout[1]').click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/btn_cancel").click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/btn_negative").click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(OrderDetail["OrderDetail"][10].keys())[0],
                                       Event=list(OrderDetail["OrderDetail"][10].values())[0])
    def CancelDialog_End(cls, sn):
        logger.log_info("Skin Mall has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(3, 5))
        Check_Result.delete_tracker_log(sn)
        d(resourceId="com.living.store:id/rb_payment").click()
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.living.store:id/rv_list"]/android.widget.LinearLayout[1]').click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/btn_cancel").click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/btn_negative").click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(OrderDetail["OrderDetail"][13].keys())[0],
                                       Event=list(OrderDetail["OrderDetail"][13].values())[0])
    def DeleteOrder(cls, sn):
        logger.log_info("Skin Mall has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(3, 5))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.living.store:id/rv_list"]/android.widget.LinearLayout[1]').click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/btn_del").click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/btn_negative").click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(OrderDetail["OrderDetail"][14].keys())[0],
                                       Event=list(OrderDetail["OrderDetail"][14].values())[0])
    def DeleteDialog_Start(cls, sn):
        logger.log_info("Skin Mall has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(3, 5))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.living.store:id/rv_list"]/android.widget.LinearLayout[1]').click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/btn_del").click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/btn_negative").click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(OrderDetail["OrderDetail"][16].keys())[0],
                                       Event=list(OrderDetail["OrderDetail"][16].values())[0])
    def DeleteDialog_Cancel(cls, sn):
        logger.log_info("Skin Mall has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(3, 5))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.living.store:id/rv_list"]/android.widget.LinearLayout[1]').click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/btn_del").click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.living.store:id/btn_negative").click()
        time.sleep(random.randint(3, 5))

    @classmethod
    @Check_Skin_Mall_Actions.check_log(Action=list(OrderDetail["OrderDetail"][19].keys())[0],
                                       Event=list(OrderDetail["OrderDetail"][19].values())[0])
    def LifeCycle_End(cls, sn):
        logger.log_info("Skin Mall has showed ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        d = u2.connect(sn)
        logger.log_debug(d.info, \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno)
        time.sleep(random.randint(3, 5))
        Check_Result.delete_tracker_log(sn)
        time.sleep(random.randint(3, 5))
        d.xpath('//*[@resource-id="com.living.store:id/rv_list"]/android.widget.LinearLayout[1]').click()
        time.sleep(random.randint(3, 5))
        d(resourceId="com.android.systemui:id/status_bar_back").click()
        time.sleep(random.randint(3, 5))





























