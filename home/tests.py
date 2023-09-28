from django.test import TestCase

class HomeTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        print("Ran setUpTestData. Should only run once")

    def setUp(self):
        print("Ran test setup: should run before each test")
        pass

    def test_true_is_true(self):
        print("Ran a basic test")
        self.assertTrue(True == True)
        pass
