class FeatureFlagMiddleware:
    """
    Middleware to attach feature flags to request.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Attach flags to request object
        request.feature_flags = {}

        from .registry import FEATURE_FLAGS
        request.feature_flags.update(FEATURE_FLAGS)

        response = self.get_response(request)
        return response
