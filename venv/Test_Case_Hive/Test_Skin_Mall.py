# '''
# Case Skin Mall Test Suite
# author : antony WeiJiang
# date:2020/3/25
# '''
# import pytest
# import sys
# import os
# import time
# import subprocess
# import random
# import pytest_html.extras
# import pytest_html.hooks
# import pytest_html.plugin
# from Common import Skin_Mall as set
# from Common import Common as co
# from log import  logger as loger
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
# buried_log = '/update/buried_Skin_Mall.log'
# 
# buried_point = "/sdcard/Android/data/com.wm.tracker/files/temp/*"
# 
# save_data = "/update/buried_local_Skin_Mall.log"
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
# 
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
# class Test_Index():
#     @pytest.fixture(scope='function', autouse=True)
#     def message(self):
#         '''check test environment'''
#         logger.log_info("start Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         os.system("adb root")
#         time.sleep(random.randint(1, 3))
#         set.Action.kill_skill_mall_progress(sn)
#         time.sleep(random.randint(3, 5))
#         set.Action.kill_skill_mall_progress(sn)
#         time.sleep(random.randint(3, 5))
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
#         set.Action.kill_skill_mall_progress(sn)
#         time.sleep(random.randint(3, 5))
#         set.Action.kill_skill_mall_progress(sn)
#         time.sleep(random.randint(3, 5))
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Index["Index"][0].keys())[0], \
#                                list(set.Index["Index"][0].values())[0], list(set.Index.keys())[0])])
#     def test_LifeCycle_Start(self, count, action, event, page):
#         Common(count, action, event, page, set.Index_.LifeCycle_Start)
# 
#     @pytest.mark.parametrize('count,action,event,page',[(random.randint(start_step,end_step),list(set.Index["Index"][8].keys())[0],\
#                                                     list(set.Index["Index"][8].values())[0],"Unknown")])
#     def test_Open_App(self, count, action, event, page):
#         Common(count, action, event, page,set.Index_.Open_App)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Index["Index"][1].keys())[0], \
#                                list(set.Index["Index"][1].values())[0], list(set.Index.keys())[0])])
#     def test_Back(self, count, action, event, page):
#         Common(count, action, event, page, set.Index_.Back)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Index["Index"][2].keys())[0], \
#                                list(set.Index["Index"][2].values())[0], list(set.Index.keys())[0])])
#     def test_Review_Start(self, count, action, event, page):
#         Common(count, action, event, page, set.Index_.Review_Start)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Index["Index"][3].keys())[0], \
#                                list(set.Index["Index"][3].values())[0], list(set.Index.keys())[0])])
#     def test_Review_End(self, count, action, event, page):
#         Common(count, action, event, page, set.Index_.Review_End)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Index["Index"][4].keys())[0], \
#                                list(set.Index["Index"][4].values())[0], list(set.Index.keys())[0])])
#     def test_Recommend(self, count, action, event, page):
#         Common(count, action, event, page, set.Index_.Recommend)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Index["Index"][5].keys())[0], \
#                                list(set.Index["Index"][5].values())[0], list(set.Index.keys())[0])])
#     def test_Manager(self, count, action, event, page):
#         Common(count, action, event, page, set.Index_.Manager)
# 
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Index["Index"][6].keys())[0], \
#                                list(set.Index["Index"][6].values())[0], list(set.Index.keys())[0])])
#     def test_Order(self, count, action, event, page):
#         Common(count, action, event, page, set.Index_.Order)
# 
# class Test_Recommend():
#     @pytest.fixture(scope='function', autouse=True)
#     def message(self):
#         '''check test environment'''
#         logger.log_info("start Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         os.system("adb root")
#         time.sleep(random.randint(1, 3))
#         set.Action.kill_skill_mall_progress(sn)
#         time.sleep(random.randint(3, 5))
#         set.Action.kill_skill_mall_progress(sn)
#         time.sleep(random.randint(3, 5))
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
#         set.Action.kill_skill_mall_progress(sn)
#         time.sleep(random.randint(3, 5))
#         set.Action.kill_skill_mall_progress(sn)
#         time.sleep(random.randint(3, 5))
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Recommend["Recommend"][0].keys())[0], \
#                                list(set.Recommend["Recommend"][0].values())[0], list(set.Recommend.keys())[0])])
#     def test_Review_Start(self, count, action, event, page):
#         Common(count, action, event, page, set.Recommend_.Review_Start)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Recommend["Recommend"][1].keys())[0], \
#                                list(set.Recommend["Recommend"][1].values())[0], list(set.Recommend.keys())[0])])
#     def test_Review_End(self, count, action, event, page):
#         Common(count, action, event, page, set.Recommend_.Review_End)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Recommend["Recommend"][2].keys())[0], \
#                                list(set.Recommend["Recommend"][2].values())[0], list(set.Recommend.keys())[0])])
#     def test_SkinItem(self, count, action, event, page):
#         Common(count, action, event, page, set.Recommend_.SkinItem)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Recommend["Recommend"][3].keys())[0], \
#                                list(set.Recommend["Recommend"][3].values())[0], list(set.Recommend.keys())[0])])
#     def test_Refresh(self, count, action, event, page):
#         Common(count, action, event, page, set.Recommend_.Refresh)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Recommend["Recommend"][4].keys())[0], \
#                                list(set.Recommend["Recommend"][4].values())[0], list(set.Recommend.keys())[0])])
#     def test_LoadMore(self, count, action, event, page):
#         Common(count, action, event, page, set.Recommend_.LoadMore)
# 
# class Test_SkinManager():
#     @pytest.fixture(scope='function', autouse=True)
#     def message(self):
#         '''check test environment'''
#         logger.log_info("start Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         os.system("adb root")
#         time.sleep(random.randint(1, 3))
#         set.Action.kill_skill_mall_progress(sn)
#         time.sleep(random.randint(3, 5))
#         set.Action.kill_skill_mall_progress(sn)
#         time.sleep(random.randint(3, 5))
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
#         set.Action.kill_skill_mall_progress(sn)
#         time.sleep(random.randint(3, 5))
#         set.Action.kill_skill_mall_progress(sn)
#         time.sleep(random.randint(3, 5))
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.SkinManager["SkinManager"][0].keys())[0], \
#                                list(set.SkinManager["SkinManager"][0].values())[0], list(set.SkinManager.keys())[0])])
#     def test_Review_Start(self, count, action, event, page):
#         Common(count, action, event, page, set.SkinManager_.Review_Start)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.SkinManager["SkinManager"][1].keys())[0], \
#                                list(set.SkinManager["SkinManager"][1].values())[0], list(set.SkinManager.keys())[0])])
#     def test_Review_End(self, count, action, event, page):
#         Common(count, action, event, page, set.SkinManager_.Review_End)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.SkinManager["SkinManager"][2].keys())[0], \
#                                list(set.SkinManager["SkinManager"][2].values())[0], list(set.SkinManager.keys())[0])])
#     def test_SkinItem(self, count, action, event, page):
#         Common(count, action, event, page, set.SkinManager_.SkinItem)
# 
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.SkinManager["SkinManager"][3].keys())[0], \
#                                list(set.SkinManager["SkinManager"][3].values())[0], list(set.SkinManager.keys())[0])])
#     def test_Remove(self, count, action, event, page):
#         Common(count, action, event, page, set.SkinManager_.Remove)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.SkinManager["SkinManager"][4].keys())[0], \
#                                list(set.SkinManager["SkinManager"][4].values())[0], list(set.SkinManager.keys())[0])])
#     def test_RemoveDialog_Start(self, count, action, event, page):
#         Common(count, action, event, page, set.SkinManager_.RemoveDialog_Start)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.SkinManager["SkinManager"][5].keys())[0], \
#                                list(set.SkinManager["SkinManager"][5].values())[0], list(set.SkinManager.keys())[0])])
#     def test_RemoveDialog_Click_Remove(self, count, action, event, page):
#         Common(count, action, event, page, set.SkinManager_.RemoveDialog_Click_Remove)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.SkinManager["SkinManager"][6].keys())[0], \
#                                list(set.SkinManager["SkinManager"][6].values())[0], list(set.SkinManager.keys())[0])])
#     def test_RemoveDialog_Click_Cancel(self, count, action, event, page):
#         Common(count, action, event, page, set.SkinManager_.RemoveDialog_Click_Cancel)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.SkinManager["SkinManager"][7].keys())[0], \
#                                list(set.SkinManager["SkinManager"][7].values())[0], list(set.SkinManager.keys())[0])])
#     def test_RemoveDialog_End(self, count, action, event, page):
#         Common(count, action, event, page, set.SkinManager_.RemoveDialog_End)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.SkinManager["SkinManager"][8].keys())[0], \
#                                list(set.SkinManager["SkinManager"][8].values())[0], list(set.SkinManager.keys())[0])])
#     def test_Download_Click(self, count, action, event, page):
#         Common(count, action, event, page, set.SkinManager_.Download_Click)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.SkinManager["SkinManager"][9].keys())[0], \
#                                list(set.SkinManager["SkinManager"][9].values())[0], list(set.SkinManager.keys())[0])])
#     def test_Download_Start(self, count, action, event, page):
#         Common(count, action, event, page, set.SkinManager_.Download_Start)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.SkinManager["SkinManager"][10].keys())[0], \
#                                list(set.SkinManager["SkinManager"][10].values())[0], list(set.SkinManager.keys())[0])])
#     def test_Cancel(self, count, action, event, page):
#         Common(count, action, event, page, set.SkinManager_.Cancel)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.SkinManager["SkinManager"][11].keys())[0], \
#                                list(set.SkinManager["SkinManager"][11].values())[0], list(set.SkinManager.keys())[0])])
#     def test_Use(self, count, action, event, page):
#         Common(count, action, event, page, set.SkinManager_.Use)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.SkinManager["SkinManager"][12].keys())[0], \
#                                list(set.SkinManager["SkinManager"][12].values())[0], list(set.SkinManager.keys())[0])])
#     def test_UseDialog_Start(self, count, action, event, page):
#         Common(count, action, event, page, set.SkinManager_.UseDialog_Start)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.SkinManager["SkinManager"][13].keys())[0], \
#                                list(set.SkinManager["SkinManager"][13].values())[0], list(set.SkinManager.keys())[0])])
#     def test_UseDialog_Use(self, count, action, event, page):
#         Common(count, action, event, page, set.SkinManager_.UseDialog_Use)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.SkinManager["SkinManager"][14].keys())[0], \
#                                list(set.SkinManager["SkinManager"][14].values())[0], list(set.SkinManager.keys())[0])])
#     def test_UseDialog_Cancel(self, count, action, event, page):
#         Common(count, action, event, page, set.SkinManager_.UseDialog_Cancel)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.SkinManager["SkinManager"][15].keys())[0], \
#                                list(set.SkinManager["SkinManager"][15].values())[0], list(set.SkinManager.keys())[0])])
#     def test_UseDialog_End(self, count, action, event, page):
#         Common(count, action, event, page, set.SkinManager_.UseDialog_End)
# 
# class Test_Detail():
#     @pytest.fixture(scope='function', autouse=True)
#     def message(self):
#         '''check test environment'''
#         logger.log_info("start Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         os.system("adb root")
#         time.sleep(random.randint(1, 3))
#         set.Action.kill_skill_mall_progress(sn)
#         time.sleep(random.randint(3, 5))
#         set.Action.kill_skill_mall_progress(sn)
#         time.sleep(random.randint(3, 5))
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
#         set.Action.kill_skill_mall_progress(sn)
#         time.sleep(random.randint(3, 5))
#         set.Action.kill_skill_mall_progress(sn)
#         time.sleep(random.randint(3, 5))
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Detail["Detail"][0].keys())[0], \
#                                list(set.Detail["Detail"][0].values())[0], list(set.Detail.keys())[0])])
#     def test_LifeCycle(self, count, action, event, page):
#         Common(count, action, event, page, set.Detail_.LifeCycle)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Detail["Detail"][1].keys())[0], \
#                                list(set.Detail["Detail"][1].values())[0], list(set.Detail.keys())[0])])
#     def test_Back(self, count, action, event, page):
#         Common(count, action, event, page, set.Detail_.Back)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Detail["Detail"][2].keys())[0], \
#                                list(set.Detail["Detail"][2].values())[0], list(set.Detail.keys())[0])])
#     def test_Review_Start(self, count, action, event, page):
#         Common(count, action, event, page, set.Detail_.Review_Start)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Detail["Detail"][3].keys())[0], \
#                                list(set.Detail["Detail"][3].values())[0], list(set.Detail.keys())[0])])
#     def test_Review_End(self, count, action, event, page):
#         Common(count, action, event, page, set.Detail_.Review_End)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Detail["Detail"][4].keys())[0], \
#                                list(set.Detail["Detail"][4].values())[0], list(set.Detail.keys())[0])])
#     def test_Buy_Click(self, count, action, event, page):
#         Common(count, action, event, page, set.Detail_.Buy_Click)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Detail["Detail"][5].keys())[0], \
#                                list(set.Detail["Detail"][5].values())[0], list(set.Detail.keys())[0])])
#     def test_BuyBack_Click(self, count, action, event, page):
#         Common(count, action, event, page, set.Detail_.BuyBack_Click)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Detail["Detail"][9].keys())[0], \
#                                list(set.Detail["Detail"][9].values())[0], list(set.Detail.keys())[0])])
#     def test_author(self, count, action, event, page):
#         Common(count, action, event, page, set.Detail_.author)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Detail["Detail"][14].keys())[0], \
#                                list(set.Detail["Detail"][14].values())[0], list(set.Detail.keys())[0])])
#     def test_Use_Click(self, count, action, event, page):
#         Common(count, action, event, page, set.Detail_.Use_Click)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Detail["Detail"][15].keys())[0], \
#                                list(set.Detail["Detail"][15].values())[0], list(set.Detail.keys())[0])])
#     def test_UseDialog_Start(self, count, action, event, page):
#         Common(count, action, event, page, set.Detail_.UseDialog_Start)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Detail["Detail"][16].keys())[0], \
#                                list(set.Detail["Detail"][16].values())[0], list(set.Detail.keys())[0])])
#     def test_UseDialog_Click_Use(self, count, action, event, page):
#         Common(count, action, event, page, set.Detail_.UseDialog_Click_Use)
# 
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Detail["Detail"][17].keys())[0], \
#                                list(set.Detail["Detail"][17].values())[0], list(set.Detail.keys())[0])])
#     def test_UseDialog_Click_Cancel(self, count, action, event, page):
#         Common(count, action, event, page, set.Detail_.UseDialog_Click_Cancel)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Detail["Detail"][18].keys())[0], \
#                                list(set.Detail["Detail"][18].values())[0], list(set.Detail.keys())[0])])
#     def test_UseDialog_End(self, count, action, event, page):
#         Common(count, action, event, page, set.Detail_.UseDialog_End)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.Detail["Detail"][20].keys())[0], \
#                                list(set.Detail["Detail"][20].values())[0], list(set.Detail.keys())[0])])
#     def test_LifeCycle_End(self, count, action, event, page):
#         Common(count, action, event, page, set.Detail_.LifeCycle_End)
# 
# class Test_ConfirmOrder():
#     @pytest.fixture(scope='function', autouse=True)
#     def message(self):
#         '''check test environment'''
#         logger.log_info("start Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         os.system("adb root")
#         time.sleep(random.randint(1, 3))
#         set.Action.kill_skill_mall_progress(sn)
#         time.sleep(random.randint(3, 5))
#         set.Action.kill_skill_mall_progress(sn)
#         time.sleep(random.randint(3, 5))
#         set.Action.kill_skill_mall_progress(sn)
#         time.sleep(random.randint(3, 5))
#         # if set.Check_Result.deltet_lvlog(set.Action.get_sn()):
#         #     logger.log_info("delete lvlog successfully", \
#         #                     sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#         #                     sys._getframe().f_lineno)
#         set.Action.enter_pay_page(sn)
#         time.sleep(random.randint(1,3))
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
#         set.Action.kill_skill_mall_progress(sn)
#         time.sleep(random.randint(3, 5))
#         set.Action.kill_skill_mall_progress(sn)
#         time.sleep(random.randint(3, 5))
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.ConfirmOrder["ConfirmOrder"][0].keys())[0], \
#                                list(set.ConfirmOrder["ConfirmOrder"][0].values())[0], list(set.ConfirmOrder.keys())[0])])
#     def test_LifeCycle_Start(self, count, action, event, page):
#         Common(count, action, event, page, set.ConfirmOrder_.LifeCycle_Start)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.ConfirmOrder["ConfirmOrder"][1].keys())[0], \
#                                list(set.ConfirmOrder["ConfirmOrder"][1].values())[0], list(set.ConfirmOrder.keys())[0])])
#     def test_Back(self, count, action, event, page):
#         Common(count, action, event, page, set.ConfirmOrder_.Back)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(random.randint(start_step, end_step), list(set.ConfirmOrder["ConfirmOrder"][2].keys())[0], \
#                                list(set.ConfirmOrder["ConfirmOrder"][2].values())[0], list(set.ConfirmOrder.keys())[0])])
#     def test_Review_Start(self, count, action, event, page):
#         Common(count, action, event, page, set.ConfirmOrder_.Review_Start)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(
#                               random.randint(start_step, end_step), list(set.ConfirmOrder["ConfirmOrder"][3].keys())[0], \
#                               list(set.ConfirmOrder["ConfirmOrder"][3].values())[0], list(set.ConfirmOrder.keys())[0])])
#     def test_Review_End(self, count, action, event, page):
#         Common(count, action, event, page, set.ConfirmOrder_.Review_End)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(
#                               random.randint(start_step, end_step), list(set.ConfirmOrder["ConfirmOrder"][4].keys())[0], \
#                               list(set.ConfirmOrder["ConfirmOrder"][4].values())[0], list(set.ConfirmOrder.keys())[0])])
#     def test_AliPay(self, count, action, event, page):
#         Common(count, action, event, page, set.ConfirmOrder_.AliPay)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(
#                               random.randint(start_step, end_step), list(set.ConfirmOrder["ConfirmOrder"][5].keys())[0], \
#                               list(set.ConfirmOrder["ConfirmOrder"][5].values())[0], list(set.ConfirmOrder.keys())[0])])
#     def test_WxPay(self, count, action, event, page):
#         Common(count, action, event, page, set.ConfirmOrder_.WxPay)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(
#                               random.randint(start_step, end_step), list(set.ConfirmOrder["ConfirmOrder"][6].keys())[0], \
#                               list(set.ConfirmOrder["ConfirmOrder"][6].values())[0], list(set.ConfirmOrder.keys())[0])])
#     def test_SubmitOrder(self, count, action, event, page):
#         Common(count, action, event, page, set.ConfirmOrder_.SubmitOrder)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(
#                               random.randint(start_step, end_step), list(set.ConfirmOrder["ConfirmOrder"][8].keys())[0], \
#                               list(set.ConfirmOrder["ConfirmOrder"][8].values())[0], list(set.ConfirmOrder.keys())[0])])
#     def test_LifeCycle_End(self, count, action, event, page):
#         Common(count, action, event, page, set.ConfirmOrder_.LifeCycle_End)
# 
# class Test_QrCode():
#     @pytest.fixture(scope='function', autouse=True)
#     def message(self):
#         '''check test environment'''
#         logger.log_info("start Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         os.system("adb root")
#         time.sleep(random.randint(1, 3))
#         set.Action.kill_skill_mall_progress(sn)
#         time.sleep(random.randint(3, 5))
#         set.Action.kill_skill_mall_progress(sn)
#         time.sleep(random.randint(3, 5))
#         set.Action.kill_skill_mall_progress(sn)
#         time.sleep(random.randint(3, 5))
#         # if set.Check_Result.deltet_lvlog(set.Action.get_sn()):
#         #     logger.log_info("delete lvlog successfully", \
#         #                     sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#         #                     sys._getframe().f_lineno)
#         set.Action.enter_pay_page(sn)
#         time.sleep(random.randint(1,3))
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
#         set.Action.kill_skill_mall_progress(sn)
#         time.sleep(random.randint(3, 5))
#         set.Action.kill_skill_mall_progress(sn)
#         time.sleep(random.randint(3, 5))
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(
#                                      random.randint(start_step, end_step),
#                                      list(set.QrCode["QrCode"][0].keys())[0], \
#                                      list(set.QrCode["QrCode"][0].values())[0],
#                                      list(set.QrCode.keys())[0])])
#     def test_LifeCycle_Start(self, count, action, event, page):
#         Common(count, action, event, page, set.QrCode_.LifeCycle_Start)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(
#                                      random.randint(start_step, end_step),
#                                      list(set.QrCode["QrCode"][1].keys())[0], \
#                                      list(set.QrCode["QrCode"][1].values())[0],
#                                      list(set.QrCode.keys())[0])])
#     def test_Back(self, count, action, event, page):
#         Common(count, action, event, page, set.QrCode_.Back)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(
#                                      random.randint(start_step, end_step),
#                                      list(set.QrCode["QrCode"][2].keys())[0], \
#                                      list(set.QrCode["QrCode"][2].values())[0],
#                                      list(set.QrCode.keys())[0])])
#     def test_Review_Start(self, count, action, event, page):
#         Common(count, action, event, page, set.QrCode_.Review_Start)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(
#                                      random.randint(start_step, end_step),
#                                      list(set.QrCode["QrCode"][3].keys())[0], \
#                                      list(set.QrCode["QrCode"][3].values())[0],
#                                      list(set.QrCode.keys())[0])])
#     def test_Review_End(self, count, action, event, page):
#         Common(count, action, event, page, set.QrCode_.Review_End)
# 
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(
#                                      random.randint(start_step, end_step),
#                                      list(set.QrCode["QrCode"][4].keys())[0], \
#                                      list(set.QrCode["QrCode"][4].values())[0],
#                                      list(set.QrCode.keys())[0])])
#     def test_TimeOutDialog_Start(self, count, action, event, page):
#         Common(count, action, event, page, set.QrCode_.TimeOutDialog_Start)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(
#                                      random.randint(start_step, end_step),
#                                      list(set.QrCode["QrCode"][5].keys())[0], \
#                                      list(set.QrCode["QrCode"][5].values())[0],
#                                      list(set.QrCode.keys())[0])])
#     def test_TimeOutDialog_Click(self, count, action, event, page):
#         Common(count, action, event, page, set.QrCode_.TimeOutDialog_Click)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(
#                                      random.randint(start_step, end_step),
#                                      list(set.QrCode["QrCode"][7].keys())[0], \
#                                      list(set.QrCode["QrCode"][7].values())[0],
#                                      list(set.QrCode.keys())[0])])
#     def test_TimeOutDialog_End(self, count, action, event, page):
#         Common(count, action, event, page, set.QrCode_.TimeOutDialog_End)
# 
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(
#                                      random.randint(start_step, end_step),
#                                      list(set.QrCode["QrCode"][10].keys())[0], \
#                                      list(set.QrCode["QrCode"][10].values())[0],
#                                      list(set.QrCode.keys())[0])])
#     def test_PayClose(self, count, action, event, page):
#         Common(count, action, event, page, set.QrCode_.PayClose)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(
#                                      random.randint(start_step, end_step),
#                                      list(set.QrCode["QrCode"][11].keys())[0], \
#                                      list(set.QrCode["QrCode"][11].values())[0],
#                                      list(set.QrCode.keys())[0])])
#     def test_LifeCycle_End(self, count, action, event, page):
#         Common(count, action, event, page, set.QrCode_.LifeCycle_End)
# 
# class Test_Feedback():
#     @pytest.fixture(scope='function', autouse=True)
#     def message(self):
#         '''check test environment'''
#         logger.log_info("start Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         os.system("adb root")
#         time.sleep(random.randint(1, 3))
#         set.Action.kill_skill_mall_progress(sn)
#         time.sleep(random.randint(3, 5))
#         set.Action.kill_skill_mall_progress(sn)
#         time.sleep(random.randint(3, 5))
#         set.Action.kill_skill_mall_progress(sn)
#         time.sleep(random.randint(3, 5))
#         # if set.Check_Result.deltet_lvlog(set.Action.get_sn()):
#         #     logger.log_info("delete lvlog successfully", \
#         #                     sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#         #                     sys._getframe().f_lineno)
#         set.Action.enter_pay_page(sn)
#         time.sleep(random.randint(1,3))
#         set.Action.click_submit_button(sn)
#         time.sleep(random.randint(1,3))
# 
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
#         set.Action.kill_skill_mall_progress(sn)
#         time.sleep(random.randint(3, 5))
#         set.Action.kill_skill_mall_progress(sn)
#         time.sleep(random.randint(3, 5))
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(
#                                      random.randint(start_step, end_step),
#                                      list(set.Feedback["Feedback"][0].keys())[0], \
#                                      list(set.Feedback["Feedback"][0].values())[0],
#                                      list(set.Feedback.keys())[0])])
#     def test_LifeCycle_Start(self, count, action, event, page):
#         Common(count, action, event, page, set.Feedback_.LifeCycle_Start)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(
#                                      random.randint(start_step, end_step),
#                                      list(set.Feedback["Feedback"][1].keys())[0], \
#                                      list(set.Feedback["Feedback"][1].values())[0],
#                                      list(set.Feedback.keys())[0])])
#     def test_Back(self, count, action, event, page):
#         Common(count, action, event, page, set.Feedback_.Back)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(
#                                      random.randint(start_step, end_step),
#                                      list(set.Feedback["Feedback"][2].keys())[0], \
#                                      list(set.Feedback["Feedback"][2].values())[0],
#                                      list(set.Feedback.keys())[0])])
#     def test_Review_Start(self, count, action, event, page):
#         Common(count, action, event, page, set.Feedback_.Review_Start)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(
#                                      random.randint(start_step, end_step),
#                                      list(set.Feedback["Feedback"][3].keys())[0], \
#                                      list(set.Feedback["Feedback"][3].values())[0],
#                                      list(set.Feedback.keys())[0])])
#     def test_Review_End(self, count, action, event, page):
#         Common(count, action, event, page, set.Feedback_.Review_End)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(
#                                      random.randint(start_step, end_step),
#                                      list(set.Feedback["Feedback"][4].keys())[0], \
#                                      list(set.Feedback["Feedback"][4].values())[0],
#                                      list(set.Feedback.keys())[0])])
#     def test_LifeCycle_End(self, count, action, event, page):
#         Common(count, action, event, page, set.Feedback_.LifeCycle_End)
# 
# class Test_Author():
#     @pytest.fixture(scope='function', autouse=True)
#     def message(self):
#         '''check test environment'''
#         logger.log_info("start Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         os.system("adb root")
#         time.sleep(random.randint(1, 3))
#         set.Action.kill_skill_mall_progress(sn)
#         time.sleep(random.randint(3, 5))
#         set.Action.kill_skill_mall_progress(sn)
#         time.sleep(random.randint(3, 5))
#         set.Action.kill_skill_mall_progress(sn)
#         time.sleep(random.randint(3, 5))
#         # if set.Check_Result.deltet_lvlog(set.Action.get_sn()):
#         #     logger.log_info("delete lvlog successfully", \
#         #                     sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#         #                     sys._getframe().f_lineno)
#         set.Action.skin_author(sn)
#         time.sleep(random.randint(1,3))
#         # 
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
#         set.Action.kill_skill_mall_progress(sn)
#         time.sleep(random.randint(3, 5))
#         set.Action.kill_skill_mall_progress(sn)
#         time.sleep(random.randint(3, 5))
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(
#                                      random.randint(start_step, end_step),
#                                      list(set.Author["Author"][0].keys())[0], \
#                                      list(set.Author["Author"][0].values())[0],
#                                      list(set.Author.keys())[0])])
#     def test_LifeCycle_Start(self, count, action, event, page):
#         Common(count, action, event, page, set.Author_.LifeCycle_Start)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(
#                                      random.randint(start_step, end_step),
#                                      list(set.Author["Author"][1].keys())[0], \
#                                      list(set.Author["Author"][1].values())[0],
#                                      list(set.Author.keys())[0])])
#     def test_Back(self, count, action, event, page):
#         Common(count, action, event, page, set.Author_.Back)
# 
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(
#                                      random.randint(start_step, end_step),
#                                      list(set.Author["Author"][2].keys())[0], \
#                                      list(set.Author["Author"][2].values())[0],
#                                      list(set.Author.keys())[0])])
#     def test_AuthorBack(self, count, action, event, page):
#         Common(count, action, event, page, set.Author_.AuthorBack)
# 
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(
#                                      random.randint(start_step, end_step),
#                                      list(set.Author["Author"][3].keys())[0], \
#                                      list(set.Author["Author"][3].values())[0],
#                                      list(set.Author.keys())[0])])
#     def test_Review_Start(self, count, action, event, page):
#         Common(count, action, event, page, set.Author_.Review_Start)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(
#                                      random.randint(start_step, end_step),
#                                      list(set.Author["Author"][4].keys())[0], \
#                                      list(set.Author["Author"][4].values())[0],
#                                      list(set.Author.keys())[0])])
#     def test_Review_End(self, count, action, event, page):
#         Common(count, action, event, page, set.Author_.Review_End)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(
#                                      random.randint(start_step, end_step),
#                                      list(set.Author["Author"][5].keys())[0], \
#                                      list(set.Author["Author"][5].values())[0],
#                                      list(set.Author.keys())[0])])
#     def test_SkinItem(self, count, action, event, page):
#         Common(count, action, event, page, set.Author_.SkinItem)
# 
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(
#                                      random.randint(start_step, end_step),
#                                      list(set.Author["Author"][6].keys())[0], \
#                                      list(set.Author["Author"][6].values())[0],
#                                      list(set.Author.keys())[0])])
#     def test_LifeCycle_End(self, count, action, event, page):
#         Common(count, action, event, page, set.Author_.LifeCycle_End)
# 
# class Test_Order():
#     @pytest.fixture(scope='function', autouse=True)
#     def message(self):
#         '''check test environment'''
#         logger.log_info("start Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         os.system("adb root")
#         time.sleep(random.randint(1, 3))
#         set.Action.kill_skill_mall_progress(sn)
#         time.sleep(random.randint(3, 5))
#         set.Action.kill_skill_mall_progress(sn)
#         time.sleep(random.randint(3, 5))
#         set.Action.kill_skill_mall_progress(sn)
#         time.sleep(random.randint(3, 5))
#         # if set.Check_Result.deltet_lvlog(set.Action.get_sn()):
#         #     logger.log_info("delete lvlog successfully", \
#         #                     sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#         #                     sys._getframe().f_lineno)
#         set.Action.enter_skin_main_page(sn)
#         time.sleep(random.randint(1,3))
# 
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
#         set.Action.kill_skill_mall_progress(sn)
#         time.sleep(random.randint(3, 5))
#         set.Action.kill_skill_mall_progress(sn)
#         time.sleep(random.randint(3, 5))
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(
#                                      random.randint(start_step, end_step),
#                                      list(set.Order["Order"][0].keys())[0], \
#                                      list(set.Order["Order"][0].values())[0],
#                                      list(set.Order.keys())[0])])
#     def test_LifeCycle_Start(self, count, action, event, page):
#         Common(count, action, event, page, set.Order_.LifeCycle_Start)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(
#                                      random.randint(start_step, end_step),
#                                      list(set.Order["Order"][1].keys())[0], \
#                                      list(set.Order["Order"][1].values())[0],
#                                      list(set.Order.keys())[0])])
#     def test_Back(self, count, action, event, page):
#         Common(count, action, event, page, set.Order_.Back)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(
#                                      random.randint(start_step, end_step),
#                                      list(set.Order["Order"][2].keys())[0], \
#                                      list(set.Order["Order"][2].values())[0],
#                                      list(set.Order.keys())[0])])
#     def test_Review_Start(self, count, action, event, page):
#         Common(count, action, event, page, set.Order_.Review_Start)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(
#                                      random.randint(start_step, end_step),
#                                      list(set.Order["Order"][3].keys())[0], \
#                                      list(set.Order["Order"][3].values())[0],
#                                      list(set.Order.keys())[0])])
#     def test_Review_End(self, count, action, event, page):
#         Common(count, action, event, page, set.Order_.Review_End)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(
#                                      random.randint(start_step, end_step),
#                                      list(set.Order["Order"][4].keys())[0], \
#                                      list(set.Order["Order"][4].values())[0],
#                                      list(set.Order.keys())[0])])
#     def test_TabAll(self, count, action, event, page):
#         Common(count, action, event, page, set.Order_.TabAll)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(
#                                      random.randint(start_step, end_step),
#                                      list(set.Order["Order"][5].keys())[0], \
#                                      list(set.Order["Order"][5].values())[0],
#                                      list(set.Order.keys())[0])])
#     def test_TabPayment(self, count, action, event, page):
#         Common(count, action, event, page, set.Order_.TabPayment)
# 
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(
#                                      random.randint(start_step, end_step),
#                                      list(set.Order["Order"][6].keys())[0], \
#                                      list(set.Order["Order"][6].values())[0],
#                                      list(set.Order.keys())[0])])
#     def test_TabPaymented(self, count, action, event, page):
#         Common(count, action, event, page, set.Order_.TabPaymented)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(
#                                      random.randint(start_step, end_step),
#                                      list(set.Order["Order"][7].keys())[0], \
#                                      list(set.Order["Order"][7].values())[0],
#                                      list(set.Order.keys())[0])])
#     def test_OrderItem(self, count, action, event, page):
#         Common(count, action, event, page, set.Order_.OrderItem)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(
#                                      random.randint(start_step, end_step),
#                                      list(set.Order["Order"][8].keys())[0], \
#                                      list(set.Order["Order"][8].values())[0],
#                                      list(set.Order.keys())[0])])
#     def test_Refresh(self, count, action, event, page):
#         Common(count, action, event, page, set.Order_.Refresh, flag=2)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(
#                                      random.randint(start_step, end_step),
#                                      list(set.Order["Order"][9].keys())[0], \
#                                      list(set.Order["Order"][9].values())[0],
#                                      list(set.Order.keys())[0])])
#     def test_LoadMore(self, count, action, event, page):
#         Common(count, action, event, page, set.Order_.LoadMore)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(
#                                      random.randint(start_step, end_step),
#                                      list(set.Order["Order"][10].keys())[0], \
#                                      list(set.Order["Order"][10].values())[0],
#                                      list(set.Order.keys())[0])])
#     def test_LifeCycle_End(self, count, action, event, page):
#         Common(count, action, event, page, set.Order_.LifeCycle_End)
# 
# class Test_OrderDetail():
#     @pytest.fixture(scope='function', autouse=True)
#     def message(self):
#         '''check test environment'''
#         logger.log_info("start Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         os.system("adb root")
#         time.sleep(random.randint(1, 3))
#         set.Action.kill_skill_mall_progress(sn)
#         time.sleep(random.randint(3, 5))
#         set.Action.kill_skill_mall_progress(sn)
#         time.sleep(random.randint(3, 5))
#         set.Action.kill_skill_mall_progress(sn)
#         time.sleep(random.randint(3, 5))
#         # if set.Check_Result.deltet_lvlog(set.Action.get_sn()):
#         #     logger.log_info("delete lvlog successfully", \
#         #                     sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#         #                     sys._getframe().f_lineno)
#         set.Action.enter_skin_list_details(sn)
#         time.sleep(random.randint(1,3))
# 
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
#         set.Action.kill_skill_mall_progress(sn)
#         time.sleep(random.randint(3, 5))
#         set.Action.kill_skill_mall_progress(sn)
#         time.sleep(random.randint(3, 5))
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(
#                                      random.randint(start_step, end_step),
#                                      list(set.OrderDetail["OrderDetail"][0].keys())[0], \
#                                      list(set.OrderDetail["OrderDetail"][0].values())[0],
#                                      list(set.OrderDetail.keys())[0])])
#     def test_LifeCycle_Start(self, count, action, event, page):
#         Common(count, action, event, page, set.OrderDetail_.LifeCycle_Start)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(
#                                      random.randint(start_step, end_step),
#                                      list(set.OrderDetail["OrderDetail"][1].keys())[0], \
#                                      list(set.OrderDetail["OrderDetail"][1].values())[0],
#                                      list(set.OrderDetail.keys())[0])])
#     def test_Back(self, count, action, event, page):
#         Common(count, action, event, page, set.OrderDetail_.Back)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(
#                                      random.randint(start_step, end_step),
#                                      list(set.OrderDetail["OrderDetail"][2].keys())[0], \
#                                      list(set.OrderDetail["OrderDetail"][2].values())[0],
#                                      list(set.OrderDetail.keys())[0])])
#     def test_Review_Start(self, count, action, event, page):
#         Common(count, action, event, page, set.OrderDetail_.Review_Start)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(
#                                      random.randint(start_step, end_step),
#                                      list(set.OrderDetail["OrderDetail"][3].keys())[0], \
#                                      list(set.OrderDetail["OrderDetail"][3].values())[0],
#                                      list(set.OrderDetail.keys())[0])])
#     def test_Review_End(self, count, action, event, page):
#         Common(count, action, event, page, set.OrderDetail_.Review_End)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(
#                                      random.randint(start_step, end_step),
#                                      list(set.OrderDetail["OrderDetail"][4].keys())[0], \
#                                      list(set.OrderDetail["OrderDetail"][4].values())[0],
#                                      list(set.OrderDetail.keys())[0])])
#     def test_SkinClick(self, count, action, event, page):
#         Common(count, action, event, page, set.OrderDetail_.SkinClick)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(
#                                      random.randint(start_step, end_step),
#                                      list(set.OrderDetail["OrderDetail"][5].keys())[0], \
#                                      list(set.OrderDetail["OrderDetail"][5].values())[0],
#                                      list(set.OrderDetail.keys())[0])])
#     def test_Pay(self, count, action, event, page):
#         Common(count, action, event, page, set.OrderDetail_.Pay)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(
#                                      random.randint(start_step, end_step),
#                                      list(set.OrderDetail["OrderDetail"][6].keys())[0], \
#                                      list(set.OrderDetail["OrderDetail"][6].values())[0],
#                                      list(set.OrderDetail.keys())[0])])
#     def test_PayBack(self, count, action, event, page):
#         Common(count, action, event, page, set.OrderDetail_.PayBack)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(
#                                      random.randint(start_step, end_step),
#                                      list(set.OrderDetail["OrderDetail"][7].keys())[0], \
#                                      list(set.OrderDetail["OrderDetail"][7].values())[0],
#                                      list(set.OrderDetail.keys())[0])])
#     def test_CancelOrder(self, count, action, event, page):
#         Common(count, action, event, page, set.OrderDetail_.CancelOrder)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(
#                                      random.randint(start_step, end_step),
#                                      list(set.OrderDetail["OrderDetail"][9].keys())[0], \
#                                      list(set.OrderDetail["OrderDetail"][9].values())[0],
#                                      list(set.OrderDetail.keys())[0])])
#     def test_CancelDialog(self, count, action, event, page):
#         Common(count, action, event, page, set.OrderDetail_.CancelDialog)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(
#                                      random.randint(start_step, end_step),
#                                      list(set.OrderDetail["OrderDetail"][10].keys())[0], \
#                                      list(set.OrderDetail["OrderDetail"][10].values())[0],
#                                      list(set.OrderDetail.keys())[0])])
#     def test_CancelDialog_End(self, count, action, event, page):
#         Common(count, action, event, page, set.OrderDetail_.CancelDialog_End)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(
#                                      random.randint(start_step, end_step),
#                                      list(set.OrderDetail["OrderDetail"][13].keys())[0], \
#                                      list(set.OrderDetail["OrderDetail"][13].values())[0],
#                                      list(set.OrderDetail.keys())[0])])
#     def test_DeleteOrder(self, count, action, event, page):
#         Common(count, action, event, page, set.OrderDetail_.DeleteOrder)
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(
#                                      random.randint(start_step, end_step),
#                                      list(set.OrderDetail["OrderDetail"][14].keys())[0], \
#                                      list(set.OrderDetail["OrderDetail"][14].values())[0],
#                                      list(set.OrderDetail.keys())[0])])
#     def test_DeleteDialog_Start(self, count, action, event, page):
#         Common(count, action, event, page, set.OrderDetail_.DeleteDialog_Start)
# 
# 
#     @pytest.mark.parametrize('count,action,event,page',
#                              [(
#                                      random.randint(start_step, end_step),
#                                      list(set.OrderDetail["OrderDetail"][16].keys())[0], \
#                                      list(set.OrderDetail["OrderDetail"][16].values())[0],
#                                      list(set.OrderDetail.keys())[0])])
#     def test_DeleteDialog_Cancel(self, count, action, event, page):
#         Common(count, action, event, page, set.OrderDetail_.DeleteDialog_Cancel)
# 
# class Test_Check_Skin_Mall_Hive_Result(object):
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
#                              [(list(set.Index["Index"][0].keys())[0], \
#                                list(set.Index["Index"][0].values())[0], list(set.Index.keys())[0])])
#     def test_Index_LifeCycle_Start(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Index["Index"][8].keys())[0], \
#                                list(set.Index["Index"][8].values())[0], "Unknown")])
#     def test_Index_Open_App(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Index["Index"][1].keys())[0], \
#                                list(set.Index["Index"][1].values())[0], list(set.Index.keys())[0])])
#     def test_Index_Back(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Index["Index"][2].keys())[0], \
#                                list(set.Index["Index"][2].values())[0], list(set.Index.keys())[0])])
#     def test_Index_Review_Start(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Index["Index"][3].keys())[0], \
#                                list(set.Index["Index"][3].values())[0], list(set.Index.keys())[0])])
#     def test_Index_Review_End(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Index["Index"][4].keys())[0], \
#                                list(set.Index["Index"][4].values())[0], list(set.Index.keys())[0])])
#     def test_Index_Recommend(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Index["Index"][5].keys())[0], \
#                                list(set.Index["Index"][5].values())[0], list(set.Index.keys())[0])])
#     def test_Index_Manager(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Index["Index"][6].keys())[0], \
#                                list(set.Index["Index"][6].values())[0], list(set.Index.keys())[0])])
#     def test_Index_Order(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Recommend["Recommend"][0].keys())[0], \
#                                list(set.Recommend["Recommend"][0].values())[0], list(set.Recommend.keys())[0])])
#     def test_Recommend_Review_Start(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Recommend["Recommend"][1].keys())[0], \
#                                list(set.Recommend["Recommend"][1].values())[0], list(set.Recommend.keys())[0])])
#     def test_Recommend_Review_End(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Recommend["Recommend"][2].keys())[0], \
#                                list(set.Recommend["Recommend"][2].values())[0], list(set.Recommend.keys())[0])])
#     def test_Recommend_SkinItem(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Recommend["Recommend"][3].keys())[0], \
#                                list(set.Recommend["Recommend"][3].values())[0], list(set.Recommend.keys())[0])])
#     def test_Recommend_Refresh(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Recommend["Recommend"][4].keys())[0], \
#                                list(set.Recommend["Recommend"][4].values())[0], list(set.Recommend.keys())[0])])
#     def test_Recommend_LoadMore(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.SkinManager["SkinManager"][0].keys())[0], \
#                                list(set.SkinManager["SkinManager"][0].values())[0], list(set.SkinManager.keys())[0])])
#     def test_SkinManager_Review_Start(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.SkinManager["SkinManager"][1].keys())[0], \
#                                list(set.SkinManager["SkinManager"][1].values())[0], list(set.SkinManager.keys())[0])])
#     def test_SkinManager_Review_End(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.SkinManager["SkinManager"][2].keys())[0], \
#                                list(set.SkinManager["SkinManager"][2].values())[0], list(set.SkinManager.keys())[0])])
#     def test_SkinManager_SkinItem(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.SkinManager["SkinManager"][3].keys())[0], \
#                                list(set.SkinManager["SkinManager"][3].values())[0], list(set.SkinManager.keys())[0])])
#     def test_SkinManager_Remove(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.SkinManager["SkinManager"][4].keys())[0], \
#                                list(set.SkinManager["SkinManager"][4].values())[0], list(set.SkinManager.keys())[0])])
#     def test_SkinManager_RemoveDialog_Start(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.SkinManager["SkinManager"][5].keys())[0], \
#                                list(set.SkinManager["SkinManager"][5].values())[0], list(set.SkinManager.keys())[0])])
#     def test_SkinManager_RemoveDialog_Click_Remove(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.SkinManager["SkinManager"][6].keys())[0], \
#                                list(set.SkinManager["SkinManager"][6].values())[0], list(set.SkinManager.keys())[0])])
#     def test_SkinManager_RemoveDialog_Click_Cancel(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.SkinManager["SkinManager"][7].keys())[0], \
#                                list(set.SkinManager["SkinManager"][7].values())[0], list(set.SkinManager.keys())[0])])
#     def test_SkinManager_RemoveDialog_End(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.SkinManager["SkinManager"][8].keys())[0], \
#                                list(set.SkinManager["SkinManager"][8].values())[0], list(set.SkinManager.keys())[0])])
#     def test_SkinManager_Download_Click(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.SkinManager["SkinManager"][9].keys())[0], \
#                                list(set.SkinManager["SkinManager"][9].values())[0], list(set.SkinManager.keys())[0])])
#     def test_SkinManager_Download_Start(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.SkinManager["SkinManager"][10].keys())[0], \
#                                list(set.SkinManager["SkinManager"][10].values())[0], list(set.SkinManager.keys())[0])])
#     def test_SkinManager_Cancel(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.SkinManager["SkinManager"][11].keys())[0], \
#                                list(set.SkinManager["SkinManager"][11].values())[0], list(set.SkinManager.keys())[0])])
#     def test_SkinManager_Use(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.SkinManager["SkinManager"][12].keys())[0], \
#                                list(set.SkinManager["SkinManager"][12].values())[0], list(set.SkinManager.keys())[0])])
#     def test_SkinManager_UseDialog_Start(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.SkinManager["SkinManager"][13].keys())[0], \
#                                list(set.SkinManager["SkinManager"][13].values())[0], list(set.SkinManager.keys())[0])])
#     def test_SkinManager_UseDialog_Use(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.SkinManager["SkinManager"][14].keys())[0], \
#                                list(set.SkinManager["SkinManager"][14].values())[0], list(set.SkinManager.keys())[0])])
#     def test_SkinManager_UseDialog_Cancel(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.SkinManager["SkinManager"][15].keys())[0], \
#                                list(set.SkinManager["SkinManager"][15].values())[0], list(set.SkinManager.keys())[0])])
#     def test_SkinManager_UseDialog_End(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Detail["Detail"][0].keys())[0], \
#                                list(set.Detail["Detail"][0].values())[0], list(set.Detail.keys())[0])])
#     def test_Detail_LifeCycle(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Detail["Detail"][1].keys())[0], \
#                                list(set.Detail["Detail"][1].values())[0], list(set.Detail.keys())[0])])
#     def test_Detail_Back(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Detail["Detail"][2].keys())[0], \
#                                list(set.Detail["Detail"][2].values())[0], list(set.Detail.keys())[0])])
#     def test_Detail_Review_Start(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Detail["Detail"][3].keys())[0], \
#                                list(set.Detail["Detail"][3].values())[0], list(set.Detail.keys())[0])])
#     def test_Detail_Review_End(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Detail["Detail"][4].keys())[0], \
#                                list(set.Detail["Detail"][4].values())[0], list(set.Detail.keys())[0])])
#     def test_Detail_Buy_Click(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Detail["Detail"][5].keys())[0], \
#                                list(set.Detail["Detail"][5].values())[0], list(set.Detail.keys())[0])])
#     def test_Detail_BuyBack_Click(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Detail["Detail"][9].keys())[0], \
#                                list(set.Detail["Detail"][9].values())[0], list(set.Detail.keys())[0])])
#     def test_Detail_author(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Detail["Detail"][14].keys())[0], \
#                                list(set.Detail["Detail"][14].values())[0], list(set.Detail.keys())[0])])
#     def test_Detail_Use_Click(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Detail["Detail"][15].keys())[0], \
#                                list(set.Detail["Detail"][15].values())[0], list(set.Detail.keys())[0])])
#     def test_Detail_UseDialog_Start(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Detail["Detail"][16].keys())[0], \
#                                list(set.Detail["Detail"][16].values())[0], list(set.Detail.keys())[0])])
#     def test_Detail_UseDialog_Click_Use(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Detail["Detail"][17].keys())[0], \
#                                list(set.Detail["Detail"][17].values())[0], list(set.Detail.keys())[0])])
#     def test_Detail_UseDialog_Click_Cancel(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Detail["Detail"][18].keys())[0], \
#                                list(set.Detail["Detail"][18].values())[0], list(set.Detail.keys())[0])])
#     def test_Detail_UseDialog_End(self,action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Detail["Detail"][20].keys())[0], \
#                                list(set.Detail["Detail"][20].values())[0], list(set.Detail.keys())[0])])
#     def test_Detail_LifeCycle_End(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.ConfirmOrder["ConfirmOrder"][0].keys())[0], \
#                               list(set.ConfirmOrder["ConfirmOrder"][0].values())[0], list(set.ConfirmOrder.keys())[0])])
#     def test_ConfirmOrder_LifeCycle_Start(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.ConfirmOrder["ConfirmOrder"][1].keys())[0], \
#                               list(set.ConfirmOrder["ConfirmOrder"][1].values())[0], list(set.ConfirmOrder.keys())[0])])
#     def test_ConfirmOrder_Back(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.ConfirmOrder["ConfirmOrder"][2].keys())[0], \
#                               list(set.ConfirmOrder["ConfirmOrder"][2].values())[0], list(set.ConfirmOrder.keys())[0])])
#     def test_ConfirmOrder_Review_Start(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(
#                                      list(set.ConfirmOrder["ConfirmOrder"][3].keys())[0], \
#                                      list(set.ConfirmOrder["ConfirmOrder"][3].values())[0],
#                                      list(set.ConfirmOrder.keys())[0])])
#     def test_ConfirmOrder_Review_End(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(
#                                      list(set.ConfirmOrder["ConfirmOrder"][4].keys())[0], \
#                                      list(set.ConfirmOrder["ConfirmOrder"][4].values())[0],
#                                      list(set.ConfirmOrder.keys())[0])])
#     def test_ConfirmOrder_AliPay(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(
#                                      list(set.ConfirmOrder["ConfirmOrder"][5].keys())[0], \
#                                      list(set.ConfirmOrder["ConfirmOrder"][5].values())[0],
#                                      list(set.ConfirmOrder.keys())[0])])
#     def test_ConfirmOrder_WxPay(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(
#                                      list(set.ConfirmOrder["ConfirmOrder"][6].keys())[0], \
#                                      list(set.ConfirmOrder["ConfirmOrder"][6].values())[0],
#                                      list(set.ConfirmOrder.keys())[0])])
#     def test_ConfirmOrder_SubmitOrder(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(
#                                      list(set.ConfirmOrder["ConfirmOrder"][8].keys())[0], \
#                                      list(set.ConfirmOrder["ConfirmOrder"][8].values())[0],
#                                      list(set.ConfirmOrder.keys())[0])])
#     def test_ConfirmOrder_LifeCycle_End(self, action, event, page):
#         Compare(action, event, page)
# 
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(
#                                      list(set.QrCode["QrCode"][0].keys())[0], \
#                                      list(set.QrCode["QrCode"][0].values())[0],
#                                      list(set.QrCode.keys())[0])])
#     def test_QrCode_LifeCycle_Start(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(
#                                      list(set.QrCode["QrCode"][1].keys())[0], \
#                                      list(set.QrCode["QrCode"][1].values())[0],
#                                      list(set.QrCode.keys())[0])])
#     def test_QrCode_Back(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(
#                                      list(set.QrCode["QrCode"][2].keys())[0], \
#                                      list(set.QrCode["QrCode"][2].values())[0],
#                                      list(set.QrCode.keys())[0])])
#     def test_QrCode_Review_Start(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(
#                                      list(set.QrCode["QrCode"][3].keys())[0], \
#                                      list(set.QrCode["QrCode"][3].values())[0],
#                                      list(set.QrCode.keys())[0])])
#     def test_QrCode_Review_End(self, action, event, page):
#         Compare(action, event, page)
# 
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(
#                                      list(set.QrCode["QrCode"][4].keys())[0], \
#                                      list(set.QrCode["QrCode"][4].values())[0],
#                                      list(set.QrCode.keys())[0])])
#     def test_QrCode_TimeOutDialog_Start(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(
#                                      list(set.QrCode["QrCode"][5].keys())[0], \
#                                      list(set.QrCode["QrCode"][5].values())[0],
#                                      list(set.QrCode.keys())[0])])
#     def test_QrCode_TimeOutDialog_Click(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(
#                                      list(set.QrCode["QrCode"][7].keys())[0], \
#                                      list(set.QrCode["QrCode"][7].values())[0],
#                                      list(set.QrCode.keys())[0])])
#     def test_QrCode_TimeOutDialog_End(self, action, event, page):
#         Compare(action, event, page)
# 
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(
#                                      list(set.QrCode["QrCode"][10].keys())[0], \
#                                      list(set.QrCode["QrCode"][10].values())[0],
#                                      list(set.QrCode.keys())[0])])
#     def test_QrCode_PayClose(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(
#                                      list(set.QrCode["QrCode"][11].keys())[0], \
#                                      list(set.QrCode["QrCode"][11].values())[0],
#                                      list(set.QrCode.keys())[0])])
#     def test_QrCode_LifeCycle_End(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(
#                                      list(set.Feedback["Feedback"][0].keys())[0], \
#                                      list(set.Feedback["Feedback"][0].values())[0],
#                                      list(set.Feedback.keys())[0])])
#     def test_Feedback_LifeCycle_Start(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(
#                                      list(set.Feedback["Feedback"][1].keys())[0], \
#                                      list(set.Feedback["Feedback"][1].values())[0],
#                                      list(set.Feedback.keys())[0])])
#     def test_Feedback_Back(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(
#                                      list(set.Feedback["Feedback"][2].keys())[0], \
#                                      list(set.Feedback["Feedback"][2].values())[0],
#                                      list(set.Feedback.keys())[0])])
#     def test_Feedback_Review_Start(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(
#                                      list(set.Feedback["Feedback"][3].keys())[0], \
#                                      list(set.Feedback["Feedback"][3].values())[0],
#                                      list(set.Feedback.keys())[0])])
#     def test_Feedback_Review_End(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(
#                                      list(set.Feedback["Feedback"][4].keys())[0], \
#                                      list(set.Feedback["Feedback"][4].values())[0],
#                                      list(set.Feedback.keys())[0])])
#     def test_Feedback_LifeCycle_End(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(
#                                      list(set.Author["Author"][0].keys())[0], \
#                                      list(set.Author["Author"][0].values())[0],
#                                      list(set.Author.keys())[0])])
#     def test_Author_LifeCycle_Start(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(
#                                      list(set.Author["Author"][1].keys())[0], \
#                                      list(set.Author["Author"][1].values())[0],
#                                      list(set.Author.keys())[0])])
#     def test_Author_Back(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(
#                                      list(set.Author["Author"][2].keys())[0], \
#                                      list(set.Author["Author"][2].values())[0],
#                                      list(set.Author.keys())[0])])
#     def test_Author_AuthorBack(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(
#                                      list(set.Author["Author"][3].keys())[0], \
#                                      list(set.Author["Author"][3].values())[0],
#                                      list(set.Author.keys())[0])])
#     def test_Author_Review_Start(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(
#                                      list(set.Author["Author"][4].keys())[0], \
#                                      list(set.Author["Author"][4].values())[0],
#                                      list(set.Author.keys())[0])])
#     def test_Author_Review_End(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(
#                                      list(set.Author["Author"][5].keys())[0], \
#                                      list(set.Author["Author"][5].values())[0],
#                                      list(set.Author.keys())[0])])
#     def test_Author_SkinItem(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(
#                                      list(set.Author["Author"][6].keys())[0], \
#                                      list(set.Author["Author"][6].values())[0],
#                                      list(set.Author.keys())[0])])
#     def test_Author_LifeCycle_End(self, action, event, page):
#         Compare(action, event, page)
# 
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(
#                                      list(set.Order["Order"][0].keys())[0], \
#                                      list(set.Order["Order"][0].values())[0],
#                                      list(set.Order.keys())[0])])
#     def test_Order_LifeCycle_Start(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(
#                                      list(set.Order["Order"][1].keys())[0], \
#                                      list(set.Order["Order"][1].values())[0],
#                                      list(set.Order.keys())[0])])
#     def test_Order_Back(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(
#                                      list(set.Order["Order"][2].keys())[0], \
#                                      list(set.Order["Order"][2].values())[0],
#                                      list(set.Order.keys())[0])])
#     def test_Order_Review_Start(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(
#                                      list(set.Order["Order"][3].keys())[0], \
#                                      list(set.Order["Order"][3].values())[0],
#                                      list(set.Order.keys())[0])])
#     def test_Order_Review_End(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(
#                                      list(set.Order["Order"][4].keys())[0], \
#                                      list(set.Order["Order"][4].values())[0],
#                                      list(set.Order.keys())[0])])
#     def test_Order_TabAll(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(
#                                      list(set.Order["Order"][5].keys())[0], \
#                                      list(set.Order["Order"][5].values())[0],
#                                      list(set.Order.keys())[0])])
#     def test_Order_TabPayment(self, action, event, page):
#         Compare(action, event, page)
# 
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(
#                                      list(set.Order["Order"][6].keys())[0], \
#                                      list(set.Order["Order"][6].values())[0],
#                                      list(set.Order.keys())[0])])
#     def test_Order_TabPaymented(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(
#                                      list(set.Order["Order"][7].keys())[0], \
#                                      list(set.Order["Order"][7].values())[0],
#                                      list(set.Order.keys())[0])])
#     def test_Order_OrderItem(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(
#                                      list(set.Order["Order"][8].keys())[0], \
#                                      list(set.Order["Order"][8].values())[0],
#                                      list(set.Order.keys())[0])])
#     def test_Order_Refresh(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(
#                                      list(set.Order["Order"][9].keys())[0], \
#                                      list(set.Order["Order"][9].values())[0],
#                                      list(set.Order.keys())[0])])
#     def test_Order_LoadMore(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(
#                                      list(set.Order["Order"][10].keys())[0], \
#                                      list(set.Order["Order"][10].values())[0],
#                                      list(set.Order.keys())[0])])
#     def test_Order_LifeCycle_End(self, action, event, page):
#         Compare(action, event, page)
# 
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(
#                                      list(set.OrderDetail["OrderDetail"][0].keys())[0], \
#                                      list(set.OrderDetail["OrderDetail"][0].values())[0],
#                                      list(set.OrderDetail.keys())[0])])
#     def test_OrderDetail_LifeCycle_Start(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(
#                                      list(set.OrderDetail["OrderDetail"][1].keys())[0], \
#                                      list(set.OrderDetail["OrderDetail"][1].values())[0],
#                                      list(set.OrderDetail.keys())[0])])
#     def test_OrderDetail_Back(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(
#                                      list(set.OrderDetail["OrderDetail"][2].keys())[0], \
#                                      list(set.OrderDetail["OrderDetail"][2].values())[0],
#                                      list(set.OrderDetail.keys())[0])])
#     def test_OrderDetail_Review_Start(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(
#                                      list(set.OrderDetail["OrderDetail"][3].keys())[0], \
#                                      list(set.OrderDetail["OrderDetail"][3].values())[0],
#                                      list(set.OrderDetail.keys())[0])])
#     def test_OrderDetail_Review_End(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(
#                                      list(set.OrderDetail["OrderDetail"][4].keys())[0], \
#                                      list(set.OrderDetail["OrderDetail"][4].values())[0],
#                                      list(set.OrderDetail.keys())[0])])
#     def test_OrderDetail_SkinClick(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(
#                                      list(set.OrderDetail["OrderDetail"][5].keys())[0], \
#                                      list(set.OrderDetail["OrderDetail"][5].values())[0],
#                                      list(set.OrderDetail.keys())[0])])
#     def test_OrderDetail_Pay(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(
#                                      list(set.OrderDetail["OrderDetail"][6].keys())[0], \
#                                      list(set.OrderDetail["OrderDetail"][6].values())[0],
#                                      list(set.OrderDetail.keys())[0])])
#     def test_OrderDetail_PayBack(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(
#                                      list(set.OrderDetail["OrderDetail"][7].keys())[0], \
#                                      list(set.OrderDetail["OrderDetail"][7].values())[0],
#                                      list(set.OrderDetail.keys())[0])])
#     def test_OrderDetail_CancelOrder(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(
#                                      list(set.OrderDetail["OrderDetail"][9].keys())[0], \
#                                      list(set.OrderDetail["OrderDetail"][9].values())[0],
#                                      list(set.OrderDetail.keys())[0])])
#     def test_OrderDetail_CancelDialog(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(
#                                      list(set.OrderDetail["OrderDetail"][10].keys())[0], \
#                                      list(set.OrderDetail["OrderDetail"][10].values())[0],
#                                      list(set.OrderDetail.keys())[0])])
#     def test_OrderDetail_CancelDialog_End(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(
#                                      list(set.OrderDetail["OrderDetail"][13].keys())[0], \
#                                      list(set.OrderDetail["OrderDetail"][13].values())[0],
#                                      list(set.OrderDetail.keys())[0])])
#     def test_OrderDetail_DeleteOrder(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(
#                                      list(set.OrderDetail["OrderDetail"][14].keys())[0], \
#                                      list(set.OrderDetail["OrderDetail"][14].values())[0],
#                                      list(set.OrderDetail.keys())[0])])
#     def test_OrderDetail_DeleteDialog_Start(self, action, event, page):
#         Compare(action, event, page)
# 
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(
#                                      list(set.OrderDetail["OrderDetail"][16].keys())[0], \
#                                      list(set.OrderDetail["OrderDetail"][16].values())[0],
#                                      list(set.OrderDetail.keys())[0])])
#     def test_OrderDetail_DeleteDialog_Cancel(self, action, event, page):
#         Compare(action, event, page)
# 
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
# 
# 
# 
# 
# 
# 
# 
# 
# 
