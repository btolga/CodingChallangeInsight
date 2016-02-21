import unittest
from TolgaCodingChallange import cleanme

class CodingchalangeTestCase(unittest.TestCase):
	"""Tests for 'TolgaCodingChallange.py'."""

	def test_is_clean_mid(self):
		"""Is the list clean of non alpha-numeric?"""
		self.assertEqual(cleanme("12##$@@abc"), "12abc")

	def test_is_clean_start(self):
		"""Is the list clean of non alpha-numeric?"""
		self.assertEqual(cleanme("##$@@abc"), "abc")

	def test_is_clean_end(self):
		"""Is the list clean of non alpha-numeric?"""
		self.assertEqual(cleanme("123##$@@"), "123")

if __name__ == '__main__':
	unittest.main()