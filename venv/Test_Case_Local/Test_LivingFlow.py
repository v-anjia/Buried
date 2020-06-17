# '''
# Buried Point for Living Flow
# author: antony weijiang
# date: 2020/3/16
# '''
#
#
# class Check_Result(object):
#     def __init__(self):
#         self.total = 0
#         self.count_pass = 0
#         self.count_fail = 0
#
#     def set_total(self, total):
#         self.total = total
#
#     def get_total(self):
#         return self.total
#
#     def set_count_pass(self, count_pass):
#         self.count_pass = count_pass
#
#     def get_count_pass(self):
#         return self.count_pass
#
#     def set_count_fail(self, count_fail):
#         self.count_fail = count_fail
#
#     def get_count_fail(self):
#         return self.count_fail
#
#     @classmethod
#     def delete_lvlog(cls, sn):
#         try:
#             cmd = 'adb -s %s shell "rm -rf %s;echo $?"' % (sn, setting_log)
#             Result = subprocess.check_output(cmd, shell=True)
#             Result = co.removal(Result)
#             logger.log_debug("Result value is :%s" % (Result), \
#                              sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                              sys._getframe().f_lineno)
#             if Result == '0':
#                 logger.log_info("delete lvlog successfully", \
#                                 sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                                 sys._getframe().f_lineno)
#                 return 0
#             else:
#                 logger.log_error("delete lvlog failed", \
#                                  sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                                  sys._getframe().f_lineno)
#                 return 1
#         except Exception as e:
#             logger.log_error("%s" % (e), \
#                              sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                              sys._getframe().f_lineno)
#             return 1
#
#     @classmethod
#     def delete_tracker_log(cls, sn):
#         try:
#             cmd = 'adb -s %s shell "rm -rf %s;echo $?' % (sn, buried_point)
#             Result = subprocess.check_output(cmd, shell=True)
#             Result = co.removal(Result)
#             logger.log_debug("Result value is : %s" % (Result), \
#                              sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                              sys._getframe().f_lineno)
#
#             if int(Result) == 0:
#                 logger.log_info("delete tracker log successfully", \
#                                 sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                                 sys._getframe().f_lineno)
#                 return 1
#             else:
#                 logger.log_error("delete tracker log failed", \
#                                  sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                                  sys._getframe().f_lineno)
#                 return 0
#         except Exception as e:
#             logger.log_error("%s" % (e), \
#                              sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                              sys._getframe().f_lineno)
#             return 1
#
#     @classmethod
#     def check_android_tracker_log(cls, sn, action=None, event=None):
#         try:
#             time.sleep(2)
#             str_expr = ".*%s.*event.{3}%s.*" % (action, event)
#             logger.log_info("%s" % (str_expr), \
#                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                             sys._getframe().f_lineno)
#             print(str_expr)
#             cmd = 'adb -s %s shell "cat %s |grep -iE %s |%s wc -l"' % (sn, buried_point, str_expr, busybox)
#             # cmd = 'adb -s %s shell "cat %s |grep %s |grep %s|grep -v grep | %s wc -l"' %(sn, buried_point, action, event, busybox)
#             Result = subprocess.check_output(cmd, shell=True)
#             Result = int(co.removal(Result))
#             logger.log_info("antony @@@debug %s" % (Result), \
#                             sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                             sys._getframe().f_lineno)
#             print("antony @@@debug %s" % (Result))
#             logger.log_debug("tracker directory log collect result is : %s" % (Result), \
#                              sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                              sys._getframe().f_lineno)
#             return Result
#         except Exception as e:
#             logger.log_error("%s" % (e), \
#                              sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                              sys._getframe().f_lineno)
#             return False
#
#     def check_android_tracker_log_exist(self, sn):
#         try:
#             cmd = 'adb -s %s shell "cat %s |grep %s |grep %s | %s wc -l   "' % (
#             sn, buried_point, app_id, module_id, busybox)
#             Result = subprocess.check_call(cmd, stdout=subprocess.PIPE, shell=True)
#             if Result == '0':
#                 logger.log_info("tracker log exist", \
#                                 sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                                 sys._getframe().f_lineno)
#                 return False
#             else:
#                 logger.log_info("tracker log not exist", \
#                                 sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                                 sys._getframe().f_lineno)
#                 return True
#         except Exception as e:
#             logger.log_error("%s" % (e), \
#                              sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                              sys._getframe().f_lineno)
#             return False
#
#     def check_reboot_log_exist(self, sn):
#         loop_count = 3
#         logger.log_info("reboot system", sys._getframe().f_code.co_filename, \
#                         sys._getframe().f_code.co_name, sys._getframe().f_lineno)
#         os.system('adb -s %s reboot' % (sn))
#         logger.log_info("wait for adb device", sys._getframe().f_code.co_filename, \
#                         sys._getframe().f_code.co_name, sys._getframe().f_lineno)
#         p = subprocess.Popen('adb -s %s wait-for-device' % (sn), stderr=subprocess.PIPE, stdin=subprocess.PIPE,
#                              stdout=subprocess.PIPE, shell=False)
#         while True:
#             time.sleep(random.randint(20, 30))
#             print(p.poll())
#             if p.poll() is not None:
#                 logger.log_info("adb devices init successfully", \
#                                 sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                                 sys._getframe().f_lineno)
#                 if self.check_android_tracker_log_exist():
#                     logger.log_info("file transfer to platform", \
#                                     sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                                     sys._getframe().f_lineno)
#                     return 0
#                 else:
#                     logger.log_error("file not  transfer to platform", \
#                                      sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                                      sys._getframe().f_lineno)
#                     return 1
#             else:
#                 serial.open_adb_through_serial(self.count)
#                 if loop_count <= 0:
#                     logger.log_error("adb devices init failed", \
#                                      sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name,
#                                      sys._getframe().f_lineno)
#                     return 1
#             loop_count = loop_count - 1
#
#
#
#
