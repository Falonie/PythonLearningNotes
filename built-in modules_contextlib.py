from contextlib import contextmanager,closing
from urllib.request import urlopen

class Query(object):

    def __init__(self,name):
        self.name=name

    def query(self):
        print('Query info about {}...'.format(self.name))

@contextmanager
def create_query(name):
    print('Begin')
    q=Query(name)
    yield q
    print('End')

with create_query('Bob') as a:
    a.query()

@contextmanager
def tag(name):
    print('<%s>'%name)
    yield
    print('<%s>'%name)
with tag('h1'):
    print('Hello')
    print('Python!')

with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)

@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()