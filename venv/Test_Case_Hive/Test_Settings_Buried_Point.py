# '''
# Case Settings Test Suite
# author : antony WeiJiang
# date:2020/1/7
# '''
# import pytest
# import sys
# import os
# import subprocess
# import time
# import random
# import pytest_html.extras
# import pytest_html.hooks
# import pytest_html.plugin
# from Common import Setting as set
# from Common import Common as co
# from log import  logger as loger
# from Common import Hive_Connect as hc
# # print(list(set.Setting_Actions["settings"][3].keys())[0])
# logger = loger.Current_Module()
# 
# adb_object = co.ADB_SN()
# 
# vin_number = co.Install_Package().update_fota_package()[3]
# 
# date_time = co.Install_Package().update_fota_package()[5]
# 
# sn = adb_object.check_adb_device_isalive()
# set.Action.set_sn(sn)
# start_step = 2
# end_step = 2
# 
# buried_log = '/update/buried_Settings.log'
# 
# buried_point = "/sdcard/Android/data/com.wm.tracker/files/temp/*"
# 
# save_data = "/update/buried_local_Settings.log"
# busybox = "/yf/bin/busybox"
# LOG_PATH = 'logcat -v time |grep -iE \".*wmTracker.*EventModel.*\" |grep -v "clientSendMessage" > %s &' %(buried_log)
# Delete_Log = 'rm -rf %s' %(buried_log)
# logcat_pid_exist = "ps |grep logcat | %s awk \'{print $2}\' |%s xargs kill -9 " %(busybox,busybox)
# hc_object = hc.hive_connect()
# hc_connect = hc_object.connect()
# 
# def Save_TempData(sn,temp_file,save_file):
#     logger.log_info("save data to /update/ directory", \
#                     sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                     sys._getframe().f_lineno)
#     os.system('adb -s %s shell "cat %s >> %s"' %(sn,temp_file,save_file))
# 
# def Common(count, action, event, page,function_name= [], flag = 1):
#     try:
#         logger.log_info("start test %s  function,total count is %s" % (function_name.__name__ , count), \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno
#                         )
#         function_name(set.Action.get_sn())
#         time.sleep(0.5)
#         Save_TempData(set.Action.get_sn(), buried_point, save_data)
#         time.sleep(random.randint(55, 60))
#     except Exception as e:
#         logger.log_error("%s" % (e), \
#                          sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                          sys._getframe().f_lineno)
# 
# def total_local_data(action, event, page):
#     cmd = 'cat %s|grep %s |grep %s|grep %s|%s wc -l' %(buried_log,page,action,event,busybox)
#     logger.log_info("start collect pagename : %s action : %s  event: %s times" %(page,action,event), \
#                     sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                     sys._getframe().f_lineno)
#     result = subprocess.check_output('adb -s %s shell "%s"' %(set.Action.get_sn(),cmd), shell=True)
#     result = co.removal(result)
#     logger.log_debug("local data is : %s" %(result), \
#                      sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                      sys._getframe().f_lineno)
#     return result
# 
# def total_hive_data(action, event, page):
#     logger.log_info("start collect hive data", \
#                     sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                     sys._getframe().f_lineno)
#     time.sleep(3)
#     # print(date_time)
#     # print(vin_number)
#     result = hc_object.execute_sql(hc_connect, date_time, vin_number, page, action, event)
#     logger.log_debug("hive data is : %s" %(result), \
#                      sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                      sys._getframe().f_lineno)
#     return result
# 
# def Compare(action, event, page):
#     if int(total_hive_data(action,event,page)) == int(total_local_data(action,event,page)):
#         assert True
# 
#     else:
#         assert False
# 
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
# 
# class Test_Settings_Buried_Point():
#     @pytest.fixture(scope='function', autouse=True)
#     def message(self):
#         '''check test environment'''
#         logger.log_info("start Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         logger.log_info("enter setting ui ", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.kill_setting()
#         time.sleep(random.randint(1,3))
#         # if set.Check_Result.deltet_lvlog(set.Action.get_sn()):
#         #     logger.log_info("delete lvlog successfully", \
#         #                     sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#         #                     sys._getframe().f_lineno)
#         # if set.Check_Result.delete_tracker_log(set.Action.get_sn()):
#         #     logger.log_info("delete tracker successfully", \
#         #                     sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#         #                     sys._getframe().f_lineno)
#         time.sleep(random.randint(3,5))
#         set.Action.enter_settings_ui()
#         time.sleep(random.randint(5,8))
#         yield
#         logger.log_info("kill setting progress", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.kill_setting()
#         logger.log_info("end Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Setting_Actions["settings"][15].keys())[0], \
#                                list(set.Setting_Actions["settings"][15].values())[0],
#                                None)])
#     def test_OpenApp(self, count, action, event, page):
#         Common(count, action, event, page, set.Setting_Actions_.OpenApp)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Setting_Actions["settings"][16].keys())[0], \
#                                list(set.Setting_Actions["settings"][16].values())[0],
#                                None)])
#     def test_Foreground_Start(self, count, action, event, page):
#         Common(count, action, event, page, set.Setting_Actions_.Foreground_Start)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Setting_Actions["settings"][17].keys())[0], \
#                                list(set.Setting_Actions["settings"][17].values())[0],
#                                None)])
#     def test_Foreground_End(self, count, action, event, page):
#         Common(count, action, event, page, set.Setting_Actions_.Foreground_End)
# 
#     @pytest.mark.parametrize('count,action,event,page',[(random.randint(start_step,end_step),list(set.Setting_Actions["settings"][0].keys())[0],\
#                                                     list(set.Setting_Actions["settings"][0].values())[0],list(set.Setting_Actions.keys())[0])])
#     def test_Back(self, count, action, event,page):
#         Common(count, action, event,page, set.Setting_Actions_.Back)
# 
# 
#     @pytest.mark.parametrize('count,action,event,page',[(random.randint(start_step,end_step),list(set.Setting_Actions["settings"][1].keys())[0],\
#                                                     list(set.Setting_Actions["settings"][1].values())[0],list(set.Setting_Actions.keys())[0])])
#     def test_PageDisplay_Start(self, count, action, event,page):
#         Common(count, action, event, page,set.Setting_Actions_.PageDisplay_Start)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Setting_Actions["settings"][2].keys())[0], \
#                                list(set.Setting_Actions["settings"][2].values())[0],list(set.Setting_Actions.keys())[0])])
#     def test_PageDisplay_End(self, count, action, event,page):
#         Common(count, action, event, page,set.Setting_Actions_.PageDisplay_End)
# 
# 
#     @pytest.mark.parametrize('count,action,event,page',[(random.randint(start_step,end_step),list(set.Setting_Actions["settings"][3].keys())[0],\
#                                                     list(set.Setting_Actions["settings"][3].values())[0],list(set.Setting_Actions.keys())[0])])
#     def test_Open_WIFI(self, count, action, event,page):
#         Common(count, action, event, page,set.Setting_Actions_.Open_WIFI)
# 
# 
#     @pytest.mark.parametrize('count,action,event,page',[(random.randint(start_step,end_step),list(set.Setting_Actions["settings"][4].keys())[0],\
#                                                     list(set.Setting_Actions["settings"][4].values())[0],list(set.Setting_Actions.keys())[0])])
#     def test_OpenBluetooth(self, count, action, event,page):
#         Common(count, action, event, page,set.Setting_Actions_.OpenBluetooth)
# 
#     '''because of not choose'''
#     @pytest.mark.parametrize('count,action,event,page',[(random.randint(start_step, end_step), list(set.Setting_Actions["settings"][5].keys())[0], \
#                                                     list(set.Setting_Actions["settings"][5].values())[0],list(set.Setting_Actions.keys())[0])])
#     def test_WirelessCharging(self, count, action, event,page):
#         Common(count, action, event, page,set.Setting_Actions_.WirelessCharging)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Setting_Actions["settings"][6].keys())[0], \
#                                list(set.Setting_Actions["settings"][6].values())[0],list(set.Setting_Actions.keys())[0])])
#     def test_PrivacyMode(self, count, action, event,page):
#         Common(count, action, event, page,set.Setting_Actions_.PrivacyMode)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Setting_Actions["settings"][7].keys())[0], \
#                                list(set.Setting_Actions["settings"][7].values())[0],list(set.Setting_Actions.keys())[0])])
#     def test_ClickUser(self, count, action, event,page):
#         Common(count, action, event, page,set.Setting_Actions_.ClickUser)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Setting_Actions["settings"][8].keys())[0], \
#                                list(set.Setting_Actions["settings"][8].values())[0],list(set.Setting_Actions.keys())[0])])
#     def test_ClickBluetooth(self, count, action, event,page):
#         Common(count, action, event, page,set.Setting_Actions_.ClickBluetooth)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Setting_Actions["settings"][9].keys())[0], \
#                                list(set.Setting_Actions["settings"][9].values())[0],list(set.Setting_Actions.keys())[0])])
#     def test_ClickWIFI(self, count, action, event,page):
#         Common(count, action, event, page, set.Setting_Actions_.ClickWIFI)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Setting_Actions["settings"][10].keys())[0], \
#                                list(set.Setting_Actions["settings"][10].values())[0],list(set.Setting_Actions.keys())[0])])
#     def test_ClickPrivacy(self, count, action, event,page):
#         Common(count, action, event, page,set.Setting_Actions_.ClickPrivacy)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Setting_Actions["settings"][11].keys())[0], \
#                                list(set.Setting_Actions["settings"][11].values())[0],list(set.Setting_Actions.keys())[0])])
#     def test_ClickVoice(self, count, action, event,page):
#         Common(count, action, event, page, set.Setting_Actions_.ClickVoice)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Setting_Actions["settings"][12].keys())[0], \
#                                list(set.Setting_Actions["settings"][12].values())[0],list(set.Setting_Actions.keys())[0])])
#     def test_ClickVolume(self, count, action, event, page):
#         Common(count, action, event, page,set.Setting_Actions_.ClickVolume)
# 
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Setting_Actions["settings"][13].keys())[0], \
#                                list(set.Setting_Actions["settings"][13].values())[0],list(set.Setting_Actions.keys())[0])])
#     def test_ClickCurrency(self, count, action, event,page):
#         Common(count, action, event, page,set.Setting_Actions_.ClickCurrency)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Setting_Actions["settings"][14].keys())[0], \
#                                list(set.Setting_Actions["settings"][14].values())[0],list(set.Setting_Actions.keys())[0])])
#     def test_ClickSystem(self, count, action, event,page):
#         Common(count, action, event, page,set.Setting_Actions_.ClickSystem)
# 
# class Test_WMPrivacySettings():
#     @pytest.fixture(scope='function', autouse=True)
#     def message(self):
#         '''check test environment'''
#         logger.log_info("start Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         logger.log_info("enter setting ui ", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.kill_setting()
#         time.sleep(random.randint(1, 3))
#         # if set.Check_Result.delete_lvlog(set.Action.get_sn()):
#         #     logger.log_info("delete lvlog successfully", \
#         #                     sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#         #                     sys._getframe().f_lineno)
#         logger.log_info("Enter settings ui", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.enter_settings_ui()
#         '''enter privacy page'''
#         logger.log_info("Enter privacy page", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.enter_privacy(set.Action.get_sn())
#         time.sleep(random.randint(3, 5))
# 
#         # if set.Check_Result.delete_tracker_log(set.Action.get_sn()):
#         #     logger.log_info("delete tracker successfully", \
#         #                     sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#         #                     sys._getframe().f_lineno)
# 
#         time.sleep(random.randint(3, 5))
#         yield
#         logger.log_info("kill setting progress", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.kill_setting()
#         time.sleep(random.randint(1, 3))
#         set.Action.kill_setting()
#         logger.log_info("end Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMPrivacySettings["WMPrivacySettings"][0].keys())[0], \
#                                                      list(set.WMPrivacySettings["WMPrivacySettings"][0].values())[
#                                                          0],list(set.WMPrivacySettings.keys())[0])])
#     def test_PageDisplay_Start(self, count, action, event,page):
#         Common(count, action, event, page,set.WMPrivacySettings_.PageDisplay_Start,flag=2)
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMPrivacySettings["WMPrivacySettings"][1].keys())[0], \
#                                                      list(set.WMPrivacySettings["WMPrivacySettings"][1].values())[0],list(set.WMPrivacySettings.keys())[0])])
#     def test_PrivacModeSwitch(self, count, action, event,page):
#         Common(count, action, event, page,set.WMPrivacySettings_.PrivacModeSwitch)
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMPrivacySettings["WMPrivacySettings"][2].keys())[0], \
#                                                      list(set.WMPrivacySettings["WMPrivacySettings"][2].values())[0],list(set.WMPrivacySettings.keys())[0])])
#     def test_MapSwitch(self, count, action, event,page):
#         Common(count, action, event,page, set.WMPrivacySettings_.MapSwitch)
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMPrivacySettings["WMPrivacySettings"][3].keys())[0], \
#                                                      list(set.WMPrivacySettings["WMPrivacySettings"][3].values())[0],list(set.WMPrivacySettings.keys())[0])])
#     def test_CallSwitch(self, count, action, event,page):
#         Common(count, action, event, page,set.WMPrivacySettings_.CallSwitch)
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMPrivacySettings["WMPrivacySettings"][4].keys())[0], \
#                                                      list(set.WMPrivacySettings["WMPrivacySettings"][4].values())[0],list(set.WMPrivacySettings.keys())[0])])
#     def test_DVRSwitch(self, count, action, event,page):
#         Common(count, action, event,page, set.WMPrivacySettings_.DVRSwitch)
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMPrivacySettings["WMPrivacySettings"][5].keys())[0], \
#                                                      list(set.WMPrivacySettings["WMPrivacySettings"][5].values())[0],list(set.WMPrivacySettings.keys())[0])])
#     def test_VideoSwitch(self, count, action, event,page):
#         Common(count, action, event, page,set.WMPrivacySettings_.VideoSwitch)
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMPrivacySettings["WMPrivacySettings"][6].keys())[0], \
#                                                      list(set.WMPrivacySettings["WMPrivacySettings"][6].values())[0],list(set.WMPrivacySettings.keys())[0])])
#     def test_WeChat(self, count, action, event,page):
#         Common(count, action, event, page,set.WMPrivacySettings_.WeChat)
# 
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMPrivacySettings["WMPrivacySettings"][7].keys())[0], \
#                                                      list(set.WMPrivacySettings["WMPrivacySettings"][7].values())[0],list(set.WMPrivacySettings.keys())[0])])
#     def test_CarHomeSwitch(self, count, action, event,page):
#         Common(count, action, event, page,set.WMPrivacySettings_.CarHomeSwitch)
# 
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMPrivacySettings["WMPrivacySettings"][8].keys())[0], \
#                                                      list(set.WMPrivacySettings["WMPrivacySettings"][8].values())[0],list(set.WMPrivacySettings.keys())[0])])
#     def test_VehicleSettingSwitch(self, count, action, event,page):
#         Common(count, action, event, page,set.WMPrivacySettings_.VehicleSettingSwitch)
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMPrivacySettings["WMPrivacySettings"][9].keys())[0], \
#                                                      list(set.WMPrivacySettings["WMPrivacySettings"][9].values())[0],list(set.WMPrivacySettings.keys())[0])])
#     def test_SetClick(self, count, action, event,page):
#         Common(count, action, event, page,set.WMPrivacySettings_.SetClick)
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMPrivacySettings["WMPrivacySettings"][10].keys())[0], \
#                                                      list(set.WMPrivacySettings["WMPrivacySettings"][10].values())[0],list(set.WMPrivacySettings.keys())[0])])
#     def test_Back(self, count, action, event,page):
#         Common(count, action, event,page, set.WMPrivacySettings_.Back)
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMPrivacySettings["WMPrivacySettings"][10].keys())[0], \
#                                                      list(set.WMPrivacySettings["WMPrivacySettings"][10].values())[0],list(set.WMPrivacySettings.keys())[0])])
#     def test_PageDisplay_End(self, count, action, event,page):
#         Common(count, action, event, page,set.WMPrivacySettings_.PageDisplay_End)
# 
# class Test_WMBluetoothSettings():
#     @pytest.fixture(scope='function', autouse=True)
#     def message(self):
#         '''check test environment'''
#         logger.log_info("start Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         logger.log_info("enter setting ui ", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.kill_setting()
#         time.sleep(random.randint(1, 3))
#         # if set.Check_Result.delete_lvlog(set.Action.get_sn()):
#         #     logger.log_info("delete lvlog successfully", \
#         #                     sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#         #                     sys._getframe().f_lineno)
#         logger.log_info("Enter settings ui", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.enter_settings_ui()
#         ''' enter bluetooth page'''
#         logger.log_info("Enter bluetooth page", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.enter_bluetooth(set.Action.get_sn())
#         time.sleep(random.randint(3, 5))
#         # if set.Check_Result.delete_tracker_log(set.Action.get_sn()):
#         #     logger.log_info("deltet tracker successfully", \
#         #                     sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#         #                     sys._getframe().f_lineno)
# 
#         time.sleep(random.randint(1, 3))
#         yield
#         logger.log_info("kill setting progress", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.kill_setting()
#         time.sleep(random.randint(1,3))
#         set.Action.kill_setting()
#         logger.log_info("end Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
# 
#     @pytest.mark.parametrize('count,action,event,page',[(random.randint(start_step,end_step),list(set.WMBluetoothSettings["WMBluetoothSettings"][0].keys())[0],\
#                                                     list(set.WMBluetoothSettings["WMBluetoothSettings"][0].values())[0],list(set.WMBluetoothSettings.keys())[0])])
#     def test_PageDisplay_Start(self, count, action, event,page):
#         time.sleep(10)
#         Common(count, action, event, page,set.WMBluetoothSettings_.PageDisplay_Start)
# 
#     @pytest.mark.parametrize('count,action,event,page',[(random.randint(start_step,end_step),list(set.WMBluetoothSettings["WMBluetoothSettings"][1].keys())[0],\
#                                                     list(set.WMBluetoothSettings["WMBluetoothSettings"][1].values())[0],list(set.WMBluetoothSettings.keys())[0])])
#     def test_OpenBluetoothSwitch(self, count, action, event,page):
#         Common(count, action, event, page,set.WMBluetoothSettings_.OpenBluetoothSwitch)
# 
#     @pytest.mark.parametrize('count,action,event,page',[(random.randint(start_step,end_step),list(set.WMBluetoothSettings["WMBluetoothSettings"][2].keys())[0],\
#                                                     list(set.WMBluetoothSettings["WMBluetoothSettings"][2].values())[0],list(set.WMBluetoothSettings.keys())[0])])
#     def test_VehicleName(self, count, action, event,page):
#         Common(count, action, event, page,set.WMBluetoothSettings_.VehicleName)
# 
#     @pytest.mark.parametrize('count,action,event,page',[(random.randint(start_step,end_step),list(set.WMBluetoothSettings["WMBluetoothSettings"][3].keys())[0],\
#                                                     list(set.WMBluetoothSettings["WMBluetoothSettings"][3].values())[0],list(set.WMBluetoothSettings.keys())[0])])
#     def test_ConnectBluetooth(self, count, action, event,page):
#         Common(count, action, event,page, set.WMBluetoothSettings_.ConnectBluetooth)
# 
#     @pytest.mark.parametrize('count,action,event,page',[(random.randint(start_step,end_step),list(set.WMBluetoothSettings["WMBluetoothSettings"][4].keys())[0],\
#                                                     list(set.WMBluetoothSettings["WMBluetoothSettings"][4].values())[0],list(set.WMBluetoothSettings.keys())[0])])
#     def test_BreakBluetooth(self, count, action, event,page):
#         Common(count, action, event, page,set.WMBluetoothSettings_.BreakBluetooth)
# 
#     @pytest.mark.parametrize('count,action,event,page',[(random.randint(start_step,end_step),list(set.WMBluetoothSettings["WMBluetoothSettings"][5].keys())[0],\
#                                                     list(set.WMBluetoothSettings["WMBluetoothSettings"][5].values())[0],list(set.WMBluetoothSettings.keys())[0])])
#     def test_ClickdeleteBluetooth(self, count, action, event,page):
#         Common(count, action, event, page,set.WMBluetoothSettings_.ClickdeleteBluetooth)
# 
#     @pytest.mark.parametrize('count,action,event,page',[(random.randint(start_step,end_step),list(set.WMBluetoothSettings["WMBluetoothSettings"][6].keys())[0],\
#                                                     list(set.WMBluetoothSettings["WMBluetoothSettings"][6].values())[0],list(set.WMBluetoothSettings.keys())[0])])
#     def test_Back(self, count, action, event, page):
#         Common(count, action, event, page,set.WMBluetoothSettings_.Back)
# 
#     @pytest.mark.parametrize('count,action,event,page',[(random.randint(start_step,end_step),list(set.WMBluetoothSettings["WMBluetoothSettings"][7].keys())[0],\
#                                                     list(set.WMBluetoothSettings["WMBluetoothSettings"][7].values())[0],list(set.WMBluetoothSettings.keys())[0])])
#     def test_PageDisplay_End(self, count, action, event,page):
#         Common(count, action, event, page,set.WMBluetoothSettings_.PageDisplay_End)
# 
# class Test_WMDeleteBluetoothDialog():
#     @pytest.fixture(scope='function', autouse=True)
#     def message(self):
#         '''check test environment'''
#         logger.log_info("start Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         logger.log_info("enter setting ui ", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.kill_setting()
#         time.sleep(random.randint(1, 3))
#         # if set.Check_Result.delete_lvlog(set.Action.get_sn()):
#         #     logger.log_info("delete lvlog successfully", \
#         #                     sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#         #                     sys._getframe().f_lineno)
#         logger.log_info("Enter settings ui", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.enter_settings_ui()
#         '''enter bluetooth page'''
#         logger.log_info("Enter bluetooth page", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.enter_bluetooth(set.Action.get_sn())
#         '''enter blue dialog'''
#         logger.log_info("Enter blue dialog page", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.enter_blue_dialog(set.Action.get_sn())
#         time.sleep(random.randint(3, 5))
#         # if set.Check_Result.delete_tracker_log(set.Action.get_sn()):
#         #     logger.log_info("deltet tracker successfully", \
#         #                     sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#         #                     sys._getframe().f_lineno)
# 
#         time.sleep(random.randint(1, 3))
#         yield
#         logger.log_info("kill setting progress", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.kill_setting()
#         time.sleep(random.randint(1,3))
#         set.Action.kill_setting()
#         logger.log_info("end Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMDeleteBluetoothDialog["WMDeleteBluetoothDialog"][0].keys())[0],\
#                                                      list(set.WMDeleteBluetoothDialog["WMDeleteBluetoothDialog"][0].values())[0],list(set.WMDeleteBluetoothDialog.keys())[0])])
#     def test_ClickdeleteBluetooth(self, count, action, event,page):
#         Common(count, action, event, page,set.WMDeleteBluetoothDialog_.PageDisplay_Start)
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMDeleteBluetoothDialog["WMDeleteBluetoothDialog"][2].keys())[0], \
#                                                      list(set.WMDeleteBluetoothDialog["WMDeleteBluetoothDialog"][2].values())[0],list(set.WMDeleteBluetoothDialog.keys())[0])])
#     def test_ClickCancel(self, count, action, event,page):
#         Common(count, action, event, page,set.WMDeleteBluetoothDialog_.ClickCancel)
# 
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMDeleteBluetoothDialog["WMDeleteBluetoothDialog"][3].keys())[0], \
#                                                      list(set.WMDeleteBluetoothDialog["WMDeleteBluetoothDialog"][3].values())[0],list(set.WMDeleteBluetoothDialog.keys())[0])])
#     def test_PageDisplay_End(self, count, action, event,page):
#         Common(count, action, event, page,set.WMDeleteBluetoothDialog_.PageDisplay_End)
# 
# 
# class Test_WifiSettings():
#     @pytest.fixture(scope='function', autouse=True)
#     def message(self):
#         '''check test environment'''
#         logger.log_info("start Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         logger.log_info("enter setting ui ", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.kill_setting()
#         time.sleep(random.randint(1, 3))
#         # if set.Check_Result.delete_lvlog(set.Action.get_sn()):
#         #     logger.log_info("delete lvlog successfully", \
#         #                     sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#         #                     sys._getframe().f_lineno)
#         logger.log_info("Enter settings ui", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.enter_settings_ui()
#         '''enter bluetooth page'''
#         logger.log_info("Enter wifi page", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.enter_wifi(set.Action.get_sn())
#         time.sleep(random.randint(3, 5))
#         # if set.Check_Result.delete_tracker_log(set.Action.get_sn()):
#         #     logger.log_info("delete tracker successfully", \
#         #                     sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#         #                     sys._getframe().f_lineno)
# 
#         time.sleep(random.randint(1, 3))
#         yield
#         logger.log_info("kill setting progress", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.kill_setting()
#         time.sleep(random.randint(1,3))
#         set.Action.kill_setting()
#         logger.log_info("end Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WifiSettings["WifiSettings"][0].keys())[0], \
#                                                      list(set.WifiSettings["WifiSettings"][0].values())[0],list(set.WifiSettings.keys())[0])])
#     def test_PageDisplay_Start(self, count, action, event,page):
#         Common(count, action, event, page,set.WifiSettings_.PageDisplay_Start)
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WifiSettings["WifiSettings"][1].keys())[0], \
#                                                      list(set.WifiSettings["WifiSettings"][1].values())[0],list(set.WifiSettings.keys())[0])])
#     def test_Back(self, count, action, event,page):
#         Common(count, action, event, page,set.WifiSettings_.Back)
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WifiSettings["WifiSettings"][2].keys())[0], \
#                                                      list(set.WifiSettings["WifiSettings"][2].values())[0],list(set.WifiSettings.keys())[0])])
#     def test_PageDisplay_End(self, count, action, event,page):
#         Common(count, action, event,page, set.WifiSettings_.PageDisplay_End)
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WifiSettings["WifiSettings"][3].keys())[0], \
#                                                      list(set.WifiSettings["WifiSettings"][3].values())[0],list(set.WifiSettings.keys())[0])])
#     def test_ClickIgnoreWIFI(self, count, action, event,page):
#         Common(count, action, event, page,set.WifiSettings_.ClickIgnoreWIFI)
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WifiSettings["WifiSettings"][4].keys())[0], \
#                                                      list(set.WifiSettings["WifiSettings"][4].values())[0],list(set.WifiSettings.keys())[0])])
#     def test_OpenWIFISwitch(self, count, action, event,page):
#         Common(count, action, event, page,set.WifiSettings_.OpenWIFISwitch)
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WifiSettings["WifiSettings"][5].keys())[0], \
#                                                      list(set.WifiSettings["WifiSettings"][5].values())[0],list(set.WifiSettings.keys())[0])])
#     def test_ConnectWIFI(self, count, action, event,page):
#         Common(count, action, event, page,set.WifiSettings_.ConnectWIFI)
# 
# class Test_WMRemoveWIFIDialog():
#     @pytest.fixture(scope='function', autouse=True)
#     def message(self):
#         '''check test environment'''
#         logger.log_info("start Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         logger.log_info("enter setting ui ", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.kill_setting()
#         time.sleep(random.randint(1, 3))
#         # if set.Check_Result.delete_lvlog(set.Action.get_sn()):
#         #     logger.log_info("delete lvlog successfully", \
#         #                     sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#         #                     sys._getframe().f_lineno)
#         logger.log_info("Enter settings ui", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.enter_settings_ui()
#         '''enter bluetooth page'''
#         logger.log_info("Enter wifi page", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.enter_wifi(set.Action.get_sn())
#         '''dialog wifi page'''
#         set.Action.enter_wifi_dialog(set.Action.get_sn())
#         time.sleep(random.randint(3, 5))
# 
#         # if set.Check_Result.delete_tracker_log(set.Action.get_sn()):
#         #     logger.log_info("delete tracker successfully", \
#         #                     sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#         #                     sys._getframe().f_lineno)
# 
#         time.sleep(random.randint(1, 3))
#         yield
#         logger.log_info("kill setting progress", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.kill_setting()
#         time.sleep(random.randint(1,3))
#         set.Action.kill_setting()
#         logger.log_info("end Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMRemoveWIFIDialog["WMRemoveWIFIDialog"][0].keys())[0], \
#                                                      list(set.WMRemoveWIFIDialog["WMRemoveWIFIDialog"][0].values())[0],list(set.WMRemoveWIFIDialog.keys())[0])])
#     def test_PageDisplay_Start(self, count, action, event,page):
#         Common(count, action, event, page,set.WMRemoveWIFIDialog_.PageDisplay_Start)
# 
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMRemoveWIFIDialog["WMRemoveWIFIDialog"][2].keys())[0], \
#                                                      list(set.WMRemoveWIFIDialog["WMRemoveWIFIDialog"][2].values())[0],list(set.WMRemoveWIFIDialog.keys())[0])])
#     def test_CancelDialog(self, count, action, event,page):
#         Common(count, action, event, page,set.WMRemoveWIFIDialog_.CancelDialog)
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMRemoveWIFIDialog["WMRemoveWIFIDialog"][3].keys())[0], \
#                                                      list(set.WMRemoveWIFIDialog["WMRemoveWIFIDialog"][3].values())[0],list(set.WMRemoveWIFIDialog.keys())[0])])
#     def test_Back(self, count, action, event,page):
#         Common(count, action, event,page, set.WMRemoveWIFIDialog_.Back)
# 
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMRemoveWIFIDialog["WMRemoveWIFIDialog"][1].keys())[0], \
#                                                      list(set.WMRemoveWIFIDialog["WMRemoveWIFIDialog"][1].values())[0],list(set.WMRemoveWIFIDialog.keys())[0])])
#     def test_RemoveWIFI(self, count, action, event,page):
#         Common(count, action, event, page,set.WMRemoveWIFIDialog_.RemoveWIFI)
# 
# class Test_WMEditTextActivity():
#     @pytest.fixture(scope='function', autouse=True)
#     def message(self):
#         '''check test environment'''
#         logger.log_info("start Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         logger.log_info("enter setting ui ", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.kill_setting()
#         time.sleep(random.randint(1, 3))
#         # if set.Check_Result.delete_lvlog(set.Action.get_sn()):
#         #     logger.log_info("delete lvlog successfully", \
#         #                     sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#         #                     sys._getframe().f_lineno)
#         logger.log_info("Enter settings ui", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.enter_settings_ui()
#         '''enter bluetooth page'''
#         logger.log_info("Enter wifi page", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.enter_wifi(set.Action.get_sn())
# 
#         '''enter wifi weditor page'''
#         logger.log_info("Enter wifi  editor page", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.enter_wifi_weditor_page(set.Action.get_sn())
#         time.sleep(random.randint(3, 5))
# 
#         # if set.Check_Result.delete_tracker_log(set.Action.get_sn()):
#         #     logger.log_info("delete tracker successfully", \
#         #                     sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#         #                     sys._getframe().f_lineno)
# 
#         time.sleep(random.randint(1, 3))
#         yield
#         logger.log_info("kill setting progress", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.kill_setting()
#         time.sleep(random.randint(1,3))
#         set.Action.kill_setting()
#         logger.log_info("end Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMEditTextActivity["WMEditTextActivity"][0].keys())[0], \
#                                                      list(set.WMEditTextActivity["WMEditTextActivity"][0].values())[0],list(set.WMEditTextActivity.keys())[0])])
#     def test_PageDisplay_Start(self, count, action, event,page):
#         Common(count, action, event, page,set.WMEditTextActivity_.PageDisplay_Start)
# 
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMEditTextActivity["WMEditTextActivity"][1].keys())[0], \
#                                                      list(set.WMEditTextActivity["WMEditTextActivity"][1].values())[
#                                                          0],list(set.WMEditTextActivity.keys())[0])])
#     def test_ClickConnectWIFI(self, count, action, event,page):
#         Common(count, action, event, page,set.WMEditTextActivity_.ClickConnectWIFI)
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMEditTextActivity["WMEditTextActivity"][2].keys())[0], \
#                                                      list(set.WMEditTextActivity["WMEditTextActivity"][2].values())[
#                                                          0],list(set.WMEditTextActivity.keys())[0])])
#     def test_ClickEliminate(self, count, action, event,page):
#         Common(count, action, event,page, set.WMEditTextActivity_.ClickEliminate)
# 
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMEditTextActivity["WMEditTextActivity"][3].keys())[0], \
#                                                      list(set.WMEditTextActivity["WMEditTextActivity"][3].values())[
#                                                          0],list(set.WMEditTextActivity.keys())[0])])
#     def test_Back(self, count, action, event,page):
#         Common(count, action, event, page,set.WMEditTextActivity_.Back)
# 
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMEditTextActivity["WMEditTextActivity"][4].keys())[0], \
#                                                      list(set.WMEditTextActivity["WMEditTextActivity"][4].values())[
#                                                          0],list(set.WMEditTextActivity.keys())[0])])
#     def test_PageDisplay_End(self, count, action, event,page):
#         Common(count, action, event, page,set.WMEditTextActivity_.PageDisplay_End)
# 
# class Test_WMSpeechSettings():
#     @pytest.fixture(scope='function', autouse=True)
#     def message(self):
#         '''check test environment'''
#         logger.log_info("start Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         logger.log_info("enter setting ui ", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.kill_setting()
#         time.sleep(random.randint(1, 3))
#         # if set.Check_Result.delete_lvlog(set.Action.get_sn()):
#         #     logger.log_info("delete lvlog successfully", \
#         #                     sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#         #                     sys._getframe().f_lineno)
#         logger.log_info("Enter settings ui", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.enter_settings_ui()
#         '''enter voice page'''
#         logger.log_info("Enter privacy page", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.enter_voice(set.Action.get_sn())
#         time.sleep(random.randint(3, 5))
# 
#         # if set.Check_Result.delete_tracker_log(set.Action.get_sn()):
#         #     logger.log_info("delete tracker successfully", \
#         #                     sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#         #                     sys._getframe().f_lineno)
# 
#         time.sleep(random.randint(1, 3))
#         yield
#         logger.log_info("kill setting progress", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.kill_setting()
#         time.sleep(random.randint(1, 3))
#         set.Action.kill_setting()
#         logger.log_info("end Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMSpeechSettings["WMSpeechSettings"][0].keys())[0], \
#                                                      list(set.WMSpeechSettings["WMSpeechSettings"][0].values())[0],list(set.WMSpeechSettings.keys())[0])])
#     def test_PageDisplay_Start(self, count, action, event,page):
#         Common(count, action, event,page, set.WMSpeechSettings_.PageDisplay_Start)
# 
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMSpeechSettings["WMSpeechSettings"][1].keys())[0], \
#                                                      list(set.WMSpeechSettings["WMSpeechSettings"][1].values())[0],list(set.WMSpeechSettings.keys())[0])])
#     def test_PageDisplay_Start(self, count, action, event,page):
#         Common(count, action, event,page, set.WMSpeechSettings_.ClickVoiceSwitch)
# 
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMSpeechSettings["WMSpeechSettings"][2].keys())[0], \
#                                                      list(set.WMSpeechSettings["WMSpeechSettings"][2].values())[0],list(set.WMSpeechSettings.keys())[0])])
#     def test_HelpDocument(self, count, action, event,page):
#         Common(count, action, event, page,set.WMSpeechSettings_.HelpDocument)
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMSpeechSettings["WMSpeechSettings"][3].keys())[0], \
#                                                      list(set.WMSpeechSettings["WMSpeechSettings"][3].values())[0],list(set.WMSpeechSettings.keys())[0])])
#     def test_Back(self, count, action, event,page):
#         Common(count, action, event, page,set.WMSpeechSettings_.Back)
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMSpeechSettings["WMSpeechSettings"][4].keys())[0], \
#                                                      list(set.WMSpeechSettings["WMSpeechSettings"][4].values())[0],list(set.WMSpeechSettings.keys())[0])])
#     def test_PageDisplay_End(self, count, action, event,page):
#         Common(count, action, event, page,set.WMSpeechSettings_.PageDisplay_End)
# 
# 
# class Test_WMSwitchVoiceDialog():
#     @pytest.fixture(scope='function', autouse=True)
#     def message(self):
#         '''check test environment'''
#         logger.log_info("start Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         logger.log_info("enter setting ui ", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.kill_setting()
#         time.sleep(random.randint(1, 3))
#         logger.log_info("Enter settings ui", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.enter_settings_ui()
#         '''enter voice page'''
#         logger.log_info("Enter privacy page", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.enter_voice(set.Action.get_sn())
#         '''enter personvoice page'''
#         logger.log_info("Enter person voice page", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.enter_voice_person_page(set.Action.get_sn())
#         time.sleep(random.randint(3, 5))
# 
#         # if set.Check_Result.delete_tracker_log(set.Action.get_sn()):
#         #     logger.log_info("delete tracker successfully", \
#         #                     sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#         #                     sys._getframe().f_lineno)
# 
#         time.sleep(random.randint(1, 3))
#         yield
#         logger.log_info("kill setting progress", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.kill_setting()
#         time.sleep(random.randint(1, 3))
#         set.Action.kill_setting()
#         logger.log_info("end Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMSwitchVoiceDialog["WMSwitchVoiceDialog"][0].keys())[0], \
#                                                      list(set.WMSwitchVoiceDialog["WMSwitchVoiceDialog"][0].values())[0],list(set.WMSwitchVoiceDialog.keys())[0])])
#     def test_PageDisplay_Start(self, count, action, event,page):
#         Common(count, action, event, page,set.WMSwitchVoiceDialog_.PageDisplay_Start)
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMSwitchVoiceDialog["WMSwitchVoiceDialog"][1].keys())[0], \
#                                                      list(set.WMSwitchVoiceDialog["WMSwitchVoiceDialog"][1].values())[0],list(set.WMSwitchVoiceDialog.keys())[0])])
#     def test_VoiceSwitch(self, count, action, event,page):
#         Common(count, action, event, page,set.WMSwitchVoiceDialog_.VoiceSwitch)
# 
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMSwitchVoiceDialog["WMSwitchVoiceDialog"][2].keys())[0], \
#                                                      list(set.WMSwitchVoiceDialog["WMSwitchVoiceDialog"][2].values())[0],list(set.WMSwitchVoiceDialog.keys())[0])])
#     def test_Back(self, count, action, event,page):
#         Common(count, action, event, page,set.WMSwitchVoiceDialog_.Back)
# 
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMSwitchVoiceDialog["WMSwitchVoiceDialog"][3].keys())[0], \
#                                                      list(set.WMSwitchVoiceDialog["WMSwitchVoiceDialog"][3].values())[0],list(set.WMSwitchVoiceDialog.keys())[0])])
#     def test_ClickClose(self, count, action, event,page):
#         Common(count, action, event, page,set.WMSwitchVoiceDialog_.ClickClose)
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMSwitchVoiceDialog["WMSwitchVoiceDialog"][4].keys())[0], \
#                                                      list(set.WMSwitchVoiceDialog["WMSwitchVoiceDialog"][4].values())[0],list(set.WMSwitchVoiceDialog.keys())[0])])
#     def test_PageDisplay_End(self, count, action, event,page):
#         Common(count, action, event, page,set.WMSwitchVoiceDialog_.PageDisplay_End)
# 
# 
# class Test_WMSoundSettings():
#     @pytest.fixture(scope='function', autouse=True)
#     def message(self):
#         '''check test environment'''
#         logger.log_info("start Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         logger.log_info("enter setting ui ", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.kill_setting()
#         time.sleep(random.randint(1, 3))
#         logger.log_info("Enter settings ui", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.enter_settings_ui()
#         '''enter sound page'''
#         logger.log_info("Enter sound page", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.enter_sound(set.Action.get_sn())
#         time.sleep(random.randint(3, 5))
#         # if set.Check_Result.delete_tracker_log(set.Action.get_sn()):
#         #     logger.log_info("delete tracker successfully", \
#         #                     sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#         #                     sys._getframe().f_lineno)
#         time.sleep(random.randint(1, 3))
#         yield
#         logger.log_info("kill setting progress", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.kill_setting()
#         time.sleep(random.randint(1, 3))
#         set.Action.kill_setting()
#         logger.log_info("end Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMSoundSettings["WMSoundSettings"][0].keys())[0], \
#                                                      list(set.WMSoundSettings["WMSoundSettings"][0].values())[0],list(set.WMSoundSettings.keys())[0])])
#     def test_PageDisplay_Start(self, count, action, event,page):
#         Common(count, action, event, page,set.WMSoundSettings_.PageDisplay_Start,flag=2)
# 
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMSoundSettings["WMSoundSettings"][1].keys())[0], \
#                                                      list(set.WMSoundSettings["WMSoundSettings"][1].values())[0],list(set.WMSoundSettings.keys())[0])])
#     def test_ClickSwitch(self, count, action, event,page):
#         Common(count, action, event, page,set.WMSoundSettings_.ClickSwitch)
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMSoundSettings["WMSoundSettings"][2].keys())[0], \
#                                                      list(set.WMSoundSettings["WMSoundSettings"][2].values())[0],list(set.WMSoundSettings.keys())[0])])
#     def test_MediaVolume(self, count, action, event,page):
#         Common(count, action, event, page,set.WMSoundSettings_.MediaVolume,flag=2)
# 
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMSoundSettings["WMSoundSettings"][3].keys())[0], \
#                                                      list(set.WMSoundSettings["WMSoundSettings"][3].values())[0],list(set.WMSoundSettings.keys())[0])])
#     def test_ConversationVolume(self, count, action, event,page):
#         Common(count, action, event, page,set.WMSoundSettings_.ConversationVolume,flag=2)
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMSoundSettings["WMSoundSettings"][4].keys())[0], \
#                                                      list(set.WMSoundSettings["WMSoundSettings"][4].values())[0],list(set.WMSoundSettings.keys())[0])])
#     def test_NavigationVolume(self, count, action, event,page):
#         Common(count, action, event, page,set.WMSoundSettings_.NavigationVolume, flag=2)
# 
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMSoundSettings["WMSoundSettings"][5].keys())[0], \
#                                                      list(set.WMSoundSettings["WMSoundSettings"][5].values())[0],list(set.WMSoundSettings.keys())[0])])
#     def test_VoiceVolume(self, count, action, event,page):
#         Common(count, action, event, page,set.WMSoundSettings_.VoiceVolume, flag=2)
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMSoundSettings["WMSoundSettings"][6].keys())[0], \
#                                                      list(set.WMSoundSettings["WMSoundSettings"][6].values())[0],list(set.WMSoundSettings.keys())[0])])
#     def test_ClickEqualizer(self, count, action, event,page):
#         Common(count, action, event, page,set.WMSoundSettings_.ClickEqualizer)
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMSoundSettings["WMSoundSettings"][7].keys())[0], \
#                                                      list(set.WMSoundSettings["WMSoundSettings"][7].values())[0],list(set.WMSoundSettings.keys())[0])])
#     def test_ClickSoundField(self, count, action, event,page):
#         Common(count, action, event, page,set.WMSoundSettings_.ClickSoundField)
# 
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMSoundSettings["WMSoundSettings"][8].keys())[0], \
#                                                      list(set.WMSoundSettings["WMSoundSettings"][8].values())[0],list(set.WMSoundSettings.keys())[0])])
#     def test_Back(self, count, action, event,page):
#         Common(count, action, event, page,set.WMSoundSettings_.Back)
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMSoundSettings["WMSoundSettings"][9].keys())[0], \
#                                                      list(set.WMSoundSettings["WMSoundSettings"][9].values())[0],list(set.WMSoundSettings.keys())[0])])
#     def test_PageDisplay_End(self, count, action, event,page):
#         Common(count, action, event, page,set.WMSoundSettings_.PageDisplay_End)
# 
# 
# class Test_WMVolumeEquilizerSettings():
#     @pytest.fixture(scope='function', autouse=True)
#     def message(self):
#         '''check test environment'''
#         logger.log_info("start Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         logger.log_info("enter setting ui ", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.kill_setting()
#         time.sleep(random.randint(1, 3))
#         logger.log_info("Enter settings ui", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.enter_settings_ui()
#         '''enter sound page'''
#         logger.log_info("Enter sound page", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.enter_sound(set.Action.get_sn())
#         '''enter VolumeEquilizer page'''
#         logger.log_info("Enter VolumeEquilizer page", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.enter_volumeequilizer(set.Action.get_sn())
#         time.sleep(random.randint(3, 5))
#         # if set.Check_Result.delete_tracker_log(set.Action.get_sn()):
#         #     logger.log_info("delete tracker successfully", \
#         #                     sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#         #                     sys._getframe().f_lineno)
#         time.sleep(random.randint(1, 3))
#         yield
#         logger.log_info("kill setting progress", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.kill_setting()
#         time.sleep(random.randint(1, 3))
#         set.Action.kill_setting()
#         logger.log_info("end Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMVolumeEquilizerSettings["WMVolumeEquilizerSettings"][0].keys())[0], \
#                                                      list(set.WMVolumeEquilizerSettings["WMVolumeEquilizerSettings"][0].values())[0],list(set.WMVolumeEquilizerSettings.keys())[0])])
#     def test_PageDisplay_End(self, count, action,event,page):
#         Common(count, action, event, page,set.WMVolumeEquilizerSettings_.PageDisplay_Start)
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMVolumeEquilizerSettings["WMVolumeEquilizerSettings"][
#                                                               1].keys())[0], \
#                                                      list(set.WMVolumeEquilizerSettings["WMVolumeEquilizerSettings"][
#                                                               1].values())[0],list(set.WMVolumeEquilizerSettings.keys())[0])])
#     def test_EqualizerSwitch(self, count, action, event,page):
#         Common(count, action, event,page, set.WMVolumeEquilizerSettings_.EqualizerSwitch)
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMVolumeEquilizerSettings["WMVolumeEquilizerSettings"][
#                                                               10].keys())[0], \
#                                                      list(set.WMVolumeEquilizerSettings["WMVolumeEquilizerSettings"][
#                                                               10].values())[0],list(set.WMVolumeEquilizerSettings.keys())[0])])
#     def test_SwitchEqualizer(self, count, action, event,page):
#         Common(count, action, event, page,set.WMVolumeEquilizerSettings_.SwitchEqualizer,flag=2)
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMVolumeEquilizerSettings["WMVolumeEquilizerSettings"][
#                                                               3].keys())[0], \
#                                                      list(set.WMVolumeEquilizerSettings["WMVolumeEquilizerSettings"][
#                                                               3].values())[0],list(set.WMVolumeEquilizerSettings.keys())[0])])
#     def test_AdjustEQ60HZ(self, count, action, event,page):
#         Common(count, action, event, page,set.WMVolumeEquilizerSettings_.AdjustEQ60HZ, flag=2)
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMVolumeEquilizerSettings["WMVolumeEquilizerSettings"][
#                                                               4].keys())[0], \
#                                                      list(set.WMVolumeEquilizerSettings["WMVolumeEquilizerSettings"][
#                                                               4].values())[0],list(set.WMVolumeEquilizerSettings.keys())[0])])
#     def test_AdjustEQ125HZ(self, count, action, event,page):
#         Common(count, action, event, page,set.WMVolumeEquilizerSettings_.AdjustEQ125HZ, flag=2)
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMVolumeEquilizerSettings["WMVolumeEquilizerSettings"][
#                                                               5].keys())[0], \
#                                                      list(set.WMVolumeEquilizerSettings["WMVolumeEquilizerSettings"][
#                                                               5].values())[0],list(set.WMVolumeEquilizerSettings.keys())[0])])
#     def test_AdjustEQ315HZ(self, count, action, event,page):
#         Common(count, action, event, page,set.WMVolumeEquilizerSettings_.AdjustEQ315HZ, flag=2)
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMVolumeEquilizerSettings["WMVolumeEquilizerSettings"][
#                                                               6].keys())[0], \
#                                                      list(set.WMVolumeEquilizerSettings["WMVolumeEquilizerSettings"][
#                                                               6].values())[0],list(set.WMVolumeEquilizerSettings.keys())[0])])
#     def test_AdjustEQ800HZ(self, count, action, event,page):
#         Common(count, action, event, page,set.WMVolumeEquilizerSettings_.AdjustEQ800HZ, flag=2)
# 
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMVolumeEquilizerSettings["WMVolumeEquilizerSettings"][
#                                                               7].keys())[0], \
#                                                      list(set.WMVolumeEquilizerSettings["WMVolumeEquilizerSettings"][
#                                                               7].values())[0],list(set.WMVolumeEquilizerSettings.keys())[0])])
#     def test_AdjustEQ2KHZ(self, count, action, event,page):
#         Common(count, action, event, page,set.WMVolumeEquilizerSettings_.AdjustEQ2KHZ, flag=2)
# 
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMVolumeEquilizerSettings["WMVolumeEquilizerSettings"][
#                                                               8].keys())[0], \
#                                                      list(set.WMVolumeEquilizerSettings["WMVolumeEquilizerSettings"][
#                                                               8].values())[0],list(set.WMVolumeEquilizerSettings.keys())[0])])
#     def test_AdjustEQ5KHZ(self, count, action, event,page):
#         Common(count, action, event, page,set.WMVolumeEquilizerSettings_.AdjustEQ5KHZ, flag=2)
# 
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMVolumeEquilizerSettings["WMVolumeEquilizerSettings"][
#                                                               9].keys())[0], \
#                                                      list(set.WMVolumeEquilizerSettings["WMVolumeEquilizerSettings"][
#                                                               9].values())[0],list(set.WMVolumeEquilizerSettings.keys())[0])])
#     def test_AdjustEQ12_5KHZ(self, count, action, event,page):
#         Common(count, action, event, page,set.WMVolumeEquilizerSettings_.AdjustEQ12_5KHZ, flag=4)
# 
# 
# class Test_WMVolumeBalanceSettingsActivity():
#     @pytest.fixture(scope='function', autouse=True)
#     def message(self):
#         '''check test environment'''
#         logger.log_info("start Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         logger.log_info("enter setting ui ", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.kill_setting()
#         time.sleep(random.randint(1, 3))
#         logger.log_info("Enter settings ui", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.enter_settings_ui()
#         '''enter sound page'''
#         logger.log_info("Enter sound page", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.enter_sound(set.Action.get_sn())
#         '''enter volumebalance page'''
#         logger.log_info("Enter volumebalance page", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.enter_volumebalance(set.Action.get_sn())
#         time.sleep(random.randint(3, 5))
#         # if set.Check_Result.delete_tracker_log(set.Action.get_sn()):
#         #     logger.log_info("delete tracker successfully", \
#         #                     sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#         #                     sys._getframe().f_lineno)
#         time.sleep(random.randint(1, 3))
#         yield
#         logger.log_info("kill setting progress", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.kill_setting()
#         time.sleep(random.randint(1, 3))
#         set.Action.kill_setting()
#         logger.log_info("end Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMVolumeBalanceSettingsActivity["WMVolumeBalanceSettingsActivity"][
#                                                               0].keys())[0], \
#                                                      list(set.WMVolumeBalanceSettingsActivity["WMVolumeBalanceSettingsActivity"][
#                                                               0].values())[0],list(set.WMVolumeBalanceSettingsActivity.keys())[0])])
#     def test_PageDisplay_Start(self, count, action, event,page):
#         Common(count, action, event, page,set.WMVolumeBalanceSettingsActivity_.PageDisplay_Start)
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMVolumeBalanceSettingsActivity["WMVolumeBalanceSettingsActivity"][
#                                                               2].keys())[0], \
#                                                      list(set.WMVolumeBalanceSettingsActivity["WMVolumeBalanceSettingsActivity"][
#                                                               2].values())[0],list(set.WMVolumeBalanceSettingsActivity.keys())[0])])
#     def test_Back(self, count, action, event,page):
#         Common(count, action, event, page,set.WMVolumeBalanceSettingsActivity_.Back)
# 
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMVolumeBalanceSettingsActivity["WMVolumeBalanceSettingsActivity"][
#                                                               3].keys())[0], \
#                                                      list(set.WMVolumeBalanceSettingsActivity["WMVolumeBalanceSettingsActivity"][
#                                                               3].values())[0],list(set.WMVolumeBalanceSettingsActivity.keys())[0])])
#     def test_PageDisplay_End(self, count, action, event,page):
#         Common(count, action, event, page,set.WMVolumeBalanceSettingsActivity_.PageDisplay_End)
# 
# class Test_WMGeneralSettings():
#     @pytest.fixture(scope='function', autouse=True)
#     def message(self):
#         '''check test environment'''
#         logger.log_info("start Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         logger.log_info("enter setting ui ", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.kill_setting()
#         time.sleep(random.randint(1, 3))
#         logger.log_info("Enter settings ui", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.enter_settings_ui()
#         '''enter general page'''
#         logger.log_info("Enter general page", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.enter_general(set.Action.get_sn())
#         time.sleep(random.randint(3, 5))
#         # if set.Check_Result.delete_tracker_log(set.Action.get_sn()):
#         #     logger.log_info("delete tracker successfully", \
#         #                     sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#         #                     sys._getframe().f_lineno)
#         # time.sleep(random.randint(1, 3))
#         yield
#         logger.log_info("kill setting progress", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.kill_setting()
#         time.sleep(random.randint(1, 3))
#         set.Action.kill_setting()
#         logger.log_info("end Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMGeneralSettings["WMGeneralSettings"][
#                                                               0].keys())[0], \
#                                                      list(set.WMGeneralSettings["WMGeneralSettings"][
#                                                               0].values())[0],list(set.WMGeneralSettings.keys())[0])])
#     def test_PageDisplay_Start(self, count, action, event,page):
#         Common(count, action, event, page,set.WMGeneralSettings_.PageDisplay_Start,flag=2)
# 
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMGeneralSettings["WMGeneralSettings"][
#                                                               1].keys())[0], \
#                                                      list(set.WMGeneralSettings["WMGeneralSettings"][
#                                                               1].values())[0],list(set.WMGeneralSettings.keys())[0])])
#     def test_TimeFormat(self, count, action, event,page):
#         Common(count, action, event, page,set.WMGeneralSettings_.TimeFormat)
# 
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMGeneralSettings["WMGeneralSettings"][
#                                                               2].keys())[0], \
#                                                      list(set.WMGeneralSettings["WMGeneralSettings"][
#                                                               2].values())[0],list(set.WMGeneralSettings.keys())[0])])
#     def test_Back(self, count, action, event,page):
#         Common(count, action, event, page,set.WMGeneralSettings_.Back)
# 
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMGeneralSettings["WMGeneralSettings"][
#                                                               3].keys())[0], \
#                                                      list(set.WMGeneralSettings["WMGeneralSettings"][
#                                                               3].values())[0],list(set.WMGeneralSettings.keys())[0])])
#     def test_PageDisplay_End(self, count, action, event,page):
#         Common(count, action, event, page,set.WMGeneralSettings_.PageDisplay_End)
# 
# 
# class Test_WMTimeFormatDialog():
#     @pytest.fixture(scope='function', autouse=True)
#     def message(self):
#         '''check test environment'''
#         logger.log_info("start Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         logger.log_info("enter setting ui ", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.kill_setting()
#         time.sleep(random.randint(1, 3))
#         logger.log_info("Enter settings ui", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.enter_settings_ui()
#         time.sleep(random.randint(1, 3))
#         '''enter general page'''
#         logger.log_info("Enter general page", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.enter_general(set.Action.get_sn())
#         time.sleep(random.randint(1, 3))
#         '''enter time formate page'''
#         logger.log_info("Enter time formate page", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.enter_timeformate(set.Action.get_sn())
#         time.sleep(random.randint(3, 5))
#         # if set.Check_Result.delete_tracker_log(set.Action.get_sn()):
#         #     logger.log_info("delete tracker successfully", \
#         #                     sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#         #                     sys._getframe().f_lineno)
#         time.sleep(random.randint(1, 3))
#         yield
#         logger.log_info("kill setting progress", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.kill_setting()
#         time.sleep(random.randint(1, 3))
#         set.Action.kill_setting()
#         logger.log_info("end Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMTimeFormatDialog["WMTimeFormatDialog"][
#                                                               0].keys())[0], \
#                                                      list(set.WMTimeFormatDialog["WMTimeFormatDialog"][
#                                                               0].values())[0],list(set.WMTimeFormatDialog.keys())[0])])
#     def test_PageDisplay_Start(self, count, action, event,page):
#         Common(count, action, event, page,set.WMTimeFormatDialog_.PageDisplay_Start)
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMTimeFormatDialog["WMTimeFormatDialog"][
#                                                               1].keys())[0], \
#                                                      list(set.WMTimeFormatDialog["WMTimeFormatDialog"][
#                                                               1].values())[0],list(set.WMTimeFormatDialog.keys())[0])])
#     def test_SwitchTimeFormat(self, count, action, event,page):
#         Common(count, action, event, page,set.WMTimeFormatDialog_.SwitchTimeFormat)
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMTimeFormatDialog["WMTimeFormatDialog"][
#                                                               2].keys())[0], \
#                                                      list(set.WMTimeFormatDialog["WMTimeFormatDialog"][
#                                                               2].values())[0],list(set.WMTimeFormatDialog.keys())[0])])
#     def test_ClickClose(self, count, action, event,page):
#         Common(count, action, event, page,set.WMTimeFormatDialog_.ClickClose)
# 
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMTimeFormatDialog["WMTimeFormatDialog"][
#                                                               3].keys())[0], \
#                                                      list(set.WMTimeFormatDialog["WMTimeFormatDialog"][
#                                                               3].values())[0],list(set.WMTimeFormatDialog.keys())[0])])
#     def test_Back(self, count, action, event,page):
#         Common(count, action, event, page,set.WMTimeFormatDialog_.Back)
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMTimeFormatDialog["WMTimeFormatDialog"][
#                                                               4].keys())[0], \
#                                                      list(set.WMTimeFormatDialog["WMTimeFormatDialog"][
#                                                               4].values())[0],list(set.WMTimeFormatDialog.keys())[0])])
#     def test_PageDisplay_End(self, count, action, event,page):
#         Common(count, action, event, page,set.WMTimeFormatDialog_.PageDisplay_End)
# 
# 
# class Test_WMSystemSettings():
#     @pytest.fixture(scope='function', autouse=True)
#     def message(self):
#         '''check test environment'''
#         logger.log_info("start Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         logger.log_info("enter setting ui ", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.kill_setting()
#         time.sleep(random.randint(1, 3))
#         logger.log_info("Enter settings ui", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.enter_settings_ui()
#         time.sleep(random.randint(1, 3))
#         '''enter system page'''
#         logger.log_info("Enter general page", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.enter_system(set.Action.get_sn())
#         time.sleep(random.randint(3, 5))
#         # if set.Check_Result.delete_tracker_log(set.Action.get_sn()):
#         #     logger.log_info("delete tracker successfully", \
#         #                     sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#         #                     sys._getframe().f_lineno)
#         time.sleep(random.randint(1, 3))
#         yield
#         logger.log_info("kill setting progress", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         set.Action.kill_setting()
#         time.sleep(random.randint(1, 3))
#         set.Action.kill_setting()
#         logger.log_info("end Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMSystemSettings["WMSystemSettings"][
#                                                               0].keys())[0], \
#                                                      list(set.WMSystemSettings["WMSystemSettings"][
#                                                               0].values())[0],list(set.WMSystemSettings.keys())[0])])
#     def test_PageDisplay_Start(self, count, action, event,page):
#         Common(count, action, event, page,set.WMSystemSettings_.PageDisplay_Start,flag=2)
# 
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMSystemSettings["WMSystemSettings"][
#                                                               1].keys())[0], \
#                                                      list(set.WMSystemSettings["WMSystemSettings"][
#                                                               1].values())[0],list(set.WMSystemSettings.keys())[0])])
#     def test_FunctionDemo(self, count, action, event,page):
#         Common(count, action, event,page, set.WMSystemSettings_.FunctionDemo)
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMSystemSettings["WMSystemSettings"][
#                                                               2].keys())[0], \
#                                                      list(set.WMSystemSettings["WMSystemSettings"][
#                                                               2].values())[0],list(set.WMSystemSettings.keys())[0])])
#     def test_ClickStorage(self, count, action, event,page):
#         Common(count, action, event, page,set.WMSystemSettings_.ClickStorage)
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMSystemSettings["WMSystemSettings"][
#                                                               3].keys())[0], \
#                                                      list(set.WMSystemSettings["WMSystemSettings"][
#                                                               3].values())[0],list(set.WMSystemSettings.keys())[0])])
#     def test_ClickTBox(self, count, action, event,page):
#         Common(count, action, event, page,set.WMSystemSettings_.ClickTBox)
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMSystemSettings["WMSystemSettings"][
#                                                               4].keys())[0], \
#                                                      list(set.WMSystemSettings["WMSystemSettings"][
#                                                               4].values())[0],list(set.WMSystemSettings.keys())[0])])
#     def test_ClickInformation(self, count, action, event,page):
#         Common(count, action, event, page,set.WMSystemSettings_.ClickInformation)
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMSystemSettings["WMSystemSettings"][
#                                                               5].keys())[0], \
#                                                      list(set.WMSystemSettings["WMSystemSettings"][
#                                                               5].values())[0],list(set.WMSystemSettings.keys())[0])])
#     def test_CilckRecoverySystem(self, count, action, event,page):
#         Common(count, action, event, page,set.WMSystemSettings_.CilckRecoverySystem)
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMSystemSettings["WMSystemSettings"][
#                                                               6].keys())[0], \
#                                                      list(set.WMSystemSettings["WMSystemSettings"][
#                                                               6].values())[0],list(set.WMSystemSettings.keys())[0])])
#     def test_Back(self, count, action, event,page):
#         Common(count, action, event, page,set.WMSystemSettings_.Back)
# 
#     @pytest.mark.parametrize('count,action,event,page', [(random.randint(start_step, end_step), \
#                                                      list(set.WMSystemSettings["WMSystemSettings"][
#                                                               7].keys())[0], \
#                                                      list(set.WMSystemSettings["WMSystemSettings"][
#                                                               7].values())[0],list(set.WMSystemSettings.keys())[0])])
#     def test_PageDisplay_End(self, count, action, event,page):
#         Common(count, action, event, page,set.WMSystemSettings_.PageDisplay_End)
# 
# 
# class Test_Check_Settings_Hive_Result(object):
# 
#     @pytest.mark.parametrize('sn',[set.Action.get_sn()])
#     def test_Kill_Buried_Progress(self,sn):
#         logger.log_info("kill logcat collect log progress", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         os.system('adb -s %s shell "%s"' %(sn,logcat_pid_exist))
#         time.sleep(7200)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Setting_Actions["settings"][15].keys())[0], \
#                               list(set.Setting_Actions["settings"][15].values())[0],
#                               None)])
#     def test_settings_OpenApp(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Setting_Actions["settings"][16].keys())[0], \
#                               list(set.Setting_Actions["settings"][16].values())[0],
#                               None)])
#     def test_settings_Foreground_Start(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Setting_Actions["settings"][17].keys())[0], \
#                               list(set.Setting_Actions["settings"][17].values())[0],
#                               None)])
#     def test_settings_Foreground_End(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Setting_Actions["settings"][0].keys())[0], \
#                                list(set.Setting_Actions["settings"][0].values())[0],
#                                list(set.Setting_Actions.keys())[0])])
#     def test_settings_Back(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Setting_Actions["settings"][1].keys())[0], \
#                                list(set.Setting_Actions["settings"][1].values())[0],
#                                list(set.Setting_Actions.keys())[0])])
#     def test_settings_PageDisplay_Start(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Setting_Actions["settings"][2].keys())[0], \
#                                list(set.Setting_Actions["settings"][2].values())[0],
#                                list(set.Setting_Actions.keys())[0])])
#     def test_settings_PageDisplay_End(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Setting_Actions["settings"][3].keys())[0], \
#                                list(set.Setting_Actions["settings"][3].values())[0],
#                                list(set.Setting_Actions.keys())[0])])
#     def test_settings_Open_WIFI(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Setting_Actions["settings"][4].keys())[0], \
#                                list(set.Setting_Actions["settings"][4].values())[0],
#                                list(set.Setting_Actions.keys())[0])])
#     def test_settings_OpenBluetooth(self, action, event, page):
#         Compare(action, event, page)
# 
#     '''because of not choose'''
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Setting_Actions["settings"][5].keys())[0], \
#                                list(set.Setting_Actions["settings"][5].values())[0],
#                                list(set.Setting_Actions.keys())[0])])
#     def test_settings_WirelessCharging(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Setting_Actions["settings"][6].keys())[0], \
#                                list(set.Setting_Actions["settings"][6].values())[0],
#                                list(set.Setting_Actions.keys())[0])])
#     def test_settings_PrivacyMode(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Setting_Actions["settings"][7].keys())[0], \
#                                list(set.Setting_Actions["settings"][7].values())[0],
#                                list(set.Setting_Actions.keys())[0])])
#     def test_settings_ClickUser(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Setting_Actions["settings"][8].keys())[0], \
#                                list(set.Setting_Actions["settings"][8].values())[0],
#                                list(set.Setting_Actions.keys())[0])])
#     def test_settings_ClickBluetooth(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Setting_Actions["settings"][9].keys())[0], \
#                                list(set.Setting_Actions["settings"][9].values())[0],
#                                list(set.Setting_Actions.keys())[0])])
#     def test_settings_ClickWIFI(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(
#                               list(set.Setting_Actions["settings"][10].keys())[0], \
#                               list(set.Setting_Actions["settings"][10].values())[0],
#                               list(set.Setting_Actions.keys())[0])])
#     def test_settings_ClickPrivacy(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(
#                               list(set.Setting_Actions["settings"][11].keys())[0], \
#                               list(set.Setting_Actions["settings"][11].values())[0],
#                               list(set.Setting_Actions.keys())[0])])
#     def test_settings_ClickVoice(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(
#                               list(set.Setting_Actions["settings"][12].keys())[0], \
#                               list(set.Setting_Actions["settings"][12].values())[0],
#                               list(set.Setting_Actions.keys())[0])])
#     def test_settings_ClickVolume(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(
#                               list(set.Setting_Actions["settings"][13].keys())[0], \
#                               list(set.Setting_Actions["settings"][13].values())[0],
#                               list(set.Setting_Actions.keys())[0])])
#     def test_settings_ClickCurrency(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(
#                               list(set.Setting_Actions["settings"][14].keys())[0], \
#                               list(set.Setting_Actions["settings"][14].values())[0],
#                               list(set.Setting_Actions.keys())[0])])
#     def test_settings_ClickSystem(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMPrivacySettings["WMPrivacySettings"][0].keys())[0], \
#                                                           list(set.WMPrivacySettings["WMPrivacySettings"][0].values())[
#                                                               0], list(set.WMPrivacySettings.keys())[0])])
#     def test_WMPrivacySettings_PageDisplay_Start(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMPrivacySettings["WMPrivacySettings"][1].keys())[0], \
#                                                           list(set.WMPrivacySettings["WMPrivacySettings"][1].values())[
#                                                               0], list(set.WMPrivacySettings.keys())[0])])
#     def test_WMPrivacySettings_PrivacModeSwitch(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMPrivacySettings["WMPrivacySettings"][2].keys())[0], \
#                                                           list(set.WMPrivacySettings["WMPrivacySettings"][2].values())[
#                                                               0], list(set.WMPrivacySettings.keys())[0])])
#     def test_WMPrivacySettings_MapSwitch(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMPrivacySettings["WMPrivacySettings"][3].keys())[0], \
#                                                           list(set.WMPrivacySettings["WMPrivacySettings"][3].values())[
#                                                               0], list(set.WMPrivacySettings.keys())[0])])
#     def test_WMPrivacySettings_CallSwitch(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMPrivacySettings["WMPrivacySettings"][4].keys())[0], \
#                                                           list(set.WMPrivacySettings["WMPrivacySettings"][4].values())[
#                                                               0], list(set.WMPrivacySettings.keys())[0])])
#     def test_WMPrivacySettings_DVRSwitch(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMPrivacySettings["WMPrivacySettings"][5].keys())[0], \
#                                                           list(set.WMPrivacySettings["WMPrivacySettings"][5].values())[
#                                                               0], list(set.WMPrivacySettings.keys())[0])])
#     def test_WMPrivacySettings_VideoSwitch(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMPrivacySettings["WMPrivacySettings"][6].keys())[0], \
#                                                           list(set.WMPrivacySettings["WMPrivacySettings"][6].values())[
#                                                               0], list(set.WMPrivacySettings.keys())[0])])
#     def test_WMPrivacySettings_WeChat(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMPrivacySettings["WMPrivacySettings"][7].keys())[0], \
#                                                           list(set.WMPrivacySettings["WMPrivacySettings"][7].values())[
#                                                               0], list(set.WMPrivacySettings.keys())[0])])
#     def test_WMPrivacySettings_CarHomeSwitch(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMPrivacySettings["WMPrivacySettings"][8].keys())[0], \
#                                                           list(set.WMPrivacySettings["WMPrivacySettings"][8].values())[
#                                                               0], list(set.WMPrivacySettings.keys())[0])])
#     def test_WMPrivacySettings_VehicleSettingSwitch(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMPrivacySettings["WMPrivacySettings"][9].keys())[0], \
#                                                           list(set.WMPrivacySettings["WMPrivacySettings"][9].values())[
#                                                               0], list(set.WMPrivacySettings.keys())[0])])
#     def test_WMPrivacySettings_SetClick(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMPrivacySettings["WMPrivacySettings"][10].keys())[
#                                                               0], \
#                                                           list(set.WMPrivacySettings["WMPrivacySettings"][10].values())[
#                                                               0], list(set.WMPrivacySettings.keys())[0])])
#     def test_WMPrivacySettings_Back(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMPrivacySettings["WMPrivacySettings"][10].keys())[
#                                                               0], \
#                                                           list(set.WMPrivacySettings["WMPrivacySettings"][10].values())[
#                                                               0], list(set.WMPrivacySettings.keys())[0])])
#     def test_WMPrivacySettings_PageDisplay_End(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [
#         (list(set.WMBluetoothSettings["WMBluetoothSettings"][0].keys())[0], \
#          list(set.WMBluetoothSettings["WMBluetoothSettings"][0].values())[0], list(set.WMBluetoothSettings.keys())[0])])
#     def test_WMBluetoothSettings_PageDisplay_Start(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [
#         (list(set.WMBluetoothSettings["WMBluetoothSettings"][1].keys())[0], \
#          list(set.WMBluetoothSettings["WMBluetoothSettings"][1].values())[0], list(set.WMBluetoothSettings.keys())[0])])
#     def test_WMBluetoothSettings_OpenBluetoothSwitch(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [
#         (list(set.WMBluetoothSettings["WMBluetoothSettings"][2].keys())[0], \
#          list(set.WMBluetoothSettings["WMBluetoothSettings"][2].values())[0], list(set.WMBluetoothSettings.keys())[0])])
#     def test_WMBluetoothSettings_VehicleName(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [
#         (list(set.WMBluetoothSettings["WMBluetoothSettings"][3].keys())[0], \
#          list(set.WMBluetoothSettings["WMBluetoothSettings"][3].values())[0], list(set.WMBluetoothSettings.keys())[0])])
#     def test_WMBluetoothSettings_ConnectBluetooth(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [
#         (list(set.WMBluetoothSettings["WMBluetoothSettings"][4].keys())[0], \
#          list(set.WMBluetoothSettings["WMBluetoothSettings"][4].values())[0], list(set.WMBluetoothSettings.keys())[0])])
#     def test_WMBluetoothSettings_BreakBluetooth(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [
#         (list(set.WMBluetoothSettings["WMBluetoothSettings"][5].keys())[0], \
#          list(set.WMBluetoothSettings["WMBluetoothSettings"][5].values())[0], list(set.WMBluetoothSettings.keys())[0])])
#     def test_WMBluetoothSettings_ClickdeleteBluetooth(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [
#         (list(set.WMBluetoothSettings["WMBluetoothSettings"][6].keys())[0], \
#          list(set.WMBluetoothSettings["WMBluetoothSettings"][6].values())[0], list(set.WMBluetoothSettings.keys())[0])])
#     def test_WMBluetoothSettings_Back(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [
#         (list(set.WMBluetoothSettings["WMBluetoothSettings"][7].keys())[0], \
#          list(set.WMBluetoothSettings["WMBluetoothSettings"][7].values())[0], list(set.WMBluetoothSettings.keys())[0])])
#     def test_WMBluetoothSettings_PageDisplay_End(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMDeleteBluetoothDialog["WMDeleteBluetoothDialog"][
#                                                                    0].keys())[0], \
#                                                           list(set.WMDeleteBluetoothDialog["WMDeleteBluetoothDialog"][
#                                                                    0].values())[0],
#                                                           list(set.WMDeleteBluetoothDialog.keys())[0])])
#     def test_WMDeleteBluetoothDialog_ClickdeleteBluetooth(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMDeleteBluetoothDialog["WMDeleteBluetoothDialog"][
#                                                                    2].keys())[0], \
#                                                           list(set.WMDeleteBluetoothDialog["WMDeleteBluetoothDialog"][
#                                                                    2].values())[0],
#                                                           list(set.WMDeleteBluetoothDialog.keys())[0])])
#     def test_WMDeleteBluetoothDialog_ClickCancel(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMDeleteBluetoothDialog["WMDeleteBluetoothDialog"][
#                                                                    3].keys())[0], \
#                                                           list(set.WMDeleteBluetoothDialog["WMDeleteBluetoothDialog"][
#                                                                    3].values())[0],
#                                                           list(set.WMDeleteBluetoothDialog.keys())[0])])
#     def test_WMDeleteBluetoothDialog_PageDisplay_End(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WifiSettings["WifiSettings"][0].keys())[0], \
#                                                           list(set.WifiSettings["WifiSettings"][0].values())[0],
#                                                           list(set.WifiSettings.keys())[0])])
#     def test_WifiSettings_PageDisplay_Start(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WifiSettings["WifiSettings"][1].keys())[0], \
#                                                           list(set.WifiSettings["WifiSettings"][1].values())[0],
#                                                           list(set.WifiSettings.keys())[0])])
#     def test_WifiSettings_Back(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WifiSettings["WifiSettings"][2].keys())[0], \
#                                                           list(set.WifiSettings["WifiSettings"][2].values())[0],
#                                                           list(set.WifiSettings.keys())[0])])
#     def test_WifiSettings_PageDisplay_End(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WifiSettings["WifiSettings"][3].keys())[0], \
#                                                           list(set.WifiSettings["WifiSettings"][3].values())[0],
#                                                           list(set.WifiSettings.keys())[0])])
#     def test_WifiSettings_ClickIgnoreWIFI(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WifiSettings["WifiSettings"][4].keys())[0], \
#                                                           list(set.WifiSettings["WifiSettings"][4].values())[0],
#                                                           list(set.WifiSettings.keys())[0])])
#     def test_WifiSettings_OpenWIFISwitch(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WifiSettings["WifiSettings"][5].keys())[0], \
#                                                           list(set.WifiSettings["WifiSettings"][5].values())[0],
#                                                           list(set.WifiSettings.keys())[0])])
#     def test_WifiSettings_ConnectWIFI(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMRemoveWIFIDialog["WMRemoveWIFIDialog"][0].keys())[
#                                                               0], \
#                                                           list(
#                                                               set.WMRemoveWIFIDialog["WMRemoveWIFIDialog"][0].values())[
#                                                               0], list(set.WMRemoveWIFIDialog.keys())[0])])
#     def test_WMRemoveWIFIDialog_PageDisplay_Start(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMRemoveWIFIDialog["WMRemoveWIFIDialog"][2].keys())[
#                                                               0], \
#                                                           list(
#                                                               set.WMRemoveWIFIDialog["WMRemoveWIFIDialog"][2].values())[
#                                                               0], list(set.WMRemoveWIFIDialog.keys())[0])])
#     def test_WMRemoveWIFIDialog_CancelDialog(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMRemoveWIFIDialog["WMRemoveWIFIDialog"][3].keys())[
#                                                               0], \
#                                                           list(
#                                                               set.WMRemoveWIFIDialog["WMRemoveWIFIDialog"][3].values())[
#                                                               0], list(set.WMRemoveWIFIDialog.keys())[0])])
#     def test_WMRemoveWIFIDialog_Back(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMRemoveWIFIDialog["WMRemoveWIFIDialog"][1].keys())[
#                                                               0], \
#                                                           list(
#                                                               set.WMRemoveWIFIDialog["WMRemoveWIFIDialog"][1].values())[
#                                                               0], list(set.WMRemoveWIFIDialog.keys())[0])])
#     def test_WMRemoveWIFIDialog_RemoveWIFI(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMEditTextActivity["WMEditTextActivity"][0].keys())[
#                                                               0], \
#                                                           list(
#                                                               set.WMEditTextActivity["WMEditTextActivity"][0].values())[
#                                                               0], list(set.WMEditTextActivity.keys())[0])])
#     def test_WMEditTextActivity_PageDisplay_Start(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMEditTextActivity["WMEditTextActivity"][1].keys())[
#                                                               0], \
#                                                           list(
#                                                               set.WMEditTextActivity["WMEditTextActivity"][1].values())[
#                                                               0], list(set.WMEditTextActivity.keys())[0])])
#     def test_WMEditTextActivity_ClickConnectWIFI(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMEditTextActivity["WMEditTextActivity"][2].keys())[
#                                                               0], \
#                                                           list(
#                                                               set.WMEditTextActivity["WMEditTextActivity"][2].values())[
#                                                               0], list(set.WMEditTextActivity.keys())[0])])
#     def test_WMEditTextActivity_ClickEliminate(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMEditTextActivity["WMEditTextActivity"][3].keys())[
#                                                               0], \
#                                                           list(
#                                                               set.WMEditTextActivity["WMEditTextActivity"][3].values())[
#                                                               0], list(set.WMEditTextActivity.keys())[0])])
#     def test_WMEditTextActivity_Back(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMEditTextActivity["WMEditTextActivity"][4].keys())[
#                                                               0], \
#                                                           list(
#                                                               set.WMEditTextActivity["WMEditTextActivity"][4].values())[
#                                                               0], list(set.WMEditTextActivity.keys())[0])])
#     def test_WMEditTextActivity_PageDisplay_End(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMSpeechSettings["WMSpeechSettings"][0].keys())[0], \
#                                                           list(set.WMSpeechSettings["WMSpeechSettings"][0].values())[0],
#                                                           list(set.WMSpeechSettings.keys())[0])])
#     def test_WMSpeechSettings_PageDisplay_Start(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMSpeechSettings["WMSpeechSettings"][1].keys())[0], \
#                                                           list(set.WMSpeechSettings["WMSpeechSettings"][1].values())[0],
#                                                           list(set.WMSpeechSettings.keys())[0])])
#     def test_WMSpeechSettings_PageDisplay_Start(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMSpeechSettings["WMSpeechSettings"][2].keys())[0], \
#                                                           list(set.WMSpeechSettings["WMSpeechSettings"][2].values())[0],
#                                                           list(set.WMSpeechSettings.keys())[0])])
#     def test_WMSpeechSettings_HelpDocument(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMSpeechSettings["WMSpeechSettings"][3].keys())[0], \
#                                                           list(set.WMSpeechSettings["WMSpeechSettings"][3].values())[0],
#                                                           list(set.WMSpeechSettings.keys())[0])])
#     def test_WMSpeechSettings_Back(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMSpeechSettings["WMSpeechSettings"][4].keys())[0], \
#                                                           list(set.WMSpeechSettings["WMSpeechSettings"][4].values())[0],
#                                                           list(set.WMSpeechSettings.keys())[0])])
#     def test_WMSpeechSettings_PageDisplay_End(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(
#                                                               set.WMSwitchVoiceDialog["WMSwitchVoiceDialog"][0].keys())[
#                                                               0], \
#                                                           list(set.WMSwitchVoiceDialog["WMSwitchVoiceDialog"][
#                                                                    0].values())[0],
#                                                           list(set.WMSwitchVoiceDialog.keys())[0])])
#     def test_WMSwitchVoiceDialog_PageDisplay_Start(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(
#                                                               set.WMSwitchVoiceDialog["WMSwitchVoiceDialog"][1].keys())[
#                                                               0], \
#                                                           list(set.WMSwitchVoiceDialog["WMSwitchVoiceDialog"][
#                                                                    1].values())[0],
#                                                           list(set.WMSwitchVoiceDialog.keys())[0])])
#     def test_WMSwitchVoiceDialog_VoiceSwitch(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(
#                                                               set.WMSwitchVoiceDialog["WMSwitchVoiceDialog"][2].keys())[
#                                                               0], \
#                                                           list(set.WMSwitchVoiceDialog["WMSwitchVoiceDialog"][
#                                                                    2].values())[0],
#                                                           list(set.WMSwitchVoiceDialog.keys())[0])])
#     def test_WMSwitchVoiceDialog_Back(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(
#                                                               set.WMSwitchVoiceDialog["WMSwitchVoiceDialog"][3].keys())[
#                                                               0], \
#                                                           list(set.WMSwitchVoiceDialog["WMSwitchVoiceDialog"][
#                                                                    3].values())[0],
#                                                           list(set.WMSwitchVoiceDialog.keys())[0])])
#     def test_WMSwitchVoiceDialog_ClickClose(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(
#                                                               set.WMSwitchVoiceDialog["WMSwitchVoiceDialog"][4].keys())[
#                                                               0], \
#                                                           list(set.WMSwitchVoiceDialog["WMSwitchVoiceDialog"][
#                                                                    4].values())[0],
#                                                           list(set.WMSwitchVoiceDialog.keys())[0])])
#     def test_WMSwitchVoiceDialog_PageDisplay_End(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMSoundSettings["WMSoundSettings"][0].keys())[0], \
#                                                           list(set.WMSoundSettings["WMSoundSettings"][0].values())[0],
#                                                           list(set.WMSoundSettings.keys())[0])])
#     def test_WMSoundSettings_PageDisplay_Start(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMSoundSettings["WMSoundSettings"][1].keys())[0], \
#                                                           list(set.WMSoundSettings["WMSoundSettings"][1].values())[0],
#                                                           list(set.WMSoundSettings.keys())[0])])
#     def test_WMSoundSettings_ClickSwitch(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMSoundSettings["WMSoundSettings"][2].keys())[0], \
#                                                           list(set.WMSoundSettings["WMSoundSettings"][2].values())[0],
#                                                           list(set.WMSoundSettings.keys())[0])])
#     def test_WMSoundSettings_MediaVolume(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMSoundSettings["WMSoundSettings"][3].keys())[0], \
#                                                           list(set.WMSoundSettings["WMSoundSettings"][3].values())[0],
#                                                           list(set.WMSoundSettings.keys())[0])])
#     def test_WMSoundSettings_ConversationVolume(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMSoundSettings["WMSoundSettings"][4].keys())[0], \
#                                                           list(set.WMSoundSettings["WMSoundSettings"][4].values())[0],
#                                                           list(set.WMSoundSettings.keys())[0])])
#     def test_WMSoundSettings_NavigationVolume(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMSoundSettings["WMSoundSettings"][5].keys())[0], \
#                                                           list(set.WMSoundSettings["WMSoundSettings"][5].values())[0],
#                                                           list(set.WMSoundSettings.keys())[0])])
#     def test_WMSoundSettings_VoiceVolume(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMSoundSettings["WMSoundSettings"][6].keys())[0], \
#                                                           list(set.WMSoundSettings["WMSoundSettings"][6].values())[0],
#                                                           list(set.WMSoundSettings.keys())[0])])
#     def test_WMSoundSettings_ClickEqualizer(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMSoundSettings["WMSoundSettings"][7].keys())[0], \
#                                                           list(set.WMSoundSettings["WMSoundSettings"][7].values())[0],
#                                                           list(set.WMSoundSettings.keys())[0])])
#     def test_WMSoundSettings_ClickSoundField(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMSoundSettings["WMSoundSettings"][8].keys())[0], \
#                                                           list(set.WMSoundSettings["WMSoundSettings"][8].values())[0],
#                                                           list(set.WMSoundSettings.keys())[0])])
#     def test_WMSoundSettings_Back(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMSoundSettings["WMSoundSettings"][9].keys())[0], \
#                                                           list(set.WMSoundSettings["WMSoundSettings"][9].values())[0],
#                                                           list(set.WMSoundSettings.keys())[0])])
#     def test_WMSoundSettings_PageDisplay_End(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMVolumeEquilizerSettings[
#                                                                    "WMVolumeEquilizerSettings"][0].keys())[0], \
#                                                           list(set.WMVolumeEquilizerSettings[
#                                                                    "WMVolumeEquilizerSettings"][0].values())[0],
#                                                           list(set.WMVolumeEquilizerSettings.keys())[0])])
#     def test_WMVolumeEquilizerSettings_PageDisplay_End(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMVolumeEquilizerSettings[
#                                                                    "WMVolumeEquilizerSettings"][
#                                                                    1].keys())[0], \
#                                                           list(set.WMVolumeEquilizerSettings[
#                                                                    "WMVolumeEquilizerSettings"][
#                                                                    1].values())[0],
#                                                           list(set.WMVolumeEquilizerSettings.keys())[0])])
#     def test_WMVolumeEquilizerSettings_EqualizerSwitch(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMVolumeEquilizerSettings[
#                                                                    "WMVolumeEquilizerSettings"][
#                                                                    10].keys())[0], \
#                                                           list(set.WMVolumeEquilizerSettings[
#                                                                    "WMVolumeEquilizerSettings"][
#                                                                    10].values())[0],
#                                                           list(set.WMVolumeEquilizerSettings.keys())[0])])
#     def test_WMVolumeEquilizerSettings_SwitchEqualizer(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMVolumeEquilizerSettings[
#                                                                    "WMVolumeEquilizerSettings"][
#                                                                    3].keys())[0], \
#                                                           list(set.WMVolumeEquilizerSettings[
#                                                                    "WMVolumeEquilizerSettings"][
#                                                                    3].values())[0],
#                                                           list(set.WMVolumeEquilizerSettings.keys())[0])])
#     def test_WMVolumeEquilizerSettings_AdjustEQ60HZ(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMVolumeEquilizerSettings[
#                                                                    "WMVolumeEquilizerSettings"][
#                                                                    4].keys())[0], \
#                                                           list(set.WMVolumeEquilizerSettings[
#                                                                    "WMVolumeEquilizerSettings"][
#                                                                    4].values())[0],
#                                                           list(set.WMVolumeEquilizerSettings.keys())[0])])
#     def test_WMVolumeEquilizerSettings_AdjustEQ125HZ(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMVolumeEquilizerSettings[
#                                                                    "WMVolumeEquilizerSettings"][
#                                                                    5].keys())[0], \
#                                                           list(set.WMVolumeEquilizerSettings[
#                                                                    "WMVolumeEquilizerSettings"][
#                                                                    5].values())[0],
#                                                           list(set.WMVolumeEquilizerSettings.keys())[0])])
#     def test_WMVolumeEquilizerSettings_AdjustEQ315HZ(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMVolumeEquilizerSettings[
#                                                                    "WMVolumeEquilizerSettings"][
#                                                                    6].keys())[0], \
#                                                           list(set.WMVolumeEquilizerSettings[
#                                                                    "WMVolumeEquilizerSettings"][
#                                                                    6].values())[0],
#                                                           list(set.WMVolumeEquilizerSettings.keys())[0])])
#     def test_WMVolumeEquilizerSettings_AdjustEQ800HZ(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMVolumeEquilizerSettings[
#                                                                    "WMVolumeEquilizerSettings"][
#                                                                    7].keys())[0], \
#                                                           list(set.WMVolumeEquilizerSettings[
#                                                                    "WMVolumeEquilizerSettings"][
#                                                                    7].values())[0],
#                                                           list(set.WMVolumeEquilizerSettings.keys())[0])])
#     def test_WMVolumeEquilizerSettings_AdjustEQ2KHZ(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMVolumeEquilizerSettings[
#                                                                    "WMVolumeEquilizerSettings"][
#                                                                    8].keys())[0], \
#                                                           list(set.WMVolumeEquilizerSettings[
#                                                                    "WMVolumeEquilizerSettings"][
#                                                                    8].values())[0],
#                                                           list(set.WMVolumeEquilizerSettings.keys())[0])])
#     def test_WMVolumeEquilizerSettings_AdjustEQ5KHZ(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMVolumeEquilizerSettings[
#                                                                    "WMVolumeEquilizerSettings"][
#                                                                    9].keys())[0], \
#                                                           list(set.WMVolumeEquilizerSettings[
#                                                                    "WMVolumeEquilizerSettings"][
#                                                                    9].values())[0],
#                                                           list(set.WMVolumeEquilizerSettings.keys())[0])])
#     def test_WMVolumeEquilizerSettings_AdjustEQ12_5KHZ(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMVolumeBalanceSettingsActivity[
#                                                                    "WMVolumeBalanceSettingsActivity"][
#                                                                    0].keys())[0], \
#                                                           list(set.WMVolumeBalanceSettingsActivity[
#                                                                    "WMVolumeBalanceSettingsActivity"][
#                                                                    0].values())[0],
#                                                           list(set.WMVolumeBalanceSettingsActivity.keys())[0])])
#     def test_WMVolumeBalanceSettingsActivity_PageDisplay_Start(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMVolumeBalanceSettingsActivity[
#                                                                    "WMVolumeBalanceSettingsActivity"][
#                                                                    2].keys())[0], \
#                                                           list(set.WMVolumeBalanceSettingsActivity[
#                                                                    "WMVolumeBalanceSettingsActivity"][
#                                                                    2].values())[0],
#                                                           list(set.WMVolumeBalanceSettingsActivity.keys())[0])])
#     def test_WMVolumeBalanceSettingsActivity_Back(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMVolumeBalanceSettingsActivity[
#                                                                    "WMVolumeBalanceSettingsActivity"][
#                                                                    3].keys())[0], \
#                                                           list(set.WMVolumeBalanceSettingsActivity[
#                                                                    "WMVolumeBalanceSettingsActivity"][
#                                                                    3].values())[0],
#                                                           list(set.WMVolumeBalanceSettingsActivity.keys())[0])])
#     def test_WMVolumeBalanceSettingsActivity_PageDisplay_End(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMGeneralSettings["WMGeneralSettings"][
#                                                                    0].keys())[0], \
#                                                           list(set.WMGeneralSettings["WMGeneralSettings"][
#                                                                    0].values())[0],
#                                                           list(set.WMGeneralSettings.keys())[0])])
#     def test_WMGeneralSettings_PageDisplay_Start(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMGeneralSettings["WMGeneralSettings"][
#                                                                    1].keys())[0], \
#                                                           list(set.WMGeneralSettings["WMGeneralSettings"][
#                                                                    1].values())[0],
#                                                           list(set.WMGeneralSettings.keys())[0])])
#     def test_WMGeneralSettings_TimeFormat(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMGeneralSettings["WMGeneralSettings"][
#                                                                    2].keys())[0], \
#                                                           list(set.WMGeneralSettings["WMGeneralSettings"][
#                                                                    2].values())[0],
#                                                           list(set.WMGeneralSettings.keys())[0])])
#     def test_WMGeneralSettings_Back(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMGeneralSettings["WMGeneralSettings"][
#                                                                    3].keys())[0], \
#                                                           list(set.WMGeneralSettings["WMGeneralSettings"][
#                                                                    3].values())[0],
#                                                           list(set.WMGeneralSettings.keys())[0])])
#     def test_WMGeneralSettings_PageDisplay_End(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMTimeFormatDialog["WMTimeFormatDialog"][
#                                                                    0].keys())[0], \
#                                                           list(set.WMTimeFormatDialog["WMTimeFormatDialog"][
#                                                                    0].values())[0],
#                                                           list(set.WMTimeFormatDialog.keys())[0])])
#     def test_WMTimeFormatDialog_PageDisplay_Start(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMTimeFormatDialog["WMTimeFormatDialog"][
#                                                                    1].keys())[0], \
#                                                           list(set.WMTimeFormatDialog["WMTimeFormatDialog"][
#                                                                    1].values())[0],
#                                                           list(set.WMTimeFormatDialog.keys())[0])])
#     def test_WMTimeFormatDialog_SwitchTimeFormat(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMTimeFormatDialog["WMTimeFormatDialog"][
#                                                                    2].keys())[0], \
#                                                           list(set.WMTimeFormatDialog["WMTimeFormatDialog"][
#                                                                    2].values())[0],
#                                                           list(set.WMTimeFormatDialog.keys())[0])])
#     def test_WMTimeFormatDialog_ClickClose(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMTimeFormatDialog["WMTimeFormatDialog"][
#                                                                    3].keys())[0], \
#                                                           list(set.WMTimeFormatDialog["WMTimeFormatDialog"][
#                                                                    3].values())[0],
#                                                           list(set.WMTimeFormatDialog.keys())[0])])
#     def test_WMTimeFormatDialog_Back(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMTimeFormatDialog["WMTimeFormatDialog"][
#                                                                    4].keys())[0], \
#                                                           list(set.WMTimeFormatDialog["WMTimeFormatDialog"][
#                                                                    4].values())[0],
#                                                           list(set.WMTimeFormatDialog.keys())[0])])
#     def test_WMTimeFormatDialog_PageDisplay_End(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMSystemSettings["WMSystemSettings"][
#                                                                    0].keys())[0], \
#                                                           list(set.WMSystemSettings["WMSystemSettings"][
#                                                                    0].values())[0],
#                                                           list(set.WMSystemSettings.keys())[0])])
#     def test_WMSystemSettings_PageDisplay_Start(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMSystemSettings["WMSystemSettings"][
#                                                                    1].keys())[0], \
#                                                           list(set.WMSystemSettings["WMSystemSettings"][
#                                                                    1].values())[0],
#                                                           list(set.WMSystemSettings.keys())[0])])
#     def test_WMSystemSettings_FunctionDemo(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMSystemSettings["WMSystemSettings"][
#                                                                    2].keys())[0], \
#                                                           list(set.WMSystemSettings["WMSystemSettings"][
#                                                                    2].values())[0],
#                                                           list(set.WMSystemSettings.keys())[0])])
#     def test_WMSystemSettings_ClickStorage(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMSystemSettings["WMSystemSettings"][
#                                                                    3].keys())[0], \
#                                                           list(set.WMSystemSettings["WMSystemSettings"][
#                                                                    3].values())[0],
#                                                           list(set.WMSystemSettings.keys())[0])])
#     def test_WMSystemSettings_ClickTBox(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMSystemSettings["WMSystemSettings"][
#                                                                    4].keys())[0], \
#                                                           list(set.WMSystemSettings["WMSystemSettings"][
#                                                                    4].values())[0],
#                                                           list(set.WMSystemSettings.keys())[0])])
#     def test_WMSystemSettings_ClickInformation(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMSystemSettings["WMSystemSettings"][
#                                                                    5].keys())[0], \
#                                                           list(set.WMSystemSettings["WMSystemSettings"][
#                                                                    5].values())[0],
#                                                           list(set.WMSystemSettings.keys())[0])])
#     def test_WMSystemSettings_CilckRecoverySystem(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMSystemSettings["WMSystemSettings"][
#                                                                    6].keys())[0], \
#                                                           list(set.WMSystemSettings["WMSystemSettings"][
#                                                                    6].values())[0],
#                                                           list(set.WMSystemSettings.keys())[0])])
#     def test_WMSystemSettings_Back(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [(
#                                                           list(set.WMSystemSettings["WMSystemSettings"][
#                                                                    7].keys())[0], \
#                                                           list(set.WMSystemSettings["WMSystemSettings"][
#                                                                    7].values())[0],
#                                                           list(set.WMSystemSettings.keys())[0])])
#     def test_WMSystemSettings_PageDisplay_End(self, action, event, page):
#         Compare(action, event, page)
# 
# # class Test_Delete_Buried_Log():
# #     @pytest.mark.parametrize('sn',
# #                              [set.Action.get_sn()])
# #     def test_Delete_buired_log(self, sn):
# #         logger.log_info("setting root partition read and write", \
# #                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
# #                         sys._getframe().f_lineno)
# #         os.system('adb root')
# #         time.sleep(random.randint(3, 5))
# #         os.system('adb -s %s shell "mount -o rw,remount /" ' % (sn))
# #         time.sleep(random.randint(3, 5))
# #         cmd = 'adb -s %s shell "%s"' % (sn, Delete_Log)
# #         logger.log_info("execute cmd is :%s" % (cmd), \
# #                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
# #                         sys._getframe().f_lineno)
# #         p_sub = subprocess.Popen(cmd, shell=True)
# #         time.sleep(random.randint(3, 5))
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
