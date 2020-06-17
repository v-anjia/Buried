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
from Common import System_Activation as set
from Common import Common as co
from log import  logger as loger
# print(list(set.Setting_Actions["settings"][3].keys())[0])
logger = loger.Current_Module()

adb_object = co.ADB_SN()

sn = adb_object.check_adb_device_isalive()
set.Action.set_sn(sn)
start_step = 2
end_step = 2
# # set.Action.set_ui_object(set.Action.get_sn())
# # uiautomator_object = set.Action.get_ui_object()
#
def Common(count, action, event, page,function_name= [], flag = 1):
    try:
        logger.log_info("start test %s  function,total count is %s" % (function_name.__name__ , count), \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                        sys._getframe().f_lineno
                        )
        Total = 0
        Passed = 0
        Failed = 0
        logger.log_info("cycle is %s" % (count), \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                        sys._getframe().f_lineno)
        for i in range(1, count, 1):
            # set.Check_Setting_Actions
            logger.log_debug("sn is :%s" % (set.Action.get_sn()), \
                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                             sys._getframe().f_lineno)
            function_name(set.Action.get_sn())
            # Result_lvlog = int(function_name(set.Action.get_sn()))
            Result_tracker = int(set.Check_Result.check_android_tracker_log(set.Action.get_sn(), action, event,page))
            if flag != 1:
                Result_tracker = Result_tracker / flag
            logger.log_info("Result_tracker is %s" %(Result_tracker), \
                            sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                            sys._getframe().f_lineno)
            print("Result_tracker is %s" %(Result_tracker))
            if i == Result_tracker:
                Passed = Passed + 1
            else:
                Failed = Failed + 1

        Total = Passed + Failed
        logger.log_debug("Total is :%s;Passed is :%s;Failed is :%s" % (Total, Passed, Failed), \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                         sys._getframe().f_lineno)
    except Exception as e:
        logger.log_error("%s" % (e), \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                         sys._getframe().f_lineno)
    if Passed == Total:
        logger.log_info("compare data successfully", \
                        sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                        sys._getframe().f_lineno)
        assert True
    else:
        logger.log_error("compare data fail", \
                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                         sys._getframe().f_lineno)
        assert False


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
        if set.Check_Result.delete_tracker_log(set.Action.get_sn()):
            logger.log_info("delete tracker successfully", \
                            sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                            sys._getframe().f_lineno)
        set.Action.wait_system_activation_page(set.Action.get_sn())
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
        if set.Check_Result.delete_tracker_log(set.Action.get_sn()):
            logger.log_info("delete tracker successfully", \
                            sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
                            sys._getframe().f_lineno)
        set.Action.wait_system_activation_page(set.Action.get_sn())
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

