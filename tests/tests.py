from unittest import TestCase
from samplepackage.samplemodule import foo


class TestSample(TestCase):
    def test(self):
        self.assertEqual(5, foo())
