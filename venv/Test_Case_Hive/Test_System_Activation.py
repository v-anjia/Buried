'''
Case System Activation Test Suite
author : antony WeiJiang
date:2020/3/17
'''

import pytest
import sys
import os
import time
import random
import pytest_html.extras
import pytest_html.hooks
import pytest_html.plugin
import subprocess
from Common import System_Activation as set
from Common import Common as co
from log import  logger as loger
from Common import Hive_Connect as hc
# print(list(set.Setting_Actions["settings"][3].keys())[0])

logger = loger.Current_Module()

adb_object = co.ADB_SN()

vin_number = co.Install_Package().update_fota_package()[3]

date_time = co.Install_Package().update_fota_package()[5]

sn = adb_object.check_adb_device_isalive()
set.Action.set_sn(sn)
start_step = 2
end_step = 2

buried_log = '/update/buried_System_Activation.log'
buried_point = "/sdcard/Android/data/com.wm.tracker/files/temp/*"

save_data = "/update/buried_local_System_Activation.log"
busybox = "/yf/bin/busybox"
LOG_PATH = 'logcat -v time |grep -iE \".*wmTracker.*EventModel.*\" |grep -v "clientSendMessage" >> %s &' %(buried_log)
Delete_Log = 'rm -rf %s' %(buried_log)
logcat_pid_exist = "ps |grep logcat | %s awk \'{print $2}\' |%s xargs kill -9 " %(busybox,busybox)
hc_object = hc.hive_connect()
hc_connect = hc_object.connect()

def Save_TempData(sn,temp_file,save_file):
    logger.log_info("save data to /update/ directory", \
                    sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                    sys._getframe().f_lineno)
    os.system('adb -s %s shell "cat %s >> %s"' %(sn,temp_file,save_file))

def Common(count, action, event, page,function_name= [], flag = 1):
    try:
        logger.log_info("start test %s  function,total count is %s" % (function_name.__name__ , count), \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                        sys._getframe().f_lineno
                        )
        function_name(set.Action.get_sn())
        time.sleep(0.5)
        Save_TempData(set.Action.get_sn(),buried_point,save_data)
        time.sleep(random.randint(55,60))
    except Exception as e:
        logger.log_error("%s" % (e), \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                         sys._getframe().f_lineno)

def total_local_data(action, event, page):
    cmd = 'cat %s|grep %s |grep %s|grep %s|%s wc -l' %(buried_log,page,action,event,busybox)
    logger.log_info("start collect pagename : %s action : %s  event: %s times" %(page,action,event), \
                    sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                    sys._getframe().f_lineno)
    result = subprocess.check_output('adb -s %s shell "%s"' %(set.Action.get_sn(),cmd), shell=True)
    result = co.removal(result)
    logger.log_debug("local data is : %s" %(result), \
                     sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                     sys._getframe().f_lineno)
    return result

def total_hive_data(action, event, page):
    logger.log_info("start collect hive data", \
                    sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                    sys._getframe().f_lineno)
    time.sleep(3)
    # print(date_time)
    # print(vin_number)
    result = hc_object.execute_sql(hc_connect, date_time, vin_number, page, action, event)
    logger.log_debug("hive data is : %s" %(result), \
                     sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                     sys._getframe().f_lineno)
    return result

def Compare(action, event, page):
    if int(total_hive_data(action,event,page)) == int(total_local_data(action,event,page)):
        assert True

    else:
        assert False

# class Test_Collect_Buried_Log():
#     @pytest.mark.parametrize('sn',
#                              [set.Action.get_sn()])
#     def test_collect_buired_result(self,sn):
#         logger.log_info("setting root partition read and write", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         os.system('adb root')
#         time.sleep(random.randint(3,5))
#         os.system('adb -s %s shell "mount -o rw,remount /" ' %(sn))
#         time.sleep(random.randint(3,5))
#         cmd = 'adb -s %s shell "%s"' %(sn, LOG_PATH)
#         logger.log_info("execute cmd is :%s" %(cmd), \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         p_sub = subprocess.Popen(cmd,shell= True)
#         time.sleep(random.randint(3,5))

class Test_Activate_Page():
    @pytest.fixture(scope='function', autouse=True)
    def message(self):
        '''check test environment'''
        logger.log_info("start Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                        sys._getframe().f_lineno)
        logger.log_info("modify flag.json file ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                        sys._getframe().f_lineno)
        os.system("adb root")
        set.Action.modify_json_file(set.Action.get_sn())
        time.sleep(random.randint(1,3))
        # if set.Check_Result.deltet_lvlog(set.Action.get_sn()):
        #     logger.log_info("delete lvlog successfully", \
        #                     sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
        #                     sys._getframe().f_lineno)
        if set.Check_Result.delete_tracker_log(set.Action.get_sn()):
            logger.log_info("delete tracker successfully", \
                            sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                            sys._getframe().f_lineno)
        set.Action.wait_system_activation_page(set.Action.get_sn())
        logger.log_info("setting root partition read and write", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                        sys._getframe().f_lineno)
        os.system('adb root')
        time.sleep(random.randint(3,5))
        os.system('adb -s %s shell "mount -o rw,remount /" ' %(set.Action.get_sn()))
        time.sleep(random.randint(3,5))
        cmd = 'adb -s %s shell "%s"' %(set.Action.get_sn(), LOG_PATH)
        logger.log_info("execute cmd is :%s" %(cmd), \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                        sys._getframe().f_lineno)
        p_sub = subprocess.Popen(cmd,shell= True)
        time.sleep(random.randint(5,8))
        yield
        logger.log_info("end Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                        sys._getframe().f_lineno)
        os.system("adb root")
        time.sleep(random.randint(1,3))

    @pytest.mark.parametrize('count,action,event,page',[(random.randint(start_step,end_step),list(set.Activate_Page["Activate_Page"][0].keys())[0],\
                                                    list(set.Activate_Page["Activate_Page"][0].values())[0],list(set.Activate_Page.keys())[0])])
    def test_PageDisplay_Start(self, count, action, event,page):
        Common(count, action, event, page,set.Activate_Page_.PageDisplay_Start)


    @pytest.mark.parametrize('count,action,event,page',[(random.randint(start_step,end_step),list(set.Activate_Page["Activate_Page"][1].keys())[0],\
                                                    list(set.Activate_Page["Activate_Page"][1].values())[0],list(set.Activate_Page.keys())[0])])
    def test_PageDisplay_End(self, count, action, event,page):
        Common(count, action, event, page,set.Activate_Page_.PageDisplay_End)

    @pytest.mark.parametrize('count,action,event,page', [
        (random.randint(start_step, end_step), list(set.Activate_Page["Activate_Page"][2].keys())[0], \
         list(set.Activate_Page["Activate_Page"][2].values())[0],list(set.Activate_Page.keys())[0])])
    def test_Get_Download_QR_Code_Click(self, count, action, event,page):
        Common(count, action, event, page,set.Activate_Page_.Get_Download_QR_Code_Click)

    @pytest.mark.parametrize('count,action,event,page', [
        (random.randint(start_step, end_step), list(set.Activate_Page["Activate_Page"][3].keys())[0], \
         list(set.Activate_Page["Activate_Page"][3].values())[0],list(set.Activate_Page.keys())[0])])
    def test_Activate_Click(self, count, action, event,page):
        Common(count, action, event,page, set.Activate_Page_.Activate_Click)

    @pytest.mark.parametrize('count,action,event,page', [
        (random.randint(start_step, end_step), list(set.Activate_Page["Activate_Page"][4].keys())[0], \
         list(set.Activate_Page["Activate_Page"][4].values())[0],list(set.Activate_Page.keys())[0])])
    def test_Close_QR_Code_Click(self, count, action, event,page):
        Common(count, action, event,page, set.Activate_Page_.Close_QR_Code_Click)


class Test_Welcome_Page():
    @pytest.fixture(scope='function', autouse=True)
    def message(self):
        '''check test environment'''
        logger.log_info("start Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                        sys._getframe().f_lineno)
        logger.log_info("modify flag.json file ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                        sys._getframe().f_lineno)
        os.system("adb root")
        set.Action.modify_json_file(set.Action.get_sn())
        time.sleep(random.randint(1,3))
        # if set.Check_Result.deltet_lvlog(set.Action.get_sn()):
        #     logger.log_info("delete lvlog successfully", \
        #                     sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
        #                     sys._getframe().f_lineno)
        # if set.Check_Result.delete_tracker_log(set.Action.get_sn()):
        #     logger.log_info("delete tracker successfully", \
        #                     sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
        #                     sys._getframe().f_lineno)
        set.Action.wait_system_activation_page(set.Action.get_sn())

        logger.log_info("setting root partition read and write", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                        sys._getframe().f_lineno)
        os.system('adb root')
        time.sleep(random.randint(3,5))
        os.system('adb -s %s shell "mount -o rw,remount /" ' %(set.Action.get_sn()))
        time.sleep(random.randint(3,5))
        cmd = 'adb -s %s shell "%s"' %(set.Action.get_sn(), LOG_PATH)
        logger.log_info("execute cmd is :%s" %(cmd), \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                        sys._getframe().f_lineno)
        p_sub = subprocess.Popen(cmd,shell= True)
        time.sleep(random.randint(5,8))
        yield
        logger.log_info("end Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                        sys._getframe().f_lineno)
        os.system("adb root")
        time.sleep(random.randint(1,3))

    @pytest.mark.parametrize('count,action,event,page', [
        (random.randint(start_step, end_step), list(set.Welcome_Page["Welcome_Page"][0].keys())[0], \
         list(set.Welcome_Page["Welcome_Page"][0].values())[0],list(set.Welcome_Page.keys())[0])])
    def test_PageDisplay_Start(self, count, action, event, page):
        Common(count, action, event, page,set.Welcome_Page_.PageDisplay_Start)

    @pytest.mark.parametrize('count,action,event,page', [
        (random.randint(start_step, end_step), list(set.Welcome_Page["Welcome_Page"][1].keys())[0], \
         list(set.Welcome_Page["Welcome_Page"][1].values())[0],list(set.Welcome_Page.keys())[0])])
    def test_PageDisplay_End(self, count, action, event,page):
        Common(count, action, event, page,set.Welcome_Page_.PageDisplay_End)

    @pytest.mark.parametrize('count,action,event,page', [
        (random.randint(start_step, end_step), list(set.Welcome_Page["Welcome_Page"][2].keys())[0], \
         list(set.Welcome_Page["Welcome_Page"][2].values())[0],list(set.Welcome_Page.keys())[0])])
    def test_Disclaimer_Page_Click(self, count, action, event,page):
        Common(count, action, event, page,set.Welcome_Page_.Disclaimer_Page_Click)


    @pytest.mark.parametrize('count,action,event,page', [
        (random.randint(start_step, end_step), list(set.Welcome_Page["Welcome_Page"][3].keys())[0], \
         list(set.Welcome_Page["Welcome_Page"][3].values())[0],list(set.Welcome_Page.keys())[0])])
    def test_Disclaimer_Agree_Select(self, count, action, event,page):
        Common(count, action, event, page,set.Welcome_Page_.Disclaimer_Agree_Select)

    @pytest.mark.parametrize('count,action,event,page', [
        (random.randint(start_step, end_step), list(set.Welcome_Page["Welcome_Page"][4].keys())[0], \
         list(set.Welcome_Page["Welcome_Page"][4].values())[0],list(set.Welcome_Page.keys())[0])])
    def test_Confirm_Click(self, count, action, event,page):
        Common(count, action, event, page,set.Welcome_Page_.Confirm_Click)


class Test_Disclaimer_Page():
    @pytest.fixture(scope='function', autouse=True)
    def message(self):
        '''check test environment'''
        logger.log_info("start Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                        sys._getframe().f_lineno)
        logger.log_info("modify flag.json file ", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                        sys._getframe().f_lineno)
        os.system("adb root")
        set.Action.modify_json_file(set.Action.get_sn())
        time.sleep(random.randint(1,3))
        # if set.Check_Result.deltet_lvlog(set.Action.get_sn()):
        #     logger.log_info("delete lvlog successfully", \
        #                     sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
        #                     sys._getframe().f_lineno)
        # if set.Check_Result.delete_tracker_log(set.Action.get_sn()):
        #     logger.log_info("delete tracker successfully", \
        #                     sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
        #                     sys._getframe().f_lineno)
        set.Action.wait_system_activation_page(set.Action.get_sn())

        logger.log_info("setting root partition read and write", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                        sys._getframe().f_lineno)
        os.system('adb root')
        time.sleep(random.randint(3,5))
        os.system('adb -s %s shell "mount -o rw,remount /" ' %(set.Action.get_sn()))
        time.sleep(random.randint(3,5))
        cmd = 'adb -s %s shell "%s"' %(set.Action.get_sn(), LOG_PATH)
        logger.log_info("execute cmd is :%s" %(cmd), \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                        sys._getframe().f_lineno)
        p_sub = subprocess.Popen(cmd,shell= True)
        time.sleep(random.randint(5,8))
        yield
        logger.log_info("end Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                        sys._getframe().f_lineno)
        os.system("adb root")
        time.sleep(random.randint(1,3))

    @pytest.mark.parametrize('count,action,event,page', [
        (random.randint(start_step, end_step), list(set.Disclaimer_Page["Disclaimer_Page"][0].keys())[0], \
         list(set.Disclaimer_Page["Disclaimer_Page"][0].values())[0],list(set.Disclaimer_Page.keys())[0])])
    def test_PageDisplay_Start(self, count, action, event,page):
        Common(count, action, event, page,set.Disclaimer_Page_.PageDisplay_Start)

    @pytest.mark.parametrize('count,action,event,page', [
        (random.randint(start_step, end_step), list(set.Disclaimer_Page["Disclaimer_Page"][1].keys())[0], \
         list(set.Disclaimer_Page["Disclaimer_Page"][1].values())[0],list(set.Disclaimer_Page.keys())[0])])
    def test_PageDisplay_End(self, count, action, event,page):
        Common(count, action, event, page,set.Disclaimer_Page_.PageDisplay_End)

    @pytest.mark.parametrize('count,action,event,page', [
        (random.randint(start_step, end_step), list(set.Disclaimer_Page["Disclaimer_Page"][2].keys())[0], \
         list(set.Disclaimer_Page["Disclaimer_Page"][2].values())[0],list(set.Disclaimer_Page.keys())[0])])
    def test_Back_Click(self, count, action, event,page):
        Common(count, action, event, page,set.Disclaimer_Page_.Back_Click)


class Test_Check_System_Activation_Hive_Result(object):

    @pytest.mark.parametrize('sn',[set.Action.get_sn()])
    def test_Kill_Buried_Progress(self,sn):
        logger.log_info("kill logcat collect log progress", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                        sys._getframe().f_lineno)
        os.system('adb -s %s shell "%s"' %(sn,logcat_pid_exist))
        time.sleep(7200)

    @pytest.mark.parametrize('action,event,page', [
        (list(set.Activate_Page["Activate_Page"][0].keys())[0], \
         list(set.Activate_Page["Activate_Page"][0].values())[0], list(set.Activate_Page.keys())[0])])
    def test_Activate_PageDisplay_Start(self, action, event, page):
        Compare(action, event, page)

    @pytest.mark.parametrize('action,event,page', [
        (list(set.Activate_Page["Activate_Page"][1].keys())[0], \
         list(set.Activate_Page["Activate_Page"][1].values())[0], list(set.Activate_Page.keys())[0])])
    def test_Activate_PageDisplay_End(self, action, event, page):
        Compare(action, event, page)

    @pytest.mark.parametrize('action,event,page', [
        (list(set.Activate_Page["Activate_Page"][2].keys())[0], \
         list(set.Activate_Page["Activate_Page"][2].values())[0], list(set.Activate_Page.keys())[0])])
    def test_Get_Download_QR_Code_Click(self, action, event, page):
        Compare(action, event, page)

    @pytest.mark.parametrize('action,event,page', [
        (list(set.Activate_Page["Activate_Page"][3].keys())[0], \
         list(set.Activate_Page["Activate_Page"][3].values())[0], list(set.Activate_Page.keys())[0])])
    def test_Activate_Click(self,action, event, page):
        Compare(action, event, page)

    @pytest.mark.parametrize('action,event,page', [
        (list(set.Activate_Page["Activate_Page"][4].keys())[0], \
         list(set.Activate_Page["Activate_Page"][4].values())[0], list(set.Activate_Page.keys())[0])])
    def test_Close_QR_Code_Click(self, count, action, event, page):
        Compare(action, event, page)

    @pytest.mark.parametrize('action,event,page', [
        (list(set.Welcome_Page["Welcome_Page"][0].keys())[0], \
         list(set.Welcome_Page["Welcome_Page"][0].values())[0], list(set.Welcome_Page.keys())[0])])
    def test_Welcome_Page_PageDisplay_Start(self, action, event, page):
        Compare(action, event, page)

    @pytest.mark.parametrize('action,event,page', [
        (list(set.Welcome_Page["Welcome_Page"][1].keys())[0], \
         list(set.Welcome_Page["Welcome_Page"][1].values())[0], list(set.Welcome_Page.keys())[0])])
    def test_Welcome_Page_PageDisplay_End(self, action, event, page):
        Compare(action, event, page)

    @pytest.mark.parametrize('action,event,page', [
        (list(set.Welcome_Page["Welcome_Page"][2].keys())[0], \
         list(set.Welcome_Page["Welcome_Page"][2].values())[0], list(set.Welcome_Page.keys())[0])])
    def test_Disclaimer_Page_Click(self, action, event, page):
        Compare(action, event, page)

    @pytest.mark.parametrize('action,event,page', [
        (list(set.Welcome_Page["Welcome_Page"][3].keys())[0], \
         list(set.Welcome_Page["Welcome_Page"][3].values())[0], list(set.Welcome_Page.keys())[0])])
    def test_Disclaimer_Agree_Select(self, action, event, page):
        Compare(action, event, page)

    @pytest.mark.parametrize('action,event,page', [
        (list(set.Welcome_Page["Welcome_Page"][4].keys())[0], \
         list(set.Welcome_Page["Welcome_Page"][4].values())[0], list(set.Welcome_Page.keys())[0])])
    def test_Confirm_Click(self, action, event, page):
        Compare(action, event, page)


# class Test_Delete_Buried_Log():
#     @pytest.mark.parametrize('sn',
#                              [set.Action.get_sn()])
#     def test_Delete_buired_log(self,sn):
#         logger.log_info("setting root partition read and write", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         os.system('adb root')
#         time.sleep(random.randint(3,5))
#         os.system('adb -s %s shell "mount -o rw,remount /" ' %(sn))
#         time.sleep(random.randint(3,5))
#         cmd = 'adb -s %s shell "%s"' %(sn,Delete_Log)
#         logger.log_info("execute cmd is :%s" %(cmd), \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         p_sub = subprocess.Popen(cmd,shell= True)
#         time.sleep(random.randint(3,5))








