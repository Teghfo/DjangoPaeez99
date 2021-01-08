from django.test import TestCase


class TestTrain(TestCase):

    @classmethod
    def setUpClass(cls):
        print("in setup class")

    @classmethod
    def tearDownClass(cls):
        print("in tearDown class")

    def setUp(self):
        print("in setup")

    def test_dummy1(self):
        print("in 1")
        assert 1 == 1

    def test_dummy2(self):
        print("in 2")

        assert 1 == 1

    def test_dummy3(self):
        print("in 3")

        assert 1 == 1

    def tearDown(self):
        print("in teardown")
