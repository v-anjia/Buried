# '''
# Case System Desktop Test Suite
# author : antony WeiJiang
# date:2020/4/7
# '''
# import pytest
# import sys
# import os
# import time
# import random
# import pytest_html.extras
# import pytest_html.hooks
# import pytest_html.plugin
# from Common import System_Desktop as set
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
#             # Result_lvlog = int(function_name(set.Action.get_sn()))
#             Result_tracker = int(set.Check_Result.check_android_tracker_log(set.Action.get_sn(), action, event,page))
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
# class Test_Default():
#     @pytest.fixture(scope='function', autouse=True)
#     def message(self):
#         '''check test environment'''
#         logger.log_info("start Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         os.system("adb root")
#         time.sleep(random.randint(1, 3))
#         set.Action.enter_system_desktop(sn)
#         time.sleep(random.randint(3, 5))
#         # if set.Check_Result.deltet_lvlog(set.Action.get_sn()):
#         #     logger.log_info("delete lvlog successfully", \
#         #                     sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#         #                     sys._getframe().f_lineno)
#         if set.Check_Result.delete_tracker_log(set.Action.get_sn()):
#             logger.log_info("delete tracker successfully", \
#                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                             sys._getframe().f_lineno)
#         yield
#         logger.log_info("end Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         logger.log_info("kill vehicles repair progress ", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         os.system("adb root")
#         time.sleep(random.randint(1, 3))
#         set.Action.enter_system_desktop(sn)
#
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Default["Default"][0].keys())[0], \
#                                list(set.Default["Default"][0].values())[0], "Default")])
#     def test_startMap(self, count, action, event, page):
#         Common(count, action, event, page, set.Default_.startMap)
#
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Default["Default"][1].keys())[0], \
#                                list(set.Default["Default"][1].values())[0], "Default")])
#     def test_startEnergy(self, count, action, event, page):
#         Common(count, action, event, page, set.Default_.startEnergy)
#
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Default["Default"][2].keys())[0], \
#                                list(set.Default["Default"][2].values())[0], "Default")])
#     def test_startMusic(self, count, action, event, page):
#         Common(count, action, event, page, set.Default_.startMusic)
#
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Default["Default"][3].keys())[0], \
#                                list(set.Default["Default"][3].values())[0], "Default")])
#     def test_startBtPhone(self, count, action, event, page):
#         Common(count, action, event, page, set.Default_.startBtPhone)
#
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Default["Default"][4].keys())[0], \
#                                list(set.Default["Default"][4].values())[0], "Default")])
#     def test_startDVR(self, count, action, event, page):
#         # Common(count, action, event, page, set.Default_.startDVR)
#         pass
#
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Default["Default"][5].keys())[0], \
#                                list(set.Default["Default"][5].values())[0], "Default")])
#     def test_startFM(self, count, action, event, page):
#         Common(count, action, event, page, set.Default_.startFM)
#
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Default["Default"][6].keys())[0], \
#                                list(set.Default["Default"][6].values())[0], "Default")])
#     def test_startSetting(self, count, action, event, page):
#         Common(count, action, event, page, set.Default_.startSetting)
#
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Default["Default"][7].keys())[0], \
#                                list(set.Default["Default"][7].values())[0], "Default")])
#     def test_startWeChat(self, count, action, event, page):
#         Common(count, action, event, page, set.Default_.startWeChat)
#
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Default["Default"][8].keys())[0], \
#                                list(set.Default["Default"][8].values())[0], "Default")])
#     def test_startMiant(self, count, action, event, page):
#         Common(count, action, event, page, set.Default_.startMiant)
#
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Default["Default"][9].keys())[0], \
#                                list(set.Default["Default"][9].values())[0], "Default")])
#     def test_startMiant(self, count, action, event, page):
#         Common(count, action, event, page, set.Default_.startVideo)
#
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Default["Default"][10].keys())[0], \
#                                list(set.Default["Default"][10].values())[0], "Default")])
#     def test_startCarControl(self, count, action, event, page):
#         Common(count, action, event, page, set.Default_.startCarControl)
#
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Default["Default"][11].keys())[0], \
#                                list(set.Default["Default"][11].values())[0], "Default")])
#     def test_startAQY(self, count, action, event, page):
#         Common(count, action, event, page, set.Default_.startAQY)
#
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Default["Default"][12].keys())[0], \
#                                list(set.Default["Default"][12].values())[0], "Default")])
#     def test_startAVM(self, count, action, event, page):
#         Common(count, action, event, page, set.Default_.startAVM)
#
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Default["Default"][13].keys())[0], \
#                                list(set.Default["Default"][13].values())[0], "Default")])
#     def test_startAudioBook(self, count, action, event, page):
#         Common(count, action, event, page, set.Default_.startAudioBook)
#
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Default["Default"][14].keys())[0], \
#                                list(set.Default["Default"][14].values())[0], "Default")])
#     def test_startSkinStore(self, count, action, event, page):
#         Common(count, action, event, page, set.Default_.startSkinStore)
#
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Default["Default"][15].keys())[0], \
#                                list(set.Default["Default"][15].values())[0], "Default")])
#     def test_startMiJia(self, count, action, event, page):
#         Common(count, action, event, page, set.Default_.startMiJia)
#
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Default["Default"][16].keys())[0], \
#                                list(set.Default["Default"][16].values())[0], "Default")])
#     def test_startWeMeet(self, count, action, event, page):
#         Common(count, action, event, page, set.Default_.startWeMeet)
#
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Default["Default"][17].keys())[0], \
#                                list(set.Default["Default"][17].values())[0], "Default")])
#     def test_EnterWidgetPage(self, count, action, event, page):
#         Common(count, action, event, page, set.Default_.EnterWidgetPage)
#
#
#
# class Test_Widget():
#     @pytest.fixture(scope='function', autouse=True)
#     def message(self):
#         '''check test environment'''
#         logger.log_info("start Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         os.system("adb root")
#         time.sleep(random.randint(1, 3))
#         set.Action.enter_system_desktop(sn)
#         time.sleep(random.randint(3, 5))
#         # if set.Check_Result.deltet_lvlog(set.Action.get_sn()):
#         #     logger.log_info("delete lvlog successfully", \
#         #                     sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#         #                     sys._getframe().f_lineno)
#         if set.Check_Result.delete_tracker_log(set.Action.get_sn()):
#             logger.log_info("delete tracker successfully", \
#                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                             sys._getframe().f_lineno)
#         yield
#         logger.log_info("end Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         logger.log_info("kill vehicles repair progress ", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         os.system("adb root")
#         time.sleep(random.randint(1, 3))
#         set.Action.enter_system_desktop(sn)
#         time.sleep(random.randint(3, 5))
#
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Widget["Widget"][0].keys())[0], \
#                                list(set.Widget["Widget"][0].values())[0], list(set.Widget.keys())[0])])
#     def test_EnterWidgetPage(self, count, action, event, page):
#         Common(count, action, event, page, set.Widget_.EnterDefaultPage)
#
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Widget["Widget"][1].keys())[0], \
#                                list(set.Widget["Widget"][1].values())[0], list(set.Widget.keys())[0])])
#     def test_showDefaultPage(self, count, action, event, page):
#         Common(count, action, event, page, set.Widget_.showDefaultPage)
#
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Widget["Widget"][2].keys())[0], \
#                                list(set.Widget["Widget"][2].values())[0], list(set.Widget.keys())[0])])
#     def test_editingWidget_Start(self, count, action, event, page):
#         Common(count, action, event, page, set.Widget_.editingWidget_Start)
#
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Widget["Widget"][3].keys())[0], \
#                                list(set.Widget["Widget"][3].values())[0], list(set.Widget.keys())[0])])
#     def test_editingWidget_End(self, count, action, event, page):
#         Common(count, action, event, page, set.Widget_.editingWidget_End)
#
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Widget["Widget"][4].keys())[0], \
#                                list(set.Widget["Widget"][4].values())[0], list(set.Widget.keys())[0])])
#     def test_EditApp(self, count, action, event, page):
#         Common(count, action, event, page, set.Widget_.EditApp)
#
#
#
#
#
#
#
#
#
