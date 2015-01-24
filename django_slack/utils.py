import random

ASCII_CHARACTER_SET = ('abcdefghijklmnopqrstuvwxyz'
                       'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                       '0123456789')


def generate_random_from_vschar_set(length=30):
    rand = random.SystemRandom()
    return ''.join(rand.choice(ASCII_CHARACTER_SET) for x in range(length))


try:
    from django.utils.functional import cached_property
except ImportError:
    class cached_property(object):
        """
        Decorator that converts a method with a single self argument into a
        property cached on the instance.
        """
        def __init__(self, func):
            self.func = func

        def __get__(self, instance, type=None):
            if instance is None:
                return self
            res = instance.__dict__[self.func.__name__] = self.func(instance)
            return res
