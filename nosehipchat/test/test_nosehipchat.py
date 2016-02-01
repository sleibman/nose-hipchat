import nose

class TestNoseHipChat(object):
    def setup(self):
        pass

    def teardown(self):
        pass

    def passing_test(self):
        nose.tools.assert_true(True)

