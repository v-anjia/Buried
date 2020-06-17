'''
for hive datebase object
author:antony weijiang
date:2020/4/10
'''
import jaydebeapi
import os
from log import  logger as loger
logger = loger.Current_Module()

class hive_connect(object):
    def __init__(self):
        self.url = 'jdbc:hive2://10.40.152.5:10000/ods_hu'
        self.user = 'weiyi.jiang'
        self.password = 'weiyi.jiang'
        self.driver = 'org.apache.hive.jdbc.HiveDriver'

    def set_url(self, url):
        self.url = url

    def get_url(self):
        return self.url

    def set_user(self, user):
        self.user = user

    def get_user(self):
        return self.user

    def set_password(self, password):
        self.password = password

    def get_password(self):
        return self.password

    def set_driver(self, driver):
        self.driver = driver

    def get_driver(self):
        return self.driver

    def jar_package(self):
        DIR = os.getcwd() + '/jra/new/'
        jarFile = [
            DIR + 'commons-logging-1.1.3.jar',
            DIR + 'curator-client-2.6.0.jar',
            DIR + 'curator-framework-2.6.0.jar',
            DIR + 'curator-recipes-2.6.0.jar',
            DIR + 'hadoop-common-2.6.0.jar',
            DIR + 'hive-exec-0.13.1.jar',
            DIR + 'hive-jdbc-0.13.1.jar',
            DIR + 'hive-metastore-0.13.1.jar',
            DIR + 'hive-service-0.13.1.jar',
            DIR + 'httpclient-4.4.jar',
            DIR + 'httpcore-4.4.jar',
            DIR + 'libthrift-0.9.2.jar',
            DIR + 'slf4j-api-1.7.5.jar',
            DIR + 'zookeeper-3.4.6.jar',
        ]
        # print("antony @@@debug %s " %(DIR))
        return jarFile
    
    def execute_sql(self, curs, date, vin, page_name, action, event):
        sql_str = "select from_unixtime(cast(create_time/1000 as bigint)),*  from buried where pt_day='{0}' and vin_id='{1}' and page_name='{2}' and action='{3}' and event='{4}' order by create_time".format(date, vin, page_name, action, event)
        logger.log_debug("%s" %(sql_str))
        curs.execute(sql_str)
        results = curs.fetchall()

        # curs.close()
        return len(results)

    def connect(self):
        jarFile = self.jar_package()

        conn = jaydebeapi.connect(self.driver, self.url, [self.user, self.password], jarFile)
        curs = conn.cursor()
        return curs





