import nose

class TestIntentionalFailures(object):
    def setup(self):
        pass

    def teardown(self):
        pass

    def test_fail(self):
        nose.tools.assert_true(False)

    def test_error(self):
        raise ValueError("oops")
