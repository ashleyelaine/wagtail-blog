import sys


def is_testing():
    """
    Helper function to see if we are running in a testing environment.
    """
    return len(sys.argv) > 1 and sys.argv[1] in ['test', 'behave']
