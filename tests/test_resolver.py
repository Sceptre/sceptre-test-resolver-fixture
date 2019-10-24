from resolver.test_resolver_fixture import TestResolver


class TestStackActions:
    def test_dummy_test(self):
        resolver = TestResolver()
        assert resolver.resolve() == "TEST_RESOLVER_SUCCESS"
