from django.test import TestCase


class ModelTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: запустите один раз, чтобы настроить немодифицированные данные для всех методов класса")
        pass

    def setUp(self):
        print("setUp: запустите один раз для каждого метода тестирования, чтобы настроить чистые данные")
        pass

    def test_false_is_false(self):
        print("Method: test_false_is_false")
        self.assertFalse(False)

    def test_false_is_true(self):
        print("Method: test_false_is_true")
        self.assertTrue(False)

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two")
        self.assertEqual(1 + 1, 2)