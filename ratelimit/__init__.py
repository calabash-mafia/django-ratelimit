VERSION = (3, 0, 1, 'ciq')
__version__ = '.'.join(map(str, VERSION))

ALL = (None,)  # Sentinel value for all HTTP methods.
UNSAFE = ['DELETE', 'PATCH', 'POST', 'PUT']
