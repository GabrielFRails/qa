# 
# Copyright (c) Gabriel Freitas: gabriel.estudy.reis@gmail.com
# Wrapper for unittest: python unit testing framework

# system imports
import unittest
import time

# local libs import
from libmessage import *
from liblog import *

class CustomTestResult(unittest.TextTestResult):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.results = []
		self.fail_results = []
		self.error_results = []
		self.total_time = 0
		self.unittest_msg_channel = get_msg_channel()

	def startTest(self, test):
		super().startTest(test)
		test_id = test.id()
		report_testid = self.get_test_report_id(test_id)
		msg = generate_unittest_message(report_testid, 'running')
		send_message(msg, 'unittest', self.unittest_msg_channel)
		self.start_time = time.time()

	def addSuccess(self, test):
		super().addSuccess(test)
		self.save_result(test, "ok")

	def addError(self, test, err):
		super().addError(test, err)
		self.save_result(test, "ERROR")

	def addFailure(self, test, err):
		super().addFailure(test, err)
		self.save_result(test, "FAIL")

	def save_result(self, test, outcome):
		elapsed_time = time.time() - self.start_time

		test_id = test.id()
		report_testid = self.get_test_report_id(test_id)
		msg = generate_unittest_message(report_testid, outcome)
		send_message(msg, 'unittest', self.unittest_msg_channel)
		self.results.append((report_testid, outcome, elapsed_time))

		if outcome == "FAIL":
			self.fail_results.append((report_testid, outcome, elapsed_time))

		if outcome == "ERROR":
			self.error_results.append((report_testid, outcome, elapsed_time))

		self.total_time += elapsed_time

	def print_sorted_results(self):
		sorted_results = sorted(self.results, key=lambda x: x[2], reverse=True)
		log_info("\nTest Results (Sorted by Time):")
		for test, outcome, elapsed_time in sorted_results:
			log_info(f"{test}: {outcome} [{elapsed_time:.3f}s]")

	def print_summary(self):
		log_info("\n\nTest Results:")
		log_info(f"Total run time: [{self.total_time:.3f}s]")
		for test, outcome, elapsed_time in self.results:
			log_info(f"{test} ... {outcome} [{elapsed_time:.3f}s]")

		if len(self.fail_results) > 0:
			log_info(f"\n\nFail Results ({len(self.fail_results)} failures):")
			for test, outcome, elapsed_time in self.fail_results:
				log_info(f"{test} ... {outcome} [{elapsed_time:.3f}s]")

		if len(self.error_results) > 0:
			log_info(f"\n\Errors Results ({len(self.error_results)} errors):")
			for test, outcome, elapsed_time in self.error_results:
				log_info(f"{test} ... {outcome} [{elapsed_time:.3f}s]")

		#self.print_sorted_results()

	def get_test_report_id(self, test_id):
		testid_splited = test_id.split('.')
  
		testname = testid_splited[2]
		testcase = testid_splited[1]
		testcase_list = testid_splited[0]

		report_testid = f"{testname} ({testcase_list}.{testcase})"
		return report_testid		

__testsuite = unittest.TestSuite()
def add_testcase_list(testcases):
# {
	global __testsuite

	alltests = list()
	for t in testcases:
		testlist = unittest.TestLoader().loadTestsFromTestCase(t)
		alltests.append(testlist)

	__testsuite.addTests(alltests)
# }

class CustomTextTestRunner(unittest.TextTestRunner):
	def _makeResult(self):
		return CustomTestResult(self.stream, self.descriptions, self.verbosity)

def run():
	result = CustomTextTestRunner(verbosity=3).run(__testsuite)
	result.print_summary()
	return result