'''
project main enter
anthor :antoy weijiang
date: 2020/4/10
'''
import time
import os
import sys
import pytest
import argparse
import threading
from pytest_html import plugin
from pytest_html import hooks
from pytest_html import extras
import jaydebeapi

def Main():
    parser = argparse.ArgumentParser(prog='PROG', usage='%(prog)s [options]')
    parser.add_argument('--account', dest="account", metavar='account', help="choose capture picture")
    parser.add_argument('--time', dest='time', metavar='run times', help='how long time cases need to run(hours)')
    arg = parser.parse_args(['--account', '1'])
    # arg = parser.parse_args(['--time','12'])
    if arg.time is not None:
        current_time = int(time.time())
        loop_time = current_time + int(arg.time) * 3600
        time.sleep(1)
        while current_time <= loop_time:
            pytest.main(['-s', '--repeat-scope', 'class', '%s' % (os.getcwd() + "\..\Test_Case"), '--html','Report_%s.html' % (current_time)])
            current_time = int(time.time())

    if arg.account is not None:
        account = int(arg.account)
        current_time = int(time.time())
        # pytest.main(['-s', '--metadata','Tester', 'Antony WeiJiang', '--metadata', 'Project', 'Buried Point Auto', '--metadata', 'Company', 'WM MOTOR', '--repeat-scope', 'class', '--count', '%s' % (arg.account), '%s' % (os.getcwd() + "\..\Test_Case"),'--html', 'Report_Buried_Local_Data_%s.html' % (current_time)])

        pytest.main(['-s', '--metadata', 'Tester', 'Antony WeiJiang', '--metadata', 'Project', 'Buried Point Auto',
                     '--metadata', 'Company', 'WM MOTOR', '--repeat-scope', 'class', '--count', '%s' % (arg.account),
                     '%s' % (os.getcwd() + "\..\Test_Case_Hive"), '--html', 'Report_Buried_Hive_Data_%s.html' % (current_time)])

if __name__ == "__main__":
    Main()
