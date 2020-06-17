# '''
# Case System Activation Test Suite
# author : antony WeiJiang
# date:2020/4/15
# '''
# 
# import pytest
# import sys
# import os
# import time
# import subprocess
# import random
# import pytest_html.extras
# import pytest_html.hooks
# import pytest_html.plugin
# from Common import Energy_Management as set
# from Common import Common as co
# from log import  logger as loger
# from Common import Hive_Connect as hc
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
# buried_log = '/update/buried_Energy_Management.log'
# 
# buried_point = "/sdcard/Android/data/com.wm.tracker/files/temp/*"
# 
# save_data = "/update/buried_local_Energy_Management.log"
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
# 
# class Test_Energy_Management():
#     @pytest.fixture(scope='function', autouse=True)
#     def message(self):
#         '''check test environment'''
#         logger.log_info("start Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         os.system("adb root")
#         time.sleep(random.randint(1, 3))
#         set.Action.kill_energy_management_progress(sn)
#         time.sleep(random.randint(1,3))
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
#         logger.log_info("kill energy management progress ", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         os.system("adb root")
#         time.sleep(random.randint(1, 3))
#         set.Action.kill_energy_management_progress(sn)
#         time.sleep(random.randint(1,3))
# 
#     @pytest.mark.parametrize('count,action,event,page', [
#         (random.randint(start_step, end_step), list(set.Energy_Management["Energy_Management"][0].keys())[0], \
#          list(set.Energy_Management["Energy_Management"][0].values())[0],None)])
#     def test_PageDisplay_Start(self, count, action, event,page):
#         Common(count, action, event, page,set.Energy_Management_.PageDisplay_Start)
# 
#     @pytest.mark.parametrize('count,action,event,page', [
#         (random.randint(start_step, end_step), list(set.Energy_Management["Energy_Management"][1].keys())[0], \
#          list(set.Energy_Management["Energy_Management"][1].values())[0],None)])
#     def test_PageDisplay_End(self, count, action, event,page):
#         Common(count, action, event, page,set.Energy_Management_.PageDisplay_End)
# 
#     @pytest.mark.parametrize('count,action,event,page', [
#         (random.randint(start_step, end_step), list(set.Energy_Management["Energy_Management"][2].keys())[0], \
#          list(set.Energy_Management["Energy_Management"][2].values())[0],None)])
#     def test_OpenApp(self, count, action, event,page):
#         Common(count, action, event, page,set.Energy_Management_.OpenApp)
# 
# class Test_BatteryInfo():
#     @pytest.fixture(scope='function', autouse=True)
#     def message(self):
#         '''check test environment'''
#         logger.log_info("start Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         os.system("adb root")
#         time.sleep(random.randint(1, 3))
#         set.Action.kill_energy_management_progress(sn)
#         time.sleep(random.randint(1,3))
#         set.Action.start_energy_management(sn)
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
#         logger.log_info("kill energy management progress ", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         os.system("adb root")
#         time.sleep(random.randint(1, 3))
#         set.Action.kill_energy_management_progress(sn)
#         time.sleep(random.randint(1,3))
# 
#     @pytest.mark.parametrize('count,action,event,page', [
#         (random.randint(start_step, end_step), list(set.BatteryInfo["BatteryInfo"][0].keys())[0], \
#          list(set.BatteryInfo["BatteryInfo"][0].values())[0],list(set.BatteryInfo.keys())[0])])
#     def test_MileageSwitch_10KM(self, count, action, event,page):
#         Common(count, action, event, page,set.BatteryInfo_.MileageSwitch_10KM)
# 
#     @pytest.mark.parametrize('count,action,event,page', [
#         (random.randint(start_step, end_step), list(set.BatteryInfo["BatteryInfo"][1].keys())[0], \
#          list(set.BatteryInfo["BatteryInfo"][1].values())[0],list(set.BatteryInfo.keys())[0])])
#     def test_MileageSwitch_25KM(self, count, action, event,page):
#         Common(count, action, event, page,set.BatteryInfo_.MileageSwitch_25KM)
# 
#     @pytest.mark.parametrize('count,action,event,page', [
#         (random.randint(start_step, end_step), list(set.BatteryInfo["BatteryInfo"][2].keys())[0], \
#          list(set.BatteryInfo["BatteryInfo"][2].values())[0],list(set.BatteryInfo.keys())[0])])
#     def test_MileageSwitch_50KM(self, count, action, event,page):
#         Common(count, action, event, page,set.BatteryInfo_.MileageSwitch_50KM)
# 
#     @pytest.mark.parametrize('count,action,event,page', [
#         (random.randint(start_step, end_step), list(set.BatteryInfo["BatteryInfo"][3].keys())[0], \
#          list(set.BatteryInfo["BatteryInfo"][3].values())[0],list(set.BatteryInfo.keys())[0])])
#     def test_MileageSwitch_100KM(self, count, action, event,page):
#         Common(count, action, event, page,set.BatteryInfo_.MileageSwitch_100KM)
# 
#     @pytest.mark.parametrize('count,action,event,page', [
#         (random.randint(start_step, end_step), list(set.BatteryInfo["BatteryInfo"][3].keys())[0], \
#          list(set.BatteryInfo["BatteryInfo"][3].values())[0],list(set.BatteryInfo.keys())[0])])
#     def test_MileageSwitch_100KM(self, count, action, event,page):
#         Common(count, action, event, page,set.BatteryInfo_.MileageSwitch_100KM)
# 
#     @pytest.mark.parametrize('count,action,event,page', [
#         (random.randint(start_step, end_step), list(set.BatteryInfo["BatteryInfo"][4].keys())[0], \
#          list(set.BatteryInfo["BatteryInfo"][4].values())[0],list(set.BatteryInfo.keys())[0])])
#     def test_EnergyEfficiency(self, count, action, event,page):
#         Common(count, action, event, page,set.BatteryInfo_.EnergyEfficiency)
# 
# 
#     @pytest.mark.parametrize('count,action,event,page', [
#         (random.randint(start_step, end_step), list(set.BatteryInfo["BatteryInfo"][5].keys())[0], \
#          list(set.BatteryInfo["BatteryInfo"][5].values())[0],list(set.BatteryInfo.keys())[0])])
#     def test_PowerConsumeSwitch(self, count, action, event,page):
#         Common(count, action, event, page,set.BatteryInfo_.PowerConsumeSwitch)
# 
#     @pytest.mark.parametrize('count,action,event,page', [
#         (random.randint(start_step, end_step), list(set.BatteryInfo["BatteryInfo"][6].keys())[0], \
#          list(set.BatteryInfo["BatteryInfo"][6].values())[0],list(set.BatteryInfo.keys())[0])])
#     def test_SpeedSwitch(self, count, action, event,page):
#         Common(count, action, event,page, set.BatteryInfo_.SpeedSwitch)
# 
# 
#     @pytest.mark.parametrize('count,action,event,page', [
#         (random.randint(start_step, end_step), list(set.BatteryInfo["BatteryInfo"][7].keys())[0], \
#          list(set.BatteryInfo["BatteryInfo"][7].values())[0],list(set.BatteryInfo.keys())[0])])
#     def test_VoiceReport(self, count, action, event,page):
#         Common(count, action, event,page, set.BatteryInfo_.VoiceReport)
# 
# 
#     @pytest.mark.parametrize('count,action,event,page', [
#         (random.randint(start_step, end_step), list(set.BatteryInfo["BatteryInfo"][8].keys())[0], \
#          list(set.BatteryInfo["BatteryInfo"][8].values())[0],list(set.BatteryInfo.keys())[0])])
#     def test_BatteryInfoForeground_Start(self, count, action, event,page):
#         Common(count, action, event, page,set.BatteryInfo_.BatteryInfoForeground_Start)
# 
#     @pytest.mark.parametrize('count,action,event,page', [
#         (random.randint(start_step, end_step), list(set.BatteryInfo["BatteryInfo"][9].keys())[0], \
#          list(set.BatteryInfo["BatteryInfo"][9].values())[0],list(set.BatteryInfo.keys())[0])])
#     def test_BatteryInfoForeground_End(self, count, action, event,page):
#         Common(count, action, event, page,set.BatteryInfo_.BatteryInfoForeground_End)
# 
#     @pytest.mark.parametrize('count,action,event,page', [
#         (random.randint(start_step, end_step), list(set.BatteryInfo["BatteryInfo"][10].keys())[0], \
#          list(set.BatteryInfo["BatteryInfo"][10].values())[0],list(set.BatteryInfo.keys())[0])])
#     def test_IntoBatteryInfo(self, count, action, event,page):
#         Common(count, action, event, page,set.BatteryInfo_.IntoBatteryInfo)
# 
# 
# class Test_PowerConsume():
#     @pytest.fixture(scope='function', autouse=True)
#     def message(self):
#         '''check test environment'''
#         logger.log_info("start Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         os.system("adb root")
#         time.sleep(random.randint(1, 3))
#         set.Action.kill_energy_management_progress(sn)
#         time.sleep(random.randint(1,3))
#         set.Action.start_energy_management(sn)
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
#         logger.log_info("kill energy management progress ", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         os.system("adb root")
#         time.sleep(random.randint(1, 3))
#         set.Action.kill_energy_management_progress(sn)
#         time.sleep(random.randint(1,3))
# 
#     @pytest.mark.parametrize('count,action,event,page', [
#         (random.randint(start_step, end_step), list(set.PowerConsume["PowerConsume"][0].keys())[0], \
#          list(set.PowerConsume["PowerConsume"][0].values())[0],list(set.PowerConsume.keys())[0])])
#     def test_PeriodSwitch_Week(self, count, action, event, page):
#         Common(count, action, event, page,set.PowerConsume_.PeriodSwitch_Week)
# 
# 
#     @pytest.mark.parametrize('count,action,event,page', [
#         (random.randint(start_step, end_step), list(set.PowerConsume["PowerConsume"][1].keys())[0], \
#          list(set.PowerConsume["PowerConsume"][1].values())[0],list(set.PowerConsume.keys())[0])])
#     def test_PeriodSwitch_Month(self, count, action, event,page):
#         Common(count, action, event, page,set.PowerConsume_.PeriodSwitch_Month)
# 
#     @pytest.mark.parametrize('count,action,event,page', [
#         (random.randint(start_step, end_step), list(set.PowerConsume["PowerConsume"][2].keys())[0], \
#          list(set.PowerConsume["PowerConsume"][2].values())[0],list(set.PowerConsume.keys())[0])])
#     def test_PeriodSwitch_Year(self, count, action, event, page):
#         Common(count, action, event, page,set.PowerConsume_.PeriodSwitch_Year)
# 
#     @pytest.mark.parametrize('count,action,event,page', [
#         (random.randint(start_step, end_step), list(set.PowerConsume["PowerConsume"][3].keys())[0], \
#          list(set.PowerConsume["PowerConsume"][3].values())[0],list(set.PowerConsume.keys())[0])])
#     def test_PowerConsumeForeground_Start(self, count, action, event, page):
#         Common(count, action, event,page, set.PowerConsume_.PowerConsumeForeground_Start)
# 
#     @pytest.mark.parametrize('count,action,event,page', [
#         (random.randint(start_step, end_step), list(set.PowerConsume["PowerConsume"][4].keys())[0], \
#          list(set.PowerConsume["PowerConsume"][4].values())[0],list(set.PowerConsume.keys())[0])])
#     def test_PowerConsumeForeground_End(self, count, action, event, page):
#         Common(count, action, event, page, set.PowerConsume_.PowerConsumeForeground_End)
# 
#     @pytest.mark.parametrize('count,action,event,page', [
#         (random.randint(start_step, end_step), list(set.PowerConsume["PowerConsume"][5].keys())[0], \
#          list(set.PowerConsume["PowerConsume"][5].values())[0],list(set.PowerConsume.keys())[0])])
#     def test_IntoPowerConsume(self, count, action, event,page):
#         Common(count, action, event, page,set.PowerConsume_.IntoPowerConsume)
# 
# 
# class Test_HistoricalJourney():
#     @pytest.fixture(scope='function', autouse=True)
#     def message(self):
#         '''check test environment'''
#         logger.log_info("start Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         os.system("adb root")
#         time.sleep(random.randint(1, 3))
#         set.Action.kill_energy_management_progress(sn)
#         time.sleep(random.randint(1,3))
#         set.Action.start_energy_management(sn)
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
#         logger.log_info("kill energy management progress ", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         os.system("adb root")
#         time.sleep(random.randint(1, 3))
#         set.Action.kill_energy_management_progress(sn)
#         time.sleep(random.randint(1,3))
# 
#     @pytest.mark.parametrize('count,action,event,page', [
#         (random.randint(start_step, end_step), list(set.HistoricalJourney["HistoricalJourney"][0].keys())[0], \
#          list(set.HistoricalJourney["HistoricalJourney"][0].values())[0],list(set.HistoricalJourney.keys())[0])])
#     def test_HistoricalJourney_Start(self, count, action, event, page):
#         Common(count, action, event, page, set.HistoricalJourney_.HistoricalJourneyForeground_Start)
# 
#     @pytest.mark.parametrize('count,action,event,page', [
#         (random.randint(start_step, end_step), list(set.HistoricalJourney["HistoricalJourney"][1].keys())[0], \
#          list(set.HistoricalJourney["HistoricalJourney"][1].values())[0],list(set.HistoricalJourney.keys())[0])])
#     def test_HistoricalJourneyForeground_End(self, count, action, event, page):
#         Common(count, action, event, page, set.HistoricalJourney_.HistoricalJourneyForeground_End)
# 
#     @pytest.mark.parametrize('count,action,event,page', [
#         (random.randint(start_step, end_step), list(set.HistoricalJourney["HistoricalJourney"][2].keys())[0], \
#          list(set.HistoricalJourney["HistoricalJourney"][2].values())[0],list(set.HistoricalJourney.keys())[0])])
#     def test_IntoHistoricalJourney(self, count, action, event, page):
#         Common(count, action, event, page, set.HistoricalJourney_.IntoHistoricalJourney)
# 
#     @pytest.mark.parametrize('count,action,event,page', [
#         (random.randint(start_step, end_step), list(set.HistoricalJourney["HistoricalJourney"][3].keys())[0], \
#          list(set.HistoricalJourney["HistoricalJourney"][3].values())[0],list(set.HistoricalJourney.keys())[0])])
#     def test_HistoricalJourneyList(self, count, action, event, page):
#         Common(count, action, event, page, set.HistoricalJourney_.HistoricalJourneyList)
# 
# class Test_EnergyBall():
#     @pytest.fixture(scope='function', autouse=True)
#     def message(self):
#         '''check test environment'''
#         logger.log_info("start Test", sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         os.system("adb root")
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
#         logger.log_info("kill energy management progress ", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         os.system("adb root")
#         time.sleep(random.randint(1, 3))
# 
#     @pytest.mark.parametrize('count,action,event,page', [
#         (random.randint(start_step, end_step), list(set.EnergyBall["EnergyBall"][0].keys())[0], \
#          list(set.EnergyBall["EnergyBall"][0].values())[0],list(set.EnergyBall.keys())[0])])
#     def test_EconomyModeAdviseAppare(self, count, action, event, page):
#         Common(count, action, event, page, set.EnergyBall_.EconomyModeAdviseAppare)
# 
#     @pytest.mark.parametrize('count,action,event,page', [
#         (random.randint(start_step, end_step), list(set.EnergyBall["EnergyBall"][2].keys())[0], \
#          list(set.EnergyBall["EnergyBall"][2].values())[0],list(set.EnergyBall.keys())[0])])
#     def test_EnergyRecoveryAppare(self, count, action, event, page):
#         Common(count, action, event, page, set.EnergyBall_.EnergyRecoveryAppare)
# 
#     @pytest.mark.parametrize('count,action,event,page', [
#         (random.randint(start_step, end_step), list(set.EnergyBall["EnergyBall"][4].keys())[0], \
#          list(set.EnergyBall["EnergyBall"][4].values())[0], list(set.EnergyBall.keys())[0])])
#     def test_ACOffAdviseAppare(self, count, action, event, page):
#         Common(count, action, event, page, set.EnergyBall_.ACOffAdviseAppare)
# 
#     @pytest.mark.parametrize('count,action,event,page', [
#         (random.randint(start_step, end_step), list(set.EnergyBall["EnergyBall"][3].keys())[0], \
#          list(set.EnergyBall["EnergyBall"][3].values())[0], list(set.EnergyBall.keys())[0])])
#     def test_EconomyModeAdvise(self, count, action, event, page):
#         Common(count, action, event, page, set.EnergyBall_.EconomyModeAdvise)
# 
#     @pytest.mark.parametrize('count,action,event,page', [
#         (random.randint(start_step, end_step), list(set.EnergyBall["EnergyBall"][3].keys())[0], \
#          list(set.EnergyBall["EnergyBall"][3].values())[0], list(set.EnergyBall.keys())[0])])
#     def test_EnergyRecovery(self, count, action, event, page):
#         Common(count, action, event, page, set.EnergyBall_.EnergyRecovery)
# 
#     @pytest.mark.parametrize('count,action,event,page', [
#         (random.randint(start_step, end_step), list(set.EnergyBall["EnergyBall"][5].keys())[0], \
#          list(set.EnergyBall["EnergyBall"][5].values())[0], list(set.EnergyBall.keys())[0])])
#     def test_ACOffAdvise(self, count, action, event, page):
#         Common(count, action, event, page, set.EnergyBall_.ACOffAdvise)
# 
# 
# class Test_Check_Energy_Management_Hive_Result(object):
# 
#     @pytest.mark.parametrize('sn',[set.Action.get_sn()])
#     def test_Kill_Buried_Progress(self,sn):
#         logger.log_info("kill logcat collect log progress", \
#                         sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                         sys._getframe().f_lineno)
#         os.system('adb -s %s shell "%s"' %(sn,logcat_pid_exist))
#         time.sleep(7200)
# 
#     @pytest.mark.parametrize('action,event,page', [
#         (list(set.Energy_Management["Energy_Management"][0].keys())[0], \
#          list(set.Energy_Management["Energy_Management"][0].values())[0], None)])
#     def test_PageDisplay_Start(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [
#         (list(set.Energy_Management["Energy_Management"][1].keys())[0], \
#          list(set.Energy_Management["Energy_Management"][1].values())[0], None)])
#     def test_PageDisplay_End(self, count, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [
#         (list(set.Energy_Management["Energy_Management"][2].keys())[0], \
#          list(set.Energy_Management["Energy_Management"][2].values())[0], None)])
#     def test_OpenApp(self,action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [
#         (list(set.BatteryInfo["BatteryInfo"][0].keys())[0], \
#          list(set.BatteryInfo["BatteryInfo"][0].values())[0], list(set.BatteryInfo.keys())[0])])
#     def test_MileageSwitch_10KM(self,action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [
#         (list(set.BatteryInfo["BatteryInfo"][1].keys())[0], \
#          list(set.BatteryInfo["BatteryInfo"][1].values())[0], list(set.BatteryInfo.keys())[0])])
#     def test_MileageSwitch_25KM(self,action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [
#         ( list(set.BatteryInfo["BatteryInfo"][2].keys())[0], \
#          list(set.BatteryInfo["BatteryInfo"][2].values())[0], list(set.BatteryInfo.keys())[0])])
#     def test_MileageSwitch_50KM(self,action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [
#         (list(set.BatteryInfo["BatteryInfo"][3].keys())[0], \
#          list(set.BatteryInfo["BatteryInfo"][3].values())[0], list(set.BatteryInfo.keys())[0])])
#     def test_MileageSwitch_100KM(self,action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [
#         (list(set.BatteryInfo["BatteryInfo"][3].keys())[0], \
#          list(set.BatteryInfo["BatteryInfo"][3].values())[0], list(set.BatteryInfo.keys())[0])])
#     def test_MileageSwitch_100KM(self,action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [
#         (list(set.BatteryInfo["BatteryInfo"][4].keys())[0], \
#          list(set.BatteryInfo["BatteryInfo"][4].values())[0], list(set.BatteryInfo.keys())[0])])
#     def test_EnergyEfficiency(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [
#         (list(set.BatteryInfo["BatteryInfo"][5].keys())[0], \
#          list(set.BatteryInfo["BatteryInfo"][5].values())[0], list(set.BatteryInfo.keys())[0])])
#     def test_PowerConsumeSwitch(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [
#         (list(set.BatteryInfo["BatteryInfo"][6].keys())[0], \
#          list(set.BatteryInfo["BatteryInfo"][6].values())[0], list(set.BatteryInfo.keys())[0])])
#     def test_SpeedSwitch(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [
#         (list(set.BatteryInfo["BatteryInfo"][7].keys())[0], \
#          list(set.BatteryInfo["BatteryInfo"][7].values())[0], list(set.BatteryInfo.keys())[0])])
#     def test_VoiceReport(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [
#         (list(set.BatteryInfo["BatteryInfo"][8].keys())[0], \
#          list(set.BatteryInfo["BatteryInfo"][8].values())[0], list(set.BatteryInfo.keys())[0])])
#     def test_BatteryInfoForeground_Start(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [
#         (list(set.BatteryInfo["BatteryInfo"][9].keys())[0], \
#          list(set.BatteryInfo["BatteryInfo"][9].values())[0], list(set.BatteryInfo.keys())[0])])
#     def test_BatteryInfoForeground_End(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [
#         (list(set.BatteryInfo["BatteryInfo"][10].keys())[0], \
#          list(set.BatteryInfo["BatteryInfo"][10].values())[0], list(set.BatteryInfo.keys())[0])])
#     def test_IntoBatteryInfo(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [
#         (list(set.PowerConsume["PowerConsume"][0].keys())[0], \
#          list(set.PowerConsume["PowerConsume"][0].values())[0], list(set.PowerConsume.keys())[0])])
#     def test_PeriodSwitch_Week(self,action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [
#         (list(set.PowerConsume["PowerConsume"][1].keys())[0], \
#          list(set.PowerConsume["PowerConsume"][1].values())[0], list(set.PowerConsume.keys())[0])])
#     def test_PeriodSwitch_Month(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [
#         (list(set.PowerConsume["PowerConsume"][2].keys())[0], \
#          list(set.PowerConsume["PowerConsume"][2].values())[0], list(set.PowerConsume.keys())[0])])
#     def test_PeriodSwitch_Year(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [
#         (list(set.PowerConsume["PowerConsume"][3].keys())[0], \
#          list(set.PowerConsume["PowerConsume"][3].values())[0], list(set.PowerConsume.keys())[0])])
#     def test_PowerConsumeForeground_Start(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [
#         (list(set.PowerConsume["PowerConsume"][4].keys())[0], \
#          list(set.PowerConsume["PowerConsume"][4].values())[0], list(set.PowerConsume.keys())[0])])
#     def test_PowerConsumeForeground_End(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [
#         (list(set.PowerConsume["PowerConsume"][5].keys())[0], \
#          list(set.PowerConsume["PowerConsume"][5].values())[0], list(set.PowerConsume.keys())[0])])
#     def test_IntoPowerConsume(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [
#         (list(set.HistoricalJourney["HistoricalJourney"][0].keys())[0], \
#          list(set.HistoricalJourney["HistoricalJourney"][0].values())[0], list(set.HistoricalJourney.keys())[0])])
#     def test_HistoricalJourney_Start(self, action, event, page):
#         Compare(action, event, page)
#     @pytest.mark.parametrize('action,event,page', [
#         (list(set.HistoricalJourney["HistoricalJourney"][1].keys())[0], \
#          list(set.HistoricalJourney["HistoricalJourney"][1].values())[0], list(set.HistoricalJourney.keys())[0])])
#     def test_HistoricalJourneyForeground_End(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [
#         (list(set.HistoricalJourney["HistoricalJourney"][2].keys())[0], \
#          list(set.HistoricalJourney["HistoricalJourney"][2].values())[0], list(set.HistoricalJourney.keys())[0])])
#     def test_IntoHistoricalJourney(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [
#         (list(set.HistoricalJourney["HistoricalJourney"][3].keys())[0], \
#          list(set.HistoricalJourney["HistoricalJourney"][3].values())[0], list(set.HistoricalJourney.keys())[0])])
#     def test_HistoricalJourneyList(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [
#         (list(set.EnergyBall["EnergyBall"][0].keys())[0], \
#          list(set.EnergyBall["EnergyBall"][0].values())[0], list(set.EnergyBall.keys())[0])])
#     def test_EconomyModeAdviseAppare(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [
#         (list(set.EnergyBall["EnergyBall"][2].keys())[0], \
#          list(set.EnergyBall["EnergyBall"][2].values())[0], list(set.EnergyBall.keys())[0])])
#     def test_EnergyRecoveryAppare(self,action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [
#         (list(set.EnergyBall["EnergyBall"][4].keys())[0], \
#          list(set.EnergyBall["EnergyBall"][4].values())[0], list(set.EnergyBall.keys())[0])])
#     def test_ACOffAdviseAppare(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [
#         (list(set.EnergyBall["EnergyBall"][3].keys())[0], \
#          list(set.EnergyBall["EnergyBall"][3].values())[0], list(set.EnergyBall.keys())[0])])
#     def test_EconomyModeAdvise(self,action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [
#         (list(set.EnergyBall["EnergyBall"][3].keys())[0], \
#          list(set.EnergyBall["EnergyBall"][3].values())[0], list(set.EnergyBall.keys())[0])])
#     def test_EnergyRecovery(self, action, event, page):
#         Compare(action, event, page)
# 
#     @pytest.mark.parametrize('action,event,page', [
#         (list(set.EnergyBall["EnergyBall"][5].keys())[0], \
#          list(set.EnergyBall["EnergyBall"][5].values())[0], list(set.EnergyBall.keys())[0])])
#     def test_ACOffAdvise(self, count, action, event, page):
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