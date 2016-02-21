import unittest
from TolgaCodingChallange import cleanme, sortedlist

class CodingchalangeTestCase(unittest.TestCase):
	"""Tests for 'TolgaCodingChallange.py'."""

	def test_is_clean_mid(self):
		"""Is the list clean of non alpha-numeric when in the middle?"""
		self.assertEqual(cleanme("12##$@@abc"), "12abc")

	def test_is_clean_start(self):
		"""Is the list clean of non alpha-numeric when at the beginning?"""
		self.assertEqual(cleanme("##$@@abc"), "abc")

	def test_is_clean_end(self):
		"""Is the list clean of non alpha-numeric when at the end?"""
		self.assertEqual(cleanme("123##$@@"), "123")

	def test_is_sorted1(self):
		"""Is the list sorted properly?"""
		self.assertEqual(sortedlist(["123##$@@","cat","122","d@og"]), ["122","cat","123","dog"])

	def test_is_sorted2(self):
		"""Is the list sorted properly?"""
		self.assertEqual(sortedlist(["20", "cat", "bi?rd", "12", "do@g"]),
		 ["12", "bird", "cat", "20", "dog"])

	def test_is_sorted3(self):
		"""Is the list with negative numbers sorted properly?"""
		self.assertEqual(sortedlist(["20", "cat", "bi?rd", "-12", "do@g"]),
		 ["-12", "bird", "cat", "20", "dog"])

if __name__ == '__main__':
	unittest.main()