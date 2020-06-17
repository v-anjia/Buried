# '''
# Case System Activation Test Suite
# author : antony WeiJiang
# date:2020/3/17
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
# from Common import Energy_Management as set
# from Common import Common as co
# from log import  logger as loger
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
#         if set.Check_Result.delete_tracker_log(set.Action.get_sn()):
#             logger.log_info("delete tracker successfully", \
#                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                             sys._getframe().f_lineno)
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
#         if set.Check_Result.delete_tracker_log(set.Action.get_sn()):
#             logger.log_info("delete tracker successfully", \
#                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                             sys._getframe().f_lineno)
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
#         if set.Check_Result.delete_tracker_log(set.Action.get_sn()):
#             logger.log_info("delete tracker successfully", \
#                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                             sys._getframe().f_lineno)
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
#         if set.Check_Result.delete_tracker_log(set.Action.get_sn()):
#             logger.log_info("delete tracker successfully", \
#                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                             sys._getframe().f_lineno)
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
#         if set.Check_Result.delete_tracker_log(set.Action.get_sn()):
#             logger.log_info("delete tracker successfully", \
#                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                             sys._getframe().f_lineno)
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
