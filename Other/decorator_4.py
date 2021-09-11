# -*- coding: utf-8 -*-
import logging


def log(func):
    """
    Log every function call
    """

    def wrap_log(*args, **kwargs):
        name = func.__name__
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)

        # open the log file to write
        fh = logging.FileHandler("%s.log" % name) # <name>.log
        fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        formatter = logging.Formatter(fmt)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

        logger.info("Called: %s" % name)
        result = func(*args, **kwargs)
        logger.info("Result: %s" % result)
        return func

    return wrap_log


@log
def add_together_function(a, b):
    #  takes 2 integers as arguments
    #  and returns the summation of them
    return a + b


if __name__ == "__main__":
    args = [1, 2]
    for i in range(2):
        value = add_together_function(*args)