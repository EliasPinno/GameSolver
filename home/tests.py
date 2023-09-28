from django.test import TestCase

class YourTestClass(TestCase):

    def setUpTestData(self):
        print("Ran setUpTestData. Should only run once")

    def setUp(self):
        print("Ran test setup: should run before each test")
        pass

    def test_true_is_true(self):
        self.assertTrue(True == True)
        pass
