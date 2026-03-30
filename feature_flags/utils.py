from .registry import FEATURE_FLAGS

def is_enabled(flag_name):
    """
    Check if a feature flag is enabled.
    """
    return FEATURE_FLAGS.get(flag_name, False)
