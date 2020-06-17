# '''
# Case Settings Test Suite
# author : antony WeiJiang
# date:2020/1/7
# '''
# import pytest
# import sys
# import os
# import time
# import random
# import pytest_html.extras
# import pytest_html.hooks
# import pytest_html.plugin
# from Common import Setting as set
# from Common import Common as co
# from log import  logger as loger
# # print(list(set.Setting_Actions["settings"][3].keys())[0])
# logger = loger.Current_Module()
#
# adb_object = co.ADB_SN()
#
# sn = adb_object.check_adb_device_isalive()
# set.Action.set_sn(sn)
# start_step = 2
# end_step = 2
# # set.Action.set_ui_object(set.Action.get_sn())
# # uiautomator_object = set.Action.get_ui_object()
#
# def Common(count, action, event, page,function_name= [], flag = 1):
#     try:
#         logger.log_info("start test %s  function,total count is %s" % (function_name.__name__ , count), \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno
#                         )
#         Total = 0
#         Passed = 0
#         Failed = 0
#         logger.log_info("cycle is %s" % (count), \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         for i in range(1, count, 1):
#             # set.Check_Setting_Actions
#             logger.log_debug("sn is :%s" % (set.Action.get_sn()), \
#                              sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                              sys._getframe().f_lineno)
#             function_name(set.Action.get_sn())
#             time.sleep(random.randint(5,10))
#             # Result_lvlog = int(function_name(set.Action.get_sn()))
#             Result_tracker = int(set.Check_Result.check_android_tracker_log(set.Action.get_sn(), action, event, page))
#             if flag != 1:
#                 Result_tracker = Result_tracker / flag
#             logger.log_info("Result_tracker is %s" %(Result_tracker), \
#                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                             sys._getframe().f_lineno)
#             print("Result_tracker is %s" %(Result_tracker))
#             if i == Result_tracker:
#                 Passed = Passed + 1
#             else:
#                 Failed = Failed + 1
#
#         Total = Passed + Failed
#         logger.log_debug("Total is :%s;Passed is :%s;Failed is :%s" % (Total, Passed, Failed), \
#                          sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                          sys._getframe().f_lineno)
#     except Exception as e:
#         logger.log_error("%s" % (e), \
#                          sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                          sys._getframe().f_lineno)
#
#     if Passed == Total:
#         logger.log_info("compare data successfully", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         assert True
#     else:
#         logger.log_error("compare data fail", \
#                          sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                          sys._getframe().f_lineno)
#         assert False
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
#         if set.Check_Result.delete_tracker_log(set.Action.get_sn()):
#             logger.log_info("delete tracker successfully", \
#                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                             sys._getframe().f_lineno)
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
#         if set.Check_Result.delete_tracker_log(set.Action.get_sn()):
#             logger.log_info("delete tracker successfully", \
#                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                             sys._getframe().f_lineno)
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
#         if set.Check_Result.delete_tracker_log(set.Action.get_sn()):
#             logger.log_info("deltet tracker successfully", \
#                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                             sys._getframe().f_lineno)
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
#         if set.Check_Result.delete_tracker_log(set.Action.get_sn()):
#             logger.log_info("deltet tracker successfully", \
#                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                             sys._getframe().f_lineno)
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
#         if set.Check_Result.delete_tracker_log(set.Action.get_sn()):
#             logger.log_info("delete tracker successfully", \
#                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                             sys._getframe().f_lineno)
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
#         if set.Check_Result.delete_tracker_log(set.Action.get_sn()):
#             logger.log_info("delete tracker successfully", \
#                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                             sys._getframe().f_lineno)
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
#         if set.Check_Result.delete_tracker_log(set.Action.get_sn()):
#             logger.log_info("delete tracker successfully", \
#                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                             sys._getframe().f_lineno)
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
#         if set.Check_Result.delete_tracker_log(set.Action.get_sn()):
#             logger.log_info("delete tracker successfully", \
#                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                             sys._getframe().f_lineno)
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
#         if set.Check_Result.delete_tracker_log(set.Action.get_sn()):
#             logger.log_info("delete tracker successfully", \
#                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                             sys._getframe().f_lineno)
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
#         if set.Check_Result.delete_tracker_log(set.Action.get_sn()):
#             logger.log_info("delete tracker successfully", \
#                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                             sys._getframe().f_lineno)
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
#         if set.Check_Result.delete_tracker_log(set.Action.get_sn()):
#             logger.log_info("delete tracker successfully", \
#                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                             sys._getframe().f_lineno)
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
#         if set.Check_Result.delete_tracker_log(set.Action.get_sn()):
#             logger.log_info("delete tracker successfully", \
#                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                             sys._getframe().f_lineno)
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
#         if set.Check_Result.delete_tracker_log(set.Action.get_sn()):
#             logger.log_info("delete tracker successfully", \
#                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                             sys._getframe().f_lineno)
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
#         if set.Check_Result.delete_tracker_log(set.Action.get_sn()):
#             logger.log_info("delete tracker successfully", \
#                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                             sys._getframe().f_lineno)
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
#         if set.Check_Result.delete_tracker_log(set.Action.get_sn()):
#             logger.log_info("delete tracker successfully", \
#                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                             sys._getframe().f_lineno)
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
