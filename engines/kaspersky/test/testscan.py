
from nose.tools import ok_
import unittest
from engines.kaspersky.scanner import kaspersky_engine
from engines.generic.test.common import AVEngineTemplate


class TestKasperskyAV(AVEngineTemplate, unittest.TestCase):
	scan_class = kaspersky_engine
	infected_string = 'EICAR-Test-File'

	def test_update(self):
		"""
		Run test of A/V definition update functionality. This test requires root privs (sudo).
		"""

		# version returns dict, test needs 'definitions' element.
		# definitions is string like: 7.11.55.60
		# initial ver on A/V defs

		init_ver = self.scanner.version['definitions']
		#print init_ver

		# run update_definitions()
		self.scanner.update_definitions()
		# final date on A/V defs
		final_ver = self.scanner.version['definitions']
		#print final_ver

		# If the defs were updated, final_ver is > init_ver.
		# In the case where they were already updated, then final_ver == init_ver.
		ok_(final_ver >= init_ver, msg="Test A/V def update - version")
