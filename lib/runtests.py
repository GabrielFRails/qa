# 
# Copyright (c) Gabriel Freitas: gabriel.estudy.reis@gmail.com
#

import libunittest as ut

from testcase_pokeapi import *
from test_api_availability import *

ut.add_testcase_list(testcaselist_pokeapi)
ut.add_testcase_list(testcaselist_availability)
ut.run()