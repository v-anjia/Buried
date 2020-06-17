# '''
# Case Vehicles Repair Test Suite
# author : antony WeiJiang
# date:2020/4/15
# '''
# import pytest
# import sys
# import os
# import time
# import random
# import pytest_html.extras
# import pytest_html.hooks
# import pytest_html.plugin
# import subprocess
# from Common import Vehicles_Repair as set
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
# buried_log = '/update/buried_Repair.log'
# buried_point = "/sdcard/Android/data/com.wm.tracker/files/temp/*"
# 
# save_data = "/update/buried_local_Repair.log"
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
#         time.sleep(random.randint(1,3))
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
# 
# 
#         time.sleep(random.randint(3,5))
# 
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
#             pass
#             # logger.log_info("delete tracker successfully", \
#             #                 sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#             #                 sys._getframe().f_lineno)
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
#     def test_Check_Report_Hide(self, count, action, event, page):
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
#         # if set.Check_Result.delete_tracker_log(set.Action.get_sn()):
#         #     logger.log_info("delete tracker successfully", \
#         #                     sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#         #                     sys._getframe().f_lineno)
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
#         # if set.Check_Result.delete_tracker_log(set.Action.get_sn()):
#         #     logger.log_info("delete tracker successfully", \
#         #                     sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#         #                     sys._getframe().f_lineno)
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
#         # if set.Check_Result.delete_tracker_log(set.Action.get_sn()):
#         #     logger.log_info("delete tracker successfully", \
#         #                     sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#         #                     sys._getframe().f_lineno)
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
# 
# 
# class Test_Check_Vehicles_Repair_Hive_Result(object):
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
#                              [(list(set.Home["Home"][0].keys())[0], \
#                                list(set.Home["Home"][0].values())[0], list(set.Home.keys())[0])])
#     def test_Foreground_Start(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Home["Home"][1].keys())[0], \
#                                list(set.Home["Home"][1].values())[0], list(set.Home.keys())[0])])
#     def test_Foreground_End(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Home["Home"][2].keys())[0], \
#                                list(set.Home["Home"][2].values())[0], list(set.Home.keys())[0])])
#     def test_Home_Start(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Home["Home"][4].keys())[0], \
#                                list(set.Home["Home"][4].values())[0], list(set.Home.keys())[0])])
#     def test_Home_startResult(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Home["Home"][5].keys())[0], \
#                                list(set.Home["Home"][5].values())[0], list(set.Home.keys())[0])])
#     def test_Home_Result(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Home["Home"][6].keys())[0], \
#                                list(set.Home["Home"][6].values())[0], list(set.Home.keys())[0])])
#     def test_Check_Click(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Home["Home"][7].keys())[0], \
#                                list(set.Home["Home"][7].values())[0], list(set.Home.keys())[0])])
#     def test_Check_Start(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Home["Home"][8].keys())[0], \
#                                list(set.Home["Home"][8].values())[0], list(set.Home.keys())[0])])
#     def test_Check_End(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Home["Home"][9].keys())[0], \
#                                list(set.Home["Home"][9].values())[0], list(set.Home.keys())[0])])
#     def test_Check_Result(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Home["Home"][10].keys())[0], \
#                                list(set.Home["Home"][10].values())[0], list(set.Home.keys())[0])])
#     def test_Check_Report_Click(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Home["Home"][11].keys())[0], \
#                                list(set.Home["Home"][11].values())[0], list(set.Home.keys())[0])])
#     def test_Check_Report_Start(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Home["Home"][12].keys())[0], \
#                                list(set.Home["Home"][12].values())[0], list(set.Home.keys())[0])])
#     def test_Check_Report_Hide(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Home["Home"][13].keys())[0], \
#                                list(set.Home["Home"][13].values())[0], list(set.Home.keys())[0])])
#     def test_Check_Report_End(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Home["Home"][14].keys())[0], \
#                                list(set.Home["Home"][14].values())[0], list(set.Home.keys())[0])])
#     def test_History(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Home["Home"][15].keys())[0], \
#                                list(set.Home["Home"][15].values())[0], list(set.Home.keys())[0])])
#     def test_Remind(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.History["History"][0].keys())[0], \
#                                list(set.History["History"][0].values())[0], list(set.History.keys())[0])])
#     def test_History_Start(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.History["History"][1].keys())[0], \
#                                list(set.History["History"][1].values())[0], list(set.History.keys())[0])])
#     def test_History_End(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.History["History"][2].keys())[0], \
#                                list(set.History["History"][2].values())[0], list(set.History.keys())[0])])
#     def test_History_Result(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Remind["Remind"][0].keys())[0], \
#                                list(set.Remind["Remind"][0].values())[0], list(set.Remind.keys())[0])])
#     def test_Remind_Start(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Remind["Remind"][1].keys())[0], \
#                                list(set.Remind["Remind"][1].values())[0], list(set.Remind.keys())[0])])
#     def test_Remind_End(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Remind["Remind"][2].keys())[0], \
#                                list(set.Remind["Remind"][2].values())[0], list(set.Remind.keys())[0])])
#     def test_Remind_Result(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Widget_maintain["Widget_maintain"][0].keys())[0], \
#                                list(set.Widget_maintain["Widget_maintain"][0].values())[0],
#                                list(set.Widget_maintain.keys())[0])])
#     def test_Widget_maintain_Click(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Widget_maintain["Widget_maintain"][1].keys())[0], \
#                                list(set.Widget_maintain["Widget_maintain"][1].values())[0],
#                                list(set.Widget_maintain.keys())[0])])
#     def test_Widget_maintain_Start(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Widget_maintain["Widget_maintain"][2].keys())[0], \
#                                list(set.Widget_maintain["Widget_maintain"][2].values())[0],
#                                list(set.Widget_maintain.keys())[0])])
#     def test_Widget_maintain_End(self, action, event, page):
#         Compare(action, event, page)
# 
# # class Test_Delete_Buried_Log():
# #     @pytest.mark.parametrize('sn',
# #                              [set.Action.get_sn()])
# #     def test_Delete_buired_log(self,sn):
# #         logger.log_info("setting root partition read and write", \
# #                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
# #                         sys._getframe().f_lineno)
# #         os.system('adb root')
# #         time.sleep(random.randint(3,5))
# #         os.system('adb -s %s shell "mount -o rw,remount /" ' %(sn))
# #         time.sleep(random.randint(3,5))
# #         cmd = 'adb -s %s shell "%s"' %(sn,Delete_Log)
# #         logger.log_info("execute cmd is :%s" %(cmd), \
# #                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
# #                         sys._getframe().f_lineno)
# #         p_sub = subprocess.Popen(cmd,shell= True)
# #         time.sleep(random.randint(3,5))
# 
# 
# 
# 
