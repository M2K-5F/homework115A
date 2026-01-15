from unittest import TestCase
from application.api.logic import get_group_count


class LogicTestCase(TestCase):
    def test_case_1(self):
        self.assertEqual(0, get_group_count([]))

    def test_case_2(self):
        self.assertEqual(1, get_group_count([-1, -1]))

    def test_case_3(self):
        self.assertEqual(5, get_group_count([2, -1, 3, 4, 5, -1]))