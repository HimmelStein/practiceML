import sys
import os
import types
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import practiceML


def hello_world():
    print('hellw world from practing machine learning')


if __name__ == '__main__':
    hello_world()
    print([a for a in dir(practiceML) if isinstance(practiceML.__dict__.get(a), types.FunctionType)])