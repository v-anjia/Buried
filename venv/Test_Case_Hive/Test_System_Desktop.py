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
# import subprocess
# from Common import System_Desktop as set
# # from Check_Hive_Result import System_Desktop as set
# from Common import Common as co
# from log import  logger as loger
# from Common import Hive_Connect as hc
# 
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
# buried_log = '/update/buried_System_Desktop.log'
# busybox = "/yf/bin/busybox"
# 
# buried_point = "/sdcard/Android/data/com.wm.tracker/files/temp/*"
# 
# save_data = "/update/buried_local_System_Desktop.log"
# LOG_PATH = 'logcat -v time |grep -iE \".*wmTracker.*EventModel.*\" |grep -v "clientSendMessage" > %s &' %(buried_log)
# Delete_Log = 'rm -rf /update/buried_System_Desktop.log'
# logcat_pid_exist = "ps |grep logcat | %s awk \'{print $2}\' |%s xargs kill -9 " %(busybox,busybox)
# hc_object = hc.hive_connect()
# 
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
# class Test_Check_System_Desktop_Hive_Result(object):
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
#                              [(list(set.Default["Default"][0].keys())[0], \
#                                list(set.Default["Default"][0].values())[0], "Default")])
#     def test_startMap(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Default["Default"][1].keys())[0], \
#                                list(set.Default["Default"][1].values())[0], "Default")])
#     def test_startEnergy(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Default["Default"][2].keys())[0], \
#                                list(set.Default["Default"][2].values())[0], "Default")])
#     def test_startMusic(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Default["Default"][3].keys())[0], \
#                                list(set.Default["Default"][3].values())[0], "Default")])
#     def test_startBtPhone(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Default["Default"][4].keys())[0], \
#                                list(set.Default["Default"][4].values())[0], "Default")])
#     def test_startDVR(self, action, event, page):
#         # Common(count, action, event, page, set.Default_.startDVR)
#         pass
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Default["Default"][5].keys())[0], \
#                                list(set.Default["Default"][5].values())[0], "Default")])
#     def test_startFM(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Default["Default"][6].keys())[0], \
#                                list(set.Default["Default"][6].values())[0], "Default")])
#     def test_startSetting(self,action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Default["Default"][7].keys())[0], \
#                                list(set.Default["Default"][7].values())[0], "Default")])
#     def test_startWeChat(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Default["Default"][8].keys())[0], \
#                                list(set.Default["Default"][8].values())[0], "Default")])
#     def test_startMiant(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Default["Default"][9].keys())[0], \
#                                list(set.Default["Default"][9].values())[0], "Default")])
#     def test_startMiant(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Default["Default"][10].keys())[0], \
#                                list(set.Default["Default"][10].values())[0], "Default")])
#     def test_startCarControl(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Default["Default"][11].keys())[0], \
#                                list(set.Default["Default"][11].values())[0], "Default")])
#     def test_startAQY(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Default["Default"][12].keys())[0], \
#                                list(set.Default["Default"][12].values())[0], "Default")])
#     def test_startAVM(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Default["Default"][13].keys())[0], \
#                                list(set.Default["Default"][13].values())[0], "Default")])
#     def test_startAudioBook(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Default["Default"][14].keys())[0], \
#                                list(set.Default["Default"][14].values())[0], "Default")])
#     def test_startSkinStore(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Default["Default"][15].keys())[0], \
#                                list(set.Default["Default"][15].values())[0], "Default")])
#     def test_startMiJia(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Default["Default"][16].keys())[0], \
#                                list(set.Default["Default"][16].values())[0], "Default")])
#     def test_startWeMeet(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Default["Default"][17].keys())[0], \
#                                list(set.Default["Default"][17].values())[0], "Default")])
#     def test_EnterWidgetPage(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Widget["Widget"][0].keys())[0], \
#                                list(set.Widget["Widget"][0].values())[0], list(set.Widget.keys())[0])])
#     def test_EnterWidgetPage(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Widget["Widget"][1].keys())[0], \
#                                list(set.Widget["Widget"][1].values())[0], list(set.Widget.keys())[0])])
#     def test_showDefaultPage(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Widget["Widget"][2].keys())[0], \
#                                list(set.Widget["Widget"][2].values())[0], list(set.Widget.keys())[0])])
#     def test_editingWidget_Start(self,action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Widget["Widget"][3].keys())[0], \
#                                list(set.Widget["Widget"][3].values())[0], list(set.Widget.keys())[0])])
#     def test_editingWidget_End(self,action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page',
#                              [(list(set.Widget["Widget"][4].keys())[0], \
#                                list(set.Widget["Widget"][4].values())[0], list(set.Widget.keys())[0])])
#     def test_EditApp(self, action, event, page):
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
