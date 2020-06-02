import math
import os
import sys

import requests

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


def test():
    pass


def test2():
    pass


r = requests.get('http://www.lobo.blog.br/')
print(r.status_code)

a = 10
