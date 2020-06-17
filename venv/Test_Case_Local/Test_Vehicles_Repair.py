# '''
# Case System Activation Test Suite
# author : antony WeiJiang
# date:2020/3/23
# '''
#
# import pytest
# import sys
# import os
# import time
# import random
# import pytest_html.extras
# import pytest_html.hooks
# import pytest_html.plugin
# from Common import Vehicles_Repair as set
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
# class Test_Home():
#     @pytest.fixture(scope='function', autouse=True)
#     def message(self):
#         '''check test environment'''
#         logger.log_info("start Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         os.system("adb root")
#         time.sleep(random.randint(1, 3))
#         set.Action.kill_vehicles_repair_progress(sn)
#         time.sleep(random.randint(1, 3))
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
#         set.Action.kill_vehicles_repair_progress(sn)
#         time.sleep(random.randint(1, 3))
#
#     @pytest.mark.parametrize('count,action,event,page',[(random.randint(start_step,end_step),list(set.Home["Home"][0].keys())[0],\
#                                                     list(set.Home["Home"][0].values())[0],list(set.Home.keys())[0])])
#     def test_Foreground_Start(self, count, action, event, page):
#         Common(count, action, event, page,set.Home_.Foreground_Start)
#
#     @pytest.mark.parametrize('count,action,event,page',[(random.randint(start_step,end_step),list(set.Home["Home"][1].keys())[0],\
#                                                     list(set.Home["Home"][1].values())[0],list(set.Home.keys())[0])])
#     def test_Foreground_End(self, count, action, event, page):
#         Common(count, action, event, page,set.Home_.Foreground_End)
#
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Home["Home"][2].keys())[0], \
#                                list(set.Home["Home"][2].values())[0], list(set.Home.keys())[0])])
#     def test_Home_Start(self, count, action, event, page):
#         Common(count, action, event, page, set.Home_.Home_Start)
#
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Home["Home"][4].keys())[0], \
#                                list(set.Home["Home"][4].values())[0], list(set.Home.keys())[0])])
#     def test_Home_startResult(self, count, action, event, page):
#         Common(count, action, event, page, set.Home_.Home_startResult)
#
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Home["Home"][5].keys())[0], \
#                                list(set.Home["Home"][5].values())[0], list(set.Home.keys())[0])])
#     def test_Home_Result(self, count, action, event, page):
#         Common(count, action, event, page, set.Home_.Home_Result)
#
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Home["Home"][6].keys())[0], \
#                                list(set.Home["Home"][6].values())[0], list(set.Home.keys())[0])])
#     def test_Check_Click(self, count, action, event, page):
#         Common(count, action, event, page, set.Home_.Check_Click)
#
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Home["Home"][7].keys())[0], \
#                                list(set.Home["Home"][7].values())[0], list(set.Home.keys())[0])])
#     def test_Check_Start(self, count, action, event, page):
#         Common(count, action, event, page, set.Home_.Check_Start)
#
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Home["Home"][8].keys())[0], \
#                                list(set.Home["Home"][8].values())[0], list(set.Home.keys())[0])])
#     def test_Check_End(self, count, action, event, page):
#         Common(count, action, event, page, set.Home_.Check_End)
#
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Home["Home"][9].keys())[0], \
#                                list(set.Home["Home"][9].values())[0], list(set.Home.keys())[0])])
#     def test_Check_Result(self, count, action, event, page):
#         Common(count, action, event, page, set.Home_.Check_Result)
#
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Home["Home"][10].keys())[0], \
#                                list(set.Home["Home"][10].values())[0], list(set.Home.keys())[0])])
#     def test_Check_Report_Click(self, count, action, event, page):
#         Common(count, action, event, page, set.Home_.Check_Report_Click)
#
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Home["Home"][11].keys())[0], \
#                                list(set.Home["Home"][11].values())[0], list(set.Home.keys())[0])])
#     def test_Check_Report_Start(self, count, action, event, page):
#         Common(count, action, event, page, set.Home_.Check_Report_Start)
#
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Home["Home"][12].keys())[0], \
#                                list(set.Home["Home"][12].values())[0], list(set.Home.keys())[0])])
#     def test_Check_Report_Start(self, count, action, event, page):
#         Common(count, action, event, page, set.Home_.Check_Report_Hide)
#
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Home["Home"][13].keys())[0], \
#                                list(set.Home["Home"][13].values())[0], list(set.Home.keys())[0])])
#     def test_Check_Report_End(self, count, action, event, page):
#         Common(count, action, event, page, set.Home_.Check_Report_End)
#
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Home["Home"][14].keys())[0], \
#                                list(set.Home["Home"][14].values())[0], list(set.Home.keys())[0])])
#     def test_History(self, count, action, event, page):
#         Common(count, action, event, page, set.Home_.History)
#
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Home["Home"][15].keys())[0], \
#                                list(set.Home["Home"][15].values())[0], list(set.Home.keys())[0])])
#     def test_Remind(self, count, action, event, page):
#         Common(count, action, event, page, set.Home_.Remind)
#
# class Test_History():
#     @pytest.fixture(scope='function', autouse=True)
#     def message(self):
#         '''check test environment'''
#         logger.log_info("start Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         os.system("adb root")
#         time.sleep(random.randint(1, 3))
#         set.Action.kill_vehicles_repair_progress(sn)
#         time.sleep(random.randint(1, 3))
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
#         set.Action.kill_vehicles_repair_progress(sn)
#         time.sleep(random.randint(1, 3))
#
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.History["History"][0].keys())[0], \
#                                list(set.History["History"][0].values())[0], list(set.History.keys())[0])])
#     def test_History_Start(self, count, action, event, page):
#         Common(count, action, event, page, set.History_.History_Start)
#
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.History["History"][1].keys())[0], \
#                                list(set.History["History"][1].values())[0], list(set.History.keys())[0])])
#     def test_History_End(self, count, action, event, page):
#         Common(count, action, event, page, set.History_.History_End)
#
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.History["History"][2].keys())[0], \
#                                list(set.History["History"][2].values())[0], list(set.History.keys())[0])])
#     def test_History_Result(self, count, action, event, page):
#         Common(count, action, event, page, set.History_.History_Result,flag=2)
#
# class Test_Remind():
#     @pytest.fixture(scope='function', autouse=True)
#     def message(self):
#         '''check test environment'''
#         logger.log_info("start Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         os.system("adb root")
#         time.sleep(random.randint(1, 3))
#         set.Action.kill_vehicles_repair_progress(sn)
#         time.sleep(random.randint(1, 3))
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
#         set.Action.kill_vehicles_repair_progress(sn)
#         time.sleep(random.randint(1, 3))
#         set.Action.kill_vehicles_repair_progress(sn)
#         time.sleep(random.randint(1, 3))
#
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Remind["Remind"][0].keys())[0], \
#                                list(set.Remind["Remind"][0].values())[0], list(set.Remind.keys())[0])])
#     def test_Remind_Start(self, count, action, event, page):
#         Common(count, action, event, page, set.Remind_.Remind_Start)
#
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Remind["Remind"][1].keys())[0], \
#                                list(set.Remind["Remind"][1].values())[0], list(set.Remind.keys())[0])])
#     def test_Remind_End(self, count, action, event, page):
#         Common(count, action, event, page, set.Remind_.Remind_End)
#
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Remind["Remind"][2].keys())[0], \
#                                list(set.Remind["Remind"][2].values())[0], list(set.Remind.keys())[0])])
#     def test_Remind_Result(self, count, action, event, page):
#         Common(count, action, event, page, set.Remind_.Remind_Result,flag=2)
#
# class Test_Widget_maintain():
#     @pytest.fixture(scope='function', autouse=True)
#     def message(self):
#         '''check test environment'''
#         logger.log_info("start Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         os.system("adb root")
#         time.sleep(random.randint(1, 3))
#         set.Action.kill_vehicles_repair_progress(sn)
#         time.sleep(random.randint(1, 3))
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
#         set.Action.kill_vehicles_repair_progress(sn)
#         time.sleep(random.randint(1, 3))
#         set.Action.kill_vehicles_repair_progress(sn)
#         time.sleep(random.randint(1, 3))
#
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Widget_maintain["Widget_maintain"][0].keys())[0], \
#                                list(set.Widget_maintain["Widget_maintain"][0].values())[0], list(set.Widget_maintain.keys())[0])])
#     def test_Widget_maintain_Click(self, count, action, event, page):
#         Common(count, action, event, page, set.Widget_maintain_.Widget_maintain_Click)
#
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step),
#                                list(set.Widget_maintain["Widget_maintain"][1].keys())[0], \
#                                list(set.Widget_maintain["Widget_maintain"][1].values())[0],
#                                list(set.Widget_maintain.keys())[0])])
#     def test_Widget_maintain_Start(self, count, action, event, page):
#         Common(count, action, event, page, set.Widget_maintain_.Widget_maintain_Start)
#
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step),
#                                list(set.Widget_maintain["Widget_maintain"][2].keys())[0], \
#                                list(set.Widget_maintain["Widget_maintain"][2].values())[0],
#                                list(set.Widget_maintain.keys())[0])])
#     def test_Widget_maintain_End(self, count, action, event, page):
#         Common(count, action, event, page, set.Widget_maintain_.Widget_maintain_End)