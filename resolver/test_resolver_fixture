from sceptre.resolver import Resolver


class TestResolver(Resolver):
    def __init__(self, *args, **kwargs):
        super(TestResolver, self).__init__(*args, **kwargs)

    def resolve(self):
        """
        resolve is the method called by Sceptre. It should carry out the work
        intended by this resolver. It should return a string to become the
        final value.
        """
        return "TEST_RESOLVER_SUCCESS"
